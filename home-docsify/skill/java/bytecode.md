<!-- 引入 layui.css -->
<link href="//unpkg.com/layui@2.7.6/dist/css/layui.css" rel="stylesheet">

> 参考 周志磊的《深入理解Java虚拟机》 附录C 
<div id="container">
    <h2>虚拟机字节码指令表</h2>
    <table class="layui-table">
        <colgroup>
            <col width="150">
            <col width="200">
            <col>
        </colgroup>
        <thead>
            <tr>
            <th>字节码</th>
            <th>助记符</th>
            <th>指令描述</th>
            </tr> 
        </thead>
        <tbody>
            <tr v-for="(node,index) in nodes" :key="index">
                <td>{{node.opcode}}</td>
                <td>{{node.opstr}}</td>
                <td>{{node.remark}}</td>
            </tr>
        </tbody>
    </table>
</div>




<script>
    (function(){
         new Vue({
            el:'#container',
            data() {
                return {
                    nodes: [
                        {
                            "opcode": "0x00",
                            "opstr": "nop",
                            "remark": "None"
                        },
                        {
                            "opcode": "0x01",
                            "opstr": "aconst_null",
                            "remark": "将null推送至栈顶"
                        },
                        {
                            "opcode": "0x02",
                            "opstr": "iconst_m1",
                            "remark": "将int型-1推送至栈顶"
                        },
                        {
                            "opcode": "0x03",
                            "opstr": "iconst_0",
                            "remark": "将int型0推送至栈顶"
                        },
                        {
                            "opcode": "0x04",
                            "opstr": "iconst_1",
                            "remark": "将int型1推送至栈顶"
                        },
                        {
                            "opcode": "0x05",
                            "opstr": "iconst_2",
                            "remark": "将int型2推送至栈顶"
                        },
                        {
                            "opcode": "0x06",
                            "opstr": "iconst_3",
                            "remark": "将int型3推送至栈顶"
                        },
                        {
                            "opcode": "0x07",
                            "opstr": "iconst_4",
                            "remark": "将int型4推送至栈顶"
                        },
                        {
                            "opcode": "0x08",
                            "opstr": "iconst_5",
                            "remark": "将int型5推送至栈顶"
                        },
                        {
                            "opcode": "0x09",
                            "opstr": "lconst_0",
                            "remark": "将long型0推送至栈顶"
                        },
                        {
                            "opcode": "0x0a",
                            "opstr": "lconst_1",
                            "remark": "将long型1推送至栈顶"
                        },
                        {
                            "opcode": "0x0b",
                            "opstr": "fconst_0",
                            "remark": "将float型0推送至栈顶"
                        },
                        {
                            "opcode": "0x0c",
                            "opstr": "fconst_1",
                            "remark": "将float型1推送至栈顶"
                        },
                        {
                            "opcode": "0x0d",
                            "opstr": "fconst_2",
                            "remark": "将float型2推送至栈顶"
                        },
                        {
                            "opcode": "0x0e",
                            "opstr": "dconst_0",
                            "remark": "将double型0推送至栈顶"
                        },
                        {
                            "opcode": "0x0f",
                            "opstr": "dconst_1",
                            "remark": "将double型1推送至栈顶"
                        },
                        {
                            "opcode": "0x10",
                            "opstr": "bipush",
                            "remark": "将单字节的常量值(-128~127)推送至栈顶"
                        },
                        {
                            "opcode": "0x11",
                            "opstr": "sipush",
                            "remark": "将一个短整型常量(-32768~32767)推送至栈顶"
                        },
                        {
                            "opcode": "0x12",
                            "opstr": "ldc",
                            "remark": "将int,float或String型常量值从常量池中推送至栈顶"
                        },
                        {
                            "opcode": "0x13",
                            "opstr": "ldc_w",
                            "remark": "将int,float或String型常量值从常量池中推送至栈顶(宽索引)"
                        },
                        {
                            "opcode": "0x14",
                            "opstr": "ldc2_w",
                            "remark": "将long或double型常量值从常量池中推送至栈顶(宽索引)"
                        },
                        {
                            "opcode": "0x15",
                            "opstr": "iload",
                            "remark": "将指定的int型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x16",
                            "opstr": "lload",
                            "remark": "将指定的long型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x17",
                            "opstr": "fload",
                            "remark": "将指定的float型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x18",
                            "opstr": "dload",
                            "remark": "将指定的double型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x19",
                            "opstr": "aload",
                            "remark": "将指定的引用类型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x1a",
                            "opstr": "iload_0",
                            "remark": "将第一个int型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x1b",
                            "opstr": "iload_1",
                            "remark": "将第二个int型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x1c",
                            "opstr": "iload_2",
                            "remark": "将第三个int型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x1d",
                            "opstr": "iload_3",
                            "remark": "将第四个int型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x1e",
                            "opstr": "lload_0",
                            "remark": "将第一个long型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x1f",
                            "opstr": "lload_1",
                            "remark": "将第二个long型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x20",
                            "opstr": "lload_2",
                            "remark": "将第三个long型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x21",
                            "opstr": "lload_3",
                            "remark": "将第四个long型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x22",
                            "opstr": "fload_0",
                            "remark": "将第一个float型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x23",
                            "opstr": "fload_1",
                            "remark": "将第二个float型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x24",
                            "opstr": "fload_2",
                            "remark": "将第三个float型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x25",
                            "opstr": "fload_3",
                            "remark": "将第四个float型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x26",
                            "opstr": "dload_0",
                            "remark": "将第一个double型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x27",
                            "opstr": "dload_1",
                            "remark": "将第二个double型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x28",
                            "opstr": "dload_2",
                            "remark": "将第三个double型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x29",
                            "opstr": "dload_3",
                            "remark": "将第四个double型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x2a",
                            "opstr": "aload_0",
                            "remark": "将第一个引用类型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x2b",
                            "opstr": "aload_1",
                            "remark": "将第二个引用类型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x2c",
                            "opstr": "aload_2",
                            "remark": "将第三个引用类型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x2d",
                            "opstr": "aload_3",
                            "remark": "将第四个引用类型本地变量推送至栈顶"
                        },
                        {
                            "opcode": "0x2e",
                            "opstr": "iaload",
                            "remark": "将int型数组指定索引的值推送至栈顶"
                        },
                        {
                            "opcode": "0x2f",
                            "opstr": "laload",
                            "remark": "将long型数组指定索引的值推送至栈顶"
                        },
                        {
                            "opcode": "0x30",
                            "opstr": "faload",
                            "remark": "将float型数组指定索引的值推送至栈顶"
                        },
                        {
                            "opcode": "0x31",
                            "opstr": "daload",
                            "remark": "将double型数组指定索引的值推送至栈顶"
                        },
                        {
                            "opcode": "0x32",
                            "opstr": "aaload",
                            "remark": "将引用类型数组指定索引的值推送至栈顶"
                        },
                        {
                            "opcode": "0x33",
                            "opstr": "baload",
                            "remark": "将boolean或byte型数组指定索引的值推送至栈顶"
                        },
                        {
                            "opcode": "0x34",
                            "opstr": "caload",
                            "remark": "将char型数组指定索引的值推送至栈顶"
                        },
                        {
                            "opcode": "0x35",
                            "opstr": "saload",
                            "remark": "将short型数组指定索引的值推送至栈顶"
                        },
                        {
                            "opcode": "0x36",
                            "opstr": "istore",
                            "remark": "将栈顶int型数值存入指定本地变量"
                        },
                        {
                            "opcode": "0x37",
                            "opstr": "lstore",
                            "remark": "将栈顶long型数值存入指定本地变量"
                        },
                        {
                            "opcode": "0x38",
                            "opstr": "fstore",
                            "remark": "将栈顶float型数值存入指定本地变量"
                        },
                        {
                            "opcode": "0x39",
                            "opstr": "dstore",
                            "remark": "将栈顶double型数值存入指定本地变量"
                        },
                        {
                            "opcode": "0x3a",
                            "opstr": "astore",
                            "remark": "将栈顶引用类型数值存入指定本地变量"
                        },
                        {
                            "opcode": "0x3b",
                            "opstr": "istore_0",
                            "remark": "将栈顶int型数值存入第一个本地变量"
                        },
                        {
                            "opcode": "0x3c",
                            "opstr": "istore_1",
                            "remark": "将栈顶int型数值存入第二个本地变量"
                        },
                        {
                            "opcode": "0x3d",
                            "opstr": "istore_2",
                            "remark": "将栈顶int型数值存入第三个本地变量"
                        },
                        {
                            "opcode": "0x3e",
                            "opstr": "istore_3",
                            "remark": "将栈顶int型数值存入第四个本地变量"
                        },
                        {
                            "opcode": "0x3f",
                            "opstr": "lstore_0",
                            "remark": "将栈顶long型数值存入第一个本地变量"
                        },
                        {
                            "opcode": "0x40",
                            "opstr": "lstore_1",
                            "remark": "将栈顶long型数值存入第二个本地变量"
                        },
                        {
                            "opcode": "0x41",
                            "opstr": "lstore_2",
                            "remark": "将栈顶long型数值存入第三个本地变量"
                        },
                        {
                            "opcode": "0x42",
                            "opstr": "lstore_3",
                            "remark": "将栈顶long型数值存入第四个本地变量"
                        },
                        {
                            "opcode": "0x43",
                            "opstr": "fstore_0",
                            "remark": "将栈顶float型数值存入第一个本地变量"
                        },
                        {
                            "opcode": "0x44",
                            "opstr": "fstore_1",
                            "remark": "将栈顶float型数值存入第二个本地变量"
                        },
                        {
                            "opcode": "0x45",
                            "opstr": "fstore_2",
                            "remark": "将栈顶float型数值存入第三个本地变量"
                        },
                        {
                            "opcode": "0x46",
                            "opstr": "fstore_3",
                            "remark": "将栈顶float型数值存入第四个本地变量"
                        },
                        {
                            "opcode": "0x47",
                            "opstr": "dstore_0",
                            "remark": "将栈顶double型数值存入第一个本地变量"
                        },
                        {
                            "opcode": "0x48",
                            "opstr": "dstore_1",
                            "remark": "将栈顶double型数值存入第二个本地变量"
                        },
                        {
                            "opcode": "0x49",
                            "opstr": "dstore_2",
                            "remark": "将栈顶double型数值存入第三个本地变量"
                        },
                        {
                            "opcode": "0x4a",
                            "opstr": "dstore_3",
                            "remark": "将栈顶double型数值存入第四个本地变量"
                        },
                        {
                            "opcode": "0x4b",
                            "opstr": "astore_0",
                            "remark": "将栈顶引用型数值存入第一个本地变量"
                        },
                        {
                            "opcode": "0x4c",
                            "opstr": "astore_1",
                            "remark": "将栈顶引用型数值存入第二个本地变量"
                        },
                        {
                            "opcode": "0x4d",
                            "opstr": "astore_2",
                            "remark": "将栈顶引用型数值存入第三个本地变量"
                        },
                        {
                            "opcode": "0x4e",
                            "opstr": "astore_3",
                            "remark": "将栈顶引用型数值存入第四个本地变量"
                        },
                        {
                            "opcode": "0x4f",
                            "opstr": "iastore",
                            "remark": "将栈顶int型数值存入指定数组的指定索引位置"
                        },
                        {
                            "opcode": "0x50",
                            "opstr": "lastore",
                            "remark": "将栈顶long型数值存入指定数组的指定索引位置"
                        },
                        {
                            "opcode": "0x51",
                            "opstr": "fastore",
                            "remark": "将栈顶float型数值存入指定数组的指定索引位置"
                        },
                        {
                            "opcode": "0x52",
                            "opstr": "dastore",
                            "remark": "将栈顶double型数值存入指定数组的指定索引位置"
                        },
                        {
                            "opcode": "0x53",
                            "opstr": "aastore",
                            "remark": "将栈顶引用型数值存入指定数组的指定索引位置"
                        },
                        {
                            "opcode": "0x54",
                            "opstr": "bastore",
                            "remark": "将栈顶boolean或byte型数值存入指定数组的指定索引位置"
                        },
                        {
                            "opcode": "0x55",
                            "opstr": "castore",
                            "remark": "将栈顶char型数值存入指定数组的指定索引位置"
                        },
                        {
                            "opcode": "0x56",
                            "opstr": "sastore",
                            "remark": "将栈顶short型数值存入指定数组的指定索引位置"
                        },
                        {
                            "opcode": "0x57",
                            "opstr": "pop",
                            "remark": "将栈顶数值弹出(数值不能是long或double类型的)"
                        },
                        {
                            "opcode": "0x58",
                            "opstr": "pop2",
                            "remark": "将栈顶的一个(对于非long或double类型)或两个数值(对于非long或double的其他类型)弹出"
                        },
                        {
                            "opcode": "0x59",
                            "opstr": "dup",
                            "remark": "复制栈顶数值并将复制值压入栈顶"
                        },
                        {
                            "opcode": "0x5a",
                            "opstr": "dup_x1",
                            "remark": "复制栈顶数值并将两个复制值压入栈顶"
                        },
                        {
                            "opcode": "0x5b",
                            "opstr": "dup_x2",
                            "remark": "复制栈顶数值并将三个(或两个)复制值压入栈顶"
                        },
                        {
                            "opcode": "0x5c",
                            "opstr": "dup2",
                            "remark": "复制栈顶一个(对于long或double类型)或两个(对于非long或double的其他类型)数值并将复制值压入栈顶"
                        },
                        {
                            "opcode": "0x5d",
                            "opstr": "dup2_x1",
                            "remark": "dup_x1指令的双倍版本"
                        },
                        {
                            "opcode": "0x5e",
                            "opstr": "dup2_x2",
                            "remark": "dup_x2指令的双倍版本"
                        },
                        {
                            "opcode": "0x5f",
                            "opstr": "swap",
                            "remark": "将栈顶最顶端的两个数值互换(数值不能是long或double类型)"
                        },
                        {
                            "opcode": "0x60",
                            "opstr": "iadd",
                            "remark": "将栈顶两int型数值相加并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x61",
                            "opstr": "ladd",
                            "remark": "将栈顶两long型数值相加并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x62",
                            "opstr": "fadd",
                            "remark": "将栈顶两float型数值相加并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x63",
                            "opstr": "dadd",
                            "remark": "将栈顶两double型数值相加并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x64",
                            "opstr": "isub",
                            "remark": "将栈顶两int型数值相减并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x65",
                            "opstr": "lsub",
                            "remark": "将栈顶两long型数值相减并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x66",
                            "opstr": "fsub",
                            "remark": "将栈顶两float型数值相减并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x67",
                            "opstr": "dsub",
                            "remark": "将栈顶两double型数值相减并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x68",
                            "opstr": "imul",
                            "remark": "将栈顶两int型数值相乘并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x69",
                            "opstr": "lmul",
                            "remark": "将栈顶两long型数值相乘并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x6a",
                            "opstr": "fmul",
                            "remark": "将栈顶两float型数值相乘并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x6b",
                            "opstr": "dmul",
                            "remark": "将栈顶两double型数值相乘并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x6c",
                            "opstr": "idiv",
                            "remark": "将栈顶两int型数值相除并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x6d",
                            "opstr": "ldiv",
                            "remark": "将栈顶两long型数值相除并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x6e",
                            "opstr": "fdiv",
                            "remark": "将栈顶两float型数值相除并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x6f",
                            "opstr": "ddiv",
                            "remark": "将栈顶两double型数值相除并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x70",
                            "opstr": "irem",
                            "remark": "将栈顶两int型数值作取模运算并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x71",
                            "opstr": "lrem",
                            "remark": "将栈顶两long型数值作取模运算并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x72",
                            "opstr": "frem",
                            "remark": "将栈顶两float型数值作取模运算并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x73",
                            "opstr": "drem",
                            "remark": "将栈顶两double型数值作取模运算并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x74",
                            "opstr": "ineg",
                            "remark": "将栈顶int型数值取负并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x75",
                            "opstr": "lneg",
                            "remark": "将栈顶long型数值取负并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x76",
                            "opstr": "fneg",
                            "remark": "将栈顶float型数值取负并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x77",
                            "opstr": "dneg",
                            "remark": "将栈顶double型数值取负并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x78",
                            "opstr": "ishl",
                            "remark": "将int型数值左移指定位数并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x79",
                            "opstr": "lshl",
                            "remark": "将long型数值左移指定位数并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x7a",
                            "opstr": "ishr",
                            "remark": "将int型数值右(带符号)移指定位数并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x7b",
                            "opstr": "lshr",
                            "remark": "将long型数值右(带符号)移指定位数并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x7c",
                            "opstr": "iushr",
                            "remark": "将int型数值右(无符号)移指定位数并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x7d",
                            "opstr": "lushr",
                            "remark": "将long型数值右(无符号)移指定位数并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x7e",
                            "opstr": "iand",
                            "remark": "将栈顶两int型数值\"按位与\"并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x7f",
                            "opstr": "land",
                            "remark": "将栈顶两long型数值\"按位与\"并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x80",
                            "opstr": "ior",
                            "remark": "将栈顶两int型数值\"按位或\"并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x81",
                            "opstr": "lor",
                            "remark": "将栈顶两long型数值\"按位或\"并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x82",
                            "opstr": "ixor",
                            "remark": "将栈顶两int型数值\"按位异或\"并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x83",
                            "opstr": "lxor",
                            "remark": "将栈顶两long型数值\"按位异或\"并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x84",
                            "opstr": "iinc",
                            "remark": "将指定int型变量增加指定值(如i++,i–,i+=2等)"
                        },
                        {
                            "opcode": "0x85",
                            "opstr": "i2l",
                            "remark": "将栈顶int型数值强制转换为long型数值并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x86",
                            "opstr": "i2f",
                            "remark": "将栈顶int型数值强制转换为float型数值并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x87",
                            "opstr": "i2d",
                            "remark": "将栈顶int型数值强制转换为double型数值并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x88",
                            "opstr": "l2i",
                            "remark": "将栈顶long型数值强制转换为int型数值并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x89",
                            "opstr": "l2f",
                            "remark": "将栈顶long型数值强制转换为float型数值并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x8a",
                            "opstr": "l2d",
                            "remark": "将栈顶long型数值强制转换为double型数值并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x8b",
                            "opstr": "f2i",
                            "remark": "将栈顶float型数值强制转换为int型数值并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x8c",
                            "opstr": "f2l",
                            "remark": "将栈顶float型数值强制转换为long型数值并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x8d",
                            "opstr": "f2d",
                            "remark": "将栈顶float型数值强制转换为double型数值并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x8e",
                            "opstr": "d2i",
                            "remark": "将栈顶double型数值强制转换为int型数值并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x8f",
                            "opstr": "d2l",
                            "remark": "将栈顶double型数值强制转换为long型数值并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x90",
                            "opstr": "d2f",
                            "remark": "将栈顶double型数值强制转换为float型数值并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x91",
                            "opstr": "i2b",
                            "remark": "将栈顶int型数值强制转换为byte型数值并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x92",
                            "opstr": "i2c",
                            "remark": "将栈顶int型数值强制转换为char型数值并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x93",
                            "opstr": "i2s",
                            "remark": "将栈顶int型数值强制转换为short型数值并将结果压入栈顶"
                        },
                        {
                            "opcode": "0x94",
                            "opstr": "lcmp",
                            "remark": "比较栈顶两long型数值大小,并将结果(1,0或-1)压入栈顶"
                        },
                        {
                            "opcode": "0x95",
                            "opstr": "fcmpl",
                            "remark": "比较栈顶两float型数值大小,并将结果(1,0或-1)压入栈顶;当其中一个数值为NaN时,将-1压入栈顶"
                        },
                        {
                            "opcode": "0x96",
                            "opstr": "fcmpg",
                            "remark": "比较栈顶两float型数值大小,并将结果(1,0或-1)压入栈顶;当其中一个数值为NaN时,将1压入栈顶"
                        },
                        {
                            "opcode": "0x97",
                            "opstr": "dcmpl",
                            "remark": "比较栈顶两double型数值大小,并将结果(1,0或-1)压入栈顶;当其中一个数值为NaN时,将-1压入栈顶"
                        },
                        {
                            "opcode": "0x98",
                            "opstr": "dcmpg",
                            "remark": "比较栈顶两double型数值大小,并将结果(1,0或-1)压入栈顶;当其中一个数值为NaN时,将1压入栈顶"
                        },
                        {
                            "opcode": "0x99",
                            "opstr": "ifeq",
                            "remark": "当栈顶int型数值等于0时跳转"
                        },
                        {
                            "opcode": "0x9a",
                            "opstr": "ifne",
                            "remark": "当栈顶int型数值不等于0时跳转"
                        },
                        {
                            "opcode": "0x9b",
                            "opstr": "iflt",
                            "remark": "当栈顶int型数值小于0时跳转"
                        },
                        {
                            "opcode": "0x9c",
                            "opstr": "ifge",
                            "remark": "当栈顶int型数值大于等于0时跳转"
                        },
                        {
                            "opcode": "0x9d",
                            "opstr": "ifgt",
                            "remark": "当栈顶int型数值大于0时跳转"
                        },
                        {
                            "opcode": "0x9e",
                            "opstr": "ifle",
                            "remark": "当栈顶int型数值小于等于0时跳转"
                        },
                        {
                            "opcode": "0x9f",
                            "opstr": "if_icmpeq",
                            "remark": "比较栈顶两int型数值大小,当结果等于0时跳转"
                        },
                        {
                            "opcode": "0xa0",
                            "opstr": "if_icmpne",
                            "remark": "比较栈顶两int型数值大小,当结果不等于0时跳转"
                        },
                        {
                            "opcode": "0xa1",
                            "opstr": "if_icmplt",
                            "remark": "比较栈顶两int型数值大小,当结果小于0时跳转"
                        },
                        {
                            "opcode": "0xa2",
                            "opstr": "if_icmpge",
                            "remark": "比较栈顶两int型数值大小,当结果大于等于0时跳转"
                        },
                        {
                            "opcode": "0xa3",
                            "opstr": "if_icmpgt",
                            "remark": "比较栈顶两int型数值大小,当结果大于0时跳转"
                        },
                        {
                            "opcode": "0xa4",
                            "opstr": "if_icmple",
                            "remark": "比较栈顶两int型数值大小,当结果小于等于0时跳转"
                        },
                        {
                            "opcode": "0xa5",
                            "opstr": "if_acmpeq",
                            "remark": "比较栈顶两引用型数值,当结果相等时跳转"
                        },
                        {
                            "opcode": "0xa6",
                            "opstr": "if_acmpne",
                            "remark": "比较栈顶两引用型数值,当结果不相等时跳转"
                        },
                        {
                            "opcode": "0xa7",
                            "opstr": "goto",
                            "remark": "无条件跳转"
                        },
                        {
                            "opcode": "0xa8",
                            "opstr": "jsr",
                            "remark": "跳转至指定的16位offset位置,并将jsr的下一条指令地址压入栈顶"
                        },
                        {
                            "opcode": "0xa9",
                            "opstr": "ret",
                            "remark": "返回至本地变量指定的index的指令位置(一般与jsr或jsr_w联合使用)"
                        },
                        {
                            "opcode": "0xaa",
                            "opstr": "tableswitch",
                            "remark": "用于switch条件跳转,case值连续(可变长度指令)"
                        },
                        {
                            "opcode": "0xab",
                            "opstr": "lookupswitch",
                            "remark": "用于switch条件跳转,case值不连续(可变长度指令)"
                        },
                        {
                            "opcode": "0xac",
                            "opstr": "ireturn",
                            "remark": "从当前方法返回int"
                        },
                        {
                            "opcode": "0xad",
                            "opstr": "lreturn",
                            "remark": "从当前方法返回long"
                        },
                        {
                            "opcode": "0xae",
                            "opstr": "freturn",
                            "remark": "从当前方法返回float"
                        },
                        {
                            "opcode": "0xaf",
                            "opstr": "dreturn",
                            "remark": "从当前方法返回double"
                        },
                        {
                            "opcode": "0xb0",
                            "opstr": "areturn",
                            "remark": "从当前方法返回对象引用"
                        },
                        {
                            "opcode": "0xb1",
                            "opstr": "return",
                            "remark": "从当前方法返回void"
                        },
                        {
                            "opcode": "0xb2",
                            "opstr": "getstatic",
                            "remark": "获取指定类的静态域,并将其压入栈顶"
                        },
                        {
                            "opcode": "0xb3",
                            "opstr": "putstatic",
                            "remark": "为指定类的静态域赋值"
                        },
                        {
                            "opcode": "0xb4",
                            "opstr": "getfield",
                            "remark": "获取指定类的实例域,并将其压入栈顶"
                        },
                        {
                            "opcode": "0xb5",
                            "opstr": "putfield",
                            "remark": "为指定类的实例域赋值"
                        },
                        {
                            "opcode": "0xb6",
                            "opstr": "invokevirtual",
                            "remark": "调用实例方法"
                        },
                        {
                            "opcode": "0xb7",
                            "opstr": "invokespecial",
                            "remark": "调用超类构建方法,实例初始化方法,私有方法"
                        },
                        {
                            "opcode": "0xb8",
                            "opstr": "invokestatic",
                            "remark": "调用静态方法"
                        },
                        {
                            "opcode": "0xb9",
                            "opstr": "invokeinterface",
                            "remark": "调用接口方法"
                        },
                        {
                            "opcode": "0xba",
                            "opstr": "invokedynamic",
                            "remark": "调用动态方法"
                        },
                        {
                            "opcode": "0xbb",
                            "opstr": "new",
                            "remark": "创建一个对象,并将其引用引用值压入栈顶"
                        },
                        {
                            "opcode": "0xbc",
                            "opstr": "newarray",
                            "remark": "创建一个指定的原始类型(如int,float,char等)的数组,并将其引用值压入栈顶"
                        },
                        {
                            "opcode": "0xbd",
                            "opstr": "anewarray",
                            "remark": "创建一个引用型(如类,接口,数组)的数组,并将其引用值压入栈顶"
                        },
                        {
                            "opcode": "0xbe",
                            "opstr": "arraylength",
                            "remark": "获取数组的长度值并压入栈顶"
                        },
                        {
                            "opcode": "0xbf",
                            "opstr": "athrow",
                            "remark": "将栈顶的异常抛出"
                        },
                        {
                            "opcode": "0xc0",
                            "opstr": "checkcast",
                            "remark": "检验类型转换,检验未通过将抛出ClassCastException"
                        },
                        {
                            "opcode": "0xc1",
                            "opstr": "instanceof",
                            "remark": "检验对象是否是指定类的实际,如果是将1压入栈顶,否则将0压入栈顶"
                        },
                        {
                            "opcode": "0xc2",
                            "opstr": "monitorenter",
                            "remark": "获得对象的锁,用于同步方法或同步块"
                        },
                        {
                            "opcode": "0xc3",
                            "opstr": "monitorexit",
                            "remark": "释放对象的锁,用于同步方法或同步块"
                        },
                        {
                            "opcode": "0xc4",
                            "opstr": "wide",
                            "remark": "扩展本地变量的宽度"
                        },
                        {
                            "opcode": "0xc5",
                            "opstr": "multianewarray",
                            "remark": "创建指定类型和指定维度的多维数组(执行该指令时,操作栈中必须包含各维度的长度值),并将其引用压入栈顶"
                        },
                        {
                            "opcode": "0xc6",
                            "opstr": "ifnull",
                            "remark": "为null时跳转"
                        },
                        {
                            "opcode": "0xc7",
                            "opstr": "ifnonnull",
                            "remark": "不为null时跳转"
                        },
                        {
                            "opcode": "0xc8",
                            "opstr": "goto_w",
                            "remark": "无条件跳转(宽索引)"
                        },
                        {
                            "opcode": "0xc9",
                            "opstr": "jsr_w",
                            "remark": "跳转至指定的32位offset位置,并将jsr_w的下一条指令地址压入栈顶"
                        }
                    ]
                };
            }
        });
    })();
</script>