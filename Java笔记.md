<!-- TOC -->

- [一、类、对象和方法](#一类对象和方法)
    - [1.1 类](#11-类)
    - [1.2 创建对象](#12-创建对象)
    - [1.3 方法](#13-方法)
    - [1.4 构造函数](#14-构造函数)
    - [1.5 this 关键字](#15-this-关键字)
- [二、方法和类详解](#二方法和类详解)
    - [2.1 控制对类成员的访问（封装）](#21-控制对类成员的访问封装)
    - [2.2 向方法传递对象](#22-向方法传递对象)
    - [2.3 返回对象](#23-返回对象)
    - [2.4 方法重载](#24-方法重载)
    - [2.5 递归](#25-递归)
    - [2.6 static 关键字](#26-static-关键字)
    - [2.7 嵌套类和内部类](#27-嵌套类和内部类)
- [三、继承](#三继承)
    - [3.1 继承的基础知识（extends）](#31-继承的基础知识extends)
    - [3.2 成员访问和继承](#32-成员访问和继承)
    - [3.3 构造函数和继承](#33-构造函数和继承)
    - [3.4 超类引用和子类对象](#34-超类引用和子类对象)
    - [3.5 方法重写](#35-方法重写)
    - [3.6 抽象类( absctact )](#36-抽象类-absctact-)
    - [3.7 final 关键字](#37-final-关键字)
    - [3.8 Object类](#38-object类)
- [四、包和接口](#四包和接口)
    - [4.1 包和成员访问](#41-包和成员访问)
    - [4.2 导入包（import）](#42-导入包import)
    - [4.3 接口（interface）](#43-接口interface)
    - [4.4 实现接口（implements）](#44-实现接口implements)
    - [4.5 接口引用](#45-接口引用)
    - [4.6 接口变量](#46-接口变量)
    - [4.7 接口也能被扩展（extends）](#47-接口也能被扩展extends)
    - [4.8 默认接口方法（JDK8新功能 : default）](#48-默认接口方法jdk8新功能--default)
    - [4.9 多继承问题](#49-多继承问题)
    - [4.10 接口中使用静态方法](#410-接口中使用静态方法)
- [五、泛型](#五泛型)
    - [5.1 泛型基础](#51-泛型基础)
    - [5.2 约束类型](#52-约束类型)
    - [5.3 通配符实参（？ 替换 T）](#53-通配符实参-替换-t)
    - [5.4 约束通配符](#54-约束通配符)
    - [5.5 泛型方法](#55-泛型方法)
    - [5.6 泛型构造函数](#56-泛型构造函数)
    - [5.7 泛型接口](#57-泛型接口)
    - [5.8 一些泛型限制](#58-一些泛型限制)
- [六、枚举、自动装箱、静态导入和注释](#六枚举自动装箱静态导入和注释)
    - [6.1 枚举（enum）](#61-枚举enum)
- [七、异常处理](#七异常处理)
    - [7.1 异常处理基础（try catch throw throws fanally）](#71-异常处理基础try-catch-throw-throws-fanally)
- [八、使用I/O](#八使用io)
    - [8.1 流（stream）](#81-流stream)

<!-- /TOC -->
## 一、类、对象和方法
### 1.1 类
* 对象是类的实例

### 1.2 创建对象
* 包括声明和分配内存

		class-name class-var;
		class-var =new class-name(arg-list);
	等价于

		class-name class-var =new class-name(arg-list);
### 1.3 方法
	ret-type name(parameter-list){
		//body of method
	}
* 非 void 必须要有返回值（return）

### 1.4 构造函数
初始化类定义的实例变量

### 1.5 this 关键字
* 调用方法时，会向方法自动传送一个隐式实参，它是对调用对象的一个引用；若是局部变量隐藏了实例变量，可使用this找到实例变量。

## 二、方法和类详解
### 2.1 控制对类成员的访问（封装）
* 访问修饰符 public 和 private ( protected 继承时候才用到)
* 默认 public

### 2.2 向方法传递对象
* 传递实参
 * 传值调用：对子例程形参的修改不影响调用的实参
 * 引用调用：对子例程形参的修改会改变调用的实参
 
### 2.3 返回对象
* 方法返回对象时，将一直存在，直至没有对它的引用为止，即对象不会因创建它的方法结束而销毁。

### 2.4 方法重载
* 被重载的方法形参类型和数量必须不同（返回值类型相同可以）
* 重载构造函数

### 2.5 递归
* 方法可以调用自身

		//阶乘
		int factR(int n){
			int result;
		
			if(n==1) return 1;
			result=factR(n-1)*n;
			return result;
		}

### 2.6 static 关键字
* 可以在创建类的对象之前访问该成员，而无需引用任何对象。
* static 变量本质上是全局变量，类的所有实例共用同一个 static 变量。
* static 方法的限制
 * 只能直接调用其他 static 方法或数据
 * 没有 this 引用
 
* static 代码块：在类第一次加载时执行（初始化）

### 2.7 嵌套类和内部类
* 非 static 类型为内部类

## 三、继承
### 3.1 继承的基础知识（extends）
* 子类只有一个超类，一个类不能是自己的超类。

### 3.2 成员访问和继承
* 继承一个类不能超越 private 访问限制
* 声明 private 原则：
 * 实例变量只被它所在类中方法使用
 * 实例变量必须在某一范围内

### 3.3 构造函数和继承
* 只有子类定义构造函数时，只需构造子类对象即可
* 超类子类都有构造函数时，子类必须使用 super ，且 super 必须是子类构造函数中执行的第一条语句，支持重载
* super 第二种用法和this类似

### 3.4 超类引用和子类对象
* 一个类类型的引用变量通常不能引用一个其他类类型的对象；唯一例外就是，超类可以引用子类对象，但只能访问对象的超类定义的部分

### 3.5 方法重写
* 与重载区别
 * 重载：被重载的方法形参类型和数量必须不同；
 * 重写：子类中方法与超类中方法，具有相同返回类型和签名
* 要访问超类中被重写的方法，用 super
* 支持多态：当通过超类引用被重写的方法时，会根据在调用发生时引用的对象的类型来判断所要执行的方法。

### 3.6 抽象类( absctact )
* 包含抽象方法的类必须被申明为抽象类，不可用new
* 抽象方法没有内容，无需被超类实现

		abstract type name(parameter-list);
* 子类若不是抽象类，就必须重写并实现超类中所有抽象方法

### 3.7 final 关键字
* 防止方法被重写
* 防止类被继承（所以不可和 abstract 合用）
* 声明不可改变的常量

### 3.8 Object类
* 所有类的隐式超类

## 四、包和接口
### 4.1 包和成员访问

<center>类成员访问（不是类）

|       private        | 默认  | protected | public |       |
| -------------------- | :---: | :-------: | :----: | :---: |
| 在同一个类中可见     |  是   |    是     |   是   |  是   |
| 在同一包中子类可见   |  否   |    是     |   是   |  是   |
| 在同一包中非子类可见 |  否   |    是     |   是   |  是   |
| 在不同包中子类可见   |  否   |    否     |   是   |  是   |
| 在不同包中非子类可见 |  否   |    否     |   否   |  是   |
 </center>

* 类只有两种访问级别：默认和 public 。默认仅允许同一个包中其他代码访问。


### 4.2 导入包（import）

### 4.3 接口（interface）

	access interface name{
		ret-type method-name1(param-list);
		ret-type method-name2(param-list);
		type var1=value;
		type var2=value;
		//...
		ret-type method-nameN(param-list);
		type varN=value;
	}
* 接口里任何方法都不包含实体，包含接口的类必须实现接口的全部方法（类似抽象类）
* 任意数量的类都可以实现它，一个类也可以实现多个接口（和继承区别）
* 在接口中申明的变量不是实例变量，它们被隐式声明为 public 、 final 和 static ，并且必须被初始化（？）

### 4.4 实现接口（implements）

	class classname extends superclass implements interface1,interface2...{
		//class-body
	}
* 实现接口的方法必须被申明为 public 

### 4.5 接口引用
* 类似使用超类引用访问子类对象

### 4.6 接口变量
* 方便定义一些共享的常量

### 4.7 接口也能被扩展（extends）

### 4.8 默认接口方法（JDK8新功能 : default）
* 可以定义默认方法，这样实现接口的类就不用实现接口所有的方法
* 和类区别：不能通过自身创建实例，必须由类来实现（new）

### 4.9 多继承问题
* 默认方法不支持行为的多重继承，如果某个类继承了两个相同默认方法的接口，就必须对方法重写
* 类的实现优先于接口的默认实现，子类接口的默认方法优先于超类

### 4.10 接口中使用静态方法
* 类似类中 static 方法调用
* static 方法不能被实现类和子接口继承

## 五、泛型
* **参数化类型**
### 5.1 泛型基础
* 只能用于引用类型
* 泛型类型是否相同基于其类型实参，可声明多个类型实参


		声明泛型：
		class class-name<type-param-list>{//....}
		声明引用并创建实例：
		class-name<type-org-list> var-name=new class-name<type-org-list>(cons-arg-list);
		JDK7之后可简写：class-name<type-org-list> var-name=new class-name<>(cons-arg-list);

### 5.2 约束类型
	< T extends superclass >
	< T, V setends T >	//确保V与T相同或是T子类
### 5.3 通配符实参（？ 替换 T）
* 不影响创建的对象类型，只是匹配任何有效的对象
	
		boolean absEqual(NumFns<?> ob){
			if(Math.abs(num.doubleValue())==Math.abs(ob.num.doubleValue())) 
				return true;
			return false;
		}
### 5.4 约束通配符
	上层约束：
	<? extends superclass>
	下层约束：
	<? super subclass>
### 5.5 泛型方法
	<type-param-list> ret-type meth-name(param-list){//...}
	举例：
	static <T extends Comparable<T>,V extends T> boolean arraysEqual(T[] x,V[] y){//...}
### 5.6 泛型构造函数
* 类不是泛型的构造函数也可以是泛型的

### 5.7 泛型接口
* 一个类实现泛型接口，它也应该是泛型的，除非它只实现泛型接口的特定类型

		例如：class myClass implements containment<double>
### 5.8 一些泛型限制
* 类型形参不能实例化
* 静态成员不能使用由包含类声明的类型形参（？）
* 不能实例化基类型为类型形参的数组，不能创建特定类型泛型引用的数组（？）

## 六、枚举、自动装箱、静态导入和注释

### 6.1 枚举（enum）
	
	enum Transport{
		CAR,TRAIN,BOAT,AIRPLANE
	}
* Java 将枚举实现为类类型，但不能使用 new 实例化枚举

		Transport tp;
		tp=Transport.CAR;

		enum Transport {
			CAR(65),AIRPLANE(600),BOAT(22),TRAIN(70);	//注意最后分号
			private int speed;
			//注意构造函数
			Transport(int s){speed=s;}
			int getSpeed(){return speed;}
		}
* 枚举不能继承另一个类，enum 不能是超类（不能被继承）


## 七、异常处理

### 7.1 异常处理基础（try catch throw throws fanally）
* 监测程序包含在 try 中，手动抛出异常用 throw ，某些时候从方法抛出的异常用 throws，从 try 代码退出时必须执行的代码放到 finally 中
* try 和 catch 必须一起使用；只有抛出异常，才会执行 catch 语句，否则跳过所有 catch 语句；多条 catch 表达式按顺序执行，只执行第一条匹配的语句，忽略其他所有；一个超类的 catch 语句与任一个子类都匹配，所以如果既想捕获超类又想捕获子类异常，就要把子类 catch 放前面
* 异常处理完就会被删除，每次进入 try 时，都是崭新的
* try 代码可以嵌套，一般用外部 try 捕获最严重的错误，用内部的 try 捕获不太严重的错误
* throw 抛出的是对象，如果对象还不存在，必须为类型创建一个对象（new）；重新抛出的异常不会被同一个 catch 捕获，而是传送到下一个
* 无论 try 正常还是异常结束，都会执行 finally
* 如果一个方法产生自己不做处理的异常，必须用 throws 声明该异常

		ret-type methName(param-list) throws except-list{
			//body
		}
* 同一 catch 可以捕获多个异常，使用OR运算符（|）分隔
* 可以自定义创建异常子类

## 八、使用I/O

### 8.1 流（stream）
 






