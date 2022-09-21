## Java语言类型及长度
> Java中方法的实参到形参的传递，基础类型是值传递。
<!-- tabs:start -->
#### **byte 1字节**

```
基本类型：byte 二进制位数：8
包装类：java.lang.Byte
最小值：Byte.MIN_VALUE=-128
最大值：Byte.MAX_VALUE=127
```

#### **short 2字节**

```
基本类型：short 二进制位数：16
包装类：java.lang.Short
最小值：Short.MIN_VALUE=-32768
最大值：Short.MAX_VALUE=32767
```

#### **char 2字节**
```
基本类型：char 二进制位数：16
包装类：java.lang.Character
最小值：Character.MIN_VALUE=0
最大值：Character.MAX_VALUE=65535
```

#### **int 4字节**

```
基本类型：int 二进制位数：32
包装类：java.lang.Integer
最小值：Integer.MIN_VALUE=-2147483648
最大值：Integer.MAX_VALUE=2147483647
```

#### **long 8字节**

```
基本类型：long 二进制位数：64
包装类：java.lang.Long
最小值：Long.MIN_VALUE=-9223372036854775808
最大值：Long.MAX_VALUE=9223372036854775807
```

#### **float 4字节**

```
基本类型：float 二进制位数：32
包装类：java.lang.Float
最小值：Float.MIN_VALUE=1.4E-45
最大值：Float.MAX_VALUE=3.4028235E38
```

#### **double 8字节**
```
基本类型：double 二进制位数：64
包装类：java.lang.Double
最小值：Double.MIN_VALUE=4.9E-324
最大值：Double.MAX_VALUE=1.7976931348623157E308
```

<!-- tabs:end -->

## Java里String的长度？
通过查看String类的源码：
``` java
public final class String
    implements java.io.Serializable, Comparable<String>, CharSequence {
    /** 使用字符数组存储，并修饰为final */
    private final char value[];
    // 省略
    public int length() {
        return value.length;
    }
}
```
可以看出长度返回值是int类型的值，故运行期长度为2^32-1，约512M，也受到堆内存大小约束。
而在编译时会存储到常量池里，以`CONSTANT_Utf8_info`类型存储，其长度为u2，表示2个字节，即2^16-1，约65535位，65535/8/1024=8K。
``` c
CONSTANT_Utf8_info {
    u1 tag;
    u2 length;
    u1 bytes[length];
}
```
> [!TIP]
> 总结：String在编译器常量赋值时，长度不超过65535，约8K（超过则会变异报错）。
> 运行期时，长度理论上是int的最大值2^32-1，约512M，当然也受到堆内存大小约束。

## C语言基础类型及长度
请看如下代码：
``` c
#include <stdio.h>

int main() {
    printf("char size is %d byte\n", sizeof(char));
    printf("short size is %d byte\n", sizeof(short));
    printf("int size is %d byte\n", sizeof(int));
    printf("long size is %d byte\n", sizeof(long));
    printf("float size is %d byte\n", sizeof(float));
    printf("double size is %d byte\n", sizeof(double));
    printf("long double size is %d byte\n", sizeof(long double));
    return 0;
}
```
结果：
```
char size is 1 byte
short size is 2 byte
int size is 4 byte
long size is 8 byte
float size is 4 byte
double size is 8 byte
long double size is 16 byte
```


## Redis的key的长度
redis中key的底层数据结构是c语言实现的sds动态字符串类型：
``` c
struct sdshdr{
    int len # 记录当前字符串容量
    int free # 记录buf中没有使用的容量
    char buf[]  # 用于保存字符串的值
}
```
> [!TIP]
> 总结：长度类型为int(c语言int占4字节），故长度为2^32-1，约512M。

## Kafka消息长度
* broker

    `message.max.bytes`: kafka允许的最大的一个批次的消息大小，默认为1000012字节，约1M。（简单的说就是kakfa消息的集合批次，一个批次可以包含多条消息）

* topic

    `max.message.bytes`: 该配置和broker里的一样，一个是全局的，一个是指定某个topic的批次消息大小。

* producer

    `max.request.size`: 请求的最大字节数，默认为1048576字节，即1M。

    `batch.size`: 当将多个记录被发送到同一个分区时， Producer 将尝试将记录组合到更少的请求中。这有助于提升客户端和服务器端的性能。这个配置控制一个批次的默认大小（以字节为单位）。
    当记录的大小超过了配置的字节数， Producer 将不再尝试往批次增加记录。默认值为16384字节，即16K。

    > [!TIP]
    > 通常来说，max.request.size 大于 batch.size，这样每次发送消息通常会包含多个 ProducerBatch。

* consumer

    `fetch.min.bytes`: 消费者从borker获取的最小消息大小，默认为1字节。如果不足，则需等待数据。

    `fetch.max.bytes`: 服务器为获取请求应返回的最大数据量。默认为52428800字节，即50M。
    消费者将批量获取记录，并且如果获取的第一个非空分区中的第一个记录批次大于此值，则仍将返回记录批次以确保使用者可以取得进展。因此，这不是绝对最大值。代理可接受的最大记录批处理大小是通过“ message.max.bytes”（代理配置）或“ max.message.bytes”（主题配置）定义的。请注意，消费者并行执行多个提取。

    `max.partition.fetch.bytes`: 服务器将返回的每个分区的最大数据量，默认1048576字节，即1M。