doctest ：`python -m doctest -v frenchdeck.doctest`

### 1.2.3

* 默认情况下，我们自己定义的类的实例总被认为是真的，除非这个类对`__bool__ `或者` __len__ `函数有自己的实现。`bool(x)` 的背后是调用`x.__bool__()` 的结果；如果不存在` __bool__ `方法，那么 `bool(x) `会尝试调用` x.__len__()`。若返回 `0`，则` bool` 会返回 `False`；否则返回`True`。

### 2.2.1 列表推导

* 通常的原则是，只用列表推导来创建新的列表，并且尽量保持简短。

        :::python
        >>> symbols = '$¢£¥€¤'
        >>> codes = [ord(symbol) for symbol in symbols]
        >>> codes
        [36, 162, 163, 165, 8364, 164]

### 2.3.2 元组拆包

    :::python
    >>> b, a = a, b
    
    >>> a, *b, c = range(5)
    >>> b
    [1, 2, 3]
    
    >>> t = (20, 8)
    >>> divmod(*t)
    (2, 4)
    
    >>> _, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
    >>> filename
    'idrsa.pub'
    
    >>> for a, *b in [(1, 2, 3), (4, 5, 6, 7)]:
    ...     print(b)
    ...
    [2, 3]
    [5, 6, 7]
### 2.3.4 具名元组

    :::python
    >>> from collections import namedtuple
    >>> City = namedtuple('City', 'name country population coordinates') 
    >>> tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
    >>> tokyo
    City(name='Tokyo', country='JP', population=36.933, coordinates=(35.689722,
    139.691667))
    >>> tokyo.population
    36.933
    >>> tokyo[1]
    'JP'
    
    >>> City._fields ➊
    ('name', 'country', 'population', 'coordinates')
    >>> LatLong = namedtuple('LatLong', 'lat long')
    >>> delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
    >>> delhi = City._make(delhi_data) ➋
    >>> delhi._asdict() ➌
    OrderedDict([('name', 'Delhi NCR'), ('country', 'IN'), ('population',
    21.935), ('coordinates', LatLong(lat=28.613889, long=77.208889))])
    >>> for key, value in delhi._asdict().items():
    print(key + ':', value)
    name: Delhi NCR
    country: IN
    population: 21.935
    coordinates: LatLong(lat=28.613889, long=77.208889)

* ❶ `_fields` 属性是一个包含这个类所有字段名称的元组。
* ❷ 用 `_make()` 通过接受一个可迭代对象来生成这个类的一个实例，它的作用跟 `City(*delhi_data) `是一样的。

* ❸ `_asdict()` 把具名元组以 `collections.OrderedDict` 的形式返回，我们可以利用它来把元组里的信息友好地呈现出来。

### 2.4.2 对对象进行切片

    :::python
    >>> invoice = """
    ... 0.....6................................40........52...55........
    ... 1909  Pimoroni PiBrella                $17.50    3    $52.50
    ... 1489  6mm Tactile Switch x20           $4.95     2    $9.90
    ... 1510  Panavise Jr. - PV-201            $28.00    1    $28.00
    ... 1601  PiTFT Mini Kit 320x240           $34.95    1    $34.95
    ... """
    >>> SKU = slice(0, 6)
    >>> DESCRIPTION = slice(6, 40)
    >>> UNIT_PRICE = slice(40, 52)
    >>> QUANTITY = slice(52, 55)
    >>> ITEM_TOTAL = slice(55, None)
    >>> line_items = invoice.split('\n')[2:]
    >>> for item in line_items:
    ... print(item[UNIT_PRICE], item[DESCRIPTION])
    ...
    $17.50 Pimoroni PiBrella
    $4.95 6mm Tactile Switch x20
    $28.00 Panavise Jr. - PV-201
    $34.95 PiTFT Mini Kit 320x240

### 2.4.4 给切片赋值

    :::python
    >>> l = list(range(10))
    >>> l
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> l[2:5] = [20, 30]
    >>> l
    [0, 1, 20, 30, 5, 6, 7, 8, 9]
    >>> del l[5:7]
    >>> l
    [0, 1, 20, 30, 5, 8, 9]
    >>> l[3::2] = [11, 22]
    >>> l
    [0, 1, 20, 11, 5, 22, 9]
    >>> l[2:5] = 100
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    TypeError: can only assign an iterable
    >>> l[2:5] = [100]
    >>> l
    [0, 1, 100, 22, 9]

### 2.5 对序列使用`+`和`*`

    :::python
    >>> board = [['_'] * 3 for i in range(3)]
    >>> board
    [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    >>> board[1][2] = 'X'
    >>> board
    [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]
    
    >>> weird_board = [['_'] * 3] * 3   # 此为引用
    >>> weird_board
    [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    >>> weird_board[1][2] = 'O'
    >>> weird_board
    [['_', '_', 'O'], ['_', '_', 'O'], ['_', '_', 'O']]

### 2.7 `list.sort`方法和内置函数`sorted`

`list.sort` 方法会就地排序列表，也就是说不会把原列表复制一份。这也是这个方法的返回值是 `None` 的原因，提醒你本方法不会新建一个列表。与 `list.sort` 相反的是内置函数 `sorted`，它会新建一个列表作为返回值。

### 2.8.1 用`bisect`来搜索

`bisect(haystack, needle) `在 `haystack`（干草垛）里搜索`needle`（针）的位置，该位置满足的条件是，把 `needle` 插入这个位置之后，`haystack` 还能保持升序。也就是在说这个函数返回的位置前面的值，都小于或等于 `needle` 的值。其中 `haystack` 必须是一个有序的序列。你可以先用 `bisect(haystack, needle)` 查找位置 `index`，再用 `haystack.insert(index, needle) `来插入新值。

    :::python
    >>> def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    ... i = bisect.bisect(breakpoints, score)
    ... return grades[i]
    ...
    >>> [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
    ['F', 'A', 'C', 'C', 'B', 'A', 'A']

* `bisect` 函数其实是 `bisect_right `函数的别名，后者还有个姊妹函数叫 `bisect_left`。它们的区别在于，`bisect_left` 返回的插入位置是原序列中跟被插入元素相等的元素的位置，也就是新元素会被放置于它相等的元素的前面，而 `bisect_right` 返回的则是跟它相等的元素之后的位置。

### 2.8.2 用`bisect.insort`插入新元素

`insort(seq, item)` 把变量 `item` 插入到序列 `seq` 中，并能保持 `seq`的升序顺序。它也有个变体叫 `insort_left`，这个变体在背后用的是`bisect_left`。

### 2. 其他序列

如果我们需要一个只包含数字的列表，那么 array.array 比 list 更高效。

`numpy`和`scipy`

`collections.deque`

### 4.4.1 处理UnicodeEncodeError

    :::python
    >>> city = 'São Paulo'
    >>> city.encode('utf_8')
    b'S\xc3\xa3o Paulo'
    >>> city.encode('utf_16')
    b'\xff\xfeS\x00\xe3\x00o\x00 \x00P\x00a\x00u\x00l\x00o\x00'
    >>> city.encode('iso8859_1')
    b'S\xe3o Paulo'
    >>> city.encode('cp437')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/.../lib/python3.4/encodings/cp437.py", line 12, in encode
        return codecs.charmap_encode(input,errors,encoding_map)
    UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in
    position 1: character maps to <undefined>
    >>> city.encode('cp437', errors='ignore')
    b'So Paulo'
    >>> city.encode('cp437', errors='replace')
    b'S?o Paulo'
    >>> city.encode('cp437', errors='xmlcharrefreplace')
    b'São Paulo'

### 4.4.2 处理UnicodeDecodeError

    :::python
    >>> octets = b'Montr\xe9al' 
    >>> octets.decode('cp1252') 
    'Montréal'
    >>> octets.decode('iso8859_7') 
    'Montrιal'
    >>> octets.decode('koi8_r') 
    'MontrИal'
    >>> octets.decode('utf_8') 
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5:
    invalid continuation byte
    >>> octets.decode('utf_8', errors='replace') 
    'Montr􀓠al'

### 4.4.3 使用预期之外的编码加载模块时抛出的SyntaxError

### 4.4.4 如何找出字节序列的编码

统一字符编码侦测包 [Chardet](https://pypi.org/project/chardet/)

### 4.4.5 处理文本文件

处理文本的最佳实践是“Unicode 三明治”。意思是，要尽早把输入（例如读取文件时）的字节序列解码成字符串。这种三明治中的“肉片”是程序的业务逻辑，在这里只能处理字符串对象。在其他处理过程中，一定不能编码或解码。对输出来说，则要尽量晚地把字符串编码成字节序列。

### 5.2 高阶函数

map 和 filter 与列表推导比较：

    :::python
    >>> list(map(fact, range(6))) 
    [1, 1, 2, 6, 24, 120]
    >>> [fact(n) for n in range(6)] 
    [1, 1, 2, 6, 24, 120]
    >>> list(map(factorial, filter(lambda n: n % 2, range(6)))) 
    [1, 6, 120]
    >>> [factorial(n) for n in range(6) if n % 2] 
    [1, 6, 120]

使用 reduce 和 sum 计算 0~99 之和：

    :::python
    >>> from functools import reduce 
    >>> from operator import add
    >>> reduce(add, range(100)) 
    4950
    >>> sum(range(100)) 
    4950

### 6.1.4 找出模块中的全部策略

    :::python
    # globals()：返回一个字典，表示当前的全局符号表。这个符号表始终针对当前模块（对函数或方法来说，是指定义它们的模块，而不是调用它们的模块）。
    
    promos = [globals()[name] for name in globals() 
                if name.endswith('_promo') 
                and name != 'best_promo']
                
    # inspect.getmembers 函数用于获取对象（这里是 promotions 模块）的属性，第二个参数是可选的判断条件（一个布尔值函数）。我们使用的是 inspect.isfunction，只获取模块中的函数。
    
    import inspect
    promos = [func for name, func in
                    inspect.getmembers(promotions, inspect.isfunction)]

### 7.2 Python何时执行装饰器

装饰器的一个关键特性是，它们在被装饰的函数定义之后立即运行。这通常是在导入时（即 Python 加载模块时）。而被装饰的函数只在明确调用时运行。

### 7.4 变量作用域规则

Python 不要求声明变量，但是假定在函数定义体中赋值的变量是局部变量。

如果在函数中赋值时想让解释器把某个变量当成全局变量，要使用 global 声明。

### 7.6 nonlocal声明

它的作用是把变量标记为自由变量，即使在函数中为变量赋予新值了，也会变成自由变量。

    :::python
    def make_averager():
        count = 0
        total = 0
    
        def averager(new_value):
            nonlocal count, total
            count += 1
            total += new_value
            return total / count
    
        return averager

### 7.8 标准库中的装饰器

### 7.8.1 使用functools.lru_cache做备忘

functools.lru_cache 是非常实用的装饰器，它实现了备忘（memoization）功能。这是一项优化技术，它把耗时的函数的结果保存起来，避免传入相同的参数时重复计算。——适合递归

    :::python
    import functools
    
    from clockdeco import clock
    
    @functools.lru_cache()
    @clock
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-2) + fibonacci(n-1)
    
    if __name__=='__main__':
        print(fibonacci(6))

lru_cache 可以使用两个可选的参数来配置。它的签名是：

`functools.lru_cache(maxsize=128, typed=False)`

* maxsize 参数指定存储多少个调用的结果。缓存满了之后，旧的结果会被扔掉，腾出空间。为了得到最佳性能，maxsize 应该设为 2 的幂。
* typed 参数如果设为 True，把不同参数类型得到的结果分开保存，即把通常认为相等的浮点数和整数参数（如 1 和 1.0）区分开。

顺便说一下，因为 lru_cache 使用字典存储结果，而且键根据调用时传入的定位参数和关键字参数创建，所以被 lru_cache 装饰的函数，它的所有参数都必须是可散列的。

> **可散列的**：如果一个对象是可散列的，那么在这个对象的生命周期中，它的散列值是不变的，而且这个对象需要实现` __hash__()` 方法。另外可散列对象还要有 `__eq__() `方法，这样才能跟其他键做比较。如果两个可散列对象是相等的，那么它们的散列值一定是一样的……

> 原子不可变数据类型（str、bytes 和数值类型）都是可散列类型，frozenset 也是可散列的，因为根据其定义，frozenset 里只能容纳可散列类型。元组的话，只有当一个元组包含的所有元素都是可散列类型的情况下，它才是可散列的。

### 7.8.2 单分派泛函数——functools.singledispatch 装饰器

    :::python
    from functools import singledispatch
    from collections import abc
    import numbers
    import html
    
    @singledispatch  ➊
    def htmlize(obj):
        content = html.escape(repr(obj))
        return '<pre>{}</pre>'.format(content)
    
    @htmlize.register(str)  ➋
    def _(text):            ➌
        content = html.escape(text).replace('\n', '<br>\n')
        return '<p>{0}</p>'.format(content)
    
    @htmlize.register(numbers.Integral)  ➍
    def _(n):
        return '<pre>{0} (0x{0:x})</pre>'.format(n)
    
    @htmlize.register(tuple) ➎
    @htmlize.register(abc.MutableSequence)
    def _(seq):
        inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
        return '<ul>\n<li>' + inner + '</li>\n</ul>'

❶ `@singledispatch` 标记处理 object 类型的基函数。

❷ 各个专门函数使用 `@«base_function».register(«type»)` 装饰。

❸ 专门函数的名称无关紧要；`_` 是个不错的选择，简单明了。

❹ 为每个需要特殊处理的类型注册一个函数。`numbers.Integral` 是 int 的虚拟超类。

❺ 可以叠放多个 register 装饰器，让同一个函数支持不同类型。

只要可能，注册的专门函数应该处理抽象基类（如 numbers.Integral 和 abc.MutableSequence），不要处理具体实现（如 int 和 list）。这样，代码支持的兼容类型更广泛。

### 7.9 叠放装饰器

    ::::python
    @d1
    @d2
    def f():
        print('f')
        
    等同于    
    
    def f():
        print('f')
    
    f = d1(d2(f))

### 7.10 参数化装饰器

为了接受参数，装饰器必须作为函数调用（即使用`()`）。

### 8.2.1 在==和is之间选择

== 运算符比较两个对象的值（对象中保存的数据），而 is 比较对象的标识。

### 8.2.2 元组的相对不可变性

元组与多数 Python 集合（列表、字典、集，等等）一样，保存的是对象的引用。如果引用的元素是可变的，即便元组本身不可变，元素依然可变。

### 8.3 默认做浅复制（即复制了最外层容器，副本中的元素是源容器中元素的引用）

    :::python
    >>> l1 = [3, [66, 55, 44], (7, 8, 9)]
    >>> l2 = list(l1)
    >>> l1.append(100)
    >>> l1[1].remove(55)
    >>> print('l1:', l1)
    l1: [3, [66, 44], (7, 8, 9), 100]
    >>> print('l2:', l2)
    l2: [3, [66, 44], (7, 8, 9)]
    >>> l2[1] += [33, 22]
    >>> l2[2] += (10, 11)
    >>> print('l1:', l1)
    l1: [3, [66, 44, 33, 22], (7, 8, 9), 100]
    >>> print('l2:', l2)
    l2: [3, [66, 44, 33, 22], (7, 8, 9, 10, 11)]

deepcopy 和 copy

    :::python
    >>> a = [10, 20]
    >>> b = [a, 30]
    >>> a.append(b)
    >>> a
    [10, 20, [[...], 30]]
    >>> from copy import deepcopy
    >>> c = deepcopy(a)
    >>> c
    [10, 20, [[...], 30]]

### 8.4 函数的参数作为引用时

Python 唯一支持的参数传递模式是共享传参（call by sharing）。共享传参指函数的各个形式参数获得实参中各个引用的副本。也就是说，函数内部的形参是实参的别名。

    :::python
    >>> def f(a, b):
    ...     a += b
    ...     return a
    ...
    >>> x = 1
    >>> y = 2
    >>> f(x, y)
    3
    >>> x, y 
    (1, 2)
    >>> a = [1, 2]
    >>> b = [3, 4]
    >>> f(a, b)
    [1, 2, 3, 4]
    >>> a, b 
    ([1, 2, 3, 4], [3, 4])
    >>> t = (10, 20)
    >>> u = (30, 40)
    >>> f(t, u)
    (10, 20, 30, 40)
    >>> t, u
    ((10, 20), (30, 40))

### 8.4.1 不要使用可变类型作为参数的默认值

### 8.5 del和垃圾回收

del 语句删除名称，而不是对象。del 命令可能会导致对象被当作垃圾回收，但是仅当删除的变量保存的是对象的最后一个引用，或者无法得到对象时。重新绑定也可能会导致对象的引用数量归零，导致对象被销毁。

### 8.6 弱引用

弱引用不会增加对象的引用数量。引用的目标对象称为所指对象（referent）。因此我们说，弱引用不会妨碍所指对象被当作垃圾回收。

不是每个 Python 对象都可以作为弱引用的目标（或称所指对象）。基本的 list 和 dict 实例不能作为所指对象，但是它们的子类可以轻松地解决这个问题。set 实例可以作为所指对象，用户定义的类型也没问题。但是，int 和 tuple 实例不能作为弱引用的目标，甚至它们的子类也不行。

### 8.7 Python对不可变类型施加的把戏

对元组 `t` 来说，`t[:]` 不创建副本，而是返回同一个对象的引用。此外，`tuple(t) `获得的也是同一个元组的引用。

    :::python
    >>> t1 = (1, 2, 3)
    >>> t3 = (1, 2, 3)
    >>> t3 is t1
    False
    >>> s1 = 'ABC'
    >>> s2 = 'ABC'
    >>> s2 is s1
    True

> **吐槽**：Java 的 == 运算符比较的是对象（不是基本类型）的引用，而不是对象的值。就算是比较字符串这样的基本操作，Java 也强制你使用 .equals 方法。尽管如此，.equals 方法还有另一个问题：如果编写 a.equals(b)，而 a 是 null，会得到一个空指针异常。

> Python 采取了正确的方式。== 运算符比较对象的值，而 is 比较引用。此外，Python 支持重载运算符，== 能正确处理标准库中的所有对象，包括 None。

### 9.1 对象表示形式

每门面向对象的语言至少都有一种获取对象的字符串表示形式的标准方式。Python 提供了两种方式。

`repr()`

　　以便于开发者理解的方式返回对象的字符串表示形式。

`str()`

　　以便于用户理解的方式返回对象的字符串表示形式。

* `__repr__ `和 `__str__ `的区别在于，后者是在 `str() `函数被使用，或是在用 `print` 函数打印一个对象的时候才被调用的，并且它返回的字符串对终端用户更友好。如果你只想实现这两个特殊方法中的一个，`__repr__` 是更好的选择，因为如果一个对象没有` __str__ `函数，而 Python 又需要调用它的时候，解释器会用` __repr__ `作为替代。(1.2.3)

### 9.4　classmethod与staticmethod

    :::python
    >>> class Demo:
    ...     @classmethod
    ...     def klassmeth(*args):
    ...         return args
    ...     @staticmethod
    ...     def statmeth(*args):
    ...         return args
    ...
    >>> Demo.klassmeth()
    (<class '__main__.Demo'>,)
    >>> Demo.klassmeth('spam')
    (<class '__main__.Demo'>, 'spam')
    >>> Demo.statmeth() 
    ()
    >>> Demo.statmeth('spam')
    ('spam',)

不管怎样调用 Demo.klassmeth，它的第一个参数始终是 Demo 类。Demo.statmeth 的行为与普通的函数相似。

**扩展阅读**：

* [Python类方法、静态方法与实例方法](https://www.cnblogs.com/blackmatrix/p/5606364.html)
* [The definitive guide on how to use static, class or abstract methods in Python](https://julien.danjou.info/guide-python-static-class-abstract-methods/)

### 9.8　使用 __slots__ 类属性节省空间

定义` __slots__ `的方式是，创建一个类属性，使用 `__slots__` 这个名字，并把它的值设为一个字符串构成的可迭代对象，其中各个元素表示各个实例属性。我喜欢使用元组，因为这样定义的 `__slots__` 中所含的信息不会变化。

    :::python
    class Vector2d:
        __slots__ = ('__x', '__y')
    
        typecode = 'd'
        ...

如果使用得当，`__slots__ `能显著节省内存，不过有几点要注意。

* 每个子类都要定义 `__slots__` 属性，因为解释器会忽略继承的` __slots__ `属性。
* 实例只能拥有` __slots__ `中列出的属性，除非把 '`__dict__`' 加入` __slots__ `中（这样做就失去了节省内存的功效）。
* 如果不把 '`__weakref__`' 加入` __slots__`，实例就不能作为弱引用的目标。

### 10.6

使用 `zip` 函数能轻松地并行迭代两个或更多可迭代对象，它返回的元组可以拆包成变量，分别对应各个并行输入中的一个元素。

> zip 有个奇怪的特性：当一个可迭代对象耗尽后，它不发出警告就停止。

    :::python
    >>> zip(range(3), 'ABC')
    <zip object at 0x10063ae48>
    >>> list(zip(range(3), 'ABC'))
    [(0, 'A'), (1, 'B'), (2, 'C')]
    >>> list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3]))
    [(0, 'A', 0.0), (1, 'B', 1.1), (2, 'C', 2.2)]
    >>> from itertools import zip_longest
    >>> list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue=-1))
    [(0, 'A', 0.0), (1, 'B', 1.1), (2, 'C', 2.2), (-1, -1, 3.3)]

`enumerate`

    :::python
    >>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    >>> list(enumerate(seasons))
    [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
    >>> list(enumerate(seasons, start=1))
    [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

### 11.6.1 collections.abc模块中的抽象基类

![collections.abc.png](https://github.com/jlhxxxx/imgur/blob/master/others/collections.abc.png?raw=true)

* Iterable、Container 和 Sized

  各个集合应该继承这三个抽象基类，或者至少实现兼容的协议。Iterable 通过 __iter__ 方法支持迭代，Container 通过 __contains__ 方法支持 in 运算符，Sized 通过 __len__ 方法支持 len() 函数。

* Sequence、Mapping 和 Set

  这三个是主要的不可变集合类型，而且各自都有可变的子类。

* MappingView

  在 Python 3 中，映射方法 .items()、.keys() 和 .values() 返回的对象分别是 ItemsView、KeysView 和 ValuesView 的实例。前两个类还从 Set 类继承了丰富的接口，包含 3.8.3 节所述的全部运算符。

* Callable 和 Hashable

  这两个抽象基类与集合没有太大的关系，只不过因为 collections.abc 是标准库中定义抽象基类的第一个模块，而它们又太重要了，因此才把它们放到 collections.abc 模块中。我从未见过 Callable 或 Hashable 的子类。这两个抽象基类的主要作用是为内置函数 isinstance 提供支持，以一种安全的方式判断对象能不能调用或散列。

  若想检查是否能调用，可以使用内置的 callable() 函数；但是没有类似的 hashable() 函数，因此测试对象是否可散列，最好使用 isinstance(my_obj, Hashable)。

* Iterator

　　注意它是 Iterable 的子类。

### 11.6.2 抽象基类的数字塔

* Number
* Complex
* Real
* Rational
* Integral

其中 Number 是位于最顶端的超类，随后是 Complex 子类，依次往下，最底端是 Integral 类。如果想检查一个数是不是整数，可以使用 isinstance(x, numbers.Integral)，这样代码就能接受 int、bool（int 的子类），或者外部库使用 numbers 抽象基类注册的其他类型。如果一个值可能是浮点数类型，可以使用 isinstance(x, numbers.Real) 检查。这样代码就能接受 bool、int、float、fractions.Fraction，或者外部库（如 NumPy，它做了相应的注册）提供的非复数类型。

> [异常类的部分层次结构](https://docs.python.org/dev/library/exceptions.html#exception-hierarchy)

### 11.7.1 抽象基类句法详解

声明抽象类方法的推荐方式是：

    :::python
    class MyABC(abc.ABC):
        @classmethod
        @abc.abstractmethod
        def an_abstract_classmethod(cls, ...):
            pass

> 在函数上堆叠装饰器的顺序通常很重要，abstractmethod() 应该放在最里层。

### 12.1 子类化内置类型很麻烦

直接子类化内置类型（如 dict、list 或 str）容易出错，因为内置类型的方法通常会忽略用户覆盖的方法。不要子类化内置类型，用户自己定义的类应该继承 collections 模块中的类，例如 UserDict、UserList 和 UserString，这些类做了特殊设计，因此易于扩展。

    :::python
    >>> class DoppelDict(dict):
    ...     def __setitem__(self, key, value):
    ...         super().__setitem__(key, [value] * 2)
    ...
    >>> dd = DoppelDict(one=1) 
    >>> dd
    {'one': 1}
    >>> dd['two'] = 2
    >>> dd
    {'one': 1, 'two': [2, 2]}
    >>> dd.update(three=3)
    >>> dd
    {'three': 3, 'one': 1, 'two': [2, 2]}
    ************************************************************************************************
    >>> import collections
    >>> class DoppelDict2(collections.UserDict):
    ...     def __setitem__(self, key, value):
    ...         super().__setitem__(key, [value] * 2)
    ...
    >>> dd = DoppelDict2(one=1)
    >>> dd
    {'one': [1, 1]}
    >>> dd['two'] = 2
    >>> dd
    {'two': [2, 2], 'one': [1, 1]}
    >>> dd.update(three=3)
    >>> dd
    {'two': [2, 2], 'three': [3, 3], 'one': [1, 1]}

### 12.2 多重继承和方法解析顺序

    :::python
    # diamond.py
    
    class A:
        def ping(self):
            print('ping:', self)
    
    class B(A):
        def pong(self):
            print('pong:', self)
    
    class C(A):
        def pong(self):
            print('PONG:', self)
    
    class D(B, C):
    
        def ping(self):
            super().ping()
            print('post-ping:', self)
    
        def pingpong(self):
            self.ping()
            super().ping()
            self.pong()
            super().pong()
            C.pong(self)

调用：

    :::python
    >>> from diamond import *
    >>> d = D()
    >>> d.pong()  # ➊
    pong: <diamond.D object at 0x10066c278>
    >>> C.pong(d)  # ➋
    PONG: <diamond.D object at 0x10066c278>
    >>> d.pingpong()
    ping: <diamond.D object at 0x10066c278>
    post-ping: <diamond.D object at 0x10066c278>
    ping: <diamond.D object at 0x10066c278>
    pong: <diamond.D object at 0x10066c278>
    pong: <diamond.D object at 0x10066c278>
    PONG: <diamond.D object at 0x10bf235c0> 

❶ 直接调用 `d.pong()` 运行的是 B 类中的版本。Python 能区分 `d.pong()` 调用的是哪个方法，是因为 Python 会按照特定的顺序遍历继承图。这个顺序叫方法解析顺序（Method Resolution Order，MRO）。类都有一个名为` __mro__ `的属性，它的值是一个元组，按照方法解析顺序列出各个超类，从当前类一直向上，直到 object 类。

    :::python
    >>> D.__mro__
    (<class 'diamond.D'>, <class 'diamond.B'>, <class 'diamond.C'>,
    <class 'diamond.A'>, <class 'object'>)

❷ 超类中的方法都可以直接调用，此时要把实例作为显式参数传入。

### 12.4 处理多重继承

* 把接口继承和实现继承区分开

  使用多重继承时，一定要明确一开始为什么创建子类。主要原因可能有：

  * 继承接口，创建子类型，实现“是什么”关系
  * 继承实现，通过重用避免代码重复

  其实这两条经常同时出现，不过只要可能，一定要明确意图。通过继承重用代码是实现细节，通常可以换用组合和委托模式。而接口继承则是框架的支柱。

* 使用抽象基类显式表示接口

* 通过混入重用代码

  如果一个类的作用是为多个不相关的子类提供方法实现，从而实现重用，但不体现“是什么”关系，应该把那个类明确地定义为混入类（mixin class）。从概念上讲，混入不定义新类型，只是打包方法，便于重用。混入类绝对不能实例化，而且具体类不能只继承混入类。混入类应该提供某方面的特定行为，只实现少量关系非常紧密的方法。

* 在名称中明确指明混入

  因为在 Python 中没有把类声明为混入的正规方式，所以强烈推荐在名称中加入 ...Mixin 后缀。

* 抽象基类可以作为混入，反过来则不成立

  抽象基类可以实现具体方法，因此也可以作为混入使用。不过，抽象基类会定义类型，而混入做不到。此外，抽象基类可以作为其他类的唯一基类，而混入决不能作为唯一的超类，除非继承另一个更具体的混入——真实的代码很少这样做。

  抽象基类有个局限是混入没有的：抽象基类中实现的具体方法只能与抽象基类及其超类中的方法协作。这表明，抽象基类中的具体方法只是一种便利措施，因为这些方法所做的一切，用户调用抽象基类中的其他方法也能做到。

* 不要子类化多个具体类

  具体类可以没有，或最多只有一个具体超类。也就是说，具体类的超类中除了这一个具体超类之外，其余的都是抽象基类或混入。

* 为用户提供聚合类

  如果抽象基类或混入的组合对客户代码非常有用，那就提供一个类，使用易于理解的方式把它们结合起来。Grady Booch 把这种类称为聚合类（aggregate class）。

* “优先使用对象组合，而不是类继承”

### 14.2 可迭代的对象与迭代器的对比

**可迭代的对象**：使用 iter 内置函数可以获取迭代器的对象。如果对象实现了能返回迭代器的` __iter__ `方法，那么对象就是可迭代的。序列都可以迭代；实现了` __getitem__ `方法，而且其参数是从零开始的索引，这种对象也可以迭代。

**迭代器**是这样的对象：实现了无参数的` __next__ `方法，返回序列中的下一个元素；如果没有元素了，那么抛出 StopIteration 异常。Python 中的迭代器还实现了` __iter__ `方法，因此迭代器也可以迭代。

可迭代的对象一定不能是自身的迭代器。也就是说，可迭代的对象必须实现` __iter__ `方法，但不能实现 `__next__ `方法。

### 14.10 yield from

    :::python
    >>> def chain(*iterables):
    ...     for i in iterables:
    ...         yield from i
    ...
    >>> s = 'ABC'
    >>> t = tuple(range(3))
    >>> list(chain(s, t))
    ['A', 'B', 'C', 0, 1, 2]

### 15.1 if语句之外的else块

for/else、while/else 和 try/else

* 仅当 for 循环运行完毕时（即 for 循环没有被 break 语句中止）才运行 else 块
* 仅当 while 循环因为条件为假值而退出时（即 while 循环没有被 break 语句中止）才运行 else 块
* 仅当 try 块中没有异常抛出时才运行 else 块

### 15.2 上下文管理器和with块

```
:::python
>>> with open('mirror.py') as fp:
...     src = fp.read(60)
...
>>> len(src)
60
>>> fp
<_io.TextIOWrapper name='mirror.py' mode='r' encoding='UTF-8'>
>>> fp.closed, fp.encoding  
(True, 'UTF-8')
>>> fp.read(60)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

上下文管理器协议包含 __enter__ 和 __exit__ 两个方法。with 语句开始运行时，会在上下文管理器对象上调用 __enter__ 方法。with 语句运行结束后，会在上下文管理器对象上调用 __exit__ 方法，以此扮演 finally 子句的角色。举例：

```
:::python
>>> from mirror import LookingGlass
>>> with LookingGlass() as what: 
...      print('Alice, Kitty and Snowdrop') 
...      print(what)
...
pordwonS dna yttiK ,ecilA 
YKCOWREBBAJ
>>> what 
'JABBERWOCKY'
>>> print('Back to normal.') 
Back to normal.
```

mirror.py：

```
:::python
class LookingGlass:

    def __enter__(self):  
        import sys
        self.original_write = sys.stdout.write ➊ 
        sys.stdout.write = self.reverse_write ❷  
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True
```

➊ 把原来的 sys.stdout.write 方法保存在一个实例属性中，供后面使用。

❷ 为 sys.stdout.write 打猴子补丁，替换成自己编写的方法。

### 15.4 使用@contextmanager

mirror.py：

```
:::python
import contextlib

@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''  
    try:
        yield 'JABBERWOCKY'  ➊
    except ZeroDivisionError: 
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write  ➋
        if msg:
            print(msg)  
```

❶ 产出一个值，这个值会绑定到 with 语句中 as 子句的目标变量上。执行 with 块中的代码时，这个函数会在这一点暂停。

❷ 控制权一旦跳出 with 块，继续执行 yield 语句之后的代码。

使用 @contextmanager 装饰器时，要把 yield 语句放在 try/finally 语句中（或者放在 with 语句中），这是无法避免的，因为我们永远不知道上下文管理器的用户会在 with 块中做什么。在 @contextmanager 装饰器装饰的生成器中，yield 与迭代没有任何关系。在本节所举的示例中，生成器函数的作用更像是协程：执行到某一点时暂停，让客户代码运行，直到客户让协程继续做事。



```
:::python
>>> D.__mro__
(<class 'diamond.D'>, <class 'diamond.B'>, <class 'diamond.C'>,
<class 'diamond.A'>, <class 'object'>)

```

❷ 超类中的方法

❷ 控制权一旦跳出 with 块，继续执行 yield 语句之后的代码。

值是一个元组，按照方法解析顺序列出各个超类，从当前类一直向上，直到 object 类。

```
:::python
>>> D.__mro__
(<class 'diamond.D'>, <class 'diamond.B'>, <class 'diamond.C'>,
<class 'diamond.A'>, <class 'object'>)

```

❷ 超类中的方法

❷ 控制权一旦跳出 with 块，继续执行 yield 语句之后的代码。

值是一个元组，按照方法解析顺序列出各个超类，从当前类一直向上，直到 object 类。

```
:::python
>>> D.__mro__
(<class 'diamond.D'>, <class 'diamond.B'>, <class 'diamond.C'>,
<class 'diamond.A'>, <class 'object'>)

```

❷ 超类中的方法

❷ 控制权一旦跳出 with 块，继续执行 yield 语句之后的代码。

值是一个元组，按照方法解析顺序列出各个超类，从当前类一直向上，直到 object 类。

```
:::python
>>> D.__mro__
(<class 'diamond.D'>, <class 'diamond.B'>, <class 'diamond.C'>,
<class 'diamond.A'>, <class 'object'>)

```

❷ 超类中的方法