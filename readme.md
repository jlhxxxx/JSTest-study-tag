# 学习笔记
* [Java 笔记](https://github.com/jlhxxxx/JSTest-study-tag/blob/master/Java%E7%AC%94%E8%AE%B0.md)——关键字：Java
* [JS 单元测试](https://github.com/jlhxxxx/JSTest-study-tag/blob/master/JS%20%E5%8D%95%E5%85%83%E6%B5%8B%E8%AF%95.md)——关键字：Node ava mocha chai nyc JsUnit
* [修改代码的艺术](https://github.com/jlhxxxx/JSTest-study-tag/blob/master/%E4%BF%AE%E6%94%B9%E4%BB%A3%E7%A0%81%E7%9A%84%E8%89%BA%E6%9C%AF-Working%20Effectively%20with%20Legacy%20Code-Michael%20C.%20Feathers.md)——关键字：单元测试 重构
* [JMeter 学习](https://github.com/jlhxxxx/JSTest-study-tag/blob/master/JMeter%E5%AD%A6%E4%B9%A0.md)
* [JMeter 实践中遇到的问题及解决方法](https://github.com/jlhxxxx/JSTest-study-tag/blob/master/JMeter%E5%AE%9E%E8%B7%B5%E4%B8%AD%E9%81%87%E5%88%B0%E7%9A%84%E9%97%AE%E9%A2%98%E5%8F%8A%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95.md)
* [其他日常记录](https://github.com/jlhxxxx/JSTest-study-tag/blob/master/%E5%85%B6%E4%BB%96%E6%97%A5%E5%B8%B8%E8%AE%B0%E5%BD%95.md)

> 以下是没用的内容，仅仅保留一些格式

<p align="center">
  <a href="https://www.baidu.com">
    <img src="https://cldup.com/xFVFxOioAU.svg" alt="Mocha test framework"/>
  </a>
    <img src="https://cldup.com/xFVFxOioAU.svg" alt="Mocha test framework"/>
  <br>
    <img src="https://cldup.com/xFVFxOioAU.svg" alt="Mocha test framework"/>
</p>

- [ ] sdf

add some news

## github 每次 push 都要输用户名和密码解决方法

在 github.com 上建立了一个小项目，可是在每次 push 的时候，都要输入用户名和密码，很是麻烦，原因是使用了 https 方式 push，在 bash 里边输入 `git remote -v` 可以看到形如下面的返回结果：

    origin https://github.com/yuquan0821/demo.git (fetch)
    origin https://github.com/yuquan0821/demo.git (push)

下面把它换成ssh方式的：

    git remote rm origin
    git remote add origin git@github.com:yuquan0821/demo.git
    git push origin 

## 将 chrome 安装在非系统盘

chrome默认安装路径为C:\Program Files (x86)\Google\Chrome，这时要确定 C:\Program Files (x86)\Google\ 下面没有chrome这个文件夹，因为这个要由mklink来创建。而文件夹 D:\Program Files\Google\Chrome 要先建立好。
windows7系统在cmd命令行中输入：

    mklink /d "C:\Program Files (x86)\Google\Chrome" "D:\Program Files\Google\Chrome"

符号链接制作完毕，开始安装chrome，安装完后进入 D:\Chrome 文件夹，这个是chrome真正的文件夹，而 C:\Program Files (x86)\Google\Chrome 只是一个映射，不占用c盘空间。

chrome 插件安装目录：C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Default\Extensions
