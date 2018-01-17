


## 输入和输出

* `print()` 可接受多个字符串，用逗号“,”隔开，输出时逗号变成空格

        >>> print('100 + 200 =', 100 + 200)
        100 + 200 = 300
* `input()`括号内可加提示

        name = input('please enter your name: ')
* `#` 注释
* 语句以冒号 `:` 结尾时，缩进的语句视为代码块，坚持使用 4 个空格的缩进
* 大小写敏感
* 不支持 `++`、`--`、`+=`……
* `\` 转义，`\n` 表示换行，`\t` 表示制表符，`r''`表示 `''` 内部的字符串默认不转义，用 `'''...'''` 的格式表示多行内容

        >>> print('\\\t\\')
        \       \
        >>> print(r'\\\t\\')
        \\\t\\
        >>> print('''line1
        ... line2
        ... line3''')
        line1
        line2
        line3
* 布尔值 `True`、`False`，空值 `None`（注意大小写）
* `/` 除法计算结果是浮点数，结果也是浮点数；`//` 称为地板除，两个整数的除法仍然是整数

      >>> 9 / 3
      3.0
      >>> 10 % 3
      1
* `**` 求幂

      >>> 10**3
      1000
* 字符串
  * 对于单个字符的编码，Python 提供了 `ord()` 函数获取字符的整数表示，`chr()` 函数把编码转换为对应的字符

        >>> ord('A')
        65
        >>> ord('中')
        20013
        >>> chr(66)
        'B'
        >>> chr(25991)
        '文'
        >>> '\u4e2d\u6587'
        '中文'
  * Python 的字符串类型是 str，在内存中以 Unicode 表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把 str 变为以字节为单位的 bytes。Python 对 bytes 类型的数据用带 b 前缀的单引号或双引号表示：

        x = b'ABC'
    要注意区分 `'ABC'` 和 `b'ABC'`，前者是 str，后者虽然内容显示得和前者一样，但 bytes 的每个字符都只占用一个字节。

    以 Unicode 表示的 str 通过 `encode()` 方法可以编码为指定的 bytes，超出编码的会报错。

        >>> 'ABC'.encode('ascii')
        b'ABC'
        >>> '中文'.encode('utf-8')
        b'\xe4\xb8\xad\xe6\x96\x87'
        >>> '中文'.encode('ascii')
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>……
    反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是 bytes。要把 bytes 变为 str，就需要用 `decode()` 方法，无法解码的也会报错。

        >>> b'ABC'.decode('ascii')
        'ABC'
        >>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
        '中文'
    如果 bytes 中只有一小部分无效的字节，可以传入 `errors='ignore'` 忽略错误的字节：

        >>> b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
        '中'
  * `len()` 函数计算的是str的字符数，如果换成 bytes ，`len()` 函数就计算字节数。

        >>> len('abc')
        3
        >>> len(b'abc')
        3
        >>> len('中文')
        2
        >>> len('中文'.encode('utf-8'))
        6
  * 为防止乱码，通常在 py 文件开头加上：

        #!/usr/bin/env python3
        # -*- coding: utf-8 -*-
  * python 中格式化和C语言是一致的，用 `%` 实现，在字符串内部，`%s` 表示用字符串替换，`%d` 表示用整数替换，`%f` 表示用浮点数替换，`%x` 表示用十六进制整数替换，有几个 `%?` 占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个 `%?`，括号可以省略。

        >>> 'Hello, %s' % 'world'
        'Hello, world'
        >>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
        'Hi, Michael, you have $1000000.'
    不太确定应该用什么，`%s` 永远起作用，它会把任何数据类型转换为字符串，用 `%%` 来转义一个 `%`。

    另一种格式化字符串的方法是使用字符串的 `format()` 方法，它会用传入的参数依次替换字符串内的占位符 `{0}`、`{1}`……，不过这种方式写起来比 `%` 要麻烦得多：

        >>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
        'Hello, 小明, 成绩提升了 17.1%'
* list 有序集合，使用 `[]`，list 元素数据类型可以不同，也可以是另一个 list

      >>> classmates = ['Michael', 'Bob', 'Tracy']
      >>> classmates
      ['Michael', 'Bob', 'Tracy']
      >>> len(classmates)
      3

      # 正索引 0 开始
      >>> classmates[0]
      'Michael'
      # 倒索引 -1 开始
      >>> classmates[-1]
      'Tracy'

      # 追加元素到末尾
      >>> classmates.append('Lisa')
      # 插入到指定位置（同正索引）
      >>> classmates.insert(1,'Lucy')
      # 删除末尾的元素
      >>> classmates.pop()
      # 删除指定位置的元素（同正索引）
      >>> classmates.pop(1)
      # 替换直接用赋值语句
      >>> classmates[1] = 'Tom'

      # 将一个序列转换成 list
      >>> list(range(5))
      [0, 1, 2, 3, 4]

* tuple 有序集合，使用 `()`。和 list 区别：一旦初始化就不能修改（所以没有 append、insert、pop）

      >>> classmates = ('Michael', 'Bob', 'Tracy')
      # 只有一个元素时，要加逗号消除歧义
      >>> t = (1,)
      # “可变的”tuple，只是指向不变
      >>> t = ('a', 'b', ['A', 'B'])
* 条件判断（注意冒号和缩进）

      if <条件判断1>:
          <执行1>
      elif <条件判断2>:
          <执行2>
      elif <条件判断3>:
          <执行3>
      else:
          <执行4>
* 循环 `for x in ...`、`while`
  * `break` 语句可以在循环过程中直接退出循环，而 `continue` 语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合 `if` 语句使用。
* dict（Java 中 map），使用`{}`，无序，占用内存，key 必须是不可变对象且唯一

      # 取元素要使用 list
      >>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
      >>> d['Michael']
      95

      # 通过 in 判断 key 是否存在
      >>> 'Tom' in d
      False
      # 通过 get 返回值，不指定为 None，控制台不显示
      >>> d.get('Thomas')
      >>> d.get('Thomas', -1)
      -1

      # 删除 key
      >>> d.pop('Bob')
      75

      # 增加，通过赋值语句
      >>> d['Lisa'] = 99
* set 一组 key 的集合，但不存储 value，同样 key 必须是不可变对象且唯一，可以做 `&`、`|` 等操作

      # 要创建一个set，需要提供一个 list 作为输入集合
      >>> s = set([1, 1, 2, 2, 3, 3])
      >>> s
      {1, 2, 3}

      # 添加元素，add(key)
      >>> s.add(4)
      >>> s
      {1, 2, 3, 4}

      # 删除元素，remove(key)
* 定义一个函数要使用 `def` 语句，依次写出函数名、括号、括号中的参数和冒号 `:`，然后在缩进块中编写函数体，函数的返回值用 `return` 语句返回。

      def my_abs(x):
          if x >= 0:
              return x
          else:
            return -x
  如果已经把 `my_abs()` 的函数定义保存为 abstest.py 文件了，那么，可以在该文件的当前目录下启动 Python 解释器，用 `from abstest import my_abs` 来导入 `my_abs()`。

  如果想定义一个什么事也不做的空函数，可以用 `pass` 语句：

      def nop():
          pass

    Python 的函数返回多值其实就是返回一个 tuple
* 函数的参数
  * 默认参数（赋默认值，降低调用难度）

        def power(x, n=2):
            s = 1
            while n > 0:
                n = n - 1
                s = s * x
            return s

        >>> power(5)
        25
    定义默认参数要牢记一点：默认参数必须指向不变对象！

        # 错误例子
        def add_end(L=[]):
            L.append('END')
            return L

        >>> add_end()
        ['END']
        >>> add_end()
        ['END', 'END']

        # 修改后为
        def add_end(L=None):
            if L is None:
                L = []
            L.append('END')
            return L

  * 可变参数（在参数前面加一个星号 `*`）——允许传入 0 个或任意个参数，这些可变参数在函数调用时自动组装为一个 tuple

        def calc(*numbers):
            sum = 0
            for n in numbers:
                sum = sum + n * n
            return sum

        >>> calc(1,2,3)
        14
        >>> nums = [1, 2, 3]
        >>> calc(nums[0], nums[1], nums[2])
        14
        # 调用简化
        >>> cale(*num)
        14

  * 关键字参数（在参数前面加两个星号 `**`）——允许传入 0 个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个 dict

        def person(name, age, **kw):
            print('name:', name, 'age:', age, 'other:', kw)

        >>> person('Michael', 30)
        name: Michael age: 30 other: {}
        >>> person('Adam', 45, gender='M', job='Engineer')
        name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
        # 调用简化
        >>> extra = {'city': 'Beijing', 'job': 'Engineer'}
        >>> person('Jack', 24, **extra)
        name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

  * 命名关键字参数（特殊分隔符 `*`，`*` 后面的参数被视为命名关键字参数）——限制关键字参数的名字

        def person(name, age, *, city, job):
            print(name, age, city, job)
    如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符 `*` 了：

        def person(name, age, *args, city, job):
            print(name, age, args, city, job)
    命名关键字参数可以有缺省值（类似默认参数）。
  * 参数组合

      参数定义的顺序必须是：**必选参数、默认参数、可变参数、命名关键字参数和关键字参数**。

      对于任意函数，都可以通过类似 `func(*args, **kw)` 的形式调用它，无论它的参数是如何定义的。

        def f1(a, b, c=0, *args, **kw):
            print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

        >>> args = (1, 2, 3, 4)
        >>> kw = {'d': 99, 'x': '#'}
        >>> f1(*args, **kw)
        a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

* 函数递归
  * 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

* 切片

      >>> L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
      # 左闭右开
      >>> L[0:3]
      ['Michael', 'Sarah', 'Tracy']
      # 第一个索引是 0 可以省略
      >>> L[:3]
      ['Michael', 'Sarah', 'Tracy']
      >>> L[-2:]
      ['Bob', 'Jack']

      >>> L = list(range(100))
      # 前10个数，每两个取一个
      >>> L[:10:2]
      [0, 2, 4, 6, 8]
      # 所有数，每5个取一个
      >>> L[::5]
      [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
      # 原样复制
      >>> L[:]
      [0, 1, 2, 3, ..., 99]

      # 字符串倒序排列（也可以间隔取值）
      >>> 'abcd'[::-1]
      'dcba'

* 迭代
  * 在 Python 中，迭代是通过 `for ... in` 来完成的
  * 默认情况下，dict 迭代的是 key。如果要迭代 value，可以用 `for value in d.values()`，如果要同时迭代 key 和 value，可以用 `for k, v in d.items()`。
  * 如果要对 list 实现类似 Java 那样的下标循环怎么办？Python 内置的 enumerate 函数可以把一个 list 变成索引——元素对，这样就可以在 for循环中同时迭代索引和元素本身：

        >>> for i, value in enumerate(['A', 'B', 'C']):
        ...     print(i, value)
        ...
        0 A
        1 B
        2 C

* 列表生成式 `[]`，一次生成完毕，占内存

      >>> [x * x for x in range(1, 11) if x % 2 == 0]
      [4, 16, 36, 64, 100]
      >>> [m + n for m in 'ABC' for n in 'XYZ']
      ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

* 生成器（generator） `()`，一边循环一遍计算

      >>> g = (x * x for x in range(10))
      >>> g
      <generator object <genexpr> at 0x1022ef630>
      # 可以通过 next() 调用
      >>> next(g)
      0
      # 也可以通过for调用
      >>> for i in g:
      ...     print(i)

  如果一个函数定义中包含 yield 关键字，那么这个函数就不再是一个普通函数，而是一个 generator （yield 指到这里暂停并返回 yield 后的值，类似 return）

      def fib(max):
          n, a, b = 0, 0, 1
          while n < max:
              yield b
              a, b = b, a + b
              n = n + 1
          return 'done'

      >>> f = fib(6)
      >>> f
      <generator object fib at 0x104feaaa0>

* 迭代器
  * 可以直接作用于 for 循环的对象统称为可迭代对象：Iterable
  * 可以被 `next()` 函数调用并不断返回下一个值的对象称为迭代器：Iterator ，它们表示一个惰性计算的序列；
  * 生成器都是 Iterator 对象，但 list、dict、str 虽然是 Iterable，却不是 Iterator。把list、dict、str等 Iterable 变成 Iterator 可以使用 `iter()` 函数：

        >>> isinstance(iter([]), Iterator)
        True
        >>> isinstance(iter('abc'), Iterator)
        True

## 函数式编程

允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

* 高阶函数
  * 变量可以指向函数

        >>> f = abs
        >>> f(-10)
        10
  * 函数名也是变量

        >>> abs = 10
        >>> abs(-10)
        ...报错
  * 传入函数

        def add(x, y, f):
            return f(x) + f(y)

        >>> add(-5, 6, abs)
        11

  * map/reduce
    * `map()` 函数接收两个参数，一个是函数，一个是 **Iterable**，map 将传入的函数依次作用到序列的每个元素，并把结果作为新的 **Iterator** 返回。

          def f(x):
              return x * x

          >>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
          >>> list(r)
          [1, 4, 9, 16, 25, 36, 49, 64, 81]

    * `reduce()` 把一个函数作用在一个序列 [x1, x2, x3, ...] 上，这个函数必须接收两个参数，reduce 把结果继续和序列的下一个元素做累积计算，其效果就是：

          reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

  * fitter 用于过滤序列
    * 和 `map()` 类似，`filter()`也接收一个函数和一个序列。和 `map()` 不同的是，`filter()` 把传入的函数依次作用于每个元素，然后根据返回值是 True 还是 False 决定保留还是丢弃该元素（类似列表生成式后的 if 条件）。

          def not_empty(s):
              return s and s.strip()

          >>> list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
          ['A', 'B', 'C']
      注意到 `filter()` 函数返回的也是一个 Iterator，也就是一个惰性序列，所以要强迫 `filter()` 完成计算结果，需要用 `list()` 函数获得所有结果并返回 list

  * sorted 排序算法

        >>> sorted([36, 5, -12, 9, -21])
        [-21, -12, 5, 9, 36]
    可以接收一个 key 函数来实现自定义的排序 key 指定的函数将作用于 list 的每一个元素上，并根据 key 函数返回的结果进行排序

        >>> sorted([36, 5, -12, 9, -21], key=abs)
        [5, 9, -12, -21, 36]
    要进行反向排序，不必改动 key 函数，可以传入第三个参数 `reverse=True`

        >>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
        ['Zoo', 'Credit', 'bob', 'about']

* 返回函数
  * 函数作为返回值

        def lazy_sum(*args):
            def sum():
                ax = 0
                for n in args:
                    ax = ax + n
                return ax
            return sum

        当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
        >>> f = lazy_sum(1, 3, 5, 7, 9)
        >>> f
        <function lazy_sum.<locals>.sum at 0x101c6ed90>

        调用函数f时，才真正计算求和的结果：
        >>> f()
        25

        当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
        >>> f1 = lazy_sum(1, 3, 5, 7, 9)
        >>> f2 = lazy_sum(1, 3, 5, 7, 9)
        >>> f1==f2
        False

  * 闭包——返回的函数并没有立刻执行，而是直到调用了f()才执行。返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

        def count():
            fs = []
            for i in range(1, 4):
                def f():
                    return i*i
                fs.append(f)
            return fs

        >>> f1, f2, f3 = count()
        >>> f1()
        9
        >>> f2()
        9
        >>> f3()
        9
    修改后：

        def count():
            def f(j):
                def g():
                    return j*j
                return g
            fs = []
            for i in range(1, 4):
                fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
            return fs

        >>> f1, f2, f3 = count()
        >>> f1()
        1
        >>> f2()
        4
        >>> f3()
        9

* 匿名函数（有限支持）

      >>> list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
      [1, 4, 9, 16, 25, 36, 49, 64, 81]
  关键字 `lambda` 表示匿名函数，冒号前面的 `x` 表示函数参数。匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

  匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：

      >>> f = lambda x: x * x
      >>> f
      <function <lambda> at 0x101c6ef28>
      >>> f(5)
      25

* 装饰器

  假设我们要增强函数的功能，但又不希望修改函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

  由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。函数对象有一个 `__name__` 属性，可以拿到函数的名字

      >>> f = lambda x: x * x
      >>> f.__name__
      '<lambda>'

  定义一个能打印日志的decorator，可以定义如下：

      def log(func):                                  #step1：执行 log
          def wrapper(*args, **kw):                   #step3：执行 wrapper
              print('call %s():' % func.__name__)
              return func(*args, **kw)                #step4：调用 func
          return wrapper                              #step2：调用 wrapper

      @log        # 相当于 now = log(now)
      def now():
          print('2015-3-25')

      >>> now()
      call now():
      2015-3-25

  经过 decorator 装饰之后的函数，它们的`__name__`已经从原来的'now'变成了'wrapper'，所以，需要把原始函数的`__name__`等属性复制到 wrapper() 函数中，否则，有些依赖函数签名的代码执行就会出错。

      >>> now.__name__
      'wrapper'

  Python 内置的 functools.wraps 就是干这个事的，所以，一个完整的decorator 的写法如下：

      import functools

      def log(func):
          @functools.wraps(func)
          def wrapper(*args, **kw):
              print('call %s():' % func.__name__)
              return func(*args, **kw)
          return wrapper

* 偏函数—— functools.partial 的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数。

      >>> import functools
      >>> int2 = functools.partial(int, base=2)
      >>> int2('1000000')
      64
      # base 仍可以传其他值
      >>> int2('1000000', base=10)
      1000000

## 模块

* 自己创建模块时要注意命名，不能和 Python 自带的模块名称冲突。例如，系统自带了 sys 模块，自己的模块就不可命名为 `sys.py`，否则将无法导入系统自带的 sys 模块。
* 每一个包目录下面都会有一个 `__init__.py` 的文件，这个文件是必须存在的，否则，Python 就把这个目录当成普通目录，而不是一个包。`__init__.py` 可以是空文件，也可以有 Python 代码，因为 `__init__.py` 本身就是一个模块，而它的模块名就是包名。

      #!/usr/bin/env python3
      # -*- coding: utf-8 -*-

      ' a test module '

      __author__ = 'Michael Liao'

      import sys

      def test():
          args = sys.argv
          if len(args)==1:
              print('Hello, world!')
          elif len(args)==2:
              print('Hello, %s!' % args[1])
          else:
              print('Too many arguments!')

      if __name__=='__main__':
          test()

  第1行和第2行是标准注释，第1行注释可以让这个 `hello.py` 文件直接在 Unix/Linux/Mac 上运行，第2行注释表示 .py 文件本身使用标准 UTF-8 编码；  
  第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；  
  第6行使用 `__author__` 变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

  你可能注意到了，使用 sys 模块的第一步，就是导入该模块：

      import sys
  导入 sys 模块后，我们就有了变量 sys 指向该模块，利用 sys 这个变量，就可以访问 sys 模块的所有功能。  
  sys 模块有一个 argv 变量，用 list 存储了命令行的所有参数。argv 至少有一个元素，因为第一个参数永远是该 .py 文件的名称，例如  
  运行 `python3 hello.py` 获得的 sys.argv 就是 `['hello.py']`；  
  运行 `python3 hello.py Michael` 获得的 sys.argv 就是 `['hello.py', 'Michael]`。

  最后，注意到这两行代码：

      if __name__=='__main__':
      test()
  当我们在命令行运行 hello 模块文件时，Python 解释器把一个特殊变量`__name__`置为`__main__`，而如果在其他地方导入该 hello 模块时，if 判断将失败，因此，这种 if 测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。

      $ python hello.py Michael
      Hello, Michael!
* 作用域
  * 正常的函数和变量名是公开的（public），可以被直接引用，比如：`abc`，`x123`，`PI` 等；
  * 类似 `__xxx__` 这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的 `__author__`，`__name__` 就是特殊变量，hello模块定义的文档注释也可以用特殊变量 `__doc__` 访问，我们自己的变量一般不要用这种变量名；
  * 类似 `_xxx` 和 `__xxx` 这样的函数或变量就是非公开的（private），不应该被直接引用（只是不应该，并非不能），比如`_abc`，`__abc`等。

* 导入模块：关于 `from..import..` 和 `import...` 的区别：一句话总结，是否有限定名。比如通过 `from sys import path` 导入包路径，可以直接使用 `path`，如果使用 `import sys`，则需要使用 `sys.path` 来访问。

## 面向对象编程

* 类和实例
  * 定义类，类名通常是大写开头的单词，object 表示该类是从哪个类继承下来：

        class Student(object):
            pass
    可以自由地给一个实例变量绑定属性，比如，给实例 `bart` 绑定一个 `name` 属性：

        >>> bart.name = 'Bart Simpson'
  * 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的`__init__`方法，在创建实例的时候，就把 `name`，`score` 等属性绑上去：

        class Student(object):
            def __init__(self, name, score):
                self.name = name
                self.score = score
    `__init__`方法的第一个参数永远是 `self`，表示创建的实例本身，因此，在`__init__`方法内部，就可以把各种属性绑定到 `self`，因为 `self` 就指向创建的实例本身。

    和普通的函数相比，在**类中定义的函数**只有一点不同，就是第一个参数永远是实例变量 `self`，并且，调用时，不用传递该参数。

  * 可以直接在 `Student` 类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：

        class Student(object):

        def __init__(self, name, score):
            self.name = name
            self.score = score

        def print_score(self):
            print('%s: %s' % (self.name, self.score))
    要定义一个方法，除了第一个参数是 `self` 外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了 `self` 不用传递，其他参数正常传入。

* 访问限制
  * 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线`__`，将变量变成私有：

        class Student(object):

            def __init__(self, name, score):
                self.__name = name
                self.__score = score
    双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问`__name` 是因为 Python 解释器对外把`__name` 变量改成了 `_Student__name`，所以，仍然可以通过 `_Student__name` 来访问`__name` 变量，但是不要这么做。

  * 错误写法：

        bart.__name = 'New Name'
    表面上看，外部代码“成功”地设置了`__name` 变量，但实际上这个`__name` 变量和 class 内部的`__name` 变量不是一个变量！因为内部变量名称已变，这个操作其实是新增了一个变量。

* 继承和多态（同 Java）
* 获取对象信息
  * 判断对象类型，使用 `type()` 函数

        >>> type('abc')
        <class 'str'>
        >>> type(None)
        <type(None) 'NoneType'>
        >>> type(abs)
        <class 'builtin_function_or_method'>
    `type()` 函数返回的是什么类型呢？它返回对应的 Class 类型

        >>> type(123)==int
        True
        >>> type(abs)==types.BuiltinFunctionType
        True

  * 判断 class 的类型，可以使用 `isinstance()` 函数

        >>> isinstance(dog, Animal)
        True
        >>> isinstance('a', str)
        True

  * 要获得一个对象的所有属性和方法，可以使用 `dir()` 函数

        >>> dir('ABC')
        ['__add__', '__class__',..., '__subclasshook__', 'capitalize', 'casefold',..., 'zfill']
    类似`__xxx__`的属性和方法在Python中都是有特殊用途的，比如`__len__`方法返回长度。在 Python 中，如果你调用 `len()` 函数试图获取一个对象的长度，实际上，在 `len()` 函数内部，它自动去调用该对象的`__len__()` 方法。我们可以自己写`__len__()` 方法：

        >>> class MyDog(object):
        ...     def __len__(self):
        ...         return 100
        ...
        >>> dog = MyDog()
        >>> len(dog)
        100
    仅仅把属性和方法列出来是不够的，配合 `getattr()`、`setattr()` 以及 `hasattr()`，我们可以直接操作一个对象的状态：

        >>> hasattr(obj, 'y') # 有属性'y'吗？
        False
        >>> setattr(obj, 'y', 19) # 设置一个属性'y'
        >>> hasattr(obj, 'y') # 有属性'y'吗？
        True
        >>> getattr(obj, 'y', 404) # 获取属性'y',如果不存在，返回默认值 404
        19
        >>> obj.y # 获取属性'y'
        19
    也可以获得对象的方法：

        >>> hasattr(obj, 'power') # 有属性'power'吗？
        True
        >>> getattr(obj, 'power') # 获取属性'power'
        <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
        >>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
        >>> fn  # fn指向obj.power
        <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
        >>> fn() # 调用fn()与调用obj.power()是一样的
        81

* 实例属性和类属性

  给实例绑定属性的方法是通过实例变量，或者通过 self 变量：

      class Student(object):
          def __init__(self, name):
              self.name = name

      s = Student('Bob')
      s.score = 90

  直接在 class 中定义的属性是类属性，归 Student 类所有：

      class Student(object):
          name = 'Student'
  相同名称的实例属性将屏蔽掉类属性

## 面向对象高级编程
* 使用`__slots__`限制实例可绑定的属性

  正常情况下，当我们定义了一个 class，创建了一个 class 的实例后，我们可以给该实例绑定任何属性和方法。但是，给一个实例绑定的方法，对另一个实例是不起作用的。为了给所有实例都绑定方法，可以给 class 绑定方法：

      >>> def set_score(self, score):
      ...     self.score = score
      ...
      >>> Student.set_score = set_score
  Python 允许在定义 class 的时候，定义一个特殊的`__slots__`变量，来限制该class实例能添加的属性：

      class Student(object):
          __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称（包括 class 中定义的属性）
  但要注意，`__slots__`定义的属性仅对当前类实例起作用，对继承的子类是不起作用的。
* 使用 @property 对属性增加校验

      class Student(object):

          @property
          def score(self):
              return self._score

          @score.setter
          def score(self, value):
              if not isinstance(value, int):
                  raise ValueError('score must be an integer!')
              if value < 0 or value > 100:
                  raise ValueError('score must between 0 ~ 100!')
              self._score = value
  把一个 getter 方法变成属性，只需要加上 @property 就可以了，此时， @property 本身又创建了另一个装饰器 @score.setter，负责把一个 setter 方法变成属性赋值。**注意变量前要加 `_`**。

  还可以定义只读属性，只定义 getter 方法，不定义 setter 方法就是一个只读属性。

* 多重继承——Python一个子类可以继承多个父类，优先级从左往右。格式是：

      class son (father1,father2,father3):
      pass
* 定制类
  * `__str__`

        class Student(object):
            def __init__(self, name):
                self.name = name

        >>> print(Student('Michael'))
        <__main__.Student object at 0x109afb190>
    打印出的不好看，使用`__str__`

        class Student(object):
            def __init__(self, name):
                self.name = name
            def __str__(self):
                return 'Student object (name: %s)' % self.name

        >>> print(Student('Michael'))
        Student object (name: Michael)
    然而，直接敲变量还是不好看：

        >>> Student('Michael')
        <__main__.Student object at 0x109afb310>
    因为直接显示变量调用的不是`__str__()`，而是`__repr__()`，两者的区别是`__str__()` 返回用户看到的字符串，而`__repr__()` 返回程序开发者看到的字符串，解决办法是再定义一个`__repr__()`。有个偷懒的写法：

        class Student(object):
            def __init__(self, name):
                self.name = name
            def __str__(self):
                return 'Student object (name=%s)' % self.name
            __repr__ = __str__

  * `__iter__` 和`__next__`

    如果一个类想被用于 `for ... in` 循环，类似 list 或 tuple 那样，就必须实现一个`__iter__()` 方法，该方法返回一个迭代对象，然后，Python 的 for 循环就会不断调用该迭代对象的`__next__()` 方法拿到循环的下一个值，直到遇到 StopIteration 错误时退出循环。

        class Fib(object):
          def __init__(self):
              self.a, self.b = 0, 1 # 初始化两个计数器a，b

          def __iter__(self):
              return self # 实例本身就是迭代对象，故返回自己

          def __next__(self):
              self.a, self.b = self.b, self.a + self.b # 计算下一个值
              if self.a > 100000: # 退出循环的条件
                  raise StopIteration()
              return self.a # 返回下一个值

  * `__getitem__`

    Fib 实例虽然能作用于 for 循环，看起来和 list 有点像，但是还不能像list那样按照下标取出元素，这时候就需要实现`__getitem__()` 方法了：

        class Fib(object):
            def __getitem__(self, n):
                a, b = 1, 1
                for x in range(n):
                    a, b = b, a + b
                return a

        >>> f = Fib()
        >>> f[10]
        89
    但是这样切片会报错，要正确实现一个`__getitem__()` 还是有很多工作要做的。

    如果把对象看成 dict，`__getitem__()` 的参数也可能是一个可以作 key 的 object，例如 str。与之对应的是`__setitem__()` 方法，把对象视作 list 或 dict来对集合赋值。最后，还有一个`__delitem__()` 方法，用于删除某个元素。
  * `__getattr__`

    正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。要避免这个错误，Python 有一个机制，那就是写一个`__getattr__()` 方法，动态返回一个属性（函数也可以）。

        class Student(object):

            def __init__(self):
                self.name = 'Michael'

            def __getattr__(self, attr):
                if attr=='score':
                    return 99
                if attr=='age':
                    return lambda: 25
              
        >>> s.score
        99
        >>> s.age()
        25
    注意，只有在没有找到属性的情况下，才调用`__getattr__`，已有的属性不会在`__getattr__`中查找。

    此外，注意到任意调用如 s.abc 都会返回 None，这是因为我们定义的`__getattr__`默认返回就是 None。要让 class 只响应特定的几个属性，我们就要按照约定，抛出 AttributeError 的错误：

        class Student(object):

            def __getattr__(self, attr):
                if attr=='age':
                    return lambda: 25
                raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
  * `__call__`

    一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用 `instance.method()` 来调用。任何类，只需要定义一个`__call__()` 方法，就可以直接对实例进行调用。

        class Student(object):
            def __init__(self, name):
                self.name = name

            def __call__(self):
                print('My name is %s.' % self.name)

        >>> s = Student('Michael')
        >>> s() # self参数不要传入
        My name is Michael.
    `__call__()` 还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。我们判断一个对象是否能被调用，使用 `callable`：

        >>> callable(Student())
        True
* 枚举类（Enum）

      from enum import Enum
      Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
  这样我们就获得了 Month 类型的枚举类，可以直接使用 Month.Jan 来引用一个常量，或者枚举它的所有成员：

      for name, member in Month.__members__.items():
          print(name, '=>', member, ',', member.value)

      Jan => Month.Jan , 1 ……
  value 属性则是自动赋给成员的 int 常量，默认从 1 开始计数。

      from enum import Enum, unique

      @unique
      class Weekday(Enum):
          Sun = 0 # Sun的value被设定为0
          Mon = 1
          Tue = 2
          Wed = 3
          Thu = 4
          Fri = 5
          Sat = 6
  @unique装饰器可以帮助我们检查保证没有重复值。

      >>> day1 = Weekday.Mon
      >>> print(day1)
      Weekday.Mon
      >>> print(Weekday.Tue)
      Weekday.Tue
      >>> print(Weekday['Tue'])
      Weekday.Tue
      >>> print(Weekday.Tue.value)
      2
      >>> print(day1 == Weekday.Mon)
      True
      >>> print(Weekday(1))
      Weekday.Mon
* 使用元类（_略复杂，后期再补_）
  * `type()`

    动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

        >>> from hello import Hello
        >>> h = Hello()
        >>> h.hello()
        Hello, world.
        >>> print(type(Hello))
        <class 'type'>
        >>> print(type(h))
        <class 'hello.Hello'>
    `type()` 函数可以查看一个类型或变量的类型，Hello 是一个 class，它的类型就是 type，而 h 是一个实例，它的类型就是 class Hello。我们说 class 的定义是运行时动态创建的，而创建 class 的方法就是使用 `type()` 函数。

    `type()` 函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过 `type()` 函数创建出 Hello 类，而无需通过 `class Hello(object)...` 的定义：

        >>> def fn(self, name='world'): # 先定义函数
        ...     print('Hello, %s.' % name)
        ...
        >>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
        >>> h = Hello()
        >>> h.hello()
        Hello, world.
        >>> print(type(Hello))
        <class 'type'>
        >>> print(type(h))
        <class '__main__.Hello'>
    要创建一个class对象，type()函数依次传入3个参数：
    1. class的名称；
    2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
    1. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

  * metaclass

    除了使用 type( ) 动态创建类以外，要控制类的创建行为，还可以使用 metaclass。当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。但是如果我们想创建出类呢？那就必须根据 metaclass 创建出类，所以：先定义 metaclass，然后创建类。

    连接起来就是：先定义 metaclass，就可以创建类，最后创建实例。换句话说，你可以把类看成是 metaclass 创建出来的“实例”。

    定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：

        # metaclass是类的模板，所以必须从`type`类型派生：
        class ListMetaclass(type):
            def __new__(cls, name, bases, attrs):
                attrs['add'] = lambda self, value: self.append(value)
                return type.__new__(cls, name, bases, attrs)
    有了 ListMetaclass，我们在定义类的时候还要指示使用 ListMetaclass 来定制类，传入关键字参数 metaclass：

        class MyList(list, metaclass=ListMetaclass):
            pass
    当我们传入关键字参数 metaclass 时，魔术就生效了，它指示 Python 解释器在创建 MyList 时，要通过 `ListMetaclass.__new__()` 来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。`__new__()`方法接收到的参数依次是：
    * 当前准备创建的类的对象；
    * 类的名字；
    * 类继承的父类集合；
    * 类的方法集合。

          >>> L = MyList()
          >>> L.add(1)
          >> L
          [1]

          >>> L2 = list()
          >>> L2.add(1)
          报错

## 错误、调试和测试

* 错误处理

  当我们认为某些代码可能会出错时，就可以用 try 来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即 except 语句块（可以在 except 语句块后面加一个 else，当没有错误发生时，会自动执行 else语句），执行完 except 后，如果有 finally 语句块，则执行 finally 语句块，至此，执行完毕。如果没有错误发生，except 语句块不会被执行，但是 finally 仍会被执行（可以没有 finally 语句）。

      try:
          print('try...')
          r = 10 / int('2')
          print('result:', r)
      except ValueError as e:
          print('ValueError:', e)
      except ZeroDivisionError as e:
          print('ZeroDivisionError:', e)
      else:
          print('no error!')
      finally:
          print('finally...')
      print('END')
  Python 的错误其实也是 class，所有的错误类型都继承自 BaseException，所以在使用 except 时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。[常见的错误类型和继承关系看这里](https://docs.python.org/3/library/exceptions.html#exception-hierarchy)

  如果不捕获错误，自然可以让 Python 解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。Python 内置的 logging 模块可以非常容易地记录错误信息：

      import logging

      def f():
          try:
              ……
          except Exception as e:
              logging.exception(e)

  Python 的内置函数会抛出很多类型的错误，我们自己编写的函数也可以用 raise 抛出错误。raise 语句如果不带参数，就会把当前错误原样抛出。此外，在 except 中 raise一个 Error，还可以把一种类型的错误转化成另一种类型：

      try:
          10 / 0
      except ZeroDivisionError:
          raise ValueError('input error!')
* 调试
  * 通过使用 `print()`，用 print() 最大的坏处是将来还得删掉它
  * 断言 `assert`，如果断言失败，assert 语句本身就会抛出 AssertionError。程序中如果到处充斥着 assert，和 print() 相比也好不到哪去。

        def foo(s):
            n = int(s)
            assert n != 0, 'n is zero!'
            return 10 / n

        >>> foo('0')
    启动 Python 解释器时可以用 -O 参数来关闭 assert

        $ python -O err.py
  * logging，和 assert 比，logging 不会抛出错误，而且可以输出到文件。

        import logging
        logging.basicConfig(level=logging.INFO)

        s = '0'
        n = int(s)
        logging.info('n = %d' % n)
        print(10 / n)

    logging 允许你指定记录信息的级别，有debug，info，warning，error等几个级别；另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如 console 和文件。
  * pdb 单步运行

        $ python -m pdb err.py
    以参数`-m pdb` 启动后，pdb 定位到下一步要执行的代码。输入命令 `l` 来查看代码，输入命令 `n` 可以单步执行代码，任何时候都可以输入命令 `p 变量名` 来查看变量，输入命令 `q` 结束调试，退出程序。
    * `pdb.set_trace()`设置断点：

          import pdb

          s = '0'
          n = int(s)
          pdb.set_trace() # 运行到这里会自动暂停
          print(10 / n)
      不使用 pdb 正常运行代码，程序会自动在 `pdb.set_trace()` 暂停并进入 pdb 调试环境，可以用命令 p 查看变量，或者用命令 c 继续运行。
  * 最爽的办法还是 IDE ，但是最后你会发现，logging才是终极武器。
* 单元测试
  * 编写
    
    编写单元测试时，我们需要编写一个测试类，从 `unittest.TestCase` 继承，以 `test` 开头的方法就是测试方法，不以 `test` 开头的方法不被认为是测试方法，测试的时候不会被执行。

        import unittest

        class TestDict(unittest.TestCase):

            def test_init(self):
                d = Dict(a=1, b='test')
                self.assertEqual(d.a, 1)
                ……
    最常用的断言就是 `assertEqual()`、`assertTrue()`:

        self.assertEqual(abs(-1), 1) # 断言函数返回的结果与 1 相等
        self.assertTrue(isinstance(1, int))
    另一种重要的断言就是期待抛出指定类型的 Error，比如通过 `d['empty']` 访问不存在的 key 时，断言会抛出 `KeyError`：

        with self.assertRaises(KeyError):
            value = d['empty']
  * 运行

    最简单的运行方式是在最后加上两行代码：

        if __name__ == '__main__':
            unittest.main()
    这样就可以当做正常的 python 脚本运行。如：

        python mydict_test.py

    另一种方法是在命令行通过参数-m unittest直接运行单元测试：

        $ python -m unittest mydict_test
        .....
        ----------------------------------------------------------------------
        Ran 5 tests in 0.000s

        OK
    这是推荐的做法，因为这样可以一次批量运行很多单元测试，并且，有很多工具可以自动来运行这些单元测试。
  * setUp 与 tearDown

    可以在单元测试中编写两个特殊的 `setUp()` 和 `tearDown()` 方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
* 文档测试

  Python 内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。doctest 严格按照 Python 交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用...表示中间一大段烦人的输出。

      def fact(n):
        '''
        Calculate 1*2*...*n

        >>> fact(1)
        1
        >>> fact(10)
        3628800
        >>> fact(-1)
        Traceback (most recent call last):
        ...
        ValueError
        '''
        if n < 1:
            raise ValueError()
        if n == 1:
            return 1
        return n * fact(n - 1)

      if __name__ == '__main__':
        import doctest
        doctest.testmod()

## IO 编程
* 文件读写
  * 读文件

    要以读文件的模式打开一个文件对象，使用Python内置的 [`open()`](https://docs.python.org/3/library/functions.html#open) 函数，传入文件名和标示符:

        >>> f = open('/Users/michael/test.txt', 'r')
    要读取二进制文件，比如图片、视频等等，用 `'rb'` 模式打开文件即可；要读取非 UTF-8 编码的文本文件，需要传入 `encoding` 参数；遇到有些编码不规范的文件，你可能会遇到 `UnicodeDecodeError`，`open()` 函数还接收一个 `errors` 参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

        >>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
    如果文件打开成功，接下来，调用 `read()` 方法可以一次读取文件的全部内容，Python 把内容读到内存，用一个 str 对象表示：

        >>> f.read()
        'Hello, world!'
    最后一步是调用 `close()` 方法关闭文件。文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的：

        >>> f.close()
    由于文件读写时都有可能产生 `IOError`，一旦出错，后面的 `f.close()` 就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用 `try ... finally` 来实现：

        try:
            f = open('/path/to/file', 'r')
            print(f.read())
        finally:
            if f:
                f.close()
    但是每次都这么写实在太繁琐，所以，Python 引入了 `with` 语句来自动帮我们调用 `close()` 方法：

        with open('/path/to/file', 'r') as f:
            print(f.read())
    这和前面的 `try ... finally` 是一样的，但是代码更佳简洁，并且不必调用 `f.close()` 方法。

    如果文件很小，`read()` 一次性读取最方便；如果不能确定文件大小，反复调用 `read(size)` 比较保险；如果是配置文件，调用 `readlines()` 最方便：

        for line in f.readlines():
            print(line.strip()) # 把末尾的'\n'删掉
  * 写文件

    写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：

        >>> f = open('/Users/michael/test.txt', 'w')
        >>> f.write('Hello, world!')
        >>> f.close()
    当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用 `close()` 方法时，操作系统才保证把没有写入的数据全部写入磁盘。

    还是用with语句来得保险：

        with open('/Users/michael/test.txt', 'w') as f:
            f.write('Hello, world!')
    要写入特定编码的文本文件，请给 `open()` 函数传入 `encoding` 参数，将字符串自动转换成指定编码。
* [StringIO 和 BytesIO](https://docs.python.org/3/library/io.html)
  * StringIO

        >>> from io import StringIO
        >>> f = StringIO()
        >>> f.write('hello')
        5
        >>> f.write('world!')
        6
        >>> print(f.getvalue())
        helloworld!

        >>> f = StringIO('Hello!\nGoodbye!')
        >>> while True:
        ...     s = f.readline()
        ...     if s == '':
        ...         break
        ...     print(s.strip())
        ...
        Hello!
        Goodbye!
  * BytesIO

        >>> from io import BytesIO
        >>> f = BytesIO()
        >>> f.write('中文'.encode('utf-8'))
        6
        >>> print(f.getvalue())
        b'\xe4\xb8\xad\xe6\x96\x87'

        >>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
        >>> f.read()
        b'\xe4\xb8\xad\xe6\x96\x87'
* 操作文件和目录

      import os
      # 查看当前目录的绝对路径:
      >>> os.path.abspath('.')
      '/Users/michael'
      # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
      >>> os.path.join('/Users/michael', 'testdir')
      '/Users/michael/testdir'
      # 然后创建一个目录:
      >>> os.mkdir('/Users/michael/testdir')
      # 删掉一个目录:
      >>> os.rmdir('/Users/michael/testdir')
      # 拆分目录
      >>> os.path.split('/Users/michael/testdir/file.txt')
      ('/Users/michael/testdir', 'file.txt')
      # 拆分文件拓展名
      >>> os.path.splitext('/path/to/file.txt')
      ('/path/to/file', '.txt')
      # 对文件重命名:
      >>> os.rename('test.txt', 'test.py')
      # 删掉文件:
      >>> os.remove('test.py')

  这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

  列出当前目录下的所有目录，只需要一行代码：

      >>> [x for x in os.listdir('.') if os.path.isdir(x)]
      ['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]
  要列出所有的 .py 文件，也只需一行代码：

      >>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
      ['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']
* 序列化：
  * 我们把变量从内存中变成可存储或传输的过程称之为序列化，Python 提供了 `pickle` 模块来实现序列化

    `pickle.dumps()` 方法把任意对象序列化成一个 bytes，然后，就可以把这个 `bytes` 写入文件。或者用另一个方法 `pickle.dump()` 直接把对象序列化后写入一个 file-like Object：

        >>> import pickle
        >>> d = dict(name='Bob', age=20, score=88)
        >>> pickle.dumps(d)
        b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'
        >>> f = open('dump.txt', 'wb')
        >>> pickle.dump(d, f)
        >>> f.close()
    当我们要把对象从磁盘读到内存时，可以先把内容读到一个 `bytes`，然后用 `pickle.loads()` 方法反序列化出对象，也可以直接用 `pickle.load()` 方法从一个 file-like Object 中直接反序列化出对象。我们打开另一个 Python 命令行来反序列化刚才保存的对象：

        >>> f = open('dump.txt', 'rb')
        >>> d = pickle.load(f)
        >>> f.close()
        >>> d
        {'age': 20, 'score': 88, 'name': 'Bob'}
  * JSON

        >>> import json
        >>> d = dict(name='Bob', age=20, score=88)
        >>> json.dumps(d)
        '{"age": 20, "score": 88, "name": "Bob"}'
    `dumps()` 方法返回一个 str，内容就是标准的 JSON。类似的，`dump()` 方法可以直接把 JSON 写入一个 file-like Object。

    要把 JSON 反序列化为 Python 对象，用 `loads()` 或者对应的 `load()` 方法，前者把 JSON 的字符串反序列化，后者从 file-like Object 中读取字符串并反序列化：

        >>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
        >>> json.loads(json_str)
        {'age': 20, 'score': 88, 'name': 'Bob'}
  * [JSON 进阶](https://docs.python.org/3/library/json.html#json.dumps)

        import json

        class Student(object):
            def __init__(self, name, age, score):
                self.name = name
                self.age = age
                self.score = score

        s = Student('Bob', 20, 88)
        print(json.dumps(s))
        运行代码，毫不留情地得到一个TypeError：

        Traceback (most recent call last):
          ...
        TypeError: <__main__.Student object at 0x10603cc50> is not JSON serializable
    前面的代码之所以无法把 `Student` 类实例序列化为 JSON，是因为默认情况下，`dumps()` 方法不知道如何将 `Student` 实例变为一个 JSON的 `{}` 对象。可选参数 `default` 就是把任意一个对象变成一个可序列为 JSON 的对象，我们只需要为 `Student` 专门写一个转换函数，再把函数传进去即可：(**注意：转换函数不属于类而是和类同级，要顶格**)

        def student2dict(std):
            return {
                'name': std.name,
                'age': std.age,
                'score': std.score
            }
    这样，`Student` 实例首先被 `student2dict()` 函数转换成 `dict`，然后再被顺利序列化为 JSON：

        >>> print(json.dumps(s, default=student2dict))
        {"age": 20, "name": "Bob", "score": 88}
    我们可以偷个懒，把任意class的实例变为dict：

        print(json.dumps(s, default=lambda obj: obj.__dict__))
    因为通常 class 的实例都有一个`__dict__`属性，它就是一个 dict，用来存储实例变量。也有少数例外，比如定义了`__slots__`的 class。

    同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：

        def dict2student(d):
            return Student(d['name'], d['age'], d['score'])

        >>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
        >>> print(json.loads(json_str, object_hook=dict2student))
        <__main__.Student object at 0x10cd3c190>

## 进程和线程
* 多进程