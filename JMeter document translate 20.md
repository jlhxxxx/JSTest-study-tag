
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

<p id="functions_list">函数列表，不严格的按类型划分：</p>

 
|  函数类型   |          名称          |                                              注释                                              | 开始使用版本 |
| ----------- | ---------------------- | ---------------------------------------------------------------------------------------------- | ------------ |
| Information | [threadNum](#threadNum)              | get thread number                                                                              | 1.X          |
| Information | [samplerName](#samplerName)            | get the sampler name (label)                                                                   | 2.5          |
| Information | [machineIP](#machineIP)              | get the local machine IP address                                                               | 2.6          |
| Information | [machineName](#machineName)            | get the local machine name                                                                     | 1.X          |
| Information | [time](#time)                   | return current time in various formats                                                         | 2.2          |
| Information | [timeShift](#timeShift)              | return a date in various formats with the specified amount of seconds/minutes/hours/days added | 3.3          |
| Information | [log](#log)                    | log (or display) a message (and return the value)                                              | 2.2          |
| Information | [logn](#logn)                   | log (or display) a message (empty return value)                                                | 2.2          |
| Input       | [StringFromFile](#StringFromFile)         | read a line from a file                                                                        | 1.9          |
| Input       | [FileToString](#FileToString)           | read an entire file                                                                            | 2.4          |
| Input       | [CSVRead](#CSVRead)                | read from CSV delimited file                                                                   | 1.9          |
| Input       | [XPath](#XPath)                  | Use an XPath expression to read from a file                                                    | 2.0.3        |
| Calculation | [counter](#counter)                | generate an incrementing number                                                                | 1.X          |
| Calculation | [intSum](#intSum)                 | add int numbers                                                                                | 1.8.1        |
| Calculation | [longSum](#longSum)                | add long numbers                                                                               | 2.3.2        |
| Calculation | [Random](#Random)                 | generate a random number                                                                       | 1.9          |
| Calculation | [RandomDate](#RandomDate)             | generate random date within a specific date range                                              | 3.3          |
| Calculation | [RandomFromMultipleVars](#RandomFromMultipleVars) | extracts an element from the values of a set of variables separated by                         | 3.1          |
| Calculation | [RandomString](#RandomString)           | generate a random string                                                                       | 2.6          |
| Calculation | [UUID](#UUID)                   | generate a random type 4 UUID                                                                  | 2.9          |
| Scripting   | [groovy](#groovy)                 | run a Groovy script                                                                            | 3.1          |
| Scripting   | [BeanShell](#BeanShell)              | run a BeanShell script                                                                         | 1.X          |
| Scripting   | [javaScript](#javaScript)             | process JavaScript (Nashorn)                                                                   | 1.9          |
| Scripting   | [jexl2](#jexl2)                  | evaluate a Commons Jexl2 expression                                                            | jexl2(2.1.1) |
| Scripting   | [jexl3](#jexl3)                  | evaluate a Commons Jexl3 expression                                                            | jexl3 (3.0)  |
| Properties  | [property](#property)               | read a property                                                                                | 2.0          |
| Properties  | [P](#P)                      | read a property (shorthand method)                                                             | 2.0          |
| Properties  | [setProperty](#setProperty)            | set a JMeter property                                                                          | 2.1          |
| Variables   | [split](#split)                  | Split a string into variables                                                                  | 2.0.2        |
| Variables   | [V](#V)                      | evaluate a variable name                                                                       | 2.3RC3       |
| Variables   | [eval](#eval)                   | evaluate a variable expression                                                                 | 2.3.1        |
| Variables   | [evalVar](#evalVar)                | evaluate an expression stored in a variable                                                    | 2.3.1        |
| String      | [regexFunction](#regexFunction)          | parse previous response using a regular expression                                             | 1.X          |
| String      | [escapeOroRegexpChars](#escapeOroRegexpChars)   | quote meta chars used by ORO regular expression                                                | 2.9          |
| String      | [char](#char)                   | generate Unicode char values from a list of numbers                                            | 2.3.3        |
| String      | [unescape](#unescape)               | Process strings containing Java escapes (e.g. \n & \t)                                         | 2.3.3        |
| String      | [unescapeHtml](#unescapeHtml)           | Decode HTML-encoded strings                                                                    | 2.3.3        |
| String      | [escapeHtml](#escapeHtml)             | Encode strings using HTML encoding                                                             | 2.3.3        |
| String      | [escapeXml](#escapeXml)              | Encode strings using XMl encoding                                                              | 3.2          |
| String      | [urldecode](#urldecode)              | Decode a application/x-www-form-urlencoded string                                              | 2.10         |
| String      | [urlencode](#urlencode)              | Encode a string to a application/x-www-form-urlencoded string                                  | 2.10         |
| String      | [TestPlanName](#TestPlanName)           | Return name of current test plan                                                               | 2.6          |
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
在测试元件中引用一个变量可以通过使用 `${` 和 `}` 将变量名称括起来实现。  

函数引用的方法相同，但是按照惯例，函数名称以“`__`”开头来和变量名称区分开。一些函数带参数，参数放在圆括号中，用逗号分隔。如果函数不带参数，可以省略圆括号。  

**如果参数本身带逗号，必须将其转义。可以使用‘`\,`’来转义。** 这适用于例如脚本函数——Javascript, Beanshell, Jexl, groovy——有必要对所有脚本函数调用中的逗号加以转义，例如

    ${__BeanShell(vars.put("name"\,"value"))}
换一种方法，你也可以将你的脚本定义为一个变量，例如在测试计划中定义：

    SCRIPT          vars.put("name","value")
定义过的脚本可以像下面这样被引用：

    ${__BeanShell(${SCRIPT})}
在 `SCRIPT` 变量中就没有必要对逗号进行转义了，因为函数的调用在变量用其值替换之前被解析。该方法适用于 JSR223 或者 BeanShell 采样器，这两种采样器可用来测试 Javascript, Jexl 和 BeanShell 脚本。  

函数可以引用参数和其他函数，例如 `${__XPath(${__P(xpath.file),${XPATH})}` 使用“`xpath.file`”的值作为文件名，使用变量 `XPATH` 的内容作为搜索表达式。  

JMeter 提供一个工具来帮助建立各种内置函数的函数调用，只需使用复制-粘贴就可以实现。它不会自动为你转义，因为函数可以作为其他函数的参数，应该只对文本内容进行转义。
>如果一个字符串既包含反斜杠（‘`\`’）又包含函数或者变量引用，出现在‘`$`’或‘`,`’或‘`\`’之前的反斜杠会被移除。这种操作对于包含逗号或者 `${` 的嵌套函数是有必要的。如果一个字符串不包含函数或者变量引用，那么在‘`$`’或‘`,`’或‘`\`’之前的反斜杠不会被移除。

变量或函数的值可以用 [`__logn()`](#logn) 函数来报告，`__logn()` 函数在要报告的变量被定义之后可以在测试计划的任何地方被引用。除此之外，Java 请求采样器可以用来生成一个包含变量引用的采样；其输出能在合适的监听器中显示。注意也可以通过在查看结果树中使用 [Debug Sampler](http://jmeter.apache.org/usermanual/component_reference.html#Debug_Sampler) 来显示变量的值。
>如果用和内建函数同样的名称定义一个用户静态变量，那么定义的静态变量将覆盖同名内置函数。

## 20.4 函数助手对话框
函数助手对话框可以在 JMeter 的工具菜单中找到。  
    　　 ![](2017-11-19-14-42-41.png)
     　　_函数助手对话框_  

使用函数助手，可以从下拉列表中选择一个函数，并给它的参数赋值。表格左列是参数的简要说明，表格的右列填入相应参数的值。不同的函数有不同的参数。  

上述操作完成之后，点击“生成”按钮，相应调用函数的字符串就生成了，你可以复制-招贴到测试计划中的任何地方。

## 20.5 函数

<h3 id="regexFunction">__regexFunction</h3>

正则表达式函数可以使用任意正则表达式（用户提供的）来解析前面的服务器响应（或变量值）。函数返回填充了变量值的模版字符串。  

`__regexFunction` 也可以存储值供以后使用。你可以在它的第六个参数中设定一个引用名称。在函数执行之后，可以使用用户定义的值的语法在稍后时间检索相同的值。例如，如果输入 “`refName`” 作为第六个参数,那么可以使用：
* `${refName}` 来引用该函数解析的第二个参数（“Template for the replacement string”）的计算结果
* `${refName_g0}` 来引用该函数解析的整个匹配
* `${refName_g1}` 来引用该函数解析的第一个匹配组合
* `${refName_g#}` 来引用该函数解析的第 N 个匹配组合
* `${refName_matchNr}` 来引用该函数解析的匹配组合数量

>如果使用分布式测试，要切换模式（见 `jmeter.properties`）确保它不在剥离模式下，参见 [`Bug 56376`](https://bz.apache.org/bugzilla/show_bug.cgi?id=56376)。

#### 参数（Parameters）
---
属性（Attribute）| 描述| 是否必须
---------|----------|---------
 第一个参数 | 第一个参数是解析响应数据的正则表达式。它会抓取所有匹配。若你希望在模版字符串中使用的该表达式中的任何部分，请给它（要使用的部分）加上括号。例如：`<a href="(.*)">`。它将抓取链接值并储存在第一个匹配组合中（这里只有一个匹配组合）。另一个例子：`<input type="hidden" name="(.*)" value="(.*)">`。它将抓取 name 的值作为第一个匹配组合，value 的值作为第二个匹配组合。这些匹配的值可以用在模版字符串中。| 是
 第二个参数| 这是一个运行时会替换函数的模版字符串。要引用正则表达式中捕获的匹配组合，使用下面的句法：`$[group_number]$`。例如 `$1$` 或者 `$2$`你的模版可以是任意字符串。 |是
 第三个参数 | 第三个参数告诉 JMeter 使用第几个匹配。你的正则表达式可能找到多个匹配。对此有四个选项：<br>  <ul><li> 整数——直接告诉 JMeter 使用第几个匹配。‘`1`’对应第一个，‘`2`’对应第二个，以此类推。 </li><li> `RAND`——告诉 JMeter 使用随机匹配。</li><li> `ALL`——告诉 JMeter 使用所有匹配，对应每个匹配生成一个模版字符串并将它们组合到一起。这个选项很少用到。</li><li> 0 到 1 之间的浮点数——告诉 JMeter 根据公式（总的匹配个数*浮点值）计算使用第几个匹配项，计算值向最近的整数取整</li></ul> | 否，默认值 = 1
 第四个参数 | 如果上一个参数选择 `ALL`，这个参数会被插入到每个重复的模版值之间 | 否
 第五个参数 | 如果没有匹配项返回的默认值| 否
 第六个参数 | 重用此函数解析的值的引用名称,储存的值包括 `${refName}`（替换的模版字符串）和 `${refName_g#}` ,其中“`#`”代表正则表达式匹配分组的序号（“`0`”可以用来引用整个匹配） | 否
 第七个参数 | 输入变量名称。如果指定了这个参数，那么将使用变量的值作为输入，而不是使用之前的采样结果。 | 否
[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="counter">__counter</h3>

计数器每次调用会生成一个新值，从 1 开始，每次加 1。计数器可以配置成对每个虚拟用户独立的，也可以配置成对所有用户公用的。如果每个用户的值分开计数，通常用于计算测试计划的执行次数。全局计数器通常用于计算请求的次数。

计数器使用一个整型变量来保存计数，允许的最大值为 2,147,483,647。

计数器函数实例是完全独立的。全局计数器 - “`FALSE`” - 的每个实例都是独立维护的。

**`__counter` 函数在同一个迭代中的多次调用不会进一步增加值。**  
如果您想对每个采样器计数，请使用预处理器（例如[用户参数](http://jmeter.apache.org/usermanual/component_reference.html#User_Parameters)）中的功能。

#### 参数（Parameters）
---
属性（Attribute）| 描述| 是否必须
---------|----------|---------
第一个参数 | `TRUE` 如果您希望每个虚拟用户的计数器保持独立并与其他用户分开。 `FLASE` 全局计数器。 | 是
第二个参数 | 重用此函数创建的值的引用名称。<br>存储的值的格式为 `${refName}`。<br>这允许你保留一个计数器，并在多个地方引用它的值。 | 否
[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="threadNum">__threadNum</h3>

threadNum 函数只是返回当前正在执行的线程编号。线程编号独立于线程组，这意味着从该函数的角度来看，一个线程组中的线程＃1 与另一个线程组中的线程＃1 是没有区别的。

这个函数没有参数。

用法示例：

    ${__threadNum}
返回 1 到在包含线程组中配置的运行线程的最大值之间的数字。
>这个函数在任何配置元件（例如用户定义的变量）中都不起作用，因为它们是在一个单独的线程中运行的。在测试计划中也不能使用。

[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="intSum">__intSum</h3>

intSum 函数可用于计算两个或更多个整数值之和。
>引用名称是可选的，但不能是有效的整数。

#### 参数（Parameters）
---
属性（Attribute）| 描述| 是否必须
---------|----------|---------
第一个参数 | 第一个整数值 | 是
第二个参数 | 第二个整数值 | 是
第 n 个参数 | 第 n 个整数值 | 否
最后一个参数 | 重用此函数计算值的引用名称。如果该参数被指定，引用名称必须包含至少一个非数字字符，否则将被视为另一个要添加的整数值 | 否

例子：

    ${__intSum(2,5,MYVAR)}
将返回 7（2 + 5）并将结果存储在 MYVAR 变量中。所以 `${MYVAR}` 将等于 7。

    ${__intSum(2,5,7)}
将返回 14（2 + 5 + 7）并将结果存储在 MYVAR 变量中。

    ${__intSum(1,2,5,${MYVAR})}
如果 MYVAR 值等于 8，1 + 2 + 5 + ${MYVAR}，返回 16。

[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="longSum">__longSum</h3>

longSum 函数可用于计算两个或更多个长整型值之和，当计算值不在 -2147483648 到 2147483647 之间，使用此函数而不是 __intSum。

#### 参数（Parameters）
---
属性（Attribute）| 描述| 是否必须
---------|----------|---------
第一个参数 | 第一个长整型值 | 是
第二个参数 | 第二个长整型值 | 是
第 n 个参数 | 第 n 个长整型值 | 否
最后一个参数 | 重用此函数计算值的引用名称。如果该参数被指定，引用名称必须包含至少一个非数字字符，否则将被视为另一个要添加的长整型值 | 否

例子：

    ${__longSum(2,5,MYVAR)}
将返回 7（2 + 5）并将结果存储在 MYVAR 变量中。所以 `${MYVAR}` 将等于 7。

    ${__longSum(2,5,7)}
将返回 14（2 + 5 + 7）并将结果存储在 MYVAR 变量中。

    ${__longSum(1,2,5,${MYVAR})}
如果 MYVAR 值等于 8，1 + 2 + 5 + ${MYVAR}，返回 16。 

[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="StringFromFile">__StringFromFile</h3>

StringFromFile 函数可以用来从文本文件中读取字符串。这对于运行需要大量可变数据的测试非常有用。例如，在测试银行应用程序时，可能需要 100 或 1000 个不同的帐号。

另请参阅可能更易于使用的 [CSV Data Set Config 测试元件](http://jmeter.apache.org/usermanual/component_reference.html#CSV_Data_Set_Config)。但是，目前不支持多个输入文件。

每次调用该函数都会从文件中读取下一行。所有的线程共享相同的实例，所以不同的线程会读取不同的行。到达文件末尾时，除非达到最大循环次数，否则将从头开始重新读取。如果在一个测试脚本中对该函数多次引用，每此引用都将独立打开文件，即使文件名相同。【如果要在其他地方再次使用该值，请为每个函数调用使用不同的变量名称。】
>函数实例在线程之间共享，并且无论线程​​是否需要下一行输入，该文件都会（重新）打开，因此使用 `threadNumber` 作为文件名的一部分将导致不可预知的行为。

如果打开或读取文件时发生错误，函数会返回字符串“`**ERR**`”。

#### 参数（Parameters）
---
属性（Attribute）| 描述| 是否必须
---------|----------|---------
文件名称 | 文件名称的路径。（可以使用相对于 JMeter 启动目录的相对路径）如果要使用可选的序列号，路径名称应该适合转换成十进制格式。看下面的例子。 | 是
变量名称 | 引用名称 - `refName` - 用于重用由此函数创建的值。存储该值的格式为 `${refName}`。默认值是“`StringFromFile_`”。 | 否
开始序列号 | 初始序列号（如果省略，结束序列号将被视为循环计数） | 否
结束序列号 | 终止序列号（如果省略，序列号可以不受限制地增加下去） | 否

文件名称参数在文件打开或重新打开时被解析。

引用名称参数（如果支持）在每次执行函数时被解析。

**使用序列号：**

使用可选的序列号时，路径名称将使用 `java.text.DecimalFormat` 的格式字符串。当前的序列号将作为唯一的参数传入。如果没有指定可选的开始序列号，就使用路径名称作为起始值。有用的格式序列如下：

  * `#` 插入不带前导零或空格的数字
  * `000` 如有必要，插入带有前导零的三位数字

  ><h4>格式字符串的使用</h4>
  >以下是几个格式字符串以及它们将生成的对应序列。
  >
  > * `pin#'.'dat`
  >
  >   生成不带前导零的序列，`.` 还是 `.`：`pin1.dat`，...，`pin9.dat`，`pin10.dat`，...，`pin9999.dat`
pin000' 。
  >
  > * `pin000'.'dat`
  >
  >   生成带前导零的序列，同时保持 `.`。当数字位数超过三位时，序列将使用更多位数的数字：`pin001.dat`，... `pin099.dat`，...，`pin999.dat`，...，`pin9999.dat`
  >
  > * `pin'.'dat#`
  >
  >   生成不带前导零的附加数字，同时保持 `.`：`pin.dat1`，...，`pin.dat9`，...，`pin.dat999`

如果需要的位数多于格式字符数，数字将根据需要进行扩展。  
**要防止格式字符被解释，请将其包含在单引号中。请注意，“`.`”是一个格式字符，必须用单引号引起来** （尽管 `#.` 和 `000.` 在工作区能按预期的方式工作，因为它被视为小数点，而小数点也是“`.`”）。  
在其他语言环境（例如 `fr`）中，小数点是“`,`” - 这意味着“`#.`”会变成“`nnn,`”。  
有关完整的细节，请参阅 DecimalFormat （十进制格式）的文档。  
如果路径名称不包含任何特殊的格式字符，则将当前的序号直接附加到名称上，否则将根据格式化指令插入数字。  
如果起始序列号被忽略，并且指定了结束序列号，则结束序列号将被解释为循环计数，并且该文件将被使用循环计数的最大次数。在这种情况下，文件名不是格式化的。  
`${__StringFromFile(PIN#'.'DAT,,1,2)}` 读取 `PIN1.DAT`, `PIN2.DAT`  
`${__StringFromFile(PIN.DAT,,,2)}` 读取 `PIN.DAT` 两次  
注意上面 `PIN.DAT` 中的“`.`”不应被引号包含。在这种起始序列号被省略的情况下，文件名完全按原样使用。

[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="machineName">__machineName</h3>

machineName 函数返回本地主机名称。它使用 Java 方法 `InetAddress.getLocalHost()` 并将值传递给 `getHostName()`。

#### 参数（Parameters）
---
属性（Attribute）| 描述| 是否必须
---------|----------|---------
变量名称 | 重用此函数计算的值的引用名称 | 否
例子：
    
    ${__machineName()}
返回机器的主机名称

    ${__machineName}
返回机器的主机名称

[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="machineIP">__machineIP</h3>

machineIP 函数返回本地IP地址。它使用 Java 方法`InetAddress.getLocalHost()` 并将其值传递给 `getHostAddress()`。

#### 参数（Parameters）
---
属性（Attribute）| 描述| 是否必须
---------|----------|---------
变量名称 | 重用此函数计算的值的引用名称 | 否
例子：

    ${__machineIP()}
返回机器的 IP 地址

    ${__machineIP}
返回机器的 IP 地址

[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="javaScript">__javaScript</h3>

javaScript 函数执行一段 JavaScript（不是 Java！）代码并返回它的值。

JMeter Javascrip t函数调用独立的 JavaScript 解释器。Javascript 被当作脚本语言使用，所以可以做相应的计算等。
>在 JMeter 中，javaScript 并不是最好的脚本语言。如果你的测试计划需要大量的线程，建议使用`__jexl3` 或`__groovy` 函数。

对于 Nashorn 引擎，请参阅[ Java 平台标准版 Nashorn 用户指南](https://docs.oracle.com/javase/8/docs/technotes/guides/scripting/nashorn/)。

对于 Rhino 引擎，请参阅[Mozilla Rhino 概述](http://www.mozilla.org/rhino/overview.html)。

以下变量可用于脚本：
  * `log` - 函数的[记录](https://www.slf4j.org/api/org/slf4j/Logger.html)
  * `ctx` - [JMeterContext](http://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterContext.html) 对象
  * `vars` - [JMeterVariables](http://jmeter.apache.org/api/org/apache/jmeter/threads/JMeterVariables.html) 对象
  * `threadName` - 包含当前线程名称的字符串
  * `sampler` - 当前[采样器](http://jmeter.apache.org/api/org/apache/jmeter/samplers/Sampler.html)对象（如果有的话）
  * `samplerResult` - 之前的 [SampleResult](http://jmeter.apache.org/api/org/apache/jmeter/samplers/SampleResult.html) 对象（如果有的话）
  * `props` - JMeterProperties（类 [java.util.Properties](https://docs.oracle.com/javase/8/docs/api/java/util/Properties.html)）对象

Rhinoscript 允许通过其 Packages 对象访问静态方法。请参阅 [Java 脚本](https://wiki.openjdk.java.net/display/Nashorn/Rhino+Migration+Guide) 文档。例如，可以像这样访问 JMeterContextService 静态方法：`Java.type("org.apache.jmeter.threads.JMeterContextService").getTotalThreads()`。

>JMeter 不是浏览器，不能解释下载页面中的 JavaScript。

#### 参数（Parameters）
---
属性（Attribute）| 描述| 是否必须
---------|----------|---------
表达式 | 要执行的JavaScript表达式。例如：<br><ul><li>`new Date()` - 返回当前日期和时间</li><li>`Math.floor(Math.random()*(${maxRandom}+1))` - 一个介于 `0` 和变量 `maxRandom` 之间的随机数</li><li>`${minRandom}+Math.floor(Math.random()*(${maxRandom}-${minRandom}+1))` - 变量 `minRandom` 和 `maxRandom` 之间的随机数</li><li>`"${VAR}"=="abcd"` | 是
变量名称 | 重用此函数计算的值的引用名称 | 否
>请记住为文本字符串和 JMeter 变量添加必要的引号。另外，如果表达式有逗号，请确保将其转义。例如：
>
>     ${__javaScript('${sp}'.slice(7\,99999))}
>`7` 之后的逗号被转义了。

例子：

    ${__javaScript(new Date())}
返回 `Sat Jan 09 2016 16:22:15 GMT+0100 (CET)` 

    ${__javaScript(new Date(),MYDATE)}
返回 `Sat Jan 09 2016 16:22:15 GMT+0100 (CET)` 并将其存储在变量 `MYDATE` 下 

    ${__javaScript(Math.floor(Math.random()*(${maxRandom}+1)),MYRESULT)}
使用 `maxRandom` 变量，返回 `0` 和 `maxRandom` 之间的随机值并将其存储在  `MYRESULT` 中

    ${__javaScript(${minRandom}+Math.floor(Math.random()*(${maxRandom}-${minRandom}+1)),MYRESULT)}
使用 `maxRandom` 和 `minRandom` 变量，返回 `maxRandom` 和 `minRandom` 之间的随机值并将其存储在 `MYRESULT` 中

    ${__javaScript("${VAR}"=="abcd",MYRESULT)}
将 `VAR` 变量的值与 `abcd` 进行比较，返回 `true` 或 `false` 并将结果存储在 `MYRESULT` 中

[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="Random">__Random</h3>

random 函数返回一个介于给定最小值和最大值之间的随机数。

#### 参数（Parameters）
---
属性（Attribute）| 描述| 是否必须
---------|----------|---------
最小值 | 一个数字 | 是
最大值 | 一个更大的数字 | 是
变量名称 | 重用此函数计算的值的引用名称 | 否
例子：

    ${__Random(0,10)}
返回一个 0 到 10 之间的随机数

    ${__Random(0,10, MYVAR)}
返回一个 0 到 10 之间的随机数，并将其存储在 `MYVAR`中。`${MYVAR}`将包含此随机数

[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="RandomDate">__RandomDate</h3>

RandomDate 函数返回一个位于给定开始日期和结束日期值之间的随机日期。

#### 参数（Parameters）
---
属性（Attribute）| 描述| 是否必须
---------|----------|---------
时间格式 | DateTimeFormatter 的格式字符串（默认为 `yyyy-MM-dd`） | 否
开始日期 | 开始日期，现在是默认值 | 否
结束日期 | 结束日期 | 是
用于格式的区域设置 | 语言环境的字符串格式。语言代码必须是小写。国家代码必须大写。分隔符必须是下划线，例如 `en_EN`。请参阅 [http://www.oracle.com/technetwork/java/javase/javase7locales-334809.html]( http://www.oracle.com/technetwork/java/javase/javase7locales-334809.html)。如果省略，则默认情况下该函数使用 Apache JMeter 当前语言环境。 | 否
变量名称 | 要设置的变量名称 | 否
例子：

    ${__RandomDate(,,2050-07-08,,)}
返回从现在到 `2050-07-08` 之间一个随机的日期。例如 `2039-06-21` 

    ${__RandomDate(dd MM yyyy,,08 07 2050,,)}
将返回一个自定义格式的随机日期，例如 `04 03 2034`

[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="RandomString">__RandomString</h3>

RandomString 函数返回一个 chars 长度内的随机字符串。

#### 参数（Parameters）
---
属性（Attribute）| 描述| 是否必须
---------|----------|---------
长度 | 生成字符串的长度 | 是
使用的字符 | 用于生成字符串的字符 | 否
变量名称 | 重用此函数计算的值的引用名称 | 否
例子：

    ${__RandomString(5)}
返回随机的可读或不可读的 5 个字符

    ${__RandomString(10,abcdefg)}
将返回从 `abcdefg` 集合中挑选的 10 个字符的随机字符串，如 `cdbgdbeebd` 或 `adbfeggfad`，...

    ${__RandomString(6,a12zeczclk, MYVAR)}
从 `a12zeczclk` 集合中返回一个由 6 个字符组成的随机字符串，并将结果存储在 `MYVAR` 中，`MYVAR` 将包含像 `2z22ak` 或 `z11kce` 这样的字符串，...

[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="RandomFromMultipleVars">__RandomFromMultipleVars</h3>

RandomFromMultipleVars 函数根据 Source Variables 提供的变量值返回一个随机值。

变量可以是单值或多值的，它们可以由以下提取器生成：
  * [正则表达式提取器](http://jmeter.apache.org/usermanual/component_reference.html#Regular_Expression_Extractor)
  * [CSS/JQuery 提取器](http://jmeter.apache.org/usermanual/component_reference.html#CSS/JQuery_Extractor)
  * [JSON 提取器](http://jmeter.apache.org/usermanual/component_reference.html#JSON_Extractor)
  * [XPath 断言](http://jmeter.apache.org/usermanual/component_reference.html#XPath_Assertion)

多值变量就是，当你设置 `-1` 作为`匹配数字`所提取的值。当n = 1，2，3...时会创建相应匹配号变量 `varName_matchNr`，并为每个值创建变量 `varName_n`。

#### 参数（Parameters）
---
属性（Attribute）| 描述| 是否必须
---------|----------|---------
来源变量 | 变量名称包含的值将用作随机计算的输入，用 `|` 分隔 | 是
变量名称 | 重用此函数计算的值的引用名称 | 否
例子：

    ${__RandomFromMultipleVars(val)}
根据变量 val 的内容返回一个随机的字符串，不管它们是否是多值的

    ${__RandomFromMultipleVars(val1|val2)}
根据变量 val1 和 val2 的内容返回一个随机字符串，不管它们是否为多值

    ${__RandomFromMultipleVars(val1|val2, MYVAR)}
根据变量 val1 和 val2 的内容返回一个随机字符串，不管它们是否为多值，并将结果存储在 `MYVAR` 中 

[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="UUID">__UUID</h3>

UUID 函数返回伪随机类型为 4 的通用唯一标识符（UUID）。

没有参数。

例子：

    ${UUID()}
将返回具有以下格式的 UUID：`c69e0dd1-ac6b-4f2b-8d59-5d4e8743eecd`

[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="CSVRead">__CSVRead</h3>

CSVRead 函数从 CSV 文件返回一个字符串（注意与 [StringFromFile](#StringFromFile) 的区别）。

注：JMeter 支持多个文件名。

**大多数情况下，较新的 [CSV Data Set Config 元件](http://jmeter.apache.org/usermanual/component_reference.html#CSV_Data_Set_Config)更容易使用。**

对某个文件名第一次读取时，文件被打开并读取到内部数组。空行将被视为文件结尾 - 这允许使用尾部注释。

后续对同一文件名的所有引用使用相同的内部数组。注意，文件名是区分大小写的，即使操作系统不区分大小写，所以 `CSVRead(abc.txt,0)` 和 `CSVRead(aBc.txt,0)` 会引用不同的内部数组。

`*ALIAS` 功能允许同一个文件被打开多次，并且允许较短的文件名。

每个线程都有自己的内部指针，指向文件数组中的当前行。当一个线程第一次引用文件时，它将被分配到数组中的下一个空闲行，所以每个线程将访问与其他所有线程不同的行（除非线程数多于数组中的行）。

>该函数默认情况下以逗号分割行。如果要输入包含逗号的列，需要通过设置 `csvread.delimiter` 属性将分隔符更改为不出现在任何列数据中的字符。

#### 参数（Parameters）
---
属性（Attribute）| 描述| 是否必须
---------|----------|---------
文件名称 | 要读取的文件（或 `*ALIAS`） | 是
列号 | 文件中的列号。 `0` 为第一列，`1`为第二列，以此类推。"`next`" - 转到文件的下一行。 `*ALIAS` - 打开一个文件并指派一个别名 | 是
|

例如，你可以设置一些变量如下：
  * COL1a `${__CSVRead(random.txt,0)}`
  * COL2a `${__CSVRead(random.txt,1)}${__CSVRead(random.txt,next)}`
  * COL1b `${__CSVRead(random.txt,0)}`
  * COL2b `${__CSVRead(random.txt,1)}${__CSVRead(random.txt,next)}`

这将从一行中读取两列，从下一行中读取两列。如果所有变量都在相同的用户参数预处理器上定义，那么这些行将是连续的。否则的话，另外一个线程可能会读取下一行。
>该函数不适用于大文件，因为它会将整个文件存储在内存中。对于较大的文件，请使用 [CSV Data Set Config 元件](http://jmeter.apache.org/usermanual/component_reference.html#CSV_Data_Set_Config) 或 [StringFromFile](#StringFromFile)。


[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="property">__property</h3>

property 函数返回 JMeter 属性的值。如果找不到属性值，并且没有提供默认值，则返回属性名称。当提供默认值时，可以不需要函数名称——参数可以设置为 null，并且将被忽略。

例如：
  * `${__property(user.dir)}` - 返回 `user.dir` 的值
  * `${__property(user.dir,UDIR)}` - 返回 `user.dir` 的值并保存在 `UDIR` 中
  * `${__property(abcd,ABCD,atod)}` - 返回属性 `abcd` 的值（如果没有定义，则返回“`atod`”）并保存在 `ABCD` 中
  * `${__property(abcd,,atod)}` - 返回属性 `abcd`的值（如果未定义，则返回“`atod`”）但不保存

#### 参数（Parameters）
---
属性（Attribute）| 描述| 是否必须
---------|----------|---------
属性名称 | 要检索的属性名称 | 是
变量名称 | 重用此函数计算的值的引用名称 | 否
默认值 | 属性的默认值 |  否

[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="threadNum">__</h3>



#### 参数（Parameters）
---
属性（Attribute）| 描述| 是否必须
---------|----------|---------
第一个参数 |  | 是
[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="threadNum">__</h3>



#### 参数（Parameters）
---
属性（Attribute）| 描述| 是否必须
---------|----------|---------
第一个参数 |  | 是
[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="threadNum">__</h3>



#### 参数（Parameters）
---
属性（Attribute）| 描述| 是否必须
---------|----------|---------
第一个参数 |  | 是
[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="threadNum">__</h3>



#### 参数（Parameters）
---
属性（Attribute）| 描述| 是否必须
---------|----------|---------
第一个参数 |  | 是
[【返回标题】](#20-函数和变量) [【返回函数列表】](#functions_list)

<h3 id="threadNum">__</h3>
