# <center>XML——扩展标记语言</center>

## XML 基础

### XML 简介

* XML 的设计宗旨是传输数据，而非显示数据。
* XML 标签没有被预定义。您需要自行定义标签。
* XML 被设计为具有自我描述性。
* 没有任何行为的 XML，XML 是不作为的。

### XML 用途

* XML 把数据从 HTML 分离
* XML 简化数据共享和传输

### XML 树结构（类似html）

```xml
<root>
  <child>
    <subchild>.....</subchild>
  </child>
</root>
```

### XML 语法

* 所有 XML 元素都须有关闭标签

* XML 标签对大小写敏感

* XML 必须正确地嵌套

* XML 文档必须有根元素

* XML 的属性值须加引号

* 实体引用（需转义）

  | 实体引用 | 对应符号 |        |
  | -------- | -------- | ------ |
  | `&lt;`     | <        | 小于   |
  | `&gt;`     | >        | 大于   |
  | `&apos;`   | '        | 单引号 |
  | `&quot;`   | "        | 引号   |
  | `&amp;`    | &        | 和号   |


* XML 中的注释

   ```xml
   <!-- This is a comment --> 
   ```

* 在 XML 中，空格会被保留

* XML 以 LF 存储换行

### XML 元素

* 命名规则
 * 名称可以含字母、数字以及其他的字符
 * 名称不能以数字或者标点符号开始
 * 名称不能以字符 `xml`（或者 `XML`、`Xml`）开始
 * 名称不能包含空格
 * 可使用任何名称，没有保留的字词

* 最佳命名习惯
 * 避免 `-` 字符。如果您按照这样的方式进行命名：`first-name`，一些软件会认为你需要提取第一个单词
 * 避免 `.` 字符。如果您按照这样的方式进行命名：`first.name`，一些软件会认为 `name`是对象 `first` 的属性
 * 避免 `:` 字符。冒号会被转换为命名空间来使用

### XML 属性
* XML 属性必须加引号
* 尽量使用元素来描述数据。而仅仅使用属性来提供与数据无关的信息。

### XML CSS
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<?xml-stylesheet type="text/css" href="cd_catalog.css"?>
……
```

### XML XSLT（比CSS更完善）
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<?xml-stylesheet type="text/xsl" href="simple.xsl"?>
……
```

## XML JavaScript

### XML Http Request ——用于在后台与服务器交换数据

* 在不重新加载页面的情况下更新网页
* 在页面已加载后从服务器请求/接收数据
* 在后台向服务器发送数据

