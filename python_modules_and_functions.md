# Python 常用模块及函数

## [Built-in Functions](https://docs.python.org/3/library/functions.html)

* **print()** # function has the optional parameters `end` and `sep` to specify what should be printed at the end of its arguments and between its arguments (separating them)

  ```python
  print('Hello', end='')
  print('World')
  HelloWorld
  >>> print('cats', 'dogs', 'mice', sep=',')
  cats,dogs,mice
  ```

* **round()** 

  ```python
  >>> round(1425064108.017826, 2)
  1425064108.02
  >>> round(1425064108.017826)
  1425064108
  ```

### **List methods**

```python
>>> spam = ['cat', 'bat', 'rat']
```

* **index()** # return the index of the value in a list

  ```python
  >>> spam.index('hello')
  0
  ```

* **append()** # adds the argument to the end of the list

  ```python
  >>> spam.append('moose')
  >>> spam
  ['cat', 'dog', 'bat', 'moose']
  ```

* **insert()** # insert a value at any index in the list

  ```python
  >>> spam.insert(1, 'chicken')
  >>> spam
  ['cat', 'chicken', 'dog', 'bat']
  ```

* **remove()** # delete a value  from the list by  the value itself; If the value appears multiple times in the list, only the first instance of the value will be removed.

* **del()** # delete a value  from the list by index

  ```python
  >>> spam.remove('bat')
  >>> spam
  ['cat', 'rat']

  >>> del(spam[1])
  ['cat', 'rat']
  ```

* **[sort()](https://docs.python.org/3/library/stdtypes.html#list.sort)** # sort a list. You can also pass `True` for the `reverse` keyword argument to have `sort()` sort the values in reverse order.

  ```python
  >>> spam.sort()
  >>> spam
  ['bat', 'cat', 'rat']
  >>> spam.sort(reverse=True)
  >>> spam
  ['rat', 'cats', 'bat']
  ```

  If you need to sort the values in regular alphabetical order, pass `str. lower` for the `key` keyword argument in the `sort()` method call.

  ```python
  >>> spam = ['a', 'z', 'A', 'Z']
  >>> spam.sort(key=str.lower)
  >>> spam
  ['a', 'A', 'z', 'Z']
  ```

### **[Dictionary methods](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)**

*  **keys()**, **values()**, and **items()** 

  ```python
  >>> spam = {'color': 'red', 'age': 42}
  >>> for v in spam.values():
  		print(v, end=' ')
  red 42
  >>> for k in spam.keys():
          print(k, end=' ')
  color age
  >>> for i in spam.items():
          print(i, end=' ')
  ('color', 'red') ('age', 42)

  >>> spam.keys()
  dict_keys(['color', 'age'])
  >>> list(spam.keys())
  ['color', 'age']
  ```

* **get()** # this method that takes two arguments: the key of the value to retrieve and a fallback value to return if that key does not exist.

* **setdefault()** # The first argument passed to the method is the key to check for, and the second argument is the value to set at that key if the key does not exist. If the key does exist, the`setdefault()` method returns the key’s value. 

  ```python
  >>> spam = {'name': 'Pooka', 'age': 5}
  >>> spam.setdefault('color', 'black')
  'black'
  >>> spam.setdefault('color', 'white')
  'black'
  ```


### **[String methods](https://docs.python.org/3/library/stdtypes.html#string-methods)**

* **upper()** and **lower()** 、**isupper()** and **islower()**

* **isalpha()** returns `True` if the string consists only of letters and is not blank.

* **isalnum()** returns `True` if the string consists only of letters and numbers and is not blank.

* **isdecimal()** returns `True` if the string consists only of numeric characters and is not blank.

* **isspace()** returns `True` if the string consists only of spaces, tabs, and new-lines and is not blank.

* **istitle()** returns `True` if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.

* **startswith()** and **endswith()**

* **join()** # method is called on a string, gets passed a list of strings, and returns a string. The returned string is the concatenation of each string in the passed-in list.

  ```python
  >>> ', '.join(['cats', 'rats', 'bats'])
  'cats, rats, bats'
  ```

* **split()** # method calls on a string value and returns a list of strings. By default, the string  is split wherever whitespace characters such as the space, tab, or newline characters are found.

  ```python
  >>> 'My name is Simon'.split('m')
  ['My na', 'e is Si', 'on']
  ```

* **rjust()** and **ljust()** # string methods return a padded version of the string they are called on, with spaces inserted to justify the text. The first argument to both methods is an integer length for the justified string. 

  ```python
  >>> 'Hello'.rjust(10)
  '     Hello'
  >>> 'Hello'.rjust(20)
  '               Hello'
  ```

* **center()** # string method works like `ljust()` and `rjust()` but centers the text rather than justifying it to the left or right. 

  ```python
  >>> 'Hello'.center(20, '=')
  '=======Hello========'
  ```

* **strip()** # string method will return a new string without any whitespace characters at the beginning or end. The **lstrip()** and **rstrip()** methods will remove whitespace characters from the left and right ends.

  ```python
  >>> spam = '    Hello World     '
  >>> spam.strip()
  'Hello World'
  >>> spam.lstrip()
  'Hello World     '
  >>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
  >>> spam.strip('ampS')
  'BaconSpamEggs'
  ```


   The order of the characters in the string passed to `strip()` does not matter: `strip('ampS')` will do the same thing as `strip('mapS')` or `strip('Spam')`.

## import [re](https://docs.python.org/3/library/re.html) # *Regex functions* --very important and useful

* **re.compile()** # Passing a string value representing your regular expression to `re.compile()` returns a `Regex` pattern object .

  ```python
  >>> phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
  ```

  By passing `re.DOTALL` as the second argument to `re.compile()`, you can make the dot character match all characters, including the newline character.

  ```python
  >>> newlineRegex = re.compile('.*', re.DOTALL)
  >>> newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
  'Serve the public trust.\nProtect the innocent.\nUphold the law.'
  ```

  To make your regex case-insensitive, you can pass `re.IGNORECASE` or `re.I` as a second argument to `re.compile()`. 

  ```python
  >>> robocop = re.compile(r'robocop', re.I)
  >>> robocop.search('Robocop is part man.').group()
  'Robocop'
  ```

  To ignore whitespace and comments inside the regular expression string by passing the variable `re.VERBOSE` as the second argument to `re.compile()`.

  ```python
  phoneRegex = re.compile(r'''(
      (\d{3}|\(\d{3}\))?            # area code
      (\s|-|\.)?                    # separator
      \d{3}                         # first 3 digits
      (\s|-|\.)                     # separator
      \d{4}                         # last 4 digits
      (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
      )''', re.VERBOSE)
  ```

  All three options chose for the second argument will look like this:

  ```python
  >>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
  ```

* **search()** # searches the string it is passed for any matches to the regex, return a `Match` object of the *first* matched text in the searched string.

* **group()** # `Match`objects have a `group()` method that will return the actual matched text from the searched string. 

  ```python
  >>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
  >>> mo = phoneNumRegex.search('My number is 415-555-4242.')
  >>> mo.group(1)
  '415'
  >>> mo.group(2)
  '555-4242'
  >>> mo.group(0)
  '415-555-4242'
  >>> mo.group()
  '415-555-4242'
  ```

* **groups()** # If you would like to retrieve all the groups at once, use the `groups()` method—note the plural form for the name.

  ```python
  >>> mo.groups()
  ('415', '555-4242')
  ```

* **findall()** # will return the strings of *every* match in the searched string.`findall()` will not return a `Match` object but a list of strings.

  ```python
  >>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
  ['415-555-9999', '212-555-0000']
  ```


  If there *are* groups in the regular expression, then `findall()` will return a list of tuples. 

  ```python
  >>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
  >>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
  [('415', '555', '9999'), ('212', '555', '0000')]
  ```

* **sub()** # substitute new text in place of match patterns.The first argument is a string to replace any matches. The second is the string for the regular expression. The third optional argument `count` is the maximum number of pattern occurrences to be replaced. The `sub()` method returns a string with the substitutions applied.

  ```python
  >>> namesRegex = re.compile(r'Agent \w+')
  >>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret to Agent Bob.')
  'CENSORED gave the secret to CENSORED.'
  >>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret to Agent Bob.', 1)
  'CENSORED gave the secret to Agent Bob.'
  ```

## **import pyperclip** # *`copy()` and `paste()` functions that can send text to and receive text from your computer’s clipboard*

```python
>>> import pyperclip
>>> pyperclip.copy('Hello world!')
>>> pyperclip.paste()
'Hello world!'
```

Of course, if something outside of your program changes the clipboard contents, the `paste()` function will return it

## **import copy**  # *Shallow and deep copy operations*

* **copy()** and **deepcopy()** # when use `copy()`, the contains lists use references. If you need to copy contains lists, then use the `copy.deepcopy()` function instead of `copy.copy()`.

  ```python
  >>> import copy
  >>> origin = [1, 2, [3, 4]]
  >>> cop1 = copy.copy(origin)
  >>> cop2 = copy.deepcopy(origin)
  >>> origin[2][0] = "hey!" 
  >>> origin
  [1, 2, ['hey!', 4]]
  >>> cop1
  [1, 2, ['hey!', 4]]
  >>> cop2
  [1, 2, [3, 4]]
  ```

## **import pprint** # *pretty print*

These two lines are equivalent to each other:

```python
pprint.pprint(someDictionaryValue)
print(pprint.pformat(someDictionaryValue))
```

## import [os](https://docs.python.org/3/library/os.html) #  *Miscellaneous operating system interfaces*

* **os.path.join()** # pass it the string values of individual file and folder names in your path, `os.path.join()` will return a string with a file path using the correct path separators.

  ```python
  >>> os.path.join('C:\\Users\\asweigart', 'aaa.txt')
  'C:\\Users\\asweigart\\aaa.txt'
  ```

* **os.getcwd()** #  get the current working directory as a string value.

* **os.chdir()** # change the current working directory.

  ```python
  >>> os.getcwd()
  'C:\\Python34'
  >>> os.chdir('C:\\Windows\\System32')
  >>> os.getcwd()
  'C:\\Windows\\System32'
  ```

* **os.makedirs()** # create new folders (directories)

  ```python
  >>> os.makedirs('C:\\delicious\\walnut\\waffles')
  ```

**[os.path](https://docs.python.org/3/library/os.path.html)** # contains many helpful functions related to filenames and file paths

* **os.path.abspath(path)** # will return a string of the absolute path of the argument. This is an easy way to convert a relative path into an absolute one.

* **os.path.isabs(path)** # will return `True` if the argument is an absolute path and `False` if it is a relative path.

* **os.path.relpath(path, start)** # will return a string of a relative path from the *start* path to *path*. If *start* is not provided, the current working directory is used as the start path.

* **os.path.dirname(path)** # will return a string of everything that comes before the last slash in the `path` argument.

* **os.path.basename(path)** # will return a string of everything that comes after the last slash in the `path` argument.

  ```python
  >>> path = 'C:\\Windows\\System32\\calc.exe'
  >>> os.path.basename(path)
  'calc.exe'
  >>> os.path.dirname(path)
  'C:\\Windows\\System32'
  ```

* **os.path.split()** # get a tuple value with a path’s dir name and base name.

  ```python
  >>> calcFilePath = 'C:\\Windows\\System32\\calc.exe'
  >>> os.path.split(calcFilePath)
  ('C:\\Windows\\System32', 'calc.exe')
  ```

  use the `split()` string method and split on the string in `os.sep`. Recall from earlier that the `os.sep` variable is set to the correct folder-separating slash for the computer running the program.

  ```python
  >>> calcFilePath.split(os.path.sep)
  ['C:', 'Windows', 'System32', 'calc.exe']
  ```

* **os.path.getsize(path)** # will return the size in bytes of the file in the `path`argument.

* **os.listdir(path)** # will return a list of filename strings for each file in the `path` argument. (Note that this function is in the `os` module, not `os.path`.)

* **os.path.exists(path)** # will return `True` if the file or folder referred to in the argument exists and will return `False` if it does not exist.

* **os.path.isfile(path)** # will return `True` if the path argument exists and is a file and will return `False` otherwise.

* **os.path.isdir(path)** # will return `True` if the path argument exists and is a folder and will return `False` otherwise.

* **open()** # To open a file with the `open()` function, you pass it a string path indicating the file you want to open; it can be either an absolute or relative path. The `open()` function returns a `File` object.

  ```python
  >>> helloFile = open('/Users/your_home_folder/hello.txt')
  ```

  Pass `'w'` as the second argument to `open()` to open the file in write mode. Write mode will overwrite the existing file.  Append mode, on the other hand, will append text to the end of the existing file. 

  ```python
  baconFile = open('bacon.txt', 'w')
  ```

* **read()** # read the entire contents of a file as a string value.

* **readlines()** # get a `list` of string values from the file, one string for each line of text.

* **write()** # writes the string to the file and returns the number of characters written, including the newline.

* **close()** 

## import [shelve](https://docs.python.org/3/library/shelve.html) # *save variables in your Python programs to binary shelf files*

```python
>>> import shelve
>>> shelfFile = shelve.open('mydata')
>>> cats = ['Zophie', 'Pooka', 'Simon']
>>> shelfFile['cats'] = cats
>>> shelfFile.close()
```

```python
>>> shelfFile = shelve.open('mydata')
>>> list(shelfFile.keys())
['cats']
>>> list(shelfFile.values())
[['Zophie', 'Pooka', 'Simon']]
>>> shelfFile['cats']
['Zophie', 'Pooka', 'Simon']
>>> del shelfFile['cats']
>>> list(shelfFile.keys())
[]
>>> shelfFile.close()
```

## import [shutil](https://docs.python.org/3/library/shutil.html#module-shutil)  # *copy, move, rename, and delete files*

* **shutil.copy(source, destination)** # copy a single file and the return value is the path of the newly copied file.

    ```python
    >>> shutil.copy('C:\\spam.txt', 'C:\\delicious')
    'C:\\delicious\\spam.txt'
    >>> shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')
    'C:\\delicious\\eggs2.txt'
    ```

* **shutil.copytree(source, destination)** # copy an entire folder and every folder and file contained in it.

    ```python
    >>> shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
    'C:\\bacon_backup'
    ```

* **shutil.move(source, destination)** # move the file or folder at the path source to the path destination and will return a string of the absolute path of the new location，the folders that make up the destination must already exist.
    * _Note：But if there is no eggs folder, then move() will rename bacon.txt to a file named eggs without the .txt file extension._

    ```python
    >>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
    'C:\\eggs'
    ```

* **os.unlink(path)** # will delete the file at path.

* **os.rmdir(path)** # will delete the folder at path. This folder must be empty of any files or folders.

* **shutil.rmtree(path)** # will irreversibly  remove the folder at *path*, and all files and folders it contains will also be deleted.

* **send2trash.send2trash()**  # function to send folders and files to your computer’s trash or recycle bin instead of permanently deleting them by`import send2trash`

* **os.walk()** # The function is passed a single string value: the path of a folder.It can use in a `for` loop statement to walk a directory tree, much like how you can use the `range()` function to walk over a range of numbers.Unlike `range()`, the `os.walk()` function will return three values on each iteration through the loop:

    1. A string of the current folder’s name
    2. A list of strings of the folders in the current folder
    3. A list of strings of the files in the current folder

    ```python
    for folderName, subfolders, filenames in os.walk('C:\\delicious'):
        print('The current folder is ' + folderName)

        for subfolder in subfolders:
            print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
        for filename in filenames:
            print('FILE INSIDE ' + folderName + ': '+ filename)
    ```

**import [zipfile](https://docs.python.org/3/library/zipfile.html)**  # Work with ZIP archives

* **zipfile.ZipFile()** # To create a `ZipFile` object, call the  function, passing it a string of the *.zip* file’s filename.like `open()`,after`close()` all changes will be saved.

  ```python
  >>> exampleZip = zipfile.ZipFile('example.zip')
  >>> exampleZip.namelist()
  >>> pam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
  >>> spamInfo = exampleZip.getinfo('spam.txt')
  >>> spamInfo.file_size
  >>> 13908
  >>> spamInfo.compress_size
  >>> 3828
  >>> exampleZip.close()
  ```


  To create your own compressed ZIP files, you must open the `ZipFile` object in *write mode* by passing `'w'` as the second argument.

  ```python
  >>> newZip = zipfile.ZipFile('new.zip', 'w')
  >>> newZip.write('spam.txt', compress_type = zipfile.ZIP_DEFLATED)
  ```

   If you want to simply add files to an existing ZIP file, pass `'a'`as the second argument to `zipfile.`

* **extractall()** # method for `ZipFile` objects extracts all the files and folders from a ZIP file into the current working directory.

  ```python
  >>> exampleZip.extractall()
  ```

  Optionally, you can pass a folder name to `extractall()` to have it extract the files into a folder.

  ```python
  >>> exampleZip.extractall('C:\\ delicious')
  ```

* **extract()** # method for `ZipFile` objects will extract a single file from the ZIP file. 

  ```python
  >>> exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
  'C:\\some\\new\\folders\\spam.txt'
  ```


## import webbrowser # *opens a browser to a specific page*

```python
>>> import webbrowser
>>> webbrowser.open('http://inventwithpython.com/')
```

## import [requests](http://requests.readthedocs.io/en/master/) # *easily download files from the Web*

* **requests.get()** # function takes a string of a URL to download and returns a `Response` object which contains the response that the web server gave for your request.

  ```python
  >>> import requests
  >>> res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
  >>> type(res)
  <class 'requests.models.Response'>
  >>> res.status_code == requests.codes.ok
  True
  >>> res.headers['content-type']
  'text/plain'
  >>> res.encoding
  'ISO-8859-1'
  >>> res.apparent_encoding
  'UTF-8-SIG'
  >>> len(res.text)
  178981
  >>> print(res.text[:250])
  ...
  ```
  > 遇到`res.text`乱码可以使用如下类似方法解决：
  >
  > ```python
  > res.text.encode('ISO-8859-1').decode('UTF-8')
  > ```
  >
  > 参考：[python3的requests类抓取中文页面出现乱码](http://blog.csdn.net/gyy823/article/details/51678991)
  >
  > [[爬虫requests爬去网页乱码问题](http://www.cnblogs.com/laolv/p/7397429.html)]

* **raise_for_status()** # This will raise an exception if there was an error downloading the file and will do nothing if the download succeeded. 

  ```python
  >>> res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
  >>> res.raise_for_status()
  Traceback (most recent call last):
  ...
  ```

  Always call `raise_for_status()` after calling `requests.get()`. 

* **open()** and **write()** # you can save the web page to a file on your hard drive with the standard `open()` function and `write()` method. There are some slight differences. First, you must open the file in *write binary* mode by passing the string `'wb'` as the second argument to `open()`. Even if the page is in plaintext , you need to write binary data instead of text data in order to maintain the *Unicode encoding* of the text.

  To write the web page to a file, you can use a `for` loop with the `Response` object’s `iter_content()` method.

  ```python
  >>> res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
  >>> res.raise_for_status()
  >>> playFile = open('RomeoAndJuliet.txt', 'wb')
  >>> for chunk in res.iter_content(100000):
          playFile.write(chunk)

  100000
  78981
  >>> playFile.close()
  ```

## import [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/) # *extracting information from an HTML page（can't not use regex）*

* **bs4.BeautifulSoup()** # function needs to be called with a string containing the HTML it will parse and returns  a `BeautifulSoup` object. 

  ```python
  >>> import requests, bs4
  >>> res = requests.get('http://nostarch.com')
  >>> res.raise_for_status()
  >>> noStarchSoup = bs4.BeautifulSoup(res.text)
  >>> type(noStarchSoup)
  <class 'bs4.BeautifulSoup'>
  ```

  ```python
  >>> exampleFile = open('example.html')
  >>> exampleSoup = bs4.BeautifulSoup(exampleFile)
  >>> type(exampleSoup)
  <class 'bs4.BeautifulSoup'>
  ```

* **select()** # passing a string of a [CSS *selector*](http://www.w3school.com.cn/cssref/css_selectors.asp) to find the element you are looking for and return a **list** of `Tag` objects. Calling `getText()` on the element returns the element’s text, or inner HTML. Tag values also have an `attrs` attribute that shows all the HTML attributes of the tag as a dictionary.

  ```python
  >>> import bs4
  >>> exampleFile = open('example.html')
  >>> exampleSoup = bs4.BeautifulSoup(exampleFile.read())
  >>> elems = exampleSoup.select('#author')
  >>> type(elems)
  <class 'list'>
  >>> type(elems[0])
  <class 'bs4.element.Tag'>
  >>> elems[0].getText()
  'Al Sweigart'
  >>> str(elems[0])
  '<span id="author">Al Sweigart</span>'
  >>> elems[0].attrs
  {'id': 'author'}
  ```

* **get()** # The `get()` method for `Tag` objects makes it simple to access attribute values from an element. The method is passed a string of an attribute name and returns that attribute’s value. 

  ```python
  >>> elems[0].get('id')
  'author'
  ```


## from selenium import webdriver # *lets Python directly control the browser by programmatically clicking links and filling in login information*

Because it launches a web browser, it is a bit slower and hard to run in the **background** if, say, you just need to download some files from the Web.

* **webdriver._driver_()** # When `webdriver.driver()` is called, the web browser starts up. Calling `type()` on the value `webdriver.driver()` reveals it’s of the `WebDriver` data type. 

```python
>>> from selenium import webdriver
>>> browser = webdriver.Firefox()
>>> type(browser)
<class 'selenium.webdriver.firefox.webdriver.WebDriver'>
>>> browser.get('http://inventwithpython.com')
```

* **find_element_\*** and **find_elements_\*** # The `find_element_*`methods return a single `WebElement` object, representing the first element on the page that matches your query. The `find_elements_*` methods return a list of `WebElement_*` objects for *every* matching element on the page.

Once you have the `WebElement` object, you can find out more about it by reading the attributes or calling the methods in the table:

| Attribute or method       | Description                                                  |
| ------------------------- | ------------------------------------------------------------ |
| `tag_name`                | The tag name, such as `'a'` for an `<a>` element             |
| `get_attribute(`*name*`)` | The value for the element’s `name` attribute                 |
| `text`                    | The text within the element, such as `'hello'` in `<span>hello</span>` |
| `clear()`                 | For text field or text area elements, clears the text typed into it |
| `is_displayed()`          | Returns `True` if the element is visible; otherwise returns `False` |
| `is_enabled()`            | For input elements, returns `True` if the element is enabled; otherwise returns `False` |
| `is_selected()`           | For checkbox or radio button elements, returns `True` if the element is selected; otherwise returns `False` |
| `location`                | A dictionary with keys `'x'` and `'y'` for the position of the element in the page |

* **click()** # This method can be used to follow a link, make a selection on a radio button, click a Submit button, or trigger whatever else might happen when the element is clicked by the mouse.
* **send_keys()** # Sending keystrokes to text fields on a web page.
* **submit()** # Calling this method on any element will have the same result as clicking the Submit button for the form that element is in.
* **browser.back()** # Clicks the Back button.
* **browser.forward()** # Clicks the Forward button.
* **browser.refresh()** # Clicks the Refresh/Reload button.
* **browser.quit()** # Clicks the Close Window button.

## import [openpyxl](http://openpyxl.readthedocs.io/en/stable/) # *read/write Excel 2010 xlsx/xlsm files*

* **openpyxl.load_workbook()** # takes in the filename and returns a value of the `workbook` data type

  ```python
  >>> import openpyxl
  >>> wb = openpyxl.load_workbook('example.xlsx')
  >>> type(wb)
  <class 'openpyxl.workbook.workbook.Workbook'>
  ```

* **get sheet**: wb[*sheetname*]  .title  .active

  ```python
  >>> wb.sheetnames
  ['Sheet1', 'Sheet2', 'Sheet3']
  >>> sheet = wb['Sheet3']
  >>> sheet
  <Worksheet "Sheet3">
  >>> type(sheet) 
  <class 'openpyxl.worksheet.worksheet.Worksheet'>
  >>> sheet.title
  'Sheet3'
  >>> anotherSheet = wb.active
  >>> anotherSheet
  <Worksheet "Sheet1">
  ```

* **get cell**: sheet[*coordinate*] .row  .column  .coordinate .max_

* **write and save**

  ```python
  >>> sheet = wb['Sheet1']
  >>> sheet['A1']
  <Cell Sheet1.A1>
  >>> sheet['A1'].value
  datetime.datetime(2015, 4, 5, 13, 34, 2)
  >>> c = sheet['B1']
  >>> 'Row ' + str(c.row) + ', Column ' + c.column + ' is ' + c.value
  'Row 1, Column B is Apples'
  >>> 'Cell ' + c.coordinate + ' is ' + c.value
  'Cell B1 is Apples'
  >>> sheet.cell(row=1, column=2).value
  'Apples'
  >>> sheet.max_row
  7
  >>> sheet.max_column
  3
  >>> sheet['B1'] = 'banana'
  >>> sheet['B1']
  'banana'
  >>> wb.save('updateExample.xlsx')
  ```

* **openpyxl.cell.column_index_from_string()** # convert from letters to numbers

* **openpyxl.cell.get_column_letter()** # convert from numbers to letters

  ```python
  >>> import openpyxl
  >>> from openpyxl.cell import get_column_letter, column_index_from_string
  >>> wb = openpyxl.load_workbook('example.xlsx')
  >>> sheet = wb['Sheet1']
  >>> get_column_letter(sheet.max_column)
  'C'
  >>> column_index_from_string('AA')
  27
  ```

* Getting **Rows** and **Columns** from the Sheets(tuples)

  ```python
  >>> import openpyxl
  >>> wb = openpyxl.load_workbook('example.xlsx')
  >>> sheet = wb['Sheet1']
  >>> sheet['A1':'B2']
  ((<Cell Sheet1.A1>, <Cell Sheet1.B1>), (<Cell Sheet1.A2>,<Cell Sheet1.B2>))
  >>> sheet.columns[1]
  (<Cell Sheet1.B1>, <Cell Sheet1.B2>, <Cell Sheet1.B3>, <Cell Sheet1.B4>,
  <Cell Sheet1.B5>, <Cell Sheet1.B6>, <Cell Sheet1.B7>)
  >>> for rowOfCellObjects in sheet['A1':'B2']:
          for cellObj in rowOfCellObjects:
              print(cellObj.coordinate, cellObj.value)
          
  A1 2015-04-05 13:34:02
  B1 Apples
  A2 2015-04-05 03:41:23
  B2 Cherries
  ```

* **Font** # Setting the Font Style of Cells

  ```python
  >>> import openpyxl
  >>> from openpyxl.styles import Font
  >>> wb = openpyxl.Workbook()
  >>> sheet = wb.get_sheet_by_name('Sheet')
  >>> italic24Font = Font(size=24, italic=True)
  >>> sheet['A1'].font = italic24Font
  >>> sheet['A1'] = 100
  >>> sheet['A2'] = 200
  >>> sheet['A3'] = 'SUM(A1:A2)'
  >>> wb.save('styled.xlsx')
  ```

  | Keyword argument | Data type | Description                                               |
  | ---------------- | --------- | --------------------------------------------------------- |
  | `name`           | String    | The font name, such as `'Calibri'` or `'Times New Roman'` |
  | `size`           | Integer   | The point size                                            |
  | `bold`           | Boolean   | `True`, for bold font                                     |
  | `italic`         | Boolean   | `True`, for italic font                                   |

* Row **Height** and Column **Width**

  ```python
  >>> sheet.row_dimensions[1].height = 70
  >>> sheet.column_dimensions['B'].width = 20
  ```

* **Merging and Unmerging Cells** # 合并单元格

  ```python
  >>> sheet.merge_cells('A1:D3')
  >>> sheet['A1'] = 'Twelve cells merged together.'
  >>> sheet.unmerge_cells('A1:D3')
  ```

* **Freeze Panes**

  | `freeze_panes` setting                                     | Rows and columns frozen   |
  | ---------------------------------------------------------- | ------------------------- |
  | `sheet.freeze_panes = 'A2'`                                | Row 1                     |
  | `sheet.freeze_panes = 'B1'`                                | Column A                  |
  | `sheet.freeze_panes = 'C1'`                                | Columns A and B           |
  | `sheet.freeze_panes = 'C2'`                                | Row 1 and columns A and B |
  | `sheet.freeze_panes = 'A1'` or `sheet.freeze_panes = None` | No frozen panes           |

* **charts**

  To make a chart, you need to do the following:

  1. Create a `Reference` object from a rectangular selection of cells.
  2. Create a `Series` object by passing in the `Reference` object.
  3. Create a `Chart` object.
  4. Append the `Series` object to the `Chart` object.
  5. Add the `Chart` object to the `Worksheet` object, optionally specifying which cell the top left corner of the chart should be positioned.

  ```python
  >>> import openpyxl
  >>> wb = openpyxl.Workbook()
  >>> sheet = wb.active
  >>> for i in range(1, 11):         # create some data in column A
          sheet['A' + str(i)] = i

  >>> refObj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)

  >>> seriesObj = openpyxl.chart.Series(refObj, title='First series')
  >>> chartObj = openpyxl.chart.BarChart() # chart style
  >>> chartObj.title = 'My Chart'
  >>> chartObj.append(seriesObj)
  >>> sheet.add_chart(chartObj, 'C5')
  >>> wb.save('sampleChart.xlsx')
  ```

  **Unfortunately, in the current version of OpenPyXL (2.3.3), the `load_workbook()`function does not load charts in Excel files.**


## import PyPDF2 #  *interact with PDFs  documents*

* Extracting Text

  ```python
  >>> import PyPDF2
  >>> pdfFileObj = open('meetingminutes.pdf', 'rb')
  >>> pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
  >>> pdfReader.numPages
  19
  >>> pageObj = pdfReader.getPage(0)
  >>> pageObj.extractText()
  'OOFFFFIICCIIAALL BBOOAARRDD MMIINNUUTTEESS Meeting of March 7, 2015...
  ```

* **decrypt()** # *encrypted with the password*

  ```python
  >>> import PyPDF2
  >>> pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
  >>> pdfReader.isEncrypted
  True
  >>> pdfReader.getPage(0)
  Traceback (most recent call last):
  ...
  >>> pdfReader.decrypt('rosebud')
  1
  >>> pageObj = pdfReader.getPage(0)
  ```

* **creating PDFs** 

  ```python
  >>> import PyPDF2
  >>> pdf1File = open('meetingminutes.pdf', 'rb')
  >>> pdf2File = open('meetingminutes2.pdf', 'rb')
  >>> pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
  >>> pdf2Reader = PyPDF2.PdfFileReader(pdf2File)
  >>> pdfWriter = PyPDF2.PdfFileWriter()

  >>> for pageNum in range(pdf1Reader.numPages):
          pageObj = pdf1Reader.getPage(pageNum)
          pdfWriter.addPage(pageObj)

  >>> for pageNum in range(pdf2Reader.numPages):
          pageObj = pdf2Reader.getPage(pageNum)
          pdfWriter.addPage(pageObj)

  >>> pdfOutputFile = open('combinedminutes.pdf', 'wb')
  >>> pdfWriter.write(pdfOutputFile)
  >>> pdfOutputFile.close()
  >>> pdf1File.close()
  >>> pdf2File.close()
  ```

  > PyPDF2 cannot insert pages in the middle of a `PdfFileWriter` object; the `addPage()` method will only add pages to the end.

* **rotateClockwise()** and **rotateCounterClockwise()** # *旋转*

  ```python
  >>> page = pdfReader.getPage(0)
  >>> page.rotateClockwise(90)
  ```

* **mergePage()** # *overlay the contents of one page over another*

  ```python
  >>> minutesFile = open('meetingminutes.pdf', 'rb')
  >>> pdfReader = PyPDF2.PdfFileReader(minutesFile)
  >>> minutesFirstPage = pdfReader.getPage(0)
  >>> pdfWatermarkReader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))
  >>> minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))

  >>> for pageNum in range(1, pdfReader.numPages):
          pageObj = pdfReader.getPage(pageNum)
          pdfWriter.addPage(pageObj)
  >>> resultPdfFile = open('watermarkedCover.pdf', 'wb')
  >>> pdfWriter.write(resultPdfFile)
  >>> minutesFile.close()
  >>> resultPdfFile.close()
  ```

* **encrypt()** # add encryption Before calling the `write()` method to save to a file

  ```python
  >>> pdfWriter.encrypt('swordfish')
  ```

## import docx(pip install python-docx)

* Reading Word Documents # Document paragraphs runs .text

  ```python
  >>> import docx
  >>> doc = docx.Document('demo.docx')
  >>> len(doc.paragraphs)
  7
  >>> doc.paragraphs[0].text
  'Document Title'
  >>> doc.paragraphs[1].text
  'A plain paragraph with some bold and some italic'
  >>> len(doc.paragraphs[1].runs)
  4
  >>> doc.paragraphs[1].runs[3].text
  'italic'
  ```

* **style**

  When using a linked style for a `Run` object, you will need to add `'Char'` to the end of its name. For example, to set the Quote linked style for a `Paragraph` object, you would use `paragraphObj.style = 'Quote'`, but for a `Run` object, you would use `runObj.style = 'QuoteChar'`.

  Runs can be further styled using `text` attributes. Each attribute can be set to one of three values: `True` (the attribute is always enabled, no matter what other styles are applied to the run), `False` (the attribute is always disabled), or `None` (defaults to whatever the run’s style is set to).

  | Attribute       | Description                                                  |
  | --------------- | ------------------------------------------------------------ |
  | `bold`          | The text appears in bold.                                    |
  | `italic`        | The text appears in italic.                                  |
  | `underline`     | The text is underlined.                                      |
  | `strike`        | The text appears with strikethrough.                         |
  | `double_strike` | The text appears with double strikethrough.                  |
  | `all_caps`      | The text appears in capital letters.                         |
  | `small_caps`    | The text appears in capital letters, with lowercase letters two points smaller. |
  | `shadow`        | The text appears with a shadow.                              |
  | `outline`       | The text appears outlined rather than solid.                 |
  | `rtl`           | The text is written right-to-left.                           |
  | `imprint`       | The text appears pressed into the page.                      |
  | emboss          | The text appears raised off the page in relief.              |

  ```python
  >>> doc = docx.Document('demo.docx')
  >>> doc.paragraphs[0].style
  'Title'
  >>> doc.paragraphs[0].style = 'Normal'
  >>> doc.paragraphs[1].runs[0].style = 'QuoteChar'
  >>> doc.paragraphs[1].runs[1].underline = True
  >>> doc.save('restyled.docx')
  ```

  **Writing Word Documents**

* **add_paragraph()** and **add_run()** # Both `add_paragraph()` and `add_run()` accept an optional second argument that is a string of the `Paragraph` or `Run` object’s style.

  ```python
  >>> import docx
  >>> doc = docx.Document()
  >>> doc.add_paragraph('Hello world!', 'Title')
  <docx.text.Paragraph object at 0x000000000366AD30>
  >>> paraObj1 = doc.add_paragraph('This is a second paragraph.')
  >>> paraObj2 = doc.add_paragraph('This is a yet another paragraph.')
  >>> paraObj1.add_run(' This text is being added to the second paragraph.')
  <docx.text.Run object at 0x0000000003A2C860>
  >>> doc.save('multipleParagraphs.docx')
  ```

* **add_heading()** # The arguments to `add_heading()` are a string of the heading text and an integer from `0` to `4` for various heading levels.

  ```python
  >>> doc = docx.Document()
  >>> doc.add_heading('Header 0', 0)
  <docx.text.Paragraph object at 0x00000000036CB3C8>
  >>> doc.add_heading('Header 4', 4)
  <docx.text.Paragraph object at 0x00000000036CB3C8>
  ```

* **add_break()** # add a line break. If you want to add a page break instead, you need to pass the value `docx.text.WD_BREAK.PAGE`.

  ```python
  >>> doc.paragraphs[0].add_break(docx.enum.text.WD_BREAK.PAGE)
  >>> doc.add_paragraph('This is on the second page!')
  ```

* **add_picture()**

  ```python
  >>> doc.add_picture('zophie.png', width=docx.shared.Inches(1),
  height=docx.shared.Cm(4))
  ```

## import csv

* **csv.reader()**

  ```python
  >>> import csv
  >>> exampleFile = open('example.csv')
  >>> exampleReader = csv.reader(exampleFile)
  >>> list(exampleReader)
  [['4/5/2015 13:34', 'Apples', '73'], ['4/5/2015 3:41', 'Cherries', '85']...
  >>> for row in exampleReader:
          print('Row #' + str(exampleReader.line_num) + ' ' + str(row))

  Row #1 ['4/5/2015 13:34', 'Apples', '73']
  ```

* **csv.writer()**

  ```python
  >>> import csv
  >>> outputFile = open('output.csv', 'w', newline='')
  >>> outputWriter = csv.writer(outputFile)
  >>> outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
  21
  >>> outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
  32
  >>> outputWriter.writerow([1, 2, 3.141592, 4])
  16
  >>> outputFile.close()
  ```

  > If you forget the `newline=''` keyword argument in `open()`, the CSV file will be double-spaced（空一行）.

  **delimiter** and **lineterminator** Keyword Arguments:  The *delimiter* is the character that appears between cells on a row. By default, the delimiter for a CSV file is a comma. The *line terminator* is the character that comes at the end of a row. By default, the line terminator is a newline.

  ```python
  >>> csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
  ```


## import json

* **json.loads()** # translate a string containing JSON data into a Python value

  ```python
  >>> stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
  >>> import json
  >>> jsonDataAsPythonValue = json.loads(stringOfJsonData)
  >>> jsonDataAsPythonValue
  {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
  ```

* **json.dumps()**  # translate a Python value into a string of JSON-formatted data

  ```python
  >>> pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
  >>> import json
  >>> stringOfJsonData = json.dumps(pythonValue)
  >>> stringOfJsonData
  '{"isCat": true, "felineIQ": null, "miceCaught": 0, "name": "Zophie" }'
  ```

## import time 

* **time.time()** # returns the number of seconds since 19700101 12AM as a float value.

  ```python
  >>> time.time()
  1425063955.068649
  ```

* **time.sleep()** 

  > that pressing CTRL-C will not interrupt `time.sleep()` calls in IDLE. IDLE waits until the entire pause is over before raising the `KeyboardInterrupt` exception.

## import datatime

* **datetime.datetime() ** # returns a `datetime` object of the moment specified by the arguments

* **datetime.datetime.now()** 

  ```python
  >>> import datetime
  >>> datetime.datetime.now()
  datetime.datetime(2015, 2, 27, 11, 10, 49, 55, 53)
  >>> dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
  >>> dt.year, dt.month, dt.day
  (2015, 10, 21)
  >>> dt.hour, dt.minute, dt.second
  (16, 29, 0)
  ```


* **datetime.datetime.fromtimestamp()** # convert a Unix epoch timestamp to a `datetime` object

  ```python
  >>> datetime.datetime.fromtimestamp(time.time())
  datetime.datetime(2018, 1, 1, 14, 32, 0, 604980)

  # Pausing Until a Specific Date
  >>> while datetime.datetime.now() < halloween2016:
          time.sleep(1)
  ```

* **datetime.timedelta()** #  represents a *duration* of time. It takes keyword arguments `weeks`, `days`, `hours`, `minutes`, `seconds`, `milliseconds`, and `microseconds`, no `month` or `year`.

  ```python
  >>> delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
  >>> delta.days, delta.seconds, delta.microseconds
  (11, 36548, 0)
  >>> delta.total_seconds()
  986948.0
  >>> str(delta)
  '11 days, 10:09:08'

  >>> datetime.datetime.now() + delta
  datetime.datetime(2018, 3, 20, 18, 38, 50, 636181)
  ```

* **strftime()**

  | strftime directive | Meaning                                               |
  | ------------------ | ----------------------------------------------------- |
  | `%Y`               | Year with century, as in `'2014'`                     |
  | `%y`               | Year without century, `'00'` to `'99'` (1970 to 2069) |
  | `%m`               | Month as a decimal number, `'01'` to `'12'`           |
  | `%B`               | Full month name, as in `'November'`                   |
  | `%b`               | Abbreviated month name, as in `'Nov'`                 |
  | `%d`               | Day of the month, `'01'` to `'31'`                    |
  | `%j`               | Day of the year, `'001'` to `'366'`                   |
  | `%w`               | Day of the week, `'0'` (Sunday) to `'6'` (Saturday)   |
  | `%A`               | Full weekday name, as in `'Monday'`                   |
  | `%a`               | Abbreviated weekday name, as in `'Mon'`               |
  | `%H`               | Hour (24-hour clock), `'00'` to `'23'`                |
  | `%I`               | Hour (12-hour clock), `'01'` to `'12'`                |
  | `%M`               | Minute, `'00'` to `'59'`                              |
  | `%S`               | Second, `'00'` to `'59'`                              |
  | `%p`               | `'AM'` or `'PM'`                                      |
  | `%%`               | Literal `'%'` character                               |

  ```python
  >>> oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
  >>> oct21st.strftime('%Y/%m/%d %H:%M:%S')
  '2015/10/21 16:29:00'
  >>> oct21st.strftime('%I:%M %p')
  '04:29 PM'
  >>> oct21st.strftime("%B of '%y")
  "October of '15"
  ```

* **datetime.datetime.strptime()** # convert a string of date information to a `datetime` object.

  ```python
  >>> datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
  datetime.datetime(2015, 10, 21, 0, 0)
  >>> datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
  datetime.datetime(2015, 10, 21, 16, 29)
  ```

## import threading 

* **threading.Thread()**  # To create a `Thread`object

  ```python
  import threading, time
  print('Start of program.')

  def takeANap():
      time.sleep(5)
      print('Wake up!')

  threadObj = threading.Thread(target=takeANap)
  threadObj.start()

  print('End of program.')
  ```

  If the target function you want to run in the new thread takes arguments, you can pass the target function’s arguments to `threading.Thread()`. The regular arguments can be passed as a list to the `args` keyword argument. The keyword argument can be specified as a dictionary to the `kwargs` keyword argument.

  ```python
  >>> import threading
  >>> threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'],
  kwargs={'sep': ' & '})
  >>> threadObj.start()
  Cats & Dogs & Frogs
  ```

* **join()** # Say there’s some code you don’t want to run in the main thread until all the threads have completed. Calling a `Thread` object’s `join()` method will block until that thread has finished. 

  ```python
  for downloadThread in downloadThreads:
      downloadThread.join()
  print('Done.')
  ```

## import subprocess

* **subprocess.Popen()** 

  ```python
  >>> import subprocess
  >>> subprocess.Popen('calc.exe')
  <subprocess.Popen object at 0x0000000003055A58>
  ```
  You can pass command line arguments to processes you create with `Popen()`. To do so, you pass a list as the sole argument to `Popen()`.

  ```python
  >>> subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\hello.txt'])
  <subprocess.Popen object at 0x00000000032DCEB8>
  ```

  Each operating system has a program that performs the equivalent of double-clicking a document file to open it. On Windows, this is the `start` program. On OS X, this is the `open` program. On Ubuntu Linux, this is the `see` program.

  ```python
  >>> subprocess.Popen(['start', 'hello.txt'], shell=True)
  ```

*  **poll()** # the `poll()` method as asking your friend if she’s finished running the code you gave her. It will return `None` if the process is still running at the time `poll()` is called. If the program has terminated, it will return the process’s integer *exit code*.

* **wait()** # The `wait()` method is like waiting for your friend to finish working on her code before you keep working on yours. The `wait()` method will block until the launched process has terminated.

  ```python
  >>> calcProc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')
  >>> calcProc.poll() == None
  True
  >>> calcProc.wait()
  0	# after close the calc
  >>> calcProc.poll()
  0
  ```


## import smtplib # *send email*

* **smptlib.SMTP()** # connect 

  ```python
  >>> import smtplib
  >>> smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
  >>> type(smtpObj)
  <class 'smtplib.SMTP'>
  ```

  If the `smptlib.SMTP()` call is not successful, your SMTP server might not support TLS on port 587. In this case, you will need to create an `SMTP` object using `smtplib.SMTP_SSL()` and port 465 instead.

  ```python
  >>> smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  ```

* **ehlo()** # “say hello” to the SMTP email server. Just be sure to call the `ehlo()` method first thing after getting the `SMTP` object or else the later method calls will result in errors. （必要的握手）

  ```python
  >>> smtpObj.ehlo()
  (250, b'mx.google.com at your service, [216.172.148.131]\nSIZE 35882577\
  n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')
  ```

* **starttls()** # If you are connecting to port 587 on the SMTP server (that is, you’re using TLS encryption), you’ll need to call the `starttls()` method next. This required step enables encryption for your connection. If you are connecting to port 465 (using SSL), then encryption is already set up, and you should skip this step.

  ```python
  >>> smtpObj.starttls()
  (220, b'2.0.0 Ready to start TLS')
  ```

  `starttls()` puts your SMTP connection in TLS mode. The `220` in the return value tells you that the server is ready.

* **login()**

  ```python
  >>> smtpObj.login(' my_email_address@gmail.com ', ' MY_SECRET_PASSWORD ')
  (235, b'2.7.0 Accepted')
  ```

* **sendmail()**

  ```python
  >>> smtpObj.sendmail(' my_email_address@gmail.com ', ' recipient@example.com ','Subject: title\nDear Alice,...')
  {}
  ```

* **quit()**

  ```python
  >>> smtpObj.quit()
  (221, b'2.0.0 closing connection ko10sm23097611pbd.52 - gsmtp')
  ```

## import [imapclient](http://imapclient.readthedocs.io/en/master/), [pyzmail](http://www.magiksys.net/pyzmail/) (*use `easy_install pyzmail`*) # receive

```python
>>> import imapclient
>>> imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
>>> imapObj.login(' my_email_address@gmail.com ', ' MY_SECRET_PASSWORD ')
'my_email_address@gmail.com Jane Doe authenticated (Success)'
# you can use imapObj.list_folders() ...
>>> imapObj.select_folder('INBOX', readonly=True)
>>> UIDs = imapObj.search(['SINCE 05-Jul-2014'])
>>> UIDs
[40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]
>>> rawMessages = imapObj.fetch([40041], ['BODY[]', 'FLAGS'])
>>> import pyzmail
>>> message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
>>> message.get_subject()
'Hello!'
>>> message.get_addresses('from')
[('Edward Snowden', 'esnowden@nsa.gov')]
>>> message.get_addresses('to')
[(Jane Doe', 'jdoe@example.com')]
>>> message.get_addresses('cc')
[]
>>> message.get_addresses('bcc')
[]
>>> message.text_part != None
True
>>> message.text_part.get_payload().decode(message.text_part.charset)
'So long, and thanks for all the fish!\r\n\r\n-Al\r\n'
>>> message.html_part != None
True
>>> message.html_part.get_payload().decode(message.html_part.charset)
'<div dir="ltr"><div>So long, and thanks for all the fish!<br><br></div>-Al<br></div>\r\n'
>>> imapObj.logout()
```

* **search()** # The `search()` method doesn’t return the emails themselves but rather unique IDs (UIDs) for the emails, as integer values. You can then pass these UIDs to the `fetch()` method to obtain the email content.

  | Search key                                                   | Meaning                                                      |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | `'ALL'`                                                      | Returns all messages in the folder. You may run in to `imaplib` size limits if you request all the messages in a large folder. See [Size Limits](https://automatetheboringstuff.com/chapter16/#calibre_link-50). |
  | `'BEFORE`*date'*, `'ON`*date'*, `'SINCE` *date'*             | These three search keys return, respectively, messages that were received by the IMAP server before, on, or after the given *date*. The date must be formatted like `05-Jul-2015`. Also, while `'SINCE 05-Jul-2015'` will match messages on and after July 5, `'BEFORE 05-Jul-2015'` will match only messages before July 5 but not on July 5 itself. |
  | `'SUBJECT`*string'*, `'BODY`*string'*, `'TEXT`*string'*      | Returns messages where *string* is found in the subject, body, or either, respectively. If *string* has spaces in it, then enclose it with double quotes: `'TEXT "search with spaces"'`. |
  | `'FROM`*string'*, `'TO`*string'*, `'CC`*string'*, `'BCC` *string'* | Returns all messages where *string* is found in the “from” emailaddress, “to” addresses, “cc” (carbon copy) addresses, or “bcc” (blind carbon copy) addresses, respectively. If there are multiple email addresses in *string*, then separate them with spaces and enclose them all with double quotes: `'CC` *"firstcc@example.com secondcc@example.com"'*. |
  | `'SEEN'`, `'UNSEEN'`                                         | Returns all messages with and without the *\Seen* flag, respectively. An email obtains the *\Seen* flag if it has been accessed with a `fetch()`method call (described later) or if it is clicked when you’re checking your email in an email program or web browser. It’s more common to say the email has been “read” rather than “seen,” but they mean the same thing. |
  | `'ANSWERED'`, `'UNANSWERED'`                                 | Returns all messages with and without the *\Answered* flag, respectively. A message obtains the *\Answered* flag when it is replied to. |
  | `'DELETED'`, `'UNDELETED'`                                   | Returns all messages with and without the *\Deleted* flag, respectively. Email messages deleted with the `delete_messages()` method are given the *\Deleted* flag but are not permanently deleted until the `expunge()`method is called (see [Deleting Emails](https://automatetheboringstuff.com/chapter16/#calibre_link-51)). Note that some email providers, such as Gmail, automatically expunge emails. |
  | `'DRAFT'`, `'UNDRAFT'`                                       | Returns all messages with and without the *\Draft* flag, respectively. Draft messages are usually kept in a separate `Drafts` folder rather than in the `INBOX` folder. |
  | `'FLAGGED'`, `'UNFLAGGED'`                                   | Returns all messages with and without the *\Flagged* flag, respectively. This flag is usually used to mark email messages as “Important” or “Urgent.” |
  | `'LARGER` *N'*, `'SMALLER` *N'*                              | Returns all messages larger or smaller than *N* bytes, respectively. |
  | `'NOT` *search-key'*                                         | Returns the messages that *search-key* would *not* have returned. |
  | `'OR` *search-key1 search-key2'*                             | Returns the messages that match *either* the first or second *search-key*. |

  * **imapObj.search(['SINCE 01-Jan-2015', 'NOT FROM alice@example.com'])**. Returns every message sent from everyone except *alice@example.com* since the start of 2015.
  * **imapObj.search(['OR FROM alice@example.com FROM bob@example.com'])**. Returns every message ever sent from *alice@example.com* or *bob@example.com*.

* **delete_messages()**

  ```python
  >>> UIDs = imapObj.search(['ON 09-Jul-2015'])
  >>> UIDs
  [40066]
  >>> imapObj.delete_messages(UIDs)
  {40066: ('\\Seen', '\\Deleted')}
  >>> imapObj.expunge()
  ('Success', [(5452, 'EXISTS')])
  ```

## import [pillow](http://pillow.readthedocs.io/en/latest/) # *Python Imaging Library* 

* **ImageColor.getcolor()** # This function takes a color name string as its first argument, and the string `'RGBA'` as its second argument, and it returns an RGBA tuple.

  ```python
  >>> from PIL import ImageColor
  >>> ImageColor.getcolor('RED', 'RGBA')
  (255, 0, 0, 255)
  ```

* Working with the Image Data Type # `from PIL import Image`

  ```python
  >>> from PIL import Image
  >>> catIm = Image.open('zophie.png')
  >>> catIm.size
  (816, 1088)
  >>> width, height = catIm.size
  >>> width
  816
  >>> catIm.filename
  'zophie.png'
  >>> catIm.format
  'PNG'
  >>> catIm.format_description
  'Portable network graphics'
  >>> catIm.save('zophie.jpg')
  ```

* **Image.new()** #The arguments to `Image.new()` are as follows:

  * The string `'RGBA'`, which sets the color mode to RGBA. (There are other modes that this book doesn’t go into.)
  * The size, as a two-integer tuple of the new image’s width and height.
  * The background color that the image should start with, as a four-integer tuple of an RGBA value. 

  ```python
  >>> im = Image.new('RGBA', (100, 200), 'purple')
  ```

* **crop()** # this method on `Image` objects takes a box tuple and returns an `Image` object representing the cropped image.

  ```python
  >>> faceIm = catIm.crop((335, 345, 565, 560))
  >>> faceIm.size
  (230, 215)
  >>> faceIm.save('cropped.png')
  ```

* **copy()** and **paste()**

  ```python
  >>> catIm = Image.open('zophie.png')
  >>> catCopyIm = catIm.copy()
  >>> catCopyIm.paste(faceIm, (0, 0))
  >>> catCopyIm.paste(faceIm, (400, 500))
  >>> catCopyIm.save('pasted.png')
  ```

* **resize()** #  This method is called on an `Image` object and returns a new `Image` object of the specified width and height.

  ```python
  >>> width, height = catIm.size
  >>> quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
  ```

* **rotate()** # which returns a new `Image` object of the rotated image and leaves the original `Image` object unchanged.

  ```python
  >>> catIm.rotate(90).save('rotated90.png')
  ```

  The `rotate()` method has an optional `expand` keyword argument that can be set to `True` to enlarge the dimensions of the image to fit the entire rotated new image. 

  ```python
  >>> catIm.rotate(6, expand=True)
  ```

* **transpose()** # You can also get a “mirror flip” of an image with the `transpose()` method. You must pass either `Image.FLIP_LEFT_RIGHT` or `Image.FLIP_TOP_BOTTOM` to the `transpose()` method. 

  ```python
  >>> catIm.transpose(Image.FLIP_LEFT_RIGHT)
  >>> catIm.transpose(Image.FLIP_TOP_BOTTOM)
  ```

* **getpixel()** and **putpixel()** # 像素 These methods both take a tuple representing the x- and y-coordinates of the pixel. The `putpixel()` method also takes an additional tuple argument for the color of the pixel. This color argument is a four-integer RGBA tuple or a three-integer RGB tuple.

  ```python
  >>> im = Image.new('RGBA', (100, 100))
  >>> im.getpixel((0, 0))
  (0, 0, 0, 0)
  >>> for x in range(100):
          for y in range(50):
              im.putpixel((x, y), (210, 210, 210))
  >>> from PIL import ImageColor
  >>> for x in range(100):
          for y in range(50, 100):
              im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
  ```

* Drawing on Images # `from PIL import ImageDraw`

  ```python
  >>> from PIL import Image, ImageDraw
  >>> im = Image.new('RGBA', (200, 200), 'white')
  >>> draw = ImageDraw.Draw(im)
  ```

  * The `point(xy, fill)` method draws individual pixels. The *xy* argument represents a list of the points you want to draw. The list can be a list of x- and y-coordinate tuples, such as `[(x, y), (x, y), ...]`, or a list of x- and y-coordinates without tuples, such as `[x1, y1, x2, y2, ...]`.The *fill* argument is the color of the points and is either an RGBA tuple or a string of a color name, such as `'red'`. The *fill* argument is optional.
  * The `line(xy, fill, width)` method draws a line or series of lines. *xy* is either a list of tuples, such as `[(x, y), (x, y), ...]`, or a list of integers, such as `[x1, y1, x2, y2, ...]`. Each point is one of the connecting points on the lines you’re drawing.
  * The `rectangle(xy, fill, outline)` method draws a rectangle.（方形）. The *xy* argument is a box tuple of the form `(left, top, right, bottom)`.
  * The `ellipse(xy, fill, outline)` method draws an ellipse（椭圆）. The *xy* argument is a box tuple (*left*, *top*, *right*, *bottom*) that represents a box that precisely contains the ellipse.
  * The `polygon(xy, fill, outline)` method draws an arbitrary polygon. The *xy* argument is a list of tuples, such as `[(x, y), (x, y), ...]`, or integers, such as `[x1, y1, x2, y2, ...]`, representing the connecting points of the polygon’s sides. The last pair of coordinates will be automatically connected to the first pair. 

  ```python
  >>> draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
  >>> draw.rectangle((20, 30, 60, 60), fill='blue')
  ```

* Drawing Text # `from PIL import ImageFont`

  * The`text()` method for drawing text onto an image. It takes four arguments: *xy*, *text*, *fill*, and *font*.
  * The`textsize()` method. Its first argument is the string of text you want to measure, and its second argument is an optional `ImageFont` object. This method will then return a two-integer tuple of the width and height that the text in the given font would be if it were written onto the image.
  * `ImageFont.truetype()` The first argument is a string for the font’s *TrueType file*—this is the actual font file that lives on your hard drive.The second argument to `ImageFont.truetype()` is an integer for the font size in *points*(rather than, say, pixels). Keep in mind that Pillow creates PNG images that are 72 pixels per inch by default, and a point is 1/72 of an inch.

  ```python
  >>> from PIL import Image, ImageDraw, ImageFont
  >>> import os
  >>> im = Image.new('RGBA', (200, 200), 'white')
  >>> draw = ImageDraw.Draw(im)
  >>> draw.text((20, 150), 'Hello', fill='purple')
  >>> fontsFolder = 'FONT_FOLDER' # e.g. 'Library/Fonts'
  >>> arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
  >>> draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
  >>> im.save('text.png')
  ```


## import [pyautogui](http://pyautogui.readthedocs.org/)

* Pauses and Fail-Safes

  * **pyautogui.PAUSE** # set the `pyautogui.PAUSE` variable to the number of seconds you want it to pause. every PyAutoGUI function call will wait the seconds after performing its action. 
  * Moving the mouse cursor to the upper-left corner of the screen will cause PyAutoGUI to raise the `pyautogui.FailSafeException`exception. You can disable this feature by setting `pyautogui.FAILSAFE = False`.

  ```python
  >>> import pyautogui
  >>> pyautogui.PAUSE = 1
  >>> pyautogui.FAILSAFE = True
  ```

* **pyautogui.size()** # The `pyautogui.size()` function returns a two-integer tuple of the screen’s width and height in pixels.

  ```python
  >>> import pyautogui
  >>> pyautogui.size()
  (1920, 1080)
  >>> width, height = pyautogui.size()
  ```

* **pyautogui.moveTo()** # An optional `duration` integer or float keyword argument specifies the number of seconds it should take to move the mouse to the destination. 

  ```python
  >>> for i in range(10):
          pyautogui.moveTo(100, 100, duration=0.25)
  ```

* **pyautogui.moveRel()** # moves the mouse cursor *relative* to its current position.

  ```python
  pyautogui.moveRel(100, 0, duration=0.25)
  ```

* **pyautogui.position()** # get the mouse’s current position

  ```python
  >>> pyautogui.position()
  (311, 622)
  ```

* **pyautogui.click()** 

  ```
  >>> import pyautogui
  >>> pyautogui.click()
  pyautogui.click(200, 250, button='middle')
  ```

  * **pyautogui.mouseDown()** and **pyautogui.mouseUp()**
  * **pyautogui.doubleClick()** and **pyautogui.rightClick()** and **pyautogui.middleClick()**

* **pyautogui.dragTo()** and **pyautogui.dragRel()** like move

* **pyautogui.scoll()**

  ```python
  >>> import time, pyautogui
  >>> time.sleep(5); pyautogui.scroll(100)
  ```

* **pyautogui.screenshot()** # return a `Image` object

* **pyautogui.pixelMatchesColor()** # This function will return `True` if the pixel at the given x- and y-coordinates on the screen matches the given color.

  ```python
  >>> import pyautogui
  >>> im = pyautogui.screenshot()
  >>> im.getpixel((50, 200))
  (130, 135, 144)
  >>> pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
  True
  ```

* **pyautogui.locateOnScreen()** #  Give PyAutoGUI an image of what you want to click and let it figure out the coordinates. 图像识别 

  ```python
  >>> import pyautogui
  >>> pyautogui.locateOnScreen('submit.png')
  (643, 745, 70, 29)
  ```

  The four-integer tuple that `locateOnScreen()` returns has the x-coordinate of the left edge, the y-coordinate of the top edge, the width, and the height for the first place on the screen the image was found. 

  If the image cannot be found on the screen, `locateOnScreen()` will return `None`. If the image can be found in several places on the screen, `locateAllOnScreen()` will return a `Generator` object.

  ```python
  >>> list(pyautogui.locateAllOnScreen('submit.png'))
  [(643, 745, 70, 29), (1007, 801, 70, 29)]
  ```

* **pyautogui.center()** #  return x- and y-coordinates of the area’s center. 

  ```python
  >>> pyautogui.center((643, 745, 70, 29))
  (678, 759)
  ```

* **pyautogui.typewrite()**

  ```python
  >>> pyautogui.click(100, 100); pyautogui.typewrite('Hello world!', 0.25)
  ```

  | Keyboard key string                                          | Meaning                                                      |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |
  | `'a'`, `'b'`, `'c'`, `'A'`, `'B'`, `'C'`, `'1'`, `'2'`, `'3'`, `'!'`, `'@'`, `'#'`, and so on | The keys for single characters                               |
  | `'enter'` (or `'return'`or `'\n'`)                           | The ENTER key                                                |
  | `'esc'`                                                      | The ESC key                                                  |
  | `'shiftleft'`, `'shiftright'`                                | The left and right SHIFT keys                                |
  | `'altleft'`, `'altright'`                                    | The left and right ALT keys                                  |
  | `'ctrlleft'`, `'ctrlright'`                                  | The left and right CTRL keys                                 |
  | `'tab'` (or `'\t'`)                                          | The TAB key                                                  |
  | `'backspace'`, `'delete'`                                    | The BACKSPACE and DELETE keys                                |
  | `'pageup'`, `'pagedown'`                                     | The PAGE UP and PAGE DOWN keys                               |
  | `'home'`, `'end'`                                            | The HOME and END keys                                        |
  | `'up'`, `'down'`, `'left'`, `'right'`                        | The up, down, left, and right arrow keys                     |
  | `'f1'`, `'f2'`, `'f3'`, and so on                            | The F1 to F12 keys                                           |
  | `'volumemute'`, `'volumedown'`, `'volumeup'`                 | The mute, volume down, and volume up keys (some keyboards do not have these keys, but your operating system will still be able to understand these simulated keypresses) |
  | `'pause'`                                                    | The PAUSE key                                                |
  | `'capslock'`, `'numlock'`, `'scrolllock'`                    | The CAPS LOCK, NUM LOCK, and SCROLL LOCK keys                |
  | `'insert'`                                                   | The INS or INSERT key                                        |
  | `'printscreen'`                                              | The PRTSC or PRINT SCREEN key                                |
  | `'winleft'`, `'winright'`                                    | The left and right WIN keys (on Windows)                     |
  | `'command'`                                                  | The Command (![img](https://automatetheboringstuff.com/images/000085.jpg)) key (on OS X) `'option'` The OPTION key (on OS X) |

  ```python
  >>> pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])
  ```

* **pyautogui.keyDown()** and **pyautogui.keyUp()** and **pyautogui.press()**

If you need to type a string into a text field, the `typewrite()` function is more suitable. But for applications that take single-key commands, the `press()` function is the simpler approach.

* **pyautogui.hotkey()** #  takes multiple keyboard key string arguments, presses them in order, and releases them in the reverse order. 

  ```python
  pyautogui.hotkey('ctrl', 'c')
  pyautogui.hotkey('ctrl', 'alt', 'shift', 's')
  ```

  ​