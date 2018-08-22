# Flask入门系列

### Hello World

    :::python
    # 首先引入Flask包，并创建一个Web应用的实例`app`
    from flask import Flask
    app = Flask(__name__)
    
    # 定义路由规则：当地址是根路径时，就调用下面的函数
    @app.route('/')
    # 当请求的地址符合路由规则时，就会进入该函数，可以在里面获取请求的request对象，返回的内容就是response
    def index():
        return '<h1>Hello World</h1>'
    
    # 启动Web服务器
    if __name__ == '__main__':
        app.run()
如果想支持远程，需要在`run()`方法传入`host=0.0.0.0`，想改变监听端口的话，传入`port=端口号`，你还可以设置调试模式（支持热部署）。 

    :::python	
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8888, debug=True)

### 路由

#### 带参数和多URL的路由

    :::python
    @app.route('/')
    @app.route('/user')
    @app.route('/user/<path:user_name>')
    def user(user_name=None):
        if user_name is None:
            user_name = 'admin'
        return 'User Name: %s' % user_name

| 类型转换器 | 作用                 |
| ---------- | -------------------- |
| 缺省       | 字符型，但不能有斜杠 |
| int:       | 整型                 |
| float:     | 浮点型               |
| path:      | 字符型，可有斜杠     |

#### HTTP请求方法设置

    :::python
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            return 'This is a POST request'
        else:
            return 'This is a GET request'

#### URL构建方法

Flask提供了`url_for()`方法来快速获取及构建URL，方法的第一个参数指向函数名（加过`@app.route`注解的函数），后续的参数对应于要构建的URL变量。 

    :::python
    url_for('login')    # 返回/login
    url_for('login', id='1')    # 将id作为URL参数，返回/login?id=1
    url_for('hello', name='man')    # 适配hello函数的name参数，返回/hello/man
    url_for('static', filename='style.css')    # 静态文件地址，返回/static/style.css

#### 静态文件位置

Flask的风格是将所有静态文件放在`static`子目录下。在代码或模板中使用`url_for('static')`来获取静态文件目录。 如果你想改变这个静态目录的位置，你可以在创建应用时，指定`static_folder`参数。 

    :::python
    app = Flask(__name__, static_folder='files')

### 模板

Flask的模板功能是基于[Jinja2模板引擎](http://jinja.pocoo.org/)实现的。 

    :::python
    from flask import Flask
    from flask import render_template
     
    app = Flask(__name__)
     
    @app.route('/hello')
    @app.route('/hello/<name>')
    def hello(name=None):
        return render_template('hello.html', name=name)
     
    if __name__ == '__main__':
        app.run(host='0.0.0.0', debug=True)

在当前目录下，创建一个子目录”templates“（注意，一定要使用这个名字）。然后在”templates“目录下创建文”hello.html“：

    :::html
    <!doctype html>
    <title>Hello Sample</title>
    {% if name %}
      <h1>Hello {{ name }}!</h1>
    {% else %}
      <h1>Hello World!</h1>
    {% endif %}

#### 模板继承

在”templates“目录下，创建一个名”layout.html“的模板：

    :::html
    <!doctype html>
    <title>Hello Sample</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
    <div class="page">
        {% block body %}
        {% endblock %}
    </div>

再修改之前”hello.html“，把原来的代码定义在”block body“中，并在代码一开始”继承”上面的”layout.html“： 

    :::html
    {% extends "layout.html" %}
    {% block body %}
    {% if name %}
      <h1>Hello {{ name }}!</h1>
    {% else %}
      <h1>Hello World!</h1>
    {% endif %}
    {% endblock %}

#### HTML自动转义

    :::python
    @app.route('/')
    def index():
        return '<div>Hello %s</div>' % '<em>Flask</em>'

打开页面，你会看到”Flask”是斜体的，因为我们加了”em”标签。但有时我们并不想让这些HTML标签自动转义，特别是传递表单参数时，很容易导致HTML注入的漏洞。我们把上面的代码改下，引入`Markup`类：

    :::python
    from flask import Flask, Markup
     
    app = Flask(__name__)
     
    @app.route('/')
    def index():
        return Markup('<div>Hello %s</div>') % '<em>Flask</em>'

`Markup`还有很多方法，比如`escape()`呈现HTML标签， `striptags()`去除HTML标签。 

### Flask内建对象

#### 请求对象request

    :::python
    from flask import request
     
    @app.route('/login', methods=['POST', 'GET'])
    def login():
        if request.method == 'POST':
            if request.form['user'] == 'admin':
                return 'Admin login successfully!'
            else:
                return 'No such user!'
        title = request.args.get('title', 'Default')
        return render_template('login.html', title=title)

”login.html“：

    :::html
    {% extends "layout.html" %}
    {% block body %}
    <form name="login" action="/login" method="post">
        Hello {{ title }}, please login by:
        <input type="text" name="user" />
    </form>
    {% endblock %}

#### 会话对象session

    :::python
    from flask import request, session
     
    @app.route('/login', methods=['POST', 'GET'])
    def login():
        if request.method == 'POST':
            if request.form['user'] == 'admin':
                session['user'] = request.form['user']
                return 'Admin login successfully!'
            else:
                return 'No such user!'
        if 'user' in session:
            return 'Hello %s!' % session['user']
        else:
            title = request.args.get('title', 'Default')
            return render_template('login.html', title=title)
     
    app.secret_key = '123456'

”admin”登陆成功后，再打开”login”页面就不会出现表单了。 使用session时一定要设置一个密钥`app.secret_key`，如上例。不然你会得到一个运行时错误，内容大致是`RuntimeError: the session is unavailable because no secret key was set`。密钥要尽量复杂，最好使用一个随机数。

登出的方法就是清除字典里的键值 ：

    :::python
    from flask import request, session, redirect, url_for
     
    @app.route('/logout')
    def logout():
        session.pop('user', None)
        return redirect(url_for('login'))

#### 构建响应

    :::python
    from flask import request, session, make_response
     
    @app.route('/login', methods=['POST', 'GET'])
    def login():
        if request.method == 'POST':
            ...
        if 'user' in session:
            ...
        else:
            title = request.args.get('title', 'Default')
            response = make_response(render_template('login.html', title=title), 200)
            response.headers['key'] = 'value'
            return response

#### Cookie的使用

    :::python
    from flask import request, session, make_response
    import time
     
    @app.route('/login', methods=['POST', 'GET'])
    def login():
        response = None
        if 'user' in session:
            login_time = request.cookies.get('login_time')
            response = make_response('Hello %s, you logged in on %s' % (session['user'], login_time))
        else:
            if request.method == 'POST':
                if request.form['user'] == 'admin':
                    session['user'] = request.form['user']
                    response = make_response('Admin login successfully!')
                    response.set_cookie('login_time', time.strftime('%Y-%m-%d %H:%M:%S'))
                    ...
    
        return response

#### 全局对象g

`flask.g`是Flask一个全局对象，这里有点容易让人误解，其实`g`的作用范围，就在一个请求（也就是一个线程）里，它不能在多个请求间共享。你可以在`g`对象里保存任何你想保存的内容。一个最常用的例子，就是在进入请求前，保存数据库连接。（参考数据库集成部分内容） 

### 错误处理及消息闪现

#### 错误处理

使用`abort()`函数可以直接退出请求，返回错误代码：

    :::python
    from flask import abort
     
    @app.route('/error')
    def error():
        abort(404)

在遇到特定错误代码时做些事情，或者重写错误页面，可以用下面的方法： 

    :::python
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

自定义一个异常： 

    :::python
    class InvalidUsage(Exception):
        status_code = 400
     
        def __init__(self, message, status_code=400):
            Exception.__init__(self)
            self.message = message
            self.status_code = status_code
     
    @app.errorhandler(InvalidUsage)
    def invalid_usage(error):
        response = make_response(error.message)
        response.status_code = error.status_code
        return response

通过路由调用：

    :::python
    @app.route('/exception')
    def exception():
        raise InvalidUsage('No privilege to access the resource', status_code=403)

#### URL重定向：redirect()

    :::python
    from flask import session, redirect
     
    @app.route('/')
    def index():
        if 'user' in session:
            return 'Hello %s!' % session['user']
        else:
            return redirect(url_for('login'), 302)

#### 日志

Flask提供logger对象，其是一个标准的Python Logger类。修改上例中的`exception()`函数： 

    :::python
    @app.route('/exception')
    def exception():
        app.logger.debug('Enter exception method')
        app.logger.error('403 error happened')
        raise InvalidUsage('No privilege to access the resource', status_code=403)

日志配置代码： 

    :::python
    server_log = TimedRotatingFileHandler('server.log','D')
    server_log.setLevel(logging.DEBUG)
    server_log.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s'
    ))
     
    error_log = TimedRotatingFileHandler('error.log', 'D')
    error_log.setLevel(logging.ERROR)
    error_log.setFormatter(logging.Formatter(
        '%(asctime)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
     
    app.logger.addHandler(server_log)
    app.logger.addHandler(error_log)

#### 消息闪现：flash() 

    :::python
    @app.route('/login', methods=['POST', 'GET'])
    def login():
        if request.method == 'POST':
            session['user'] = request.form['user']
            flash('Login successfully!', 'message')
            flash('Login as user: %s.' % request.form['user'], 'info')
            return redirect(url_for('index'))
        ...

当用户登录成功后，就用`flash()`函数闪出一个消息（不过还要在模板中渲染一下，加上消息显示的部分）。`flash()`方法的第二个参数是消息类型，可选择的有`message`, `info`, `warning`, `error`。你可以在获取消息时，同时获取消息类型，还可以过滤特定的消息类型。只需设置`get_flashed_messages()`方法的`with_categories`和`category_filter`参数即可。将"layout.html"模板修改成如下，这样就只显示 `["message","error"]`类型的消息：

    :::html
    ...
    {% with messages = get_flashed_messages(with_categories=true, category_filter=["message","error"]) %}
      {% if messages %}
        <ul class="flash">
        {% for category, message in messages %}
          <li class="{{ category }}">{{ category }}: {{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    ...

### 数据库集成

数据库以[SQLite](https://www.sqlite.org/download.html)为例：[教程](http://www.runoob.com/sqlite/sqlite-tutorial.html)

#### 初始化数据库

初始化SQL，保存在”init.sql”文件中： 

```
:::sql
drop table if exists users;
create table users (
  id integer primary key autoincrement,
  name text not null,
  password text not null
);
 
insert into users (name, password) values ('visit', '111');
insert into users (name, password) values ('admin', '123');
```

新建“db”目录，运行sqlite3命令，初始化数据库： 

```
:::cmd
$ sqlite3 db/user.db < init.sql
```

#### 配置连接参数

创建配置文件"config.py"，保存配置信息： 

```
:::python
#coding:utf8
DATABASE = 'db/user.db'       # 数据库文件位置
DEBUG = True                  # 调试模式
SECRET_KEY = 'secret_key_1'   # 会话密钥
```

在创建Flask应用时，导入配置信息： 

```
:::python
from flask import Flask
import config
 
app = Flask(__name__)
app.config.from_object('config')
```

这里也可以用`app.config.from_envvar('FLASK_SETTINGS', silent=True)`方法来导入配置信息，此时程序会读取系统环境变量中`FLASK_SETTINGS`的值，来获取配置文件路径，并加载此文件。如果文件不存在，该语句返回`False`。参数`silent=True`表示忽略错误。 

#### 建立和释放数据库连接

```
:::python
from flask import g
import sqlite3

@app.before_request
def before_request():
    g.db = sqlite3.connect(app.config['DATABASE'])
 
@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
```

#### 查询数据库

```
:::python
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form['user']
        passwd = request.form['passwd']
        cursor = g.db.execute('select * from users where name=? and password=?', [name, passwd])
        if cursor.fetchone() is not None:
            session['user'] = name
            flash('Login successfully!')
            return redirect(url_for('index'))
        else:
            flash('No such user!', 'error')
            return redirect(url_for('login'))
    else:
        return render_template('login.html')
```

"login.html" ：

```
:::python
{% extends "layout.html" %}
{% block body %}
<form name="login" action="/login" method="post">
    Username: <input type="text" name="user" /><br>
    Password: <input type="password" name="passwd" /><br>
    <input type="submit" value="Submit" />
</form>
{% endblock %}
```

本文内容来源于：[思诚之道](http://www.bjhee.com/flask-1.html) 