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

目前共22个寄存器。

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
利用16位来存储指令
| 指令 IR 8位 | 程序状态字PSW 4位 | 微程序周期CYC 4位 |
* 2地址指令
  * MOV A,5; 占3个
* 1地址指令
  * NOT A; 占2个
* 0地址指令
  * HLT; 占一个

## 程序编译器

## 微程序生成器



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

