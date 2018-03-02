# 学习笔记

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
