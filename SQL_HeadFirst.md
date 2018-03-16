# HeadFirst-SQL学习笔记

## 第一章 基础命令

1. 创建/删除数据库：

   ```sql
   create database dbname;
   Drop database dbname;
   ```

2. 显示数据库：

   ```sql
   show databases;
   ```

3. 使用数据库：

   ```sql
   use dbname;
   ```

4. 显示数据库的表：

   ```sql
   show tables;
   ```


5. 创建表：

   ```sql
   create table tabname(columns);
   ```

   ```sql
   --Example:
   Create table bookstore(id int not null, name varchar(30) not null default 'sth');
   ```

   > 常用[数据类型](http://www.w3school.com.cn/sql/sql_datatypes.asp)：`char(size)`, `varchar(size)`, `text`, `int(size)`,    `float(size,d)`,  `double(size,d)`,  `date()`,  `datetime()`,  `time()`


6. 显示表结构：

   ```sql
   desc tabname;
   ```

7. 删除表：

   ```sql
   drop table tabname;
   ```

8. 插入表数据：

   ```sql
   insert into tabname (id,name) values (1,'sth');
   ```

9. 查看表记录：

   ```sql
   select * from tabname;

   ```

10. `show`高级用法

   ```sql
   --查看表创建的语句
   show create table tabname; 
   show create database dbname; 
   show columns/index from tabname;
   ```

## 第二章 SELECT命令

1. 条件查找：

   ```sql
   select * from tabname where id=1;
   ```


2. 综合查询：

   ```sql
   select * from tabname where id=1 and name='sth';
   ```

3. 比较运算符：`=`等于，`<>`不等于，`<`，`>`，`<=`，`>=`

4. 必须使用`is null` 选择值为 null 的数据，无法用`=`找出

5. 使用`\`进行转义

   ```sql
   select * from tabname where name like 'A_%';
   ```

**关键字**

* `and` ：且


* `or`：或者

* `like`：符合某种条件，多和通配符一起用。通配符有:

  * `%`：任意数量未知字符

    ```sql
    select * from tabname where name like '%iabi';
    ```

  * `_`：一个未知字符

    ```sql
    select * from tabname where name like '_iabi';
    ```

* `between`...`and`...：

  ```sql
   select * from tabname  where value between 100 and 1000;
  ```

* `in`：在...范围内: 

  ```sql
  select * from tabname where name in ('A','B');
  --等价于
  select * from tabname where name='A' or name='B'；
  ```

* `not in`:不在...范围内

* `not`：不满足某种条件，not和between、like一起用时要直接跟在where后面

  ```sql
  select * from tabname where not name like 'A%';
  ```

## 第三章 DELETE 和 UPDATE

1. **delete**: 和`select`相比，`delete`不需要`*`，其他用法同`select`。

   ```sql
   delete from tabname where id=1;
   ```

   * `delete`不能删除单一列或某一列的所有值
   * 为防止误删可先用`select`查看要删除的行


2. **update**:

   ```sql
   update tabname set column=‘value1’ where column=‘value’;
   ```

   * `set`后可跟多个值，用`，`隔开，`where`后语句同`select`
   * 不确定的话也可先用`select`确定一下

## 第四章  聪明的表设计

#### 原子化：把数据分割成创建有效率的表所需的最小片段

* Rule1：具有原子性数据的列中不会有多个类型相同的值；
* Rule2：具有原子性数据的表中不会有多个存储同类数据的列。

#### 1NF（First Normal Form：第一范式）

* 每个数据行必须包含具有原子性的值；

* 每个数据行必须有独一无二的识别项——主键（Primary Key）。

  主键用于独一无二的识别出每条记录，不可为null，插入记录时必须赋值，必须简洁，不可被修改。

  ```sql
  --新增表：指定id为主键,auto_increment依次递增，每个表中仅有一列可设置为auto_increment，该列必须为整型且不能包含null
  create table tabname(id int not null auto_increment,…primary key（id）)；

  --修改表：first表示把新列放在最前面
  alter table tabname
  	add column F_id int not null auto_increment first,
  	add primary key (F_id);
  ```

## 第五章 ALTER

* 上例中`first`可换成`second`、`third`…`last`（默认）、`before/after your_column`

* `add` 添加一列

* `modify` 修改现有列的数据类型或位置

* `change` 可同时改变现有列的名称和数据类型

* `drop` 可删除某列或移除某属性

  ```sql
  alter table tabname drop primary key;
  ```

* `rename`重命名表

  ```sql
  alter table tabname rename to new_tabname;
  ```

> 改变数据类型可能会遗失数据。

**一些便利的字符串函数**(字符串函数不改变表中内容，只把修改后结果当成查询返回值)

```sql
--从your_string右侧/左侧开始选取length长度字符
right/left (your_string,length)
--substring
substring_index(Location,’,’,2) --Location列第2个,前的字符串
substring(your_string,start_position,length)
--把字符串改成大写/小写形式
upper/lower (your_string)
--反转字符串
reverse(your_string)
--清除字符串左侧/右侧空格
ltrim/rtrim (your_string)
--求字符串长度
length(your_string)
--Example
select right (Location,2) from my_contacts
```

## 第六章 SELECT进阶

1. case语句

   ```sql
   update tabname set new_column =
   case
   	when column1=somevalue1 then newvalue1
   	when column2=somevalue2 then newvalue2
   	else newvalue3
   end;--end后可加where语句
   ```


2. order by 排序

   * 字符顺序：非字母 - null - 数字 - 大写字母 - 小写字母

   * `desc`用在列名后，反转排序（默认`asc`）

   * 常用数学函数(会忽略null): `sum(column)` ，`avg()`，`max()`，`min()`，`count()`

     ```sql
     select sum(volumn) from tabname where…;
     ```

   * `distinct`选出不重复的

     ```sql
     select distinct date from tabname order by date;
     select count(distinct date) from tabname;
     ```


3. group by 分组

   ```sql
   select first_name,sum(value) from tabname 
   	group by first_name
   	order by sum(value) desc;
   ```


4. limit 限制返回结果

   ```sql
   select * from tabname limit 1,2;--从第2个数据开始选择出2个
   select * from tabname limit 2;--选择出前2个
   ```

## 第七章 多张表的数据库设计

1. 创建带有外键的表`constraint`

   ```sql
   create table sontabname(
   	int son_id int not null auto_increment primary key,
   	id int not null,
   	constraint 
   		tabname_id_fk --这部分称为constraint，命名方式告诉我们来源，可用此名称解除约束
       	foreign key (id)--此id即为外键，可以随意命名
   		references tabname(id)
   );
   ```

   > 创建外键的值必须已经存在于父表的来源列中（必须有值），这是引用完整性。外键不一定是父表的主键，但必须有唯一性。

2. 表间关系

   * 一对一：父表只有一行与子表的某行相关
   * 一对多：A表中某条记录对应B表中多条记录，但B表中某条记录只对应A表中一条记录
   * 多对多：通常由两个一对多关系（A-B，B-A）并利用junction table在中间联接构成

#### 2NF（第二范式）

* Rule1：已达成1NF；
* Rule2：没有部分函数依赖性。

> 理解概念：组合主键，依赖（某列数据必须随着另一列数据改变而改变），部分函数依赖（非主键的列依赖于组合主键的某个部分），传递函数依赖（改变任何非键列造成其他非键列的改变）

#### 3NF（第三范式）

* Rule1：已达成2NF；
* Rule2：没有传递函数依赖性。

## 第八章 联接与多张表的操作

1. 关键字as（别名）: as可以省略

   ```sql
   create table profession( 
   	id int(11) not null auto_increment primary key,
   	profession varchar(20)
   )as
   	select profession from tabmane
   	group by profession
   	order by profession;
   --等价于
   create table profession( 
   	id int(11) not null auto_increment primary key,
   	new_prof varchar(20)
   )as
   	select profession as new_prof from tabmane
   	group by new_prof
   	order by new_prof;
   ```


2. cross join交叉联接，返回两张表每行相乘的结果，cross join可省略

   ```sql
   select t.toy,b.boy from toys t cross join boys b;
   ```


3. inner join内连接

   ```sql
   select t.toy,b.boy from toys t inner join boys b on b.id=t.id; --on可换成where
   ```

   equijoin（相等联接“`=`”），non-equijoin（不等联接“`<>`”），natural join（自然联接，利用两张表相同类名联接，不需要on及其之后）

   ```sql
   select toys.toy,boys.boy from toys natural join boys;
   ```

## 第九章 子查询

1. subquery（子查询）=outer query（外层查询）+ inner query（内层查询）

   ```sql
   select table1.name,table1.phone,table2.work from table1 natural join table2 where table2.work in (select work from table3);
   ```

   **构造流程**：分解问题——找出能回答部分问题的查询——继续分解查询——找出串起两个查询的方式（废话）

   如果子查询放在select语句中，用于表示某个欲选取的列，则一次只能从一列返回一个值；

   ```sql
   select t1.name,(select state from table2 where t1.code=code) as state from table1 t1;
   ```


2. 非关联子查询：子查询可以独立运行且不会引用外层查询的任何结果。

3. 关联子查询：子查询依赖外层查询

   ```sql
   select t1.name from table1 t1 where not exists (select * from table2 t2 where t1.id=t2.id);
   ```

   > 关键字：`exists`和`not exists`类似 `in`和`not in`

## 第十章 外联接、自联接与联合

1. outer join（外联接）：返回某张表所有行，并带有另一张表符合条件的行
   * left outer join（左外联接）：接收左表所有行，并用右表匹配左表，出现在from后联接前的是左表
   * right outer join（右外联接）：接收左表所有行，并用左表匹配右表，出现在from后联接前的是右表


2. self-join（自联接）：把单一表当成两张相同的表来查询

   自引用外键：处于其他目的引用同一张表的主键

   ```sql
   select t1.name,t2.name as boss from tabname t1 inner join tabname t2 on t1.boss_id=t2.id; 
   ```


3. union（联合）

   ```sql
   select title from t1 union select title from t2 union select title from t3 order by title;
   ```

   Rules：每个select语句中列的数量必须一致，所包含的表达式与统计函数也必须相同，数据类型要相同或者可以互相转换，默认清除重复值（要保留重复值用union all）。

   其他关键字：`intersect`：返回A∩B，`except`返回A-A∩B。


4. 子查询与联接比较（见仁见智）

   ```sql
   --子查询
   select table1.name,table1.phone,table2.work from table1 natural join table2 where table2.work in (select work from table3);
   --联接
   select table1.name,table1.phone,table2.work from table1 natural join table2 inner join table2 on table2.work=table3.work;
   --用子查询改写自联接
   select t1.name,(select name from tabname where t1.boss_id=id) as boss from tabname t1; 
   ```

## 第十一章 约束、视图与事务

1. check（检查约束）：可用where语句，但无法使用子查询

   ```sql
   create table bank (
       id int auto_increment not null primary key, 		coin char(1) check (coin in ('p','d','n','q'))
   );
   alter table tabname add constraint check gender in ('F' ,'M');
   ```


2. view视图——可以视为虚拟表，用来保存SQL语句

   ```sql
   --创建
   create view tabdesigners as 
   	select t.name,t.phone,t.email from tabname t;
   等价于
   select * from (select t.name, t.phone, t.email from tabname t) as tabdesigners;--此处as不能省，当select语句结果是一个虚拟表时，若没有别名，SQL就无法取得其中的表。

   --使用（当做一张表）：
   select * from tabdesigners;
   ```

   关键字：check option

   ```sql
   --检查每个insert或delete的查询，根据视图中的where子句判断能否执行
   create view tab_view as select * from tabname where genter =‘M’ with check option;
   ```

   视图使用完毕，需用drop清除空间

   ```sql
   drop view tab_view;
   ```


3. transaction（事务）

   事务的ACID检查：A原子性，C一致性，I隔离性，D持久性。

   ```sql
   --事务开始
   star transaction;
   --事务确认结束
   commit;
   --回到事务前状态
   rollback;
   ```

## 第十二章 安全性

1. 用户账号

   ```sql
   --MySQL
   set password for ‘root’@‘localhost’=password( ‘xxxxx’);
   --ORACLE
   alter user root identified by new-password; 
   --创建新用户
   create user elsie identified by ‘xxxxx’;
   ```


2. 权限

   1. grant to 赋予权限

      ```sql
      grant select(clumn_name) on tabname to Elsie;

      grant all on tablename to Elsie with grant option;--Elsie 可以把这个权限赋予别人
      ```

      使用`database_name.*`可以把权限范围运用到数据库中的每张表上

   2. revoke from 撤销权限

      ```sql
      revoke select on tabname from Elsie;

      revoke grant option on delete on tabname from Elsie;--Elsie仍有delete权限，但不可再赋给别人
      ```

      cascade和restrict有精确度的撤销操作

      ```sql
      --表示撤销权限有连锁反应（默认值，可以不用）
      revoke select on tabname from elsie cascade;
      --如果tabname已把权限赋给他人，那么返回错误信息，撤销权限失败
      revoke select on tabname from elsie restrict;
      ```

   除了select，其他针对列的权限基本没用，除非表中只有grant指定的列且必须有内容；

   grant和revoke可以用于视图，但是不可更新的视图除外。


3. role（角色）：可以授予一群人权限，同时又让他们每个人有自己的账号

   ```sql
   create role data_ertry;
   grant select,insert on some_table to data_entry;
   grant data_entry to user_name;
   drop role data_entry;
   ```

   一个用户可以身兼多角，但是要注意角色间的权限不冲突，否定性的权限优先于授予性的权限。

   ```sql
   grant data_entry to user_name with admin option;
   --user_name有data_entry的admin权限，所以可以把data_entry权限赋给其他用户
   ```

   cascard和restrict用法一样


4. 语句结合

   ```sql
   grant select on tabname to elsie identified by ‘xxxx’;
   ```

## 附录： 

1. any、all和some

   1. all

      ```sql
      select score from tabname where score>all(select score from tabname where score>60 and score <90);
      -- >all 找出大于集合中最大值的值
      -- <all 找出小于集合中最小值的值
      ```

   2.  any=some（例子同上）

      ```sql
      >any 找出大于集合中最小值的值=
      <any 找出小于集合中最大值的值
      ```

2. 临时表

   ```sql
   create temporary table my_temp_table(…);
   ```


3. 转换数据类型

   ```sql
   cast(your_column, type);
   select cast(’2015-01-01’ as date);
   ```

   不能使用`cast()`场合：从浮点转换成整数；从time、date、datetime、char转换成decimal或integer。


4. 查看当前时间、用户

   ```sql
   select current_user;
   select current_date;
   select current_time;
   ```


5. 创建索引

   ```sql
   alter table tabname add index (name);
   ```


6. 常用函数

    [SQL 函数](http://www.w3school.com.cn/sql/sql_functions.asp)