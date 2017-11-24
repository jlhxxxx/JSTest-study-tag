


## 输入和输出
* `print()` 可接受多个字符串，用逗号“,”隔开,输出时逗号变成空格

        >>> print('100 + 200 =', 100 + 200)
        100 + 200 = 300
* `input()`括号内可加提示

        name = input('please enter your name: ')

## 基础
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
    
* list 有序集合，使用 `[]`
  * list 元素数据类型可以不同，也可以是另一个 list 

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

## 函数
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

## 高级特性
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
    