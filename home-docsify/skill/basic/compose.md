## 缘起

为了更好地学习计算机的组成原理，在此将先抛出计算机组成原理的示意图，然后慢慢深入及展开各个组成部分的设计及实现。

![计算机组成](../../static/skill/basic/compose/art.png )

### 主要组成部分

* CPU
* 内存
* 总线
* 输入输出设备

## 修行[CPU]

### 缘分

为了知晓了CPU的实现原理，在B站搜索**CPU实现**后，找到了一个非常好的资源叫做[一个8位二进制CPU的设计和实现](https://www.bilibili.com/video/BV1aP4y1s7Vf/?spm_id_from=333.999.0.0&vd_source=e7848c18842bb234f7a561509976445e)。

看了之后不仅解开了心中的疑惑，也更加了解熟悉CPU了，感谢UP主[踌躇月光](https://space.bilibili.com/491131440)的分享。

故本节内容多参考以上视频内容，可理解为笔记整理。

### CPU的组成

CPU全称为`central processing unit`，又称中央处理器，芯片样式如下图：

![](../../static/skill/basic/compose/cpu/cpu.png )

其组成部分如下图：

![](../../static/skill/basic/compose/cpu/cpu-compose.png )

可以分为运算器和控制器，还有一些缓存（目前工艺多为3级缓存）：

* 运算器
  * 算术逻辑单元 ALU
  * 寄存器（暂存寄存器、累加寄存器、通用寄存器组、标志寄存器等）
* 控制器
  * 程序计数器 PC
  * 指令寄存器 IR
  * 指令译码器
  * 时序信号发生器（时钟频率）
  * 微程序控制器
  * ...

### 前置条件

需要具备如下技能：

* 数字逻辑基础 知道3大逻辑门（与And、或Or、非Not）
* 数字电路软件 [Logic Circuit](https://www.logiccircuit.org/download.html)

### 半加器

#### 定义

*半加器*电路是指对两个输入数据位相加，输出一个结果位和进位，没有进位输入的加法器电路。

#### 真值表

A：数值a | B：数值b | S：结果sum | C：进位carry


| A | B | S | C |
| - | - | - | - |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

#### 公式

$$
S = AB

$$

```plaintext
S = A^B (A异或B)
C = A&B (A与B)
```

#### 电路实现

![](../../static/skill/basic/compose/cpu/half-adder.png )

#### 电路测试

![](../../static/skill/basic/compose/cpu/ha-test.gif )
