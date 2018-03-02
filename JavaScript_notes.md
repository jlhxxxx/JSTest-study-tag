# <center>JavaScript 基础教程</center>

<center>**与Java没有一毛钱关系**</center>

## JS 教程

* **JavaScript：写入 HTML 输出、对事件作出反应、改变 HTML 元素的内容样式、改变 HTML 图像**

>提示 1：只能在 HTML 输出中使用 document.write。在文档已加载后使用它（比如在函数中），会覆盖整个文档。（点击之后记得重新加载页面）

```javascript
# Example 1：
<button onclick="theWrong()" style=" color:red">错误用法</button>
<script>
function theWrong()
{
document.write("糟糕！文档消失了。");
}
</script>
```

>提示2:HTML 中的脚本必须位于 < script > 与 < /script > 标签之间。脚本可被放置在 HTML 页面的 < body > 和 < head > 部分中。

>提示 3：在 JavaScript 中，用分号来结束语句是可选的。

>提示 4：JavaScript 对大小写敏感。

>提示 5：JavaScript 是脚本语言。浏览器会在读取代码时，逐行地执行脚本代码。而对于传统编程来说，会在执行前对所有代码进行编译。

>提示 6：我们使用 var 关键词来声明变量，变量声明之后，该变量是空的（它没有值），变量可以重新声明，重新声明不会改变该变量的值。向变量分配文本值时，应该用双引号或单引号包围这个值；向变量赋的值是数值时，不要使用引号。

>提示 7：在 JavaScript 函数内部声明的变量（使用 var）是局部变量，所以只能在函数内部访问它。在函数外声明的变量是全局变量，网页上的所有脚本和函数都能访问它。如果把值赋给尚未声明的变量，该变量将被自动作为全局变量声明。

>提示 8：break 语句用于跳出循环，continue 用于跳过循环中的一个迭代。 continue 语句（带有或不带标签引用）只能用在循环中； break 通过标签引用，可用于跳出任何 JavaScript 代码块。

* **外部的 JavaScript**  

  如需使用外部文件，请在 < script > 标签的 "src" 属性中设置该 .js 文件：

  ```javascript
  <!DOCTYPE html>
  <html>
  <body>
  <script src="myScript.js"></script>
  </body>
  </html>
  ```

* **JavaScript 数组**

   ```javascript
   var cars=new Array();
   cars[0]="Audi";
   cars[1]="BMW";
   cars[2]="Volvo";
   ```
   或者：

   ```javascript
   var cars=new Array("Audi","BMW","Volvo");
   ```

* **JavaScript 对象**

   ```javascript
   var person={firstname:"Bill", lastname:"Gates", age：56,eyecolor:"blue"};
   ```

   或者：

   ```javascript
   person=new Object();
   person.firstname="Bill";
   person.lastname="Gates";
   person.age=56;
   person.eyecolor="blue";
   ```

* **特殊的循环**  

  for/in - 循环遍历对象的属性

  ```javascript
  var person={fname:"John",lname:"Doe",age:25};
  for (x in person)
    {
    txt=txt + person[x];
    }
  ```

* **JavaScript 错误 - Throw、Try 和 Catch**  

  try 语句测试代码块的错误， catch 语句处理错误， throw 语句创建自定义错误。  

  ```javascript
  # Example 2：
  <script>
  function numTest()
  {
  try
    {
    var x=document.getElementById("demoOne").value;
    if(x=="")    throw "empty";
    if(isNaN(x)) throw "not a number";
    if(x>10)     throw "too high";
    if(x<5)      throw "too low";
    }
  catch(err)
    {
    var y=document.getElementById("mess");
    y.innerHTML="Error: " + err + ".";
    }
  }
  </script>

  <p style=" color:blue">Please input a number between 5 and 10:</p>
  <input id="demoOne" type="text" style=" color:blue">
  <button type="button" onclick="numTest()">Test Input</button>
  <p id="mess"></p>
  ```

## JavaScript HTML DOM

当网页被加载时，浏览器会创建页面的文档对象模型（Document Object Model）。HTML DOM 模型被构造为对象的树。   

<center>![](http://www.w3school.com.cn/i/ct_htmltree.gif)</center>

<center>**HTML DOM 树**</center> 

* 查找 HTML 元素

    * 通过 id 找到 HTML 元素

      ```javascript
      var x=document.getElementById("intro");
      ```

    * 通过标签名找到 HTML 元素  

      本例查找 id="main" 的元素，然后查找 "main" 中的所有 < p > 元素

      ```javascript
      var x=document.getElementById("main");
      var y=x.getElementsByTagName("p");
      ```

    * 通过类名找到 HTML 元素(在 IE 5,6,7,8 中无效)

* 改变 HTML 内容

   ```javascript
   document.getElementById(id).innerHTML=new HTML
   ```

* 改变 HTML 属性

   ```javascript
   document.getElementById(id).attribute=new value
   ```

* 改变 HTML 样式

   ```javascript
   document.getElementById(id).style.property=new style
   ```

* 使 JavaScript 对 HTML 事件做出反应

    * 当用户点击鼠标时

      ```javascript
      onclick=JavaScript
      ```
      
    * 当网页已加载时
      
      ```javascript
      onload和onunload
      ```

    * 当图像已加载时

    * 当鼠标移上/移出/点击/放弃点击元素时

      ```javascript
      onmouseover=JavaScript	
      onmouseout=JavaScript
      onmousedown=JavaScript
      onmouseup=JavaScript
      ```

    * 当输入字段被改变时

      ```javascript
      onchange=JavaScript
      ```

    * 当提交 HTML 表单时
    * 当用户触发按键时

* 添加和删除节点（HTML 元素）

    * 创建新的 HTML 元素

      ```javascript
      <div id="div1">
      <p id="p1">这是一个段落</p>
      <p id="p2">这是另一个段落</p>
      </div>
        
      <script>
      var para=document.createElement("p");
      var node=document.createTextNode("这是新段落。");
      para.appendChild(node);
          	
      var element=document.getElementById("div1");
      element.appendChild(para);
      </script>
      ```

    * 删除已有的 HTML 元素

      ```javascript
      <div id="div1">
      <p id="p1">这是一个段落。</p>
      <p id="p2">这是另一个段落。</p>
      </div>
          	
      <script>
      var parent=document.getElementById("div1");
      var child=document.getElementById("p1");
      parent.removeChild(child);
      </script>
      ```

* 例子：弹出Welcome!界面  

     ```javascript
     # Example 3：
     <button type="button" onclick="alert('You are Welcome!')" >Welcome</button>
     <button onclick="wecSb('Bill Gates','CEO')" >使用函数</button>

     <script>
     function wecSb(name,job)
     {
     alert("Welcome " + name + ", the " + job);
     }
     </script>
     ```


* 例子：修改文字内容

  ```javascript
  # Example 4：
  <p id="p1" style=" color:blue">这是一段文本。</p>
  <input type="button" value="隐藏文本" onclick="document.getElementById('p1').style.visibility='hidden'" />
  <input type="button" value="显示文本" onclick="document.getElementById('p1').style.visibility='visible'" />
  <input type="button" value="修改内容" onclick="changePara('p1')" />
  <script>
  function changePara(obj)
  {
  if(document.getElementById(obj).style.color=='black')	//注意不要漏引号，\吐血经验
  {
  document.getElementById(obj).style.color='red';
  document.getElementById(obj).innerHTML='it is red'
  }
  else{
  document.getElementById(obj).style.color='black';
  document.getElementById(obj).innerHTML='it is black'
  }
  }
  </script>
  ```


* 例子：将输入转换成大写

  ```javascript
  # Example 5：
  <script>
  function changeUp()
  {
  var x=document.getElementById("fname");
  x.value=x.value.toUpperCase();
  }
  </script>
  <p style=" color:blue">请输入英文字符：<input type="text" id="fname" onchange="changeUp()" style=" color:blue"></p>
  ```


* 例子：鼠标移上/移出/按下/释放点击元素时

  ```javascript
  # Example 6：
  <div onmouseover="mOver(this)" onmouseout="mOut(this)" onmousedown="mDown(this)" onmouseup="mUp(this)" style="background-color:green;color:#ffffff;width:90px;height:20px;padding:40px;font-size:12px;">请点击这里</div>

  <script>
  function mOver(obj)
  {
  obj.style.backgroundColor="red";
  obj.innerHTML="谢谢"
  }

  function mOut(obj)
  {
  obj.style.backgroundColor="yellow";
  obj.innerHTML="把鼠标移到上面"
  }

  function mDown(obj)
  {
  obj.style.backgroundColor="#1ec5e5";
  obj.innerHTML="请释放鼠标按钮";
  }

  function mUp(obj)
  {
  obj.style.backgroundColor="green";
  obj.innerHTML="请按下鼠标按钮";
  }
  </script>
  ```

## JS 对象

* **JS 对象**

  * 访问对象的属性

    ```javascript
    objectName.propertyName
    ```

  * 访问对象的方法

    ```javascript
    objectName.methodName()
    ```

  * 创建 JavaScript 对象
  * JavaScript 是面向对象的语言，但 JavaScript 不使用类 

* **JS 数字**

    * JavaScript 中的所有数字都存储为根为 10 的 64 位（8 比特），浮点数；整数（不使用小数点或指数计数法）最多为 15 位，小数的最大位数是 17，但是浮点运算并不总是 100% 准确。

      ```javascript
      # Example 7：
      <script>
      var x;
      document.write("<font color='blue'><p>输入 12345678901234567890 ，输出只有 17 位: </font>");
      x=12345678901234567890;
      document.write("<font color='blue'>"+x + "</p></font>");
      document.write("<font color='blue'><p>0.2 + 0.1 = </font>");
      x=0.2+0.1;
      document.write("<font color='blue'>"+x + "</p></font>");
      document.write("<font color='blue'><p>可分别乘以 10 并除以 10 : </font>");
      x=(0.2*10+0.1*10)/10;
      document.write("<font color='blue'>"+x +"</p></font>");
      </script>
      ```

     * 如果前缀为 0，则 JavaScript 会把数值常量解释为八进制数，如果前缀为 0x ，则解释为十六进制数。

      * 数字属性和方法

          | 属性                  |
          | --------------------- |
          | * MAX VALUE           |
          | * MIN VALUE           |
          | * NEGATIVE INFINITIVE |
          | * POSITIVE INFINITIVE |
          | * NaN                 |
          | * prototype           |
          | * constructor         |

          | 方法              |
          | ----------------- |
          | * toExponential() |
          | * toFixed()       |
          | * toPrecision()   |
          | * toString()      |
          | * valueOf()       |



* **JS 字符串**
   * 计算字符串的长度
   * 为字符串添加样式
   * indexOf() 方法，定位字符串中某一个指定的字符首次出现的位置
   * match() 方法，查找字符串中特定的字符，并且如果找到的话，则返回这个字符
   * replace()方法，替换字符串中的字符


* **JS 日期**
   * Date()，返回当日的日期和时间

   * getTime()，返回从 1970 年 1 月 1 日至今的毫秒数

   * setFullYear() ，设置具体的日期

   * toUTCString() ，将当日的日期（根据 UTC）转换为字符串

   * getDay() ，用数字表示星期几

   * 实时显示时间：（注意onload用法）

     ```javascript
     # Example 8：
     <script type="text/javascript">
     function checkCookie()
     {
     if (navigator.cookieEnabled==true)
     	{
     	alert("已启用 cookie")
     	}
     else
     	{
     	alert("未启用 cookie")
     	}
     startTime()
     }
     function startTime()
     {
     var today=new Date()
     var h=today.getHours()
     var m=today.getMinutes()
     var s=today.getSeconds()
     // add a zero in front of numbers<10
     m=checkTime(m)
     s=checkTime(s)
     document.getElementById('txt').innerHTML="现在的时间是："+h+":"+m+":"+s
     t=setTimeout('startTime()',500)	//每隔500毫秒执行一次
     }

     function checkTime(i)
     {
     if (i<10) 
       {i="0" + i}
       return i
     }
     </script>

     <body onload="checkCookie()">
     <div id="txt" style=" color:blue"></div>
     </body>
     ```


* **JS 数组**
    * concat()，合并两个数组

       ```javascript
       array1.concat(array2)
       ```

    * join()，用数组的元素组成字符串

       ```javascript
       array.join()	//默认用"，"连接
       array.join(".")	//用"."连接
       ```

    * sort()，数组排序（注意两种结果）

        ```javascript
        # Example 9：
        <script type="text/javascript">
        //排序方法（注意return符号）
        function sortNumber1(a, b)
        {
        return a - b
        }
        function sortNumber2(a, b)
        {
        return b - a
        }

        var arr = new Array(6)
        arr[0] = "10"
        arr[1] = "5"
        arr[2] = "40"
        arr[3] = "25"
        arr[4] = "1000"
        arr[5] = "1"

        document.write("<font color='blue'>The arr is : "+ arr + "<br /></font>")
        document.write("<font color='blue'>使用默认排序："+arr.sort()+ "<br /></font>")
        document.write("<font color='blue'>按大小正序："+arr.sort(sortNumber1)+ "<br /></font>")
        document.write("<font color='blue'>按大小倒序："+arr.sort(sortNumber2)+ "<br /></font>")
        </script>
        ```


* **JS 逻辑**
    * 如果逻辑对象无初始值或者其值为 0、-0、null、""、false、undefined 或者 NaN，那么对象的值为 false。否则，其值为 true（即使当自变量为字符串 "false" 时）！

* **JS 算数**
    * Math.round()，四舍五入

    * Math.random()

    * Math.max()

    * Math.min()

    * 算数值

      | JavaScript 提供 8 种  | 可被Math 对象访问的算数值 |
      | --------------------- | ------------------------- |
      | 常数                  | Math.E                    |
      | 圆周率                | Math.PI                   |
      | 2 的平方根            | Math.SQRT2                |
      | 1/2 的平方根          | Math.SQRT1_2              |
      | 2 的自然对数          | Math.LN2                  |
      | 10 的自然对数         | Math.LN10                 |
      | 以 2 为底的 e 的对数  | Math.LOG2E                |
      | 以 10 为底的 e 的对数 | Math.LOG10E               |

* **JS 正则表达式(RegExp)**

    * 定义 RegExp

      ```javascript
      var patt1=new RegExp("e");
      ```
      
    * RegExp 对象的方法

      * test() 方法检索字符串中的指定值。返回值是 true 或 false。
        
        ```javascript
        document.write(patt1.test("The best things in life are free")); 
        ```

      * exec() 方法检索字符串中的指定值。返回值是被找到的值。如果没有发现匹配，则返回 null。

        ```javascript
        document.write(patt1.exec("The best things in life are free"));
        ```

      * compile() 方法用于改变 RegExp，既可以改变检索模式，也可以添加或删除第二个参数。

        ```javascript
        document.write(patt1.test("The best things in life are free"));
            patt1.compile("d");
            document.write(patt1.test("The best things in life are free"));
        ```


## JS Windows（BOM）

* **JS Windows**

   ```javascript
   window.innerHeight  //浏览器窗口的内部高度
   window.innerWidth  //浏览器窗口的内部宽度
   window.open() //打开新窗口
   window.close() //关闭当前窗口
   window.moveTo() //移动当前窗口
   window.resizeTo() //调整当前窗口的尺寸
   ```

* **JS Screen**

   ```javascript
   screen.availWidth //可用的屏幕宽度
   screen.availHeight //可用的屏幕高度
   ```

* **JS Location**

   ```javascript
   location.hostname //返回 web 主机的域名
   location.pathname //返回当前页面的路径和文件名
   location.port //返回 web 主机的端口 （80 或 443）
   location.protocol //返回所使用的 web 协议（http:// 或 https://）
   location.href //属性返回当前页面的 URL
   location.assign() //方法加载新的文档
   ```

* **JS History**

   ```javascript
   history.back() //与在浏览器点击后退按钮相同
   history.forward() //与在浏览器中点击按钮向前相同
   ```

* **JS Navigator**  

  navigator 对象包含有关访问者浏览器的信息

  ```javascript
  # Example 10：
  <div id="example" style=" color:blue"></div>
  <script>
  txt = "<p>Browser CodeName: " + navigator.appCodeName + "</p>";
  txt+= "<p>Browser Name: " + navigator.appName + "</p>";
  txt+= "<p>Browser Version: " + navigator.appVersion + "</p>";
  txt+= "<p>Cookies Enabled: " + navigator.cookieEnabled + "</p>";
  txt+= "<p>Platform: " + navigator.platform + "</p>";
  txt+= "<p>User-agent header: " + navigator.userAgent + "</p>";
  txt+= "<p>User-agent language: " + navigator.systemLanguage + "</p>";

  document.getElementById("example").innerHTML=txt;
  </script>
  ```


* **JS PopupAlert**  

  * 警告框

    ```javascript
    alert("文本")
    ```

  * 确认框

    ```javascript
    confirm("文本")
    ```

  * 提示框

    ```javascript
    prompt("文本","默认值")
    ```


* **JS Timing** 

  * setTimeout()，未来的某时执行代码(可以参考上面实时时钟)

    ```javascript
    var t=setTimeout("javascript语句",毫秒)
    ```


  * clearTimeout()，取消setTimeout()

    ```javascript
    # Example 11：
    <script type="text/javascript">
    var c=0
    var t
    function timedCount()
    {      document.getElementById('txtTime').value=c
    c=c+1
    t=setTimeout("timedCount()",1000)
    }

    function stopCount()
    {
    c=0;      setTimeout("document.getElementById('txtTime').value=0",0);
    clearTimeout(t);
    }
    </script>

    <input type="button" value="开始计时！" onClick="timedCount()">
    <input type="text" id="txtTime" style=" color:blue">
    <input type="button" value="停止计时！" onClick="stopCount()">
    ```



* **JS Cookies** 

  ```javascript
  # Example 12：
  <script type="text/javascript">
  //创建一个函数来检查是否已设置 cookie
  function getCookie(c_name)
  {
  if (document.cookie.length>0)
  { 
  c_start=document.cookie.indexOf(c_name + "=")
  if (c_start!=-1)
  { 
  c_start=c_start + c_name.length+1 
  c_end=document.cookie.indexOf(";",c_start)
  if (c_end==-1) c_end=document.cookie.length
  return unescape(document.cookie.substring(c_start,c_end))
  } 
  }
  return ""
  }
  	
  //创建一个可在 cookie 变量中存储访问者姓名的函数
  function setCookie(c_name,value,expiredays)	//参数存有 cookie 的名称、值以及过期天数
  {
  var exdate=new Date()
  exdate.setDate(exdate.getDate()+expiredays)	//先将天数转换为有效的日期
  document.cookie=c_name+ "=" +escape(value)+
  ((expiredays==null) ? "" : "; expires="+exdate.toGMTString())
  }	//将 cookie 名称、值及其过期日期存入 document.cookie 对象
  	
  //如果 cookie 已设置，则显示欢迎词，否则显示提示框来要求用户输入名字
  function checkCookie1()
  {
  username=getCookie('username')
  if (username!=null && username!="")
    {alert('Welcome again '+username+'!')}
  else 
    {
    username=prompt('Please enter your name:',"")
    if (username!=null && username!="")
      {
      setCookie('username',username,365)
      }
    }
  }
  </script>
  ```

## JS 库（框架）

* **jQuery**  

  * 引用：

    ```javascript
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js">
    </script>
    ```

  * 主要的 jQuery 函数是 $() 函数（jQuery 函数）。如果您向该函数传递 DOM 对象，它会返回 jQuery 对象，带有向其添加的 jQuery 功能。

    * JavaScript 方式：

        ```javascript
        function myFunction()
        {
        var obj=document.getElementById("h01");
        obj.innerHTML="Hello jQuery";
        }
        onload=myFunction;
        ```

    * 等价的 jQuery 方式：

        ```javascript
        function myFunction()
        {
        $("#h01").html("Hello jQuery");
        }
        $(document).ready(myFunction);
        ```

        jQuery 返回 jQuery 对象，与已传递的 DOM 对象不同。jQuery 对象拥有的属性和方法，与 DOM 对象的不同。不能在 jQuery 对象上使用 HTML DOM 的属性和方法。  

  * jQuery 允许链接（链式语法）：
    
      ```javascript
      $("#h01").attr("style","color:red").html("Hello jQuery")
      ```

* **Prototype**  

  * 引用：

    ```javascript
     <script src="http://ajax.googleapis.com/ajax/libs/prototype/1.7.1.0/prototype.js">
    </script>
    ```

  * $() 函数接受 HTML DOM 元素的 id 值（或 DOM 元素），并会向 DOM 对象添加新的功能。与 jQuery 不同，Prototype 没有用以取代 window.onload() 的 ready() 方法。相反，Prototype 会向浏览器及 HTML DOM 添加扩展。

       * JavaScript 方式：

            ```javascript
            function myFunction()
            {
            var obj=document.getElementById("h01");
            obj.innerHTML="Hello Prototype";
            }
            onload=myFunction;
            ```

       * 等价的 Prototype 方式：

         ```javascript
         function myFunction()
         {
         $("h01").insert("Hello Prototype!");
         }
         Event.observe(window,"load",myFunction);
         ```

    * Event.observe() 接受三个参数：

        * 您希望处理的 HTML DOM 或 BOM（浏览器对象模型）对象
        * 您希望处理的事件
        * 您希望调用的函数

    * Prototype 同样允许链接（链式语法）： 

       ```javascript
       $("h01").writeAttribute("style","color:red").insert("Hello Prototype!");
       ```
  	
