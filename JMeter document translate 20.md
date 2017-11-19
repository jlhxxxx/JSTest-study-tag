# 20. 函数和变量
JMeter 的函数是一些特殊值，它们可以填充在测试树的任何采样器或其他元件中。函数调用语法如下：

`${__functionName(var1,var2,var3)}`

其中“__functionName”匹配函数的名称。
圆括号内为函数参数，不同函数的参数也不同，例如 `${__time(YMD)}`。没有参数的函数可以不需要圆括号，例如 `${__threadNum}`。

如果函数的参数包含逗号，需要加上“`\`”来转义，否则 JMeter 会把逗号当做参数的分隔符。例如：

    ${__time(EEE\, d MMM yyyy)}
如果逗号没有被转义——例如 `${__javaScript(Math.max(2,5))}` ——你会得到像这样的错误信息：

    ERROR - jmeter.functions.JavaScript: Error processing Javascript: [Math.max(2]
    org.mozilla.javascript.EvaluatorException: missing ) after argument list (<cmd>#1)
这是因为字符串“`Math.max(2,5)`”被当做  __javascript 函数的两个参数：  
`Math.max(2` 和 `5)`  
其他错误信息也是有可能的。

变量的引用如下：

    ${VARIABLE}
**如果引用了未定义的变量或函数，那么 JMeter 并不会报告或者记录错误信息——引用返回值就是引用自身。例如，如果 `UNDEF` 没有被定义为变量，`${UNDEF}` 的返回值就是 `${UNDEF}`。** 变量和函数（包括属性）都是区分大小写的。**JMeter 会剔除变量名称中的空格，例如 `${__Random(1,63, LOTTERY )}` 中的变量‘　`LOTTERY `　’会被‘`LOTTERY`’取代。**
>属性与变量不一样。变量对线程而言是局部的；属性是针对所有线程的，属性需要使用 `__p` 或 `__property` 函数来引用。

>在使用 Windows 路径变量（例如 `C:\test\${test}`）之前使用 `\`，要确保使用 `\` 来转义，否则 JMeter 将不能解释变量，所以要这样写：`C:\\test\\${test}`。  
还有一种方法，就是使用 `/` 作为路径分隔符，例如 `C:/test/${test}`——Windows 的 Java 虚拟机在必要时会将它转化成路径分隔符。

函数列表，不严格的按类型划分：

 
|  函数类型   |          名称          |                                              注释                                              | 开始使用版本 |
| ----------- | ---------------------- | ---------------------------------------------------------------------------------------------- | ------------ |
| Information | threadNum              | get thread number                                                                              | 1.X          |
| Information | samplerName            | get the sampler name (label)                                                                   | 2.5          |
| Information | machineIP              | get the local machine IP address                                                               | 2.6          |
| Information | machineName            | get the local machine name                                                                     | 1.X          |
| Information | time                   | return current time in various formats                                                         | 2.2          |
| Information | timeShift              | return a date in various formats with the specified amount of seconds/minutes/hours/days added | 3.3          |
| Information | log                    | log (or display) a message (and return the value)                                              | 2.2          |
| Information | logn                   | log (or display) a message (empty return value)                                                | 2.2          |
| Input       | StringFromFile         | read a line from a file                                                                        | 1.9          |
| Input       | FileToString           | read an entire file                                                                            | 2.4          |
| Input       | CSVRead                | read from CSV delimited file                                                                   | 1.9          |
| Input       | XPath                  | Use an XPath expression to read from a file                                                    | 2.0.3        |
| Calculation | counter                | generate an incrementing number                                                                | 1.X          |
| Calculation | intSum                 | add int numbers                                                                                | 1.8.1        |
| Calculation | longSum                | add long numbers                                                                               | 2.3.2        |
| Calculation | Random                 | generate a random number                                                                       | 1.9          |
| Calculation | RandomDate             | generate random date within a specific date range                                              | 3.3          |
| Calculation | RandomFromMultipleVars | extracts an element from the values of a set of variables separated by                         | 3.1          |
| Calculation | RandomString           | generate a random string                                                                       | 2.6          |
| Calculation | UUID                   | generate a random type 4 UUID                                                                  | 2.9          |
| Scripting   | groovy                 | run a Groovy script                                                                            | 3.1          |
| Scripting   | BeanShell              | run a BeanShell script                                                                         | 1.X          |
| Scripting   | javaScript             | process JavaScript (Nashorn)                                                                   | 1.9          |
| Scripting   | jexl2                  | evaluate a Commons Jexl2 expression                                                            | jexl2(2.1.1) |
| Scripting   | jexl3                  | evaluate a Commons Jexl3 expression                                                            | jexl3 (3.0)  |
| Properties  | property               | read a property                                                                                | 2.0          |
| Properties  | P                      | read a property (shorthand method)                                                             | 2.0          |
| Properties  | setProperty            | set a JMeter property                                                                          | 2.1          |
| Variables   | split                  | Split a string into variables                                                                  | 2.0.2        |
| Variables   | V                      | evaluate a variable name                                                                       | 2.3RC3       |
| Variables   | eval                   | evaluate a variable expression                                                                 | 2.3.1        |
| Variables   | evalVar                | evaluate an expression stored in a variable                                                    | 2.3.1        |
| String      | regexFunction          | parse previous response using a regular expression                                             | 1.X          |
| String      | escapeOroRegexpChars   | quote meta chars used by ORO regular expression                                                | 2.9          |
| String      | char                   | generate Unicode char values from a list of numbers                                            | 2.3.3        |
| String      | unescape               | Process strings containing Java escapes (e.g. \n & \t)                                         | 2.3.3        |
| String      | unescapeHtml           | Decode HTML-encoded strings                                                                    | 2.3.3        |
| String      | escapeHtml             | Encode strings using HTML encoding                                                             | 2.3.3        |
| String      | escapeXml              | Encode strings using XMl encoding                                                              | 3.2          |
| String      | urldecode              | Decode a application/x-www-form-urlencoded string                                              | 2.10         |
| String      | urlencode              | Encode a string to a application/x-www-form-urlencoded string                                  | 2.10         |
| String      | TestPlanName           | Return name of current test plan                                                               | 2.6          |
## 20.1 函数可以做什么
JMeter 有两种函数：用户定义的静态值（或变量）和内建函数。  
用户定义的静态值允许用户在编译或者运行测试树时，使用自定义变量来替换静态值。这种替换只在测试运行的开始阶段执行一次。例如，可以用自定义变量来替换所有 HTTP 请求的 DOMAIN 域，这样就使得测试变更在不同服务器执行相同测试成为一件简单的事情。  

注意，目前变量不支持嵌套，例如 `${Var${N}}` 是无效的，但是可以使用函数 `__V(variable)` 来实现嵌套变量的目的：`${__V(Var${N})}`。同样可以用 `${__BeanShell(vars.get("Var${N}")}` 来实现。  

这种类型的替换可以不用函数来实现，但是这样就没有那么方便和直观了。用户可以创建默认配置元件来填充采样器中的空值。变量可以替换任何给定值的一部分，而不是只填充空值。  

使用内建函数用户可以在运行时根据之前的响应数据、函数所在线程、当前时间和其他资源计算出新的变量值。这些变量的值在测试过程中会根据每个请求动态刷新。
>函数被线程共享。在测试计划中每次函数的调用，都由一个单独的函数实例来处理。

## 20.2 函数和变量可以用在哪？
函数和变量可以用在任何测试元件的任何输入域中（除了测试计划——见下文）。有些输入域只接受数字而不支持字符串，因此它们也不支持函数。然而，大多数输入域还是支持函数的。  

在测试计划中使用函数是有限制的。当函数被调用时，JMeter 线程变量并没有完全初始化，因此变量名称作为参数传递时也没有初始化，变量会引用失败，所以 `split()` 和 `regex()` 和变量赋值函数都不能正常工作。`threadNum()` 函数也不会工作（它在测试计划层也没有意义）。下面是可以在测试计划中使用的的函数：
* intSum
* longSum
* machineName
* BeanShell
* groovy
* javaScript
* jexl2/jexl3
* random
* time
* property functions
* log functions

配置元件是由独立线程处理的。因此像 `__threadNum` 这样的函数在一些测试元件（例如用户定义的变量）中不能正常地工作。同样要注意在用户定义的变量（UDV）中定义的变量，在 UDV 被处理前是不能使用的。
>当在 SQL 代码（或其他）中引用变量/函数时，要记得给文本字符串添加必要的引号，即使用
>
>       SELECT item from table where name='${VAR}'
>而不是
>
>       SELECT item from table where name=${VAR}
>除非 `VAR` 本身包含引号

## 20.3 如何引用变量和函数