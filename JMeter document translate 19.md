

# 19. 属性参考

## 19 导言

本文档介绍了 JMeter 属性。在 `jmeter.properties` 或 `reportgenerator.properties` 中的属性应该在 `user.properties` 文件中设置。这些属性通常在类加载时解析，所以仅在重新启动 JMeter 后才会生效。

## 19.1 语言

#### 参数（Parameters）

属性（Attribute）| 描述| 是否必须
---------|----------|---------
language | 首选 GUI 语言。注释掉使用 JVM 默认语言环境的语言。</br>例如：</br><pre>language=en</pre><blockquote> 该属性是唯一必须在 jmeter.properties 文件中设置的属性</blockquote></br><blockquote>要完全配置语言，请确保您设置了语言环境，请参阅[国际化：了解 Java 平台中的语言环境](http://www.oracle.com/us/technologies/java/locale-140624.html)。英语示例：</blockquote><pre>-Duser.language = en -Duser.region = EN</pre> | 否
locales.add | 可添加到显示列表的其他语言环境。</br>当前的默认列表是：`en`，`fr`，`de`，`no`，`es`，`tr`，`ja`，`zh_CN`，`zh_TW`，`pl`，`pt_BR`。</br>请参阅 `JMeterMenuBar＃makeLanguageMenu()`</br>这些条目是用逗号分隔的语言名称列表。</br>例如：</br><pre>locales.add=zu</pre> | 否

## 19.2 XML 解析器

#### 参数（Parameters）

属性（Attribute）| 描述| 是否必须
---------|----------|---------
xpath.namespace.config | 包含名称空间映射的属性文件的路径，格式为 `prefix = Namespace`。例如：</br><pre>ns=http://biz.aol.com/schema/2006-12-18 | 否

## 19.3 SSL 配置

> SSL（Java）系统属性现在在 `system.properties` 中。</br> 
> JMeter 不再将文件中的 javax.xxx 属性转换到系统属性中。</br>
> 这些现在必须在 `system.properties` 文件或命令行中定义。</br>
> `system.properties` 文件提供了更多的灵活性。

#### 参数（Parameters）

属性（Attribute）| 描述| 是否必须
---------|----------|---------
https.sessioncontext.shared | 默认情况下，SSL 会话环境现在是按每个线程创建的，而不是共享的。
通过将此属性设置为true，可以启用旧行为。默认为：false