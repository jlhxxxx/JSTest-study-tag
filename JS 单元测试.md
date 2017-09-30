___
**JS 单元测试**
___
* **目录**

<!-- TOC -->

- [1. Node.js 单元测试](#1-nodejs-单元测试)
    - [1.1 Node.js及npm环境](#11-nodejs及npm环境)
    - [1.2 测试框架](#12-测试框架)
    - [1.3 断言库](#13-断言库)
    - [1.4 测试覆盖率工具](#14-测试覆盖率工具)
- [2. 网页测试](#2-网页测试)
    - [2.1 JsUnit](#21-jsunit)
    - [2.2 QUnit](#22-qunit)

<!-- /TOC -->

> **推荐使用 ava+nyc+Node.js 或 mocha+chai+nyc+Node.js**
> [前端库](https://www.awesomes.cn/repos/Applications/Testings)

## 1. Node.js 单元测试

### 1.1 Node.js及npm环境 

 * [Node.js及npm集成环境](https://github.com/mochajs/mocha)---[Node.js（git）](https://github.com/nodejs/node)---[npm（git）](https://github.com/npm/npm)
 * [淘宝 NPM 镜像](https://npm.taobao.org) ---[cnpm（git）](https://github.com/cnpm/cnpm)
 
### 1.2 测试框架 

 * [AVA](https://github.com/avajs/ava-docs/blob/master/zh_CN/readme.md)（集成断言库，有中文文档） 
     * [ava-practice](http://i5ting.github.io/ava-practice/)
     * [ava及nyc举例](http://blog.csdn.net/dongshaoshuai/article/details/51684256)
     * [使用 AVA 做自动化测试](http://www.bijishequ.com/detail/438720?p=)---[源码](https://github.com/Barrior/ava-testing-examples)
     * [使用 ava 和 jsdom 做前端测试](https://segmentfault.com/a/1190000005834279)
 * [mocha](https://github.com/mochajs/mocha) 
     * [测试框架 Mocha 实例教程——阮一峰](http://www.ruanyifeng.com/blog/2015/12/a-mocha-tutorial-of-examples.html)---[教程demo（git）](https://github.com/ruanyf/mocha-demos)
     * [用Mocha，Chai进行Node.js测试](http://www.html-js.com/article/1875)
 * [Jasmine](https://jasmine.github.io/)
 * [QUnit](http://qunitjs.com/)

### 1.3 断言库 

 * [chai](https://github.com/chaijs/chai)---支持TDD(assert)、BDD(expect、should)
    * [Chai.js断言库API中文文档](http://www.jianshu.com/p/f200a75a15d2)
 * [expect](https://github.com/Automattic/expect.js)---支持assert、should
 * [should](https://github.com/shouldjs/should.js)---支持assert
 * [assert](https://nodejs.org/api/assert.html)---Node.js 自带-核心-默认

### 1.4 测试覆盖率工具 

 * [istanbuljs/nyc](https://github.com/istanbuljs/nyc)
     * [多进程下的测试覆盖率](http://taobaofed.org/blog/2015/12/15/nodejs-cluster-cov/)
     * [Node.js单元测试、集成测试、基准测试以及代码覆盖率测试方面总结——*ava+nyc*](http://ourjs.com/detail/5738493888feaf2d031d24fa)
     * [测试用例：mocha，should，istanbul——*fibonacci数列例子*](http://wiki.jikexueyuan.com/project/node-lessons/mocha-should-istanbul.html)
    
## 2. 网页测试

### 2.1 JsUnit
 * [JsUnit下载](http://www.jsunit.net/)
 * [JsUnit教程](http://www.javawebentry.com/html/639.html)
 * [使用JsUnit和JSMock的JavaScript测试驱动开发](http://www.infoq.com/cn/articles/javascript-tdd)

### 2.2 QUnit
 * [QUnit](http://qunitjs.com/)
