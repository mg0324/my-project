> 本篇章主要完成对一个8位CPU的设计和实现。

## 前情分析
一个8位CPU设计时，需要实现基础硬件、CPU框架、指令系统、微程序和编译器。

<img class="my-img" data-src="../../static/skill/basic/compose/cpu-app/base.png"/>


## 硬件部分
经过基础篇修行为止：
* 电源开关POW（基础篇已完成）
* 算数运算单元ALU（基础篇基本完成）
* 程序计数器PC（基础篇已完成）
* 寄存器Register（基础篇已完成）
* 内存控制器MC （基础篇已完成）
* 内存RAM （使用Logic Circuit系统提供的）
* 寄存器控制器RC （待实现）
* 微程序ROM存储器 （使用Logic Circuit系统提供的）
* 控制单元Control Unit （待实现）
* 总线Bus （基本实现）
* CPU框架 （待实现）

### 寄存器控制器RC
#### 实现思路
用5位读写输入，来控制寄存器的读写。（最多控制32个）

#### 寄存器列表

* MSR寄存器：Memory Segment Register，段寄存器。
* MAR寄存器：Memory Address Register，地址寄存器。
* MDR寄存器：Memory Date Register， 存储器数据寄存器
* IR寄存器：Instruction Register，指令寄存器。
* DST寄存器：Destination Register，目标操作数寄存器。
* SRC寄存器：Source Register，源操作数寄存器。
* A寄存器
* B寄存器
* C寄存器
* D寄存器
* 指针及变址寄存器
  * DI寄存器：目的变址寄存器，与DS寄存器连用。
  * SI寄存器：源变址寄存器，与DS寄存器连用。
  * SP寄存器：堆栈指针寄存器，始终只是栈顶的位置, 与SS寄存器一起组成栈顶数据的物理地址。
  * BP寄存器：基址指针寄存器，系统默认其指向堆栈中某一单元, 即提供栈中该单元的偏移量. 加段前缀后, BP可作非堆栈段的地址指针。
* 段寄存器
  * CS寄存器：代码段寄存器，存放当前程序的指令代码。
  * DS寄存器：数据段寄存器，存放程序所涉及的源数据或结果。
  * SS寄存器：堆栈段寄存器，以”先入后出”为原则的数据区。
  * ES寄存器：辅助段寄存器，辅助数据区, 存放串或其他数据。
* VEC寄存器：
* T1寄存器：临时寄存器1.
* T2寄存器：临时寄存器2。

目前共21个寄存器。

#### 532译码器电路实现
使用ROM方式实现(32位数中只有一位为1，表示选中)

<img class="my-img" data-src="../../static/skill/basic/compose/cpu-app/532-decode.png"/>

使用python程序生成532.bin后装载到ROM里：
``` python
with open('532.bin', 'wb') as f:
    for i in range(32):
        var = 1 << i
        byte = var.to_bytes(4, byteorder='little')
        print(byte)
        f.write(byte)

print("生成成功")
```

#### 32位异或门
需要32位异或门，避免对寄存器同时读写。

<img class="my-img" data-src="../../static/skill/basic/compose/cpu-app/32xor.png"/>

#### RC电路实现

<img class="my-img" data-src="../../static/skill/basic/compose/cpu-app/rc.png"/>

组件管脚顺序：

<img class="my-img" data-src="../../static/skill/basic/compose/cpu-app/rc-com.png"/>

#### RC电路测试

<img class="my-img" data-src="../../static/skill/basic/compose/cpu-app/rc-test.png"/>

W=2，表示第二个寄存器写，为01。
R=3，表示第3个寄存器读，为10。

### CPU控制器Control Unit
#### 读写控制器RWC

<img class="my-img" data-src="../../static/skill/basic/compose/cpu-app/rwc.png"/>

#### CPU控制器电路

<img class="my-img" data-src="../../static/skill/basic/compose/cpu-app/CPU-c.png"/>

组件显示如下：

<img class="my-img" data-src="../../static/skill/basic/compose/cpu-app/CPU-c-pin.png"/>

### ALU升级
支持8中操作，分别是加、减、加1、减1、与、或、异或和非。

<img class="my-img" data-src="../../static/skill/basic/compose/cpu-app/ALU-l2.png"/>

* 支持程序状态字PSW
  * 第一位： 有溢出，为1
  * 第二位： 全位0时，为1
  * 第三位： 奇数偶数位，奇数时为1
  * 第四位： 中断标志（未实现）


## CPU实现

<img class="my-img" data-src="../../static/skill/basic/compose/cpu-app/CPU.png"/>

在硬件层面基本设计并实现好了CPU，接下来需要对CPU做软件编程，完成CPU的运行。

## 指令系统
该指令系统是基于寄存器的设计，有多种指令，后续可以不断扩展。（参考汇编语言设计）

### 指令分类
按操作数分类如下：
* 2地址指令
  * MOV A,5; 将常量值5写入到A寄存器
  * ADD B,7; 将B寄存器里的值加7
  * ...
* 1地址指令
  * INC A; A寄存器里的值加1
  * DEC A; A寄存器里的值减1
  * NOT A; A寄存器里的值取反
  * ...
* 0地址指令
  * NOP; 中断指令
  * HLT; 停止指令
  * ...

### 指令中的操作数
* 立即数:是一个常数
* 寄存器操作数：是一个地址，计算速度最快
* 存储器操作数：是一个地址，计算速度最慢

### 指令寻址方式
[指令寻址方式](https://zhuanlan.zhihu.com/p/109398630)有很多种，此处只实现如下4种寻址方式。(微机原理)
* MOV A,5; 立即寻址
* MOV A,B; 寄存器寻址
* MOV A,[5]; 直接寻址
* MOV A,[B]; 寄存器间接寻址

### 指令存储方式
利用16位来存储指令（地址是16进制的）

| 指令 IR 8位 | 程序状态字PSW 4位 | 微程序周期CYC 4位 |

* 2地址指令
  * MOV A,5; 占3个字节
  * IR = 10xx [yy][zz] 
    * 10表示二地址指令标志(67位)
    * xx表示指令助记符（45位）(2位16进制数能表示256个指令)
    * yy表示目标操作数（23位）
    * zz表示源操作数（01位）
* 1地址指令
  * NOT A; 占2个字节
  * IR = 01xx [yyyy]
    * 01表示1地址指令(67位)
    * xx表示指令助记符（45位）(2位16进制数能表示256个指令)
    * yyyy表示目标操作数（0123位）

* 0地址指令
  * HLT; 占一个字节
  * IR=00xx xxxx
    * 00表示0地址指令（67位）
    * xxxxxx表示指令助记符（012345位）（5个16进制数能表示16^5个指令）

## 程序编译器
利用python编写程序编译器，将汇编程序编译为二进制程序码。

代码放到gitee上，地址为：https://gitee.com/mgang/python-study/blob/master/cpu/compiler.py

## 微程序生成器
利用python编写微程序控制器，实现CPU的指令周期。

代码放到gitee上，地址为：https://gitee.com/mgang/python-study/blob/master/cpu/micro-controller.py


## 指令支持实现
原理：将汇编指令通过编译器转换为微程序的微操作，通过将程序（指令）加载到内存后，CPU通过取指周期将指令加载到IR寄存器，将目标操作数加载到DST寄存器，将源操作数加载到SRC寄存器，最后执行。

其中各电路标志定义在如下文件内：https://gitee.com/mgang/python-study/blob/master/cpu/pin.py

### 取指周期 
- 占用6个微操作(已完成)
``` python
FETCH = [
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.IR_IN | pin.PC_INC,
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.DST_IN | pin.PC_INC,
    pin.PC_OUT | pin.MAR_IN,
    pin.RAM_OUT | pin.SRC_IN | pin.PC_INC,
]
```

> [!TIP]
> 重点：指令周期CYC是4位，则一个指令周期内最多执行2^4=16个微操作。取指周期固定需要6个微操作，因此还剩下10个微操作去实现汇编指令。

### 数据传输指令
#### MOV指令
  * 立即寻址 MOV A,5
  * 寄存器寻址 MOV A,B
  * 直接寻址 MOV 0Xcf,5 或者 MOV A,[5]
  * 寄存器间接寻址 MOV A,[B]
支持4种寻址方式，组合后得到12种实现如下：
``` python
# 这个地方不能用'MOV'字符串的key
MOV: {
    # 1. MOV A,5;
    (pin.AM_REG, pin.AM_INS): [
        pin.DST_W | pin.SRC_OUT,
    ],
    # 2. MOV A,B;
    (pin.AM_REG, pin.AM_REG): [
        pin.DST_W | pin.SRC_R
    ],
    # 3. MOV A,[5] or [0x12]
    (pin.AM_REG, pin.AM_DIR): [
        pin.SRC_OUT | pin.MAR_IN,
        pin.RAM_OUT | pin.DST_W
    ],
    # 4. MOV A,[B]
    (pin.AM_REG, pin.AM_RAM): [
        pin.SRC_R | pin.MAR_IN,
        pin.RAM_OUT | pin.DST_W
    ],
    # 5. MOV [5],5 or MOV [0x12],12
    (pin.AM_DIR, pin.AM_INS): [
        pin.DST_OUT | pin.MAR_IN,
        pin.RAM_IN | pin.SRC_OUT
    ],
    # 6. MOV [5],A;
    (pin.AM_DIR, pin.AM_REG): [
        pin.DST_OUT | pin.MAR_IN,
        pin.RAM_IN | pin.SRC_R
    ],
    # 7. MOV [5],[6]
    (pin.AM_DIR, pin.AM_DIR): [
        pin.SRC_OUT | pin.MAR_IN,
        pin.T1_IN | pin.RAM_OUT,
        pin.DST_OUT | pin.MAR_IN,
        pin.RAM_IN | pin.T1_OUT
    ],
    # 8. MOV [5],[A]
    (pin.AM_DIR, pin.AM_RAM): [
        pin.SRC_R | pin.MAR_IN,
        pin.T1_IN | pin.RAM_OUT,
        pin.DST_OUT | pin.MAR_IN,
        pin.RAM_IN | pin.T1_OUT
    ],
    # 9. MOV [A],5;
    (pin.AM_RAM, pin.AM_INS): [
        pin.DST_R | pin.MAR_IN,
        pin.RAM_IN | pin.SRC_OUT
    ],
    # 10. MOV [A],B;
    (pin.AM_RAM, pin.AM_REG): [
        pin.DST_R | pin.MAR_IN,
        pin.RAM_IN | pin.SRC_R
    ],
    # 11. MOV [A],[5]
    (pin.AM_RAM, pin.AM_DIR): [
        pin.SRC_OUT | pin.MAR_IN,
        pin.RAM_OUT | pin.T2_IN,
        pin.DST_R | pin.MAR_IN,
        pin.RAM_IN | pin.T2_OUT
    ],
    # 12. MOV [A],[B]
    (pin.AM_RAM, pin.AM_RAM): [
        pin.SRC_R | pin.MAR_IN,
        pin.RAM_OUT | pin.T2_IN,
        pin.DST_R | pin.MAR_IN,
        pin.RAM_IN | pin.T2_OUT
    ]
}
```
### 算术运算
之前的ALU已经支持了6种操作，分别是加、减、与、或、异或、非；现在扩展2种，分别是加1和减1。（利用硬件来实现++和--，比软件实现简单）

[升级ALU](/skill/basic/compose-cpu-make?id=alu升级)

#### 加法ADD
``` python
ADD: {
    # 1. ADD A,5;
    (pin.AM_REG, pin.AM_INS): [
        pin.DST_R | pin.A_IN,
        pin.SRC_OUT | pin.B_IN,
        pin.OP_ADD | pin.ALU_PSW | pin.DST_W | pin.ALU_OUT
    ],
    # 2. ADD A,B;
    (pin.AM_REG, pin.AM_REG): [
        pin.DST_R | pin.A_IN,
        pin.SRC_R | pin.B_IN,
        pin.OP_ADD | pin.ALU_PSW | pin.DST_W | pin.ALU_OUT
    ]
},
```
#### 减法SUB
``` python
SUB: {
    # 1. SUB A,5;
    (pin.AM_REG, pin.AM_INS): [
        pin.DST_R | pin.A_IN,
        pin.SRC_OUT | pin.B_IN,
        pin.OP_SUB | pin.ALU_PSW | pin.DST_W | pin.ALU_OUT
    ],
    # 2. SUB A,B;
    (pin.AM_REG, pin.AM_REG): [
        pin.DST_R | pin.A_IN,
        pin.SRC_R | pin.B_IN,
        pin.OP_SUB | pin.ALU_PSW | pin.DST_W | pin.ALU_OUT
    ]
},
```
#### 加一INC
``` python
INC: {
    # INC A
    pin.AM_REG: [
        pin.DST_R | pin.A_IN,
        pin.OP_INC | pin.ALU_PSW | pin.DST_W | pin.ALU_OUT
    ]
},
```
#### 减一DEC
``` python
DEC: {
    # DEC A
    pin.AM_REG: [
        pin.DST_R | pin.A_IN,
        pin.OP_DEC | pin.ALU_PSW | pin.DST_W | pin.ALU_OUT
    ]
},
```

### 逻辑运算
支持与、或、异或和非。

#### 与AND
``` python
AND: {
    # 1. AND A,5;
    (pin.AM_REG, pin.AM_INS): [
        pin.DST_R | pin.A_IN,
        pin.SRC_OUT | pin.B_IN,
        pin.OP_AND | pin.ALU_PSW | pin.DST_W | pin.ALU_OUT
    ],
    # 2. AND A,B;
    (pin.AM_REG, pin.AM_REG): [
        pin.DST_R | pin.A_IN,
        pin.SRC_R | pin.B_IN,
        pin.OP_AND | pin.ALU_PSW | pin.DST_W | pin.ALU_OUT
    ]
},
```
#### 或OR
``` python
OR: {
    # 1. OR A,5;
    (pin.AM_REG, pin.AM_INS): [
        pin.DST_R | pin.A_IN,
        pin.SRC_OUT | pin.B_IN,
        pin.OP_OR | pin.ALU_PSW | pin.DST_W | pin.ALU_OUT
    ],
    # 2. OR A,B;
    (pin.AM_REG, pin.AM_REG): [
        pin.DST_R | pin.A_IN,
        pin.SRC_R | pin.B_IN,
        pin.OP_OR | pin.ALU_PSW | pin.DST_W | pin.ALU_OUT
    ]
},
```
#### 异或XOR
``` python
XOR: {
    # 1. XOR A,5;
    (pin.AM_REG, pin.AM_INS): [
        pin.DST_R | pin.A_IN,
        pin.SRC_OUT | pin.B_IN,
        pin.OP_XOR | pin.ALU_PSW | pin.DST_W | pin.ALU_OUT
    ],
    # 2. XOR A,B;
    (pin.AM_REG, pin.AM_REG): [
        pin.DST_R | pin.A_IN,
        pin.SRC_R | pin.B_IN,
        pin.OP_XOR | pin.ALU_PSW | pin.DST_W | pin.ALU_OUT
    ]
}
```
#### 非NOT
``` python
NOT: {
    # NOT A
    pin.AM_REG: [
        pin.DST_R | pin.A_IN,
        pin.OP_NOT | pin.ALU_PSW | pin.DST_W | pin.ALU_OUT
    ]
},
```

* 标记转移
* 条件转移
* 堆栈操作
* 函数调用
* 内中断

<script>
(function(){
  // js部分如下
  const images = document.querySelectorAll('img')
  // callback是回调函数，，那么一般是需要触发条件才能执行的，一般触发两次（一次为看见目标元素时，另一次为目标元素卡看不见时）
  const callback = entries => {
      entries.forEach(entry => {
          // console.log(entry)
          // entry.isIntersecting为目标元素
          if (entry.isIntersecting) {
              const image = entry.target
              const data_src = image.getAttribute('data-src')
              image.setAttribute('src', data_src)
              // 结束观察，有几张图片就会触发几次
              observer.unobserve(image)
          }
      })
  }
  // 因为IntersectionObserver是构造函数，所以第一步要new一个实例
  const observer = new IntersectionObserver(callback)
  console.info(observer)
  images.forEach(image => {
          // 开始观察
          observer.observe(image)
  })
})();
</script>

