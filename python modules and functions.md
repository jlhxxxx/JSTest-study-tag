

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
>>> shelfFile.close()
```

## **import [shutil](https://docs.python.org/3/library/shutil.html#module-shutil) **  # *copy, move, rename, and delete files*

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
  >>> len(res.text)
  178981
  >>> print(res.text[:250])
  ...
  ```

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

## import BeautifulSoup # *extracting information from an HTML page（can't not use regex）*

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

* **select()** # passing a string of a [CSS *selector*](http://www.w3school.com.cn/cssref/css_selectors.asp) to find the element you are looking for and return a list of `Tag` objects. Calling `getText()` on the element returns the element’s text, or inner HTML. Tag values also have an `attrs` attribute that shows all the HTML attributes of the tag as a dictionary.

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

  ​