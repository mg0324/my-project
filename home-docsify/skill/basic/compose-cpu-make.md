> 本篇章主要完成对一个8位CPU的设计和实现。

## 前情分析
一个8位CPU设计时，需要实现基础硬件、CPU框架、指令系统、微程序和编译器。

<img class="my-img" data-src="../../static/skill/basic/compose/cpu-app/base.png"/>


## 硬件部分
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

