> 2022年7月读 葛一鸣的《Java高并发程序设计实现》 第二版的总结笔记。
## 走近并行
* [走入并行的世界](http://mg.meiflower.top/mb/post/juc/%E8%B5%B0%E5%85%A5%E5%B9%B6%E8%A1%8C%E7%9A%84%E4%B8%96%E7%95%8C/)
    1. <card-link id="78cf61c2d82944e7aeeb97512b762e94" title="摩尔定律逼并行"/>
    2. <card-link id="591fa19932e6473bad2798ff44bc06d5" title="同步vs异步"/>
    3. <card-link id="bc2284d4ca3c42e8b1d2115281dc90c7" title="并发vs并行"/>
    4. <card-link id="8c62b75aae4c4bc48108a376ea72a3f7" title="临界区"/>
    5. <card-link id="5bd0fbc85b7f42c2a51c1baee19f3af5" title="死锁vs饥饿vs活锁"/>
    6. <card-link id="5f3245cc14434434810bece36ea97125" title="5大并发级别"/>
    7. <card-link id="17f82a320a204cccac55ccd85baa61f0" title="并行加速比公式"/>

* [并行程序基础](http://mg.meiflower.top/mb/post/juc/%E5%B9%B6%E8%A1%8C%E7%A8%8B%E5%BA%8F%E5%9F%BA%E7%A1%80/)
    1. <card-link id="c74286688a2c4031b3b0a6a3735035eb" title="程序进程线程"/>
    2. <card-link id="0c00306f92a0407c8383ba9398da5bac" title="线程生命周期"/>
    3. <card-link id="5abb537ae59c404d89fa8521add21e24" title="Java线程状态"/>
    4. <card-link id="07c17a5de6dc46298c4d6baa95d78c4d" title="线程基本操作"/>
    5. <card-link id="0d9c36a734be4b958e3a2f064f3179dc" title="线程组"/>
    6. <card-link id="4a75d892bf914d9cb4bb93abc465da88" title="守护线程"/>
    7. <card-link id="8bbfeee1dc3d4f35a0288f392d095246" title="优先级"/>

## Java内存模型
* [熟悉Java内存模型JMM](http://mg.meiflower.top/mb/post/juc/%E7%86%9F%E6%82%89Java%E5%86%85%E5%AD%98%E6%A8%A1%E5%9E%8BJMM/)
    1. [内存模型重点关注：原子性、可见性、有序性](http://mg.meiflower.top/mb/images/juc/jmm/01.png)
    2. [内存模型关系图](http://mg.meiflower.top/mb/images/juc/jmm/011.png)
    3. <card-link id="03449da0f3374293b2ce82d84878d558" title="JMM8大原子操作"/>
    4. <card-link id="5fa6fa394aef4e7ea0611236327f26b0" title="指令重排序"/>
    5. 哪些指令不能重排序？ <card-link id="9f81309f85584ae182f1046ec7c515d7" title="Happen Before8大原则"/>

## Java的线程实现
* [Java的线程实现](http://mg.meiflower.top/mb/post/juc/Java%E7%9A%84%E7%BA%BF%E7%A8%8B%E5%AE%9E%E7%8E%B0/)
    1. <card-link id="a94865d218bc49869cda6e392497903c" title="3种线程模型"/>
    2. <card-link id="8222484d4443413cb60ad722368a3408" title="使用内核线程实现的模式"/>
    3. <card-link id="550596dfcb5d44f0a3953a51fd90659c" title="使用用户线程实现的模式"/>
    4. <card-link id="c3e44d856ed944169754595c6c315ede" title="使用用户线程和轻量级线程混合实现的模式"/>
    5. <card-link id="872dca99d1eb4b35b2e5d5153b968713" title="Java的线程实现"/>
    5. <card-link id="30c046ed8ca346aea176c38777cdfeef" title="Java的线程调度"/>

## 线程池
* [线程池入门到精通](http://mg.meiflower.top/mb/post/juc/%E7%BA%BF%E7%A8%8B%E6%B1%A0%E5%85%A5%E9%97%A8%E5%88%B0%E7%B2%BE%E9%80%9A/)


## Java并发的努力
* [Java关键字volatile](http://mg.meiflower.top/mb/post/juc/Java%E5%85%B3%E9%94%AE%E5%AD%97%E4%B9%8Bvolatile/)
* [Java多线程间同步控制方法](http://mg.meiflower.top/mb/post/juc/Java%E5%A4%9A%E7%BA%BF%E7%A8%8B%E5%90%8C%E6%AD%A5%E6%8E%A7%E5%88%B6%E6%96%B9%E6%B3%95/) 包含旧的同步方式，和1.5后新增的JUC并发包里的锁
    - synchronized关键字
    - ReentrantLock和Condition可重入锁
    - 信号量 Semaphore
    - 读写锁 ReadWriteLock
    - 倒计数器 CountDownLatch
    - 循环栅栏 CyclicBarrier
    - 阻塞工具类 LockSupport
* [Java关键字synchronized](http://mg.meiflower.top/mb/post/juc/Java%E5%85%B3%E9%94%AE%E5%AD%97synchronized/)


## 并发模式
* [并发模式之单例和不变模式](http://mg.meiflower.top/mb/post/juc/%E5%B9%B6%E5%8F%91%E6%A8%A1%E5%BC%8F%E4%B9%8B%E5%8D%95%E4%BE%8B%E5%92%8C%E4%B8%8D%E5%8F%98%E6%A8%A1%E5%BC%8F/)
* [并发模式之生产者消费者模式](http://mg.meiflower.top/mb/post/juc/%E5%B9%B6%E5%8F%91%E6%A8%A1%E5%BC%8F%E4%B9%8B%E7%94%9F%E4%BA%A7%E8%80%85%E6%B6%88%E8%B4%B9%E8%80%85%E6%A8%A1%E5%BC%8F/)
* [并发模式之异步回调Future模式](http://mg.meiflower.top/mb/post/juc/%E5%B9%B6%E5%8F%91%E6%A8%A1%E5%BC%8F%E4%B9%8B%E5%BC%82%E6%AD%A5%E5%9B%9E%E8%B0%83Future%E6%A8%A1%E5%BC%8F/)