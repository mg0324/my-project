> 请先学习基础篇。

## 存储器相关组件

### 8位存储器

#### 定义

首先我们知道一个D边沿触发器能存储一位数据，则将8个组合起来存储8位（1个字节）的存储器。

#### 电路实现

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/byte.png"/>

#### 电路测试

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/byte-test.gif"/>

### 8位3态门开关

#### 定位

当一条线路上连接了多个器件时，需要通过3态门来控制哪些连接，哪些断开。

面对一个8位的输入，因此需要8位的3态门开关对应。

#### 电路实现

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/8B-3T.png"/>

#### 电路测试

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/8B-3T-test.gif"/>

### 8位寄存器

#### 定义

利用存储器存一个字节数据基础上，加上读写控制位。

#### 电路实现

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/register.png"/>

#### 电路测试

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/register-test.gif"/>

### 38译码器

#### 定义

在组合8个寄存器用来存储8个字节的数据时，遇到一个问题：如何每次只能选中8个寄存器中的一个进行读写？

此时就需要38译码器来做选择控制了。

#### 参数说明

3位输入8位输出，只有一个为1，为1的位置表示选中。

#### 真值表


| A2 | A1 | A0 | B7 | B6 | B5 | B4 | B3 | B2 | B1 | B0 |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| 0  | 0  | 0  | -  | -  | -  | -  | -  | -  | -  | 1  |
| 0  | 0  | 1  | -  | -  | -  | -  | -  | -  | 1  | -  |
| 0  | 1  | 0  | -  | -  | -  | -  | -  | 1  | -  | -  |
| 0  | 1  | 1  | -  | -  | -  | -  | 1  | -  | -  | -  |
| 1  | 0  | 0  | -  | -  | -  | 1  | -  | -  | -  | -  |
| 1  | 0  | 1  | -  | -  | 1  | -  | -  | -  | -  | -  |
| 1  | 1  | 0  | -  | 1  | -  | -  | -  | -  | -  | -  |
| 1  | 1  | 1  | 1  | -  | -  | -  | -  | -  | -  | -  |

#### 公式

* B0 = A2‘A1‘A0’ （A2取反 与上 A1取反 与上 A0取反）
* B1 = A2‘A1‘A0 （A2取反 与上 A1取反 与上 A0）
* B2 = A2‘A1A0’ （A2取反 与上 A1 与上 A0取反）
* B3 = A2‘A1A0 （A2取反 与上 A1 与上 A0）
* B4 = A2A1‘A0’ （A2 与上 A1取反 与上 A0取反）
* B5 = A2A1‘A0 （A2 与上 A1取反 与上 A0）
* B6 = A2A1A0’ （A2 与上 A1 与上 A0取反）
* B7 = A2A1A0 （A2 与上 A1 与上 A0）

#### 电路实现

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/38S.png"/>

#### 电路测试

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/38S-test.gif"/>

### 8字节存储器

#### 定义

组合8个1字节寄存器组件，利用38译码器选中每次要读写的1个字节寄存器来做数据读取和写入。

#### 电路实现

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/8Byte.png"/>

#### 电路测试

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/8Byte-test.gif"/>

#### 优化后电路

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/8Byte-yh.png"/>

输入优化位CS和WE。（片选信号和写启用信号）

### 存储器扩展

#### 定义

组合2个8x1的字节的存储器，得到8x2字节的存储器。有2种扩展方式，分别是位扩展和字扩展。

#### 位扩展电路实现

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/16Byte.png"/>

如上图，将2个8x1字节的存储器横向组合，使得数据宽度变成了8x2字节，则称为位扩展。

#### 位扩展电路测试

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/16Byte-test.gif"/>

#### 字扩展电路实现

因为16x1是2个8x1的存储器通过字扩展（扩展地址线）组合的，所以需要用到12译码器。（片选其中一个芯片）

##### 12译码器电路

和38译码器类似。

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/12-select.png"/>

##### 低位交叉编址

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/16x1-L.png"/>

##### 高位交叉编址

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/16x1-H.png"/>

> [!TIP]
> 低位交叉编址推荐使用，因为低位01交替，这样能交替选择不同片，效率高。（同一个组件连续访问需要有一定间隔）

##### 电路测试

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/16x1-test.png"/>

有16个1字节的存储器，通过地址线切换不同的芯片存储数据。

### 存储器的问题

#### 同时读写的问题

可以参考D触发器中Reset和Set不能同时为1的处理逻辑。
将输入从R和W，调整位WE，表示写启用。

#### 接入片选信号

将片选信号作为输入，作为3态门的输入条件之一。

#### 寄存器优化后电路

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/byte-yh.png"/>

#### 寄存器优化后电路测试

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/8byte-yh-test.png"/>

CS=1，输出无法同时读写。

#### 8x1byte优化后电路

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/8x1-byte-yh.png"/>

#### 8x2byte优化后电路

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/8x2-byte-yh.png"/>

#### 16x1高位优化后电路

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/16x1-byte-H-yh.png"/>

#### 16x1低位优化后电路

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/16x1-byte-L-yh.png"/>


### 3位计数器
#### 定义
在做片选时，需要在8个芯片中选一个索引，因此需要加1的计数器，范围从0-7。
所以可以参考[8位行波极速器](/skill/basic/compose-cpu?id=行波计数器)做出3位的计数器。

#### 电路实现

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/3CT.png"/>

#### 电路测试

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/3CT-test.gif"/>

#### 接入地址输入应用

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/3CT-yy-test.gif"/>

## 核心组件
### ALU
支持加法和减法的ALU实现，详细请参考[ALU](/skill/basic/compose-cpu?id=alu支持加法和减法)

#### ALU增强
* 支持程序状态字
    * 第一位： 有溢出，为1
    * 第二位： 全位0时，为1
    * 第三位： 奇数偶数位
    * 第四位： 中断标志（未实现）
* 支持的运算（通过OP切换）
    * 8位加法(OP=0)
    * 8位减法(OP=1)
    * 8位逻辑与(OP=2)
    * 8位逻辑或(OP=3)
    * 8位逻辑异或(OP=4)
    * 8位逻辑取反（已经有了，请参考[8位取反器](/skill/basic/compose-cpu?id=_8位取反器))(OP=5)

#### 8位逻辑运算组件封装
只贴出8位逻辑与，结构类似，比较简单。

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/8B-and.png"/>

#### ALU增强后电路

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/ALU-super.png"/>

#### ALU增强后测试

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/ALU-super-test.png"/>

### 寄存器
* [优化前版本](/skill/basic/compose-cpu?id=_8位寄存器)
* [寄存器优化后版本](/skill/basic/compose-cpu?id=寄存器优化后电路)

### 开机电路
#### 参数说明
* 输入
    * Reset：重置信号
    * Power：电源信号
    * Manual： 手动信号
    * Pul： 手动点击信号
    * Halt： 暂停信号
    * CP：时钟信号
* 输出：
    * Reset：重置信号
    * CP：时钟信号

#### 电路实现

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/POW.png"/>

#### 电路测试

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/POW-test.gif"/>

### 程序计数器PC
#### 定义
需要支持写入的增1计数器。

#### 电路实现

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/PC.png"/>

#### 电路测试

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/PC-test.gif"/>

### 内存控制器
#### 说明
其实[存储器相关](/skill/basic/compose-cpu?id=存储器相关组件)的就是内存，但是没有提供的RAM好用。

#### 电路实现

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/MC-1.png"/>

用来控制RAM内存的。

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/MC-2.png"/>

#### 电路测试

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/MC-test.jpg"/>

### 总线
可以理解为就是一条线，连接到总线上的组件需要有3态门的支持。（某一个时刻只有一个连通）

目前计算机中有数据总线、地址总线、指令总线等。

## 应用实践
### 半自动加法机
#### 定义
需求：将1到5连续做加法运输，半自动电路实现。

#### 实现说明
* 将1,2,3,4,5分别存到ROM中。
* 利用3位计数器改变地址线。
* 利用ALU实现加法。
* 将加好的结果存到寄存器中。

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/half-ALU-ROM.png"/>

#### 电路实现

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/half-ALU.png"/>

#### 电路测试

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/half-ALU-test.gif"/>


### 全自动加法机
#### 说明
基于[POW开机电路](/skill/basic/compose-cpu?id=开机电路)，将上面半自动加法机修改为全自动加法机。

#### 电路实现

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/auto-ALU.png"/>

在时钟下降沿时读取ROM中的值做加法，在上升沿的时候将加法结果存到寄存器。

#### 电路测试

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/auto-ALU-test.gif"/>

## 微程序控制
### 说明
用微程序来实现指令系统或某些特定控制功能。

### 应用示例说明
有如下RAM内存：

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/RAM.jpg"/>

内存里00地址的值为3，01地址的值为4，02地址的值为9。
计算9-(3+4)=2结果设置到第03地址上。

### 前置处理
让ALU加上三态门，支持连接到总线上。

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/ALU-with-bus.png"/>

### 电路实现

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/micro-app.png"/>

其中微程序控制序列存在ROM中，通过位状态来控制电路运行。

### python编写微程序

``` python
A_WE = 2 ** 0
A_CS = 2 ** 1

B_WE = 2 ** 2
B_CS = 2 ** 3

ALU_SUB = 2 ** 4
ALU_EN = 2 ** 5

C_WE = 2 ** 6
C_CS = 2 ** 7

MC_WE = 2 ** 8
MC_CS = 2 ** 9

PC_WE = 2 ** 10
PC_EN = 2 ** 11
PC_CS = 2 ** 12

HLT = 2 ** 15

micro = [
    # 内存里1地址的数据放到总线上，并存到A寄存器中,PC计数器加一
    A_WE | A_CS | MC_CS | PC_EN | PC_CS | PC_WE,
    # 将内存里2地址的数据写到B寄存器中
    B_WE | B_CS | MC_CS,
    # A寄存器值加B寄存器值计算加法，将结果存到C寄存器，PC计数器加一
    A_CS | B_CS | ALU_EN | C_CS | C_WE | PC_EN | PC_CS | PC_WE,
    # 将C寄存器里的加法结果写入到B寄存器
    B_WE | B_CS | C_CS,
    # 将内存地址3上的数据存到寄存器A
    A_WE | A_CS | MC_CS,
    # A寄存器值减B寄存器值，将结果存到C寄存器，PC计数器加一
    A_CS | B_CS | ALU_EN | ALU_SUB | C_CS | C_WE | PC_EN | PC_CS | PC_WE,
    # 将C寄存器里的结果写入到内存地址4中
    MC_WE | MC_CS | C_CS,
    # 停止
    HLT,
]

with open('micro.bin', 'wb') as f:
    for var in micro:
        byte = var.to_bytes(2, byteorder='little')
        f.write(byte)
        print(var, byte)

print('生成成功')
```
生成的二进制文件装载到ROM中即可。

### 微程序测试

<img class="my-img" data-src="../../static/skill/basic/compose/cpu/micro-app-test.gif"/>


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