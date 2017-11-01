# The Python Interpreter
The Python interpreter is a program that reads Python program statements and executes them immediately. To use the interpreter, you need
to open a terminal window or command prompt on your workstation. The interpreter operates in two modes.1
Interactive Mode
You can use the interpreter as an interactive tool. In interactive mode, you run the Python program and you will see a new prompt, >>>, and you can then enter Python statements one by one. In Microsoft Windows, you might see something like this:
C:\Users\Paul>python
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit
(Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> _
The interpreter executes program statements immediately. Interactive mode is really useful when you want to experiment or try things out. For example, sometimes you need to see how a particular function (that you haven’t used before) behaves. On other occasions, you might need to see exactly what a piece of failing code does in isolation.

The >>> prompt can be used to enter one-line commands or code blocks that define
classes or functions (discussed later). Some example commands are shown here:
1   >>> dir(print)
2   ['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__',
    '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
    '__init__', '__le__', '__lt__', '__module__','__name__','__ne__',
    '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__',
    '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
    '__text_signature__']
3 >>>
4   >>> 123.456 + 987.654
5 1111.11
6 >>>
7   >>> 'This'+'is'+'a'+'joined'+'up'+'string.'
8   'Thisisajoinedupstring.'
9 >>>
10  >>> len('Thisisajoinedupstring.')
11  22
The dir() command on line 1 lists all the attributes of an object, helpful if you need to know what you can do with an object type. dir() run without an argument tells you what modules you have available. dir(print) shows a list of all the built-in methods for print(), most of which you’ll never need.
Ifyoutypeanexpressionvalue,asonline4,123.456 + 987.654theinterpreterwill execute the calculation and provide the result. The expression on line 7 joins the strings of characters into one long string. The len() function on line 10 gives you the length of a string in characters.
If you define a new function2 in interactive mode, the interpreter prompts you to complete the definition and will treat a blank line as the end of the function.
1   >>> def addTwoNumbers(a,b):
2   ...     result = a + b
3   ...     return result
4 ...
5   >>> addTwoNumbers(3,6)
69
7 >>>
Note that when the interpreter expects more code to be supplied in a function, for example, it prints the ellipsis prompt (...). In the case of function definitions, a blank line (see line 4 above) completes the function definition.
We define the function in lines 1 through 3 (note the indentation), and the blank line 4 ends the definition. We call the function on line 5 and add 6 + 3, and the result is (correctly) 9.

One other feature of the interactive interpreter is the help() function. You can use
this to see the documentation of built-in keywords and functions. For example:
>>> help(open)
Help on built-in function open in module io:
open(...)
    open(file, mode='r', buffering=-1, encoding=None, errors=None,
newline=None, closefd=True, opener=None) -> file object
... etc. etc.

Command-Line Mode
In command-line mode, the Python program is still run at the command line but you add the name of a file (that contains your program) to the command:
python myprogram.py
The interpreter reads the contents of the file (myprogram.py in this case), scans and validates the code, compiles the program, and then executes the program. If the interpreter encounters a fault in the syntax of your program, it will report a compilation error. If the program fails during execution, you will see a runtime error. If the program executes successfully, you will see the output(s) of the program.
You don’t need to worry about how the interpreter does what it does, but you do need to be familiar with the types of error messages it produces.
We use command-line mode to execute our programs in files.
Coding, Testing and Debugging Python Programs
The normal sequence of steps when creating a new program is as follows:
1. Create a new .py file that will contain the Python program (sometimes called source code).
2. Edit your .py file to create new code (or amend existing code) and save the file.
3. Run your program at the command prompt to test it, and interpret the outcome.
4. If the program does not work as required, or you need to add more features, figure out what changes are required and go to Step 2.

It’s usually a good idea to document your code with comments. This is part of the editing process, Step 2. If you need to make changes to a working program, again, you start at Step 2.
Writing new programs is often called coding. When your programs don’t work properly, getting programs to do exactly what you want them to do is often called debugging.
Comments, Code Blocks, and Indentation
Python, like all programming languages has conventions that we must follow. Some programming languages use punctuation such as braces ({}) and semicolons (;) to structure code blocks. Python is somewhat different (and easier on the eye) because it uses white space and indentation to define code structure.3 Sometimes code needs a little explanation, so we use comments to help readers of the code (including you) understand it.
We introduce indentation and comments with some examples.
 #
# some text after hashes
#
brdr = 2 # thick border
def my_func(a, b, c):
    d = a + b + c
... ...
if this_var==23:
    doThis()
    doThat()
... else:
    do_other()
    ...
def addTwoNumbers(a, b):
    "adds two numbers"
    return a + b
if long_var is True && \
    middle==10 && \
    small_var is False:
    ...
    ...
Any text that appears after a hash character (#) is ignored by the interpreter and treated as a comment. We use comments to provide documentation.
The colon character (:) denotes the end of aheaderlinethatdemarksacodeblock. The statements that follow the header line should be indented.
Colons are most often used at the end of if, elif, else, while, and for statements, and function definitions (that start with the def keyword).
In this example the text in quotes
is a docsctring. This text is what a help(addTwoNumbers) command would display in the interactive interpreter.
The backslash character (\) at the end
of the line indicates that the statement extends onto the next line. Some very long statements might extend over several lines.
 3Python 3 disallows mixed spaces and tabs, by the way (unlike version 2).

xxxxxxxxxxxxxx:
    xxxxxxxxxxxx
    xxxxxxxxxxxx
    xxxxxxxxxxxx
xxxxxxxxx:
    xxxxxxxxxxx:
All code blocks are indented once a
header line with a colon appears. All the statements in that block must have the same indentation.
Code blocks can be nested within each other, with the same rule: All code in a block has the same indentation.
Indentation is most often achieved using four-space increments.
The semicolon character (;) can be used to join multiple statements in a single line. The first line is equivalent to the two lines that follow it.
a=b +
a=b+ p=q+
xxxxxxx
xxxxxxxxxxx:
xxxx xxxx
c;p=q+ r
c r

  Variables
A variable is a named location in the program’s memory that can be used to store some data. There are some rules for naming variables:
• The first character must be a letter or underscore ( _ ).
• Additional characters may be alphanumeric or underscore.
• Names are case-sensitive.
Common Assignment Operations
When you store data in a variable it is called assignment. An assignment statement places a value or the result of an expression into variable(s). The general format of an assignment is:
var = expression
An expression could be a literal, a calculation, a call to a function, or a combination
of all three. Some expressions generate a list of values; for example:
var1, var2, var3 = expression
Here are some more examples:
>>> # 3 into integer myint
>>> myint = 3
>>>
>>> # a string of characters into a string variable
>>> text = 'Some text'

>>> # a floating point number
>>> cost = 3 * 123.45
>>> # a longer string
>>> Name = 'Mr' + ' ' + 'Fred' + ' ' + 'Bloggs'
>>> # a list
>>> shoppingList = ['ham','eggs','mushrooms']
>>> # multiple assignment (a=1, b=2, b=3)
>>> a, b, c = 1, 2, 3
Other Assignment Operations
Augmented assignment provides a slightly shorter notation, where a variable has its value adjusted in some way.
  This assignment
x+=1
x-=23
x/=6
x*=2.3
Is equivalent to
x = x + 1
x = x – 23
x = x / 6
x = x * 2.3
   Multiple assignment provides a slightly shorter notation, where several variables are given the same value at once.
This assignment Is equivalent to
a=b=c=1 a =1 b =1 c =1
So-called multuple assignment provides a slightly shorter notation, where several variables are given their values at once.
       This assignment
x, y, z = 99, 100, 'OK'
p, q, r = myFunc()
Python Keywords
Explanation
Results in:
x=99, y= 100,andz='OK'
IfmyFunc()returnsthreevalues,p,q, and r are assigned those three values.
   Like all programming languages, in Python, some words have defined meanings and are reserved for the Python interpreter. You must not use these words as variable names. Note that they are all lowercase.


   and
class
elif
finally
if
lambda
print
while
as                 assert             break
continue           def                del
else               except             exec
for                from               global
import             in                 is
not                or                 pass
raise              return             try
with               yield

     There are a large number of built-in names that you must not use, except for their intended purpose. The cases of True, False, and None are important. The most common ones are listed here.
   True               False
all                any
dir                eval
float              format
max                min
open               print
round              set
tuple              type
None               abs
chr                dict
exit               file
input              int
next               object
quit               range
str                sum
vars               zip
  To see a list of these built-ins, list the contents of the __builtins__ module in the shell like this:
>>> dir(__builtins__)
Special Identifiers
Python also provides some special identifiers that use underscores. Their name will be of the form:
_xxx
__xxx__
__xxx

Mostly, you can ignore these.4 However, one that you might encounter in your
programming is the special system variable:
__name__
This variable specifies how the module was called. __name__ contains:
• The name of the module if imported.
• The string '__main__' if executed directly.
You often see the following code at the bottom of modules. The interpreter loads your program and runs it if necessary.
if __name__ == '__main__':
    main()
Python Modules
Python code is usually stored in text files that are read by the Python interpreter at runtime. Often, programs get so large that it makes sense to split them into smaller ones called modules. One module can be imported into others using the import statement.
import othermod # makes the code in othermod import mymodule # and mymodule available
Typical Program Structure
The same program or module structure appears again and again, so you should try and follow it. In this way, you know what to expect from other programmers and they will know what to expect from you.
 #!/usr/bin/python
#
# this module does
# interesting things like
# calculate salaries
#
Used only in Linux/Unix environments (tells the shell where to find the Python program).
Modules should have some explanatory text describing or documenting their behavior.
(continued)
  4The only ones you really need to know are the __name__ variable and the __init__() method called when a new object is created. Don’t start your variable names with an underscore and you’ll be fine.

  from datetime import datetime
now =datetime.now()
class bookClass(object):
    "Book object"
    def __init__(self,title):
        self.title=title
return
def testbook():
    "testing testing..."
    title="How to test Py"
    book=bookClass(title)
    print("Tested the book")
if __name__=='__main__':
    testBook()


 Module imports come first so their content
can be used later in the module.
Createaglobalvariablethatisaccessibleto all classes and functions in the module.
Class definitions appear first. Code that imports this module can then use these classes.
Functions are defined next. When imported, functions are accessed as module.function().
If imported, the module defines classes and functions. If this module is run, the code here (e.g., testBook()) is executed.

PYTHON OBJECTS 

Every variable in Python is actually an object. You don’t have to write object-oriented (OO) code to use Python, but the way Python is constructed encourages an OO approach.1
Object Types
All variables have a type that can be seen by using the built-in type() function.
>>> type(23)
<type 'int'>
>>> type('some more text')
<type 'str'>
>>> c=[1,2,'some more text']
>>> type(c)
<type 'list'>
Other types are 'class', 'module', 'function', 'file', 'bool', 'NoneType', and 'long'.
The special constants True and False are 'bool' types. The special constant None is a 'NoneType'.
To see a textual definition of any object, you can use the str() function; for example, the variable c can be represented as a string:
>>> str(c)
"[1,2,'some text']"
Factory Functions
There are a series of functions that create variable types directly. Here are the most commonly used ones.

int(4.0)
str(4)
list(1, 2, 3, 4)
tuple(1, 2, 3, 4)
dict(one=1, two=2)
Numbers
Creates integer 4
Creates string '4'
Creates list [1,2,3,4]
Creates tuple (1,2,3,4)
Creates dictionary {'one':1,'two':2}
 Integer numbers have no realistic limit; you can store and manipulate numbers with 1,000 digits, for example. These are stored as “long” numbers, for example:
>>> 12345678901234567890
12345678901234567890
Real numbers (i.e., those with decimal points) are stored with what is called double- precision. For example:
>>>1 / 7.0
0.14285714285714285
The actual degree of precision depends on the architecture of the hardware you use. Very large or very small real numbers can be described using scientific notation.
>>> x = 1E20
>>> x / 7.0
1.4285714285714285e+19
>>> int(x/7.0)
14285714285714285714286592
>>> y = 1E-20
>>> y / 7.0
1.4285714285714285e-21
Arithmetic Operators
The four arithmetic operators work as expected.

 # Addition
2 + 3
2.0 + 3
# Subtraction
3 - 2
3.0 - 2
# Multiplication
3 * 2
3 * 2.0
3.0 * 2.0
# Division
3 / 2
-6 / 2
-6 / 4
3 / 2.0
Other Operators
# Modulus
15 % 4
# Exponentiation
4 ** 3
-4 ** 3
4 ** -3
# Integer 5
# Real 5.0 (if one or more operands
# are real)
# Integer 1
# Real 1.0
# Integer 6
# Real 6.0
# Real 6.0
All divisions produce real numbers
# 1.5
# -3.0
# -1.5
# 1.3
# Real 3.0 (remainder after
# dividing 15 by 4)
# Integer 64
# Integer -64 (the '–' applies to
# the result)
# Real 0.015625 (NB negative
# exponents force operand to real
# numbers
CHAPTER 2 ■ PYTHON OBJECTS
    Conversion Functions
 int(1.234)
int(-1.234)
long(1.234)
long(-1.234)
long('1234')
long('1.234')
long(float('1.234'))
float(4)
float('4.321')
# Integer 1
# Integer -1
# Long1L
# Long -1L
# Long 1234L
# ** error ** needs 2
# conversions
# Long 1L (after two
# conversions)
# Real 4.0
# Real 4.321

Boolean Numbers
Booleans are actually held as integers but have a value of either True or False.
 bool(23)
bool(0)
bool('any text')
bool('')
bool([])
# True - all nonzero integers # False -zero
# True – any string
# False – zero length strings
# False – empty lists
 Random Numbers
Two random number generators are useful (you need to import the random module).
 import random
random.randint(a,b)
random.random()
# Generates a random integer
# between a and b inclusive.
# Generates a random real
# number between 0.0 and 1.0
 Sequences: Strings, Lists, and Tuples
So far, we have looked at variables that hold a single value. A sequence is a variable that holds multiple values as an array. Each element can be addressed by its position in the sequence as an offset from the first element. The three types of sequence are as follows:
• Strings: A sequence of characters that together form a text string.
• Lists: A sequence of values where each value can be accessed
using an offset from the first entry in the list.
• Tuples: A sequence of values, very much like a list, but the entries in a tuple are immutable; they cannot be changed.
We’ll look at the Python features that are common to all sequences and then look at the three types separately.
Sequence Storage and Access
The elements of a sequence are stored as a contiguous series of memory locations. The first element in the sequence can be accessed at position 0 and the last element at position n – 1 where n is the number of elements in the sequence (see Figure 2-1).

You can iterate through the elements of a sequence x having n elements starting at elementx[0]andadding+1eachtimex[1], x[2] 1⁄4 x[n-1],andsoon.Youcanalso iteratefromtheendandsubtract1eachtime:x[n-1], x[n-2] 1⁄4 x[0].
Membership
A common check is to determine whether a value exists in a sequence. For example:

  'a' in 'track'
9 in [1,2,3,4,5,6]
'x' not in 'next'
'red' not in ['tan','pink']
# True # False
# False # True
 Concatenation2
Two or more sequences can be added together to make longer sequences. The plus sign
(+) is used to concatenate strings, lists, or tuples.
sequence1 + sequence2 # results in a new sequence # that appends sequence2 to
# sequence1 'mr'+'joe'+'soap' # 'mrjoesoap'
2It is recommended that you use the join() string method to join a list of strings or a tuple, as it is more efficient. For example:
>>> '-'.join(('a','b','c','d'))
'a-b-c-d'

Sequence Elements and Slices
A sequence is an ordered list of elements, so a single element is identified by its offset from the first. A slice is a convenient way to select a subset of these elements in sequence, producing a new sequence. A slice is identified using this notation:
[startindex:endindex]
The slice will consist of elements starting as the startindex up to but not including endindex.
Some examples will make it easier to understand:
 mylist=['a','b','c','d','e']
mylist[0]
mylist[3]
mylist[5]
mylist[-1]
mylist[1:3]
mylist[:4]
mylist[3:]
# a list with five
# elements
# 'a'
# 'd'
# results in an error
# 'e'
# ['b','c']
# ['a','b','c']
# ['d','e']
 Sequences can be nested and elements accessed using multiple indexes, for example:
mylist = [1,2,3,['a','b','c'],5]
mylist[2]
mylist[3]
mylist[3][1]
# 3
# ['a','b','c']
# 'b'
Sequence Built-In Functions
 mylist=[4,5,6,7,1,2,3]
len(seq)
len(mylist)
max(seq)
max(mylist)
min(mylist)
Strings
# the length of seq #7
# maximum value inseq #7
# 1 – the minimum
 A string is a sequence of characters that make up a piece of text. Strings are immutable, but you can update the value of a string by assigning a new string to the same string variable.

 >>> mystr = 'Paddington Station'
>>> mystr=mystr.upper()     # replaces mystr
>>> mystr
PADDINGTON STATION
Assignment
You can delimit strings with either single (') or double (") quotes, as long as they are matched. You can embed either quote inside the other.
>>> text = 'Hello World!'
>>> longtext = "A longer piece of text"
>>> print(text)
Hello World!
>>>longtext
'A longer piece of text'
>>> text = 'Paul said, "Hello World!"'
>>>print(text)
Paul said, "Hello World!"
Accessing Substrings
You access substrings with slices, of course:
text='Paul said, "Hi"'
text[:4]
text[-4:]
text[5:9]
text[0:4] + text[12:14]
String Comparison Strings can be compared3 as follows:
'mcr'>'liv'
'liv'>'tot'
'mcr'=='X'
'X'>'t'
   # 'Paul'
   # '"Hi"'
   # 'said'
   # 'PaulHi'
# True
# False
# False
# False

    

    Membership (Searching)
We can check whether a substring is in a string, character by character or using substrings. The outcome is a Boolean.
 'a' in 'the task'
'w' in 'the task'
'as' in 'the task'
'job' not in 'the task'
'task' in 'the task'
# True
# False
# True
# True
# True
 Special Characters and Escaping
A string can contain nonprinting and control characters (e.g., tab, newline, and other special characters) by “escaping” them with a backslash (\). Common escape characters are the following:
\0 Null character
\t Horizontal tab
\n Newline character
\' Single quote
\" Double quote
\\ Backslash
>>> multiline='Line 1\nLine 2\nLine 3'
>>> print(multiline)
Line 1
Line 2
Line 3
Triple Quotes
Longer pieces of text with embedded newlines can be assigned using the triple quotes notation; for example:
>>> multiline="""Line1 1⁄4 Line 2
1⁄4 Line 3"""
>>> multiline
'Line 1\nLine 2\nLine 3'

text = 'This is text'
nums = '123456'
# finding text
text.find('is')
text.find('your')
# Validation checks
text.isalpha()
text.isdigit()
nums.isdigit()
# concatenation
''.join((text,nums))
' '.join((text,nums))
# case changing
text.upper()
text.lower()
# splitting string
text.split(' ')
# substitution
text.replace('is','was')
# stripping
text.rstrip()
text.lstrip()
text.strip()
Lists
# returns2
# returns -1
# all alphas?True
# all digits? False
# True
#'This is text123456'
#'This is text 123456'
# 'THIS IS TEXT'
# 'this is text'
# list of strings:
#['This','is','text']
# This was text
# remove trailing space
# remove leading space
# remove trailing and leading spaces
 Lists are widely used to store values that are collected and processed in sequence, such as lines of text read from or written to a text file, or where prepared values are looked up by their position or offset in the array.
Creating Lists
mylist = []
names=['Tom','Dick','Harry']
mixedlist = [1,2,3,'four']
elist = [1,2,3,[4,5,6]]
# an empty list
# list of strings
# list of mixed
# types
# embedded list

You can find the length of lists using the len() function. The length is the number of elements in the list. The last element index of a list mylist would be accessed as mylist[len(mylist)-1].
l = len(names) # 3
Values in the preceding lists are accessed as shown in the following code fragments.
CHAPTER 2 ■ PYTHON OBJECTS
   names[1]
mixedlist[0]
mixedlist[3]
mixedlist[2:4]
elist[2]
elist[3]
elist[3][1]
# 'Dick'
# 1
# 'four'
# [3,'four']
# 3
# [4,5,6] # 5
 If you try to access a nonexistent element in the list, you will get a 'list index out of range'error.
Updating Lists
Use the append() method to add entries to the end of a list. Use the del statement to delete an entry. For example:
 mylist = []
mylist.append('Tom')
mylist.append('Dick')
mylist.append('Harry')
# Change an entry
mylist[1]='Bill'
# Delete an entry
del mylist[1]
Indexing
# an empty list
# ['Tom']
# ['Tom','Dick']
# ['Tom','Dick','Harry']
# ['Tom','Bill','Harry']
# ['Tom','Harry']
 Whereas the membership (in, not in) operators return a Boolean True or False, the index() method finds an entry in your list and returns the offset of that entry. If the entry cannot be found, it returns an error.
 mylist=['Tom','Dick','Harry']
mylist.index('Dick')
mylist.index('Henry')
# 1
# ValueError: Henry
# not in list

Sequence Operations and Functions
The sequence operators—comparisons, slices, membership, and concatenation—all work the same as they do with strings.
Thesequencefunctions—len(), max(), min(), sum(), sorted()and reversed()—all work as expected.
Tuples
Like numbers and strings, tuples are immutable. They are useful for preset lookups or validators you might reuse.
Creating Tuples
To distinguish a tuple from a list, Python uses parentheses () to enclose the entries in a tuple.
>>> mynumbers = (1,2,3,4,5,6,7)
>>> months=('Jan','Feb','Mar','Apr','May','Jun',
1⁄4 'Jul','Aug','Sep','Oct','Nov','Dec')
>>> mixed = ('a',123,'some text',[1,2,3,'testing'])
# accessing tuples
>>> mynumbers[3]
>>> months[3:6]
>>> mixed[2]+' '+mixed[3][3]
# 4
# ('Apr','May','Jun')
# 'some text testing'
You can find the length of tuples using the len() function. The length is the number of elements in the list.
If you try to access a nonexistent element in the list, you will get a 'tuple index out of range'error.
Sequence Operations and Functions
The sequence operators—comparisons, slices, membership, and concatenation—all work as expected. The index() method works exactly as that for lists. The sequence functions—len(), max(), min(), sum(), sorted(), and reversed()—all work as expected.
Dictionaries
If we want our program to remember a collection of values, we can use lists and we can access the entries using the index to those values. To find the value we want, though, we must know the offset to that value (or search for it).
Dictionaries provide a lookup facility based on key/value pairs. The order of the entries in a dictionary is not defined (in fact, it is somewhat random), but every entry can be retrieved by using its key. Keys must be unique; there can only be one entry in a dictionary for each key.

Creating a Dictionary
You can create a dictionary using a set of key/value pairs.
>>> # days of week – seven key-value pairs >>> wdays={'M':'Monday','T':'Tuesday',
1⁄4 'W':'Wednesday','Th':'Thursday',
1⁄4 'F':'Friday','Sa':'Saturday',
1⁄4 'Su':'Sunday'} >>> wdays['M'] 'Monday'
>>> wdays['W'] 'Wednesday'
>>> wdays['Su']
'Sunday'
>>> newdict = {}
# empty dictionary
Updating a Dictionary
You can update dictionaries using the dict[key] convention.
>>> newdict = {}      # empty dictionary
>>> newdict['1st'] = 'first entry' # add 1st entry
>>> newdict['2nd'] = 'second entry'# add 2nd entry
>>> newdict['1st'] = 'new value'
>>> del newdict['2nd']
>>> len(newdict)
Dictionary Operations
# update 1st entry
# delete 2nd entry
# 1
The sequence operators—comparisons, membership, and concatenation—all work as expected. Here are a few dictionary operations that you might find useful:
# days of week – seven key/value pairs
# key existence
>>> 'Sa' in wdays
True
>>> 'Sp' in wdays
False

# create list of keys
>>> wdays.keys()
['M','T','W','Th','F','Sa','Su']
# create an iterable list of values
>>> wdays.values()
dict_values(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',
'Sunday'])
# look up a key with a default if key not found
>>> wdays.get('X','Not a day')
'Not a day'

PROGRAM Structure


Decision Making
Some simple utilities might be a short list of statements run in order, but a useful program usually needs to make decisions and choices. The decision making in a program determines the path that the program takes. Decisions are made by if statements.
The if Statement
if statements depend on some form of test or condition. The normal format of an if statement is shown here:
if test:
   statement1
   statement2
   statement3
# note the colon ':'.
# The statements following the
# if are indented and executed
# if the test is True.
In this case, the three statements are executed if test is True. Otherwise these statements are skipped and the interpreter skips to the statement following the code block.
Often, the False outcome of the test has its own code block, as follows:
if test:
   DoThis()
else:
   DoThat()
# note the colon ':'.
# DoThis() ... if test=True
# note the colon after 'else'
# DoThat() ... if test=False
The else: keyword separates the True outcome of the test from the False outcome of the test and directs the compiler to take the alternate code block: DoThat().
So far, we’ve seen a binary decision with only a True and a False outcome. Some if statements make a choice from more than two alternatives. In this case, the elif: keyword separates the different choices and the else: keyword is the final choice if no other test is met. For example:
1   If code=='RED':
2       SoundRedAlert()

3 4 5 6
elif code=='AMBER':
    GiveWarning()
else: pass
 ■ Note that the indentation of the if and its corresponding elif and else keywords must all be the same.
The pass Statement
In the preceding example, depending on the value of code, the program makes a choice to do something, but the third choice was pass. The pass statement is a “do nothing” statement. The third clause (else) is not strictly necessary, but pass is often useful to show explicitly what the program is doing (or not doing).
Types of Test
The tests that are applied in an if statement can take many forms, but the main patterns are summarized here.
 26
• Comparisons
    var1 > var2
    var1 == var2
    var1 != var2
# greater than
# equal to
# not equal to
• Sequence (list, tuple, or dictionary) membership var in seq
var not in seq
• Sequence length len(x)>0
• Boolean value fileopen
not fileopen
• Has a value? var
# sequence has entries?
# fileopen==True?
# fileopen==False?
# not None (or zero or '')

• Validation
var.isalpha() # alphanumeric?
          var.isdigit()    # is all digits?
• Calculations
(price*quantity) > 100.0 # cost>100?
          (cost-budget) > 0.0      # overbudget?
In the case of calculations it is often better to use braces to force the calculations than to rely on the default operator precedence.
Some decisions are more complex and require multiple tests to implement. For example:
if hungry and foodInFridge and notTooTired:
    cookAMeal()
else:
    getTakeAway()
In this case, the and operator joins the three conditions and all must be True for cookAMeal() to be executed.
There are three logical operators—and, or, and not—that can be used to link decisions.
Decisions can be nested; that is, they can appear inside the indented code blocks of other decisions. For example:
if age>19:
    if carValue>10000:
        if gotConvictions:
           rejectInsuranceApplication()
Loops and Iteration
Some features need to perform activities repetitively to process a number of items, including the following:
• Lists of values.
• Entries in a dictionary.
• Rows of data in a database.
• Lines of text in a disk file.
These constructs, usually called loops, perform a defined code block repeatedly on some item of data until some condition or test is met (or not met). These loops are implemented using for and while statements.

For Statement
The for statement acts as a header statement for a code block that is to be executed until some condition is met. The for statement operates on an iterable set of elements, often a sequence.
>>> theTeam=['Julia','Jane','Tom','Dick','Harry']
>>> for person in theTeam:
...    print('%s is in the team' % person)
Julia is in the team
Jane is in the team
Tom is in the team
Dick is in the team
Harry is in the team
Thegeneralformatis'for var in seq:'.
For each iteration through the members of the sequence, the variable var takes the value of the entry in the list or tuple, or it takes the value of the key in a dictionary.
Sometimes we don’t want to iterate through a list or dictionary, but we want to execute a loop a specific number of times. Python provides a useful range() function that generates an iterable list of specific size for us. It can take three arguments—start, end, and step—that specify the first number, the maximum number, and the increment between elements in the generated range, respectively. If you provide just one number argument, it creates a list with that number of integer elements starting with zero.
>>> range(10)
range(0,10)
>>> range(1,10)
range(1,10)
>>> range(1,20,3)
range(1,20,3)
# a list of ten elements 0-9
# default step=1
# list: [1,2,3,4,5,6,7,8,9]
# steps of 3
# list: [1,4,7,10,13,16,19]
>>> for i in range(3):
...    print(i)
0
1
2
While Statement
The while statement is similar to the for statement in that it provides a header statement for a code block to be repeated a number of times. Instead of an iterable set of elements, the while statement repeats the loop until a test is not met.
>>> n=4
>>> while n>0:
... print(n)
... n-=1

4 3 2 1
Often, the condition to be met is a counter that is decremented in the loop or a Boolean value the value of which is changed inside the loop, and then the loop is terminated.
>>> foundSmith=False
>>> while not foundSmith:
...   name=getNextName()   # get next person record
...   if name=='smith':    # name is 'smith'?
              foundSmith=True
Break Statement
A break statement is used to terminate the current loop and continue to the next statement after the for or while code block.
1 2 3 4 5 6 7
while True:     # this is an infinite loop
   command=input('Enter command:')
   if command=='exit': # infinite till user exits
        break              # skips to line 7
    else:
        doCommand(command) # execute command
print('bye')

Continue Statement: (In the examples that follow, the doCommand() function needs to be defined, of course.)
A continue statement is used in the code block of a loop to exit from the current code block and skip to the next iteration of the loop. The while or for loop test is checked as normal.
1 2 3 4 5 6 7 8 9 10
while True:     # this is an infinite loop
    command=input('Enter command:')
    if len(command)==0:  # no command - try again
        continue     # goes to next loop (line 1)
    elif command=='exit': # user exit
        print('Goodbye')
        break        # skips to line 10
    else:
        doCommand(command)
 print('bye')


List Comprehensions
A list comprehension (also known as a listcomp) is a way of dynamically creating a list of elements in an elegant shorthand. Suppose you wanted to create a list of the squares of the first ten integers. You could use this code:
squares=[]
for i in range(1,11):
   squares.append(i*i)
Or you could use this:
squares=[i*i for i in range(1,11)]
The syntax for listcomps is:
[expr for element in iterable if condition]
The if condition can be used to select elements from the iterable. Here are some examples of this syntax in use:
# a list of even numbers between 1 and 100
evens = [i for i in range(1,100) if not i % 2]
# a list of strings in lines containing 'True'
trulines = [l for l in lines if l.find('True')>-1]
Using Functions
Why Write Functions?
When you write more complicated programs, you can choose to write them in long, complicated modules, but complicated modules are harder to write and difficult to understand. A better approach is to modularize a complicated program into smaller, simpler, more focused modules and functions.
The main motivation for splitting large programs into modules and functions is to better manage the complexity of the process.
• Modularization “divides and conquers” the complexity into smaller chunks of less complex code, so design is easier.
• Functions that do one thing well are easier to understand and can be very useful to you and other programmers.
• Functions can often be reused in different parts of a system to avoid duplicating code.
• If you want to change some behavior, if it’s in a function, you only need to change code in one place.
• Smaller functions are easier to test, debug, and get working.

Importantly, if you choose to use a function written by someone else, you shouldn’t
need to worry too much how it works, but you need to trust it.2
What Is a Function?
A function is a piece of program code that is:
• A self-contained coherent piece of functionality.
• Callable by other programs and modules.
• Passed data using arguments (if required) by the calling module.
• Capable of returning results to its caller (if required).
You already know about quite a few built-in Python functions. One of these is the len() function. We just call len() and pass a sequence as a parameter. We don’t need to write our own len() function, but suppose we did write one of our own (for lists and dictionaries only). It might look something like this:
>>> def lenDictList(seq):
...
...
...
...
...
...
... return nelems
...
The header line has a distinct format:
if type(seq) not in [list,dict]: # a seq?
     return -1
nelems=0
# no - fail!
# length zero
# for elem
# add one
# length
for elem in seq:
   nelems+=1
• The keyword def to signify it is a new function.
• A function name lenDictList (that meets the variable naming rules).
• Braces to enclose the arguments (none, 1 or more).
• A colon to denote the end of the header line.
The code inside the function is indented. The code uses the arguments in the function definitions and does not need to define them (they will be passed by the calling module). Here are some examples:
>>> l = [1,2,3,4,5]
>>> d = {1:'one',2:'two',3:'three'}
>>> lenDictList(l)
5

>>> lenDictList(d)
3
>>> lenDictList(34)
-1
Note that the real len() handles any sequence including tuples and strings and does better error-handling. This is a much oversimplified version.
Return Values
The results of the function are returned to the caller using the return statement. In the preceding example, there is one return value: the length of the list or dictionary provided or it is –1 if the argument is neither.
Some functions do not return a result; they simply exit.
It is for the programmer to choose how to design his or her functions. Here are some example return statements.
 return
return
return
return
return
True
False
r1, r2, r3
dict(a=v1,b=v2)
# does not return a value
# True – perhaps success?
# False – perhaps a failure?
# returns three results
# returns a dictionary
 Calling a Function
Functions are called by using their name and adding parentheses enclosing the variables or values to be passed as arguments. You know len() already. The other functions are invented to illustrate how functions are used.
>>> count = len(seq)      # length of a sequence
>>>
>>> # the call below returns three results, the
>>> # maximum, the minimum, and the average of
>>> # the numbers in a list
>>> max, min, average = analyse(numlist)
>>>
>>> # the next call provides three parameters
>>> # and the function calculates a fee
>>> fee = calculateFee(hours, rate, taxfactor)

Note: The number of variables on the left of the assignment must match the number of return values provided by the function.
 
 Named Arguments
If a function just has a single argument, then you might not worry what its name is in a function call. Sometimes, though, not all arguments are required to be provided and they can take a default value. In this case you don’t have to provide a value for the argument. If you do name some arguments in the function call, then you must provide the named arguments after the unnamed arguments. Here is an example:
def fn(a, b, c=1.0):
return a*b*c
fn(1,2,3)
fn(1,2)
fn(1,b=2)
fn(a=1,b=2,c=3)
fn(1,b=2,3)
# 1*2*3 = 6
# 1*2*1 = 2 – c=default 1.0
# 1*2*1 = 2 – same result
# 1*2*3 = 6 - as before
# error! You must provide
# named args *after* unnamed
# args
■ Note In your code, you must define a function before you can call it. A function call must not appear earlier in the code than the definition of that function or you will get an “undefined” error.
Variable Scope
The variables that are defined and used inside a function are not visible or usable to other functions or code outside the function. However, if you define a variable in a module and call a function inside that module, then that variable is available in the called function. If a variable is defined outside all the functions in a module, the variable is available to all of the functions in the module.3 For example:

    sharedvar="I'm sharable"
def first():
   print(sharedvar)
   firstvar='Not shared'
   return
def second():
   print(sharedvar)
   print(firstvar)
   return
# a var shared by both
# functions
# this is OK
# this is unique to first
# this is OK
# this would fail!

INPUT AND OUTPUT


If a program did not produce any output, it wouldn’t be very useful, would it? If a program did not accept some data that varied from time to time, it would produce the same result again and again and again, and that wouldn’t be very useful either (after its first run at least). Most programs, therefore, need to accept some inputs or input data, so that they can product output data, outputs, or results.
In this chapter, we cover three important input/output mechanisms:
• Displayed output.
• Getting data from the user through the keyboard.
• Getting input from and writing output to disk files.
Displaying Output
You’ve seen the print() function1 quite a few times already. The most common way
of getting output from a program is to use the print() statement. Print is a function
that takes as its arguments the items to be displayed. Optionally, you can also define a separator that is placed between the displayed items and a line terminator value that can replace a newline. The function call looks like this:
print(arg1,arg2,arg3...,sep=' ',end='\n')
Here are some examples of the print() function in use.
>>> boy="Jack"
>>> girl="Jill"
>>> print("Hello World!")
Hello World!
>>> print(boy,'and',girl,'went up the hill')
Jack and Jill went up the hill
Note: that in Version 2, print was a statement, not a function, so it behaves differently. Print() is a common Version 3 stumbling block so take a look at https://docs.python.org/3/ whatsnew/3.0.html.


String Formatting

The percent (%) operator provides string formatting functionality. This feature has a structure like this:
formatstring % (arguments to format)
formatstring is a string that contains text to be output with embedded conversion symbols denoted by a percent sign (%). These are the common conversion symbols:
%c %s %d %f %%
        Single character/string of length 1
        String
        Signed decimal integer
        Floating point number
        Percent character
Here are some examples:

  >>> ntoys = 4
>>> myname='Fred'
>>> length = 1234.5678
>>> '%s has %d toys' % (myname,ntoys)
'Fred has 4 toys'
>>> 'is %s playing?' % (myname)
'is Fred playing?'
>>> 'length= %.2f cm' % length
'length= 1234.56 cm'
>>> 'units are %6s meters' % length
In the preceding examples, the .2 in %.2f indicates the number of decimal places. The 6 in %6s implies a field width of 6 characters.
String Functions
There are a large number of built-in string functions. The most common ones are illustrated here. Note that these all return a new string; they do not make changes to strings because strings are immutable.

 It is common to use the string formatting feature.
>>> print('%d plus %d makes %d' % (3, 7, 10))
3 plus 7 makes 10
You can suppress the trailing newline by setting the end argument to an empty string (or something else).
>>> #
>>> # the end= argument defaults to '\n'
>>> # if you change it, there won't be a newline
>>> #
>>> print('one...','two...','three',end='')
one... two... three>>>    # note the >>> prompt
The string separator defaults to a single space but can be changed or suppressed by setting it to an empty string.
>>> #
>>> # the sep= argument defaults to a space ' '
>>> # but you can change it, for example...
>>> #
>>> print('one...','two...','three',sep='***')
one...***two...***three
Getting User Input
The easiest way to get data into the program is to use the input()2 function. It takes one argument, which is the prompt you see displayed on the command line. The function returns a string value, so if you are asking for numeric or multiple values separated by commas, you will have to parse and process the text in the code before the data can be used.
>>> yourName=input('Enter your name: ')
Enter your name: Paul
>>> print('Your name is',yourName)
Your name is Paul
If you ask the user for an integer number, you should check that the entered text is valid and can be converted to an integer. To do this, you might do the following:
• Use len(text) to verify that some text has been entered.
• Use the string function text.isdigit() to check the text
represents a number.
2In Version 2, Python uses the function raw_input() instead. It works exactly like the input() function in Version 3.

• Use the int(text) to convert the text to an integer so you can
process it.
You might have heard of the “garbage-in, garbage-out” concept. If you don’t validate the data coming into your program, its behavior might be unpredictable or it might fail or just produce strange results. Don’t forget that hackers can exploit poor input validation to cause mayhem on Internet sites.
■ Note It is your responsibility, as programmer, to ensure that only data that meets your validation rules is accepted by your program.
Writing and Reading Files
At one point or another, you are going to have to read and write text files on disks or other devices. We look specifically here at text-only files and how you can access them.
Opening Files
To access a file on disk you create a file object and you use the open() function to do this. The format of the open call is:
fileobj = open(filename,mode)
The named file would normally be opened in the current directory, but the name can include a path so it can open any file on any disk and in any directory (local permissions allowing). The mode tells the interpreter to open the file for reading 'r', writing 'w', or appending 'a'.
Table 4-1 shows the outcomes of opening existing and nonexistent files with the three mode values.
Table4-1. OpeningFileswiththeThreeModeValues
     Open Mode
'r' 'w'
'a'
■ Note
valuable data and lose it.
File Exists
Openforreading
Overwritten by empty file and open for writing
Open for appending
File Does Not Exist
No such file or directoryerror Open for writing
New empty file created and open for writing
     Be careful when using the write mode; you might overwrite a file containing

Here are some examples of how to open files:
fname='myfile.txt'
fp = open(fname,'r')  # open for reading (must exist)
fp = open(fname,'w')  # creates new file for writing
fp = open(fname,'a')  # opens file for appending
Closing Files
Once you have finished reading from or writing to a file, it is a good idea to close it using
the close() function.
fp = open(fname,'w')  # open for writing
#
# do some writing, etc.
#
fp.close()
If you don’t explicitly close files, you shouldn’t encounter any major problem, but it is always best to pair open() and close() functions for the sake of completeness and tidiness.
Reading Files
The standard function to read data from a file is read(). It reads the entire contents of the file into a string variable. The content can then be split into separate lines delimited by the newline character ('\n').
fp = open(fname,'r')  # open for reading
text = fp.read()
lines=text.split('\n')
fp.close()
A more common way to read a file into memory is readlines(), which returns a list containing each line.
fp = open(fname,'r')  # open for reading
lines = fp.readlines()
fp.close()
Every entry in the lines list just shown will have a newline at its end, so a good way of cleaning up the readlines() data would be to use a list comprehension:
lines = [line.rstrip() for line in fp.readlines()]

If you want to read a file line by line, the best way is to make use of the fact that the
file object itself returns an iterator like this:
fp = open(fname,'r')  # open for reading
for eachLine in fp:
  #
  # process each line in turn
  #
  print(eachLine,end='')  # suppress the extra \n
fp.close()
■ Note Whichever way you read a file, the text that is read contains the trailing newline character; you must remove it yourself.
Writing to Files
The standard function to write data to a file is write(), which works exactly as you would expect.
fp.write(textline)
Note that the write() function does not append a newline to the text before writing.
Here is a simple example:
fp = open('text.txt','w')
while True:
    text = input('Enter text (end with blank):')
    if len(text)==0:
break else:
        fp.write(text+'\n')
fp.close()
If you didn’t add the trailing '\n' newline in the write statement, all the lines of text would be merged into a single long string. If you have a list of strings, you can write the list out as a file in one statement, but you must remember to append a newline to each string to make the file appear as you expect.
Here are two ways of writing out a list to a file:
lines=['line 1','line 2','line 3','line 4']
# write all lines with no '\n'
fp.writelines(lines)

# writes all line with '\n'
fp.writelines([line+'\n' for line in lines])
■ Note The write() and writelines() functions do not append trailing newline (\n) characters; you must do that yourself.
Accessing the File System
There are a number of useful file system functions. They are all available using the os module, which you must import.
import os
# remove a file (deleteme.txt) from disk
os.unlink('deleteme.txt')
# rename file on disk (from file.txt to newname.txt)
os.rename('file.txt','newname.txt')
# change current/working directory
os.chdir(newdirectory)
# create list of files in a directory
filelist = os.listdir(dirname)
# obtain current directory
curdir = os.getcwd()
# create a directory
os.mkdir(dirname)
# remove a directory (requires it to be empty)
os.rmdir(dirname)
# in the following examples, we need to use
# the os.path module
#
# does the file/directory exist?
exists = os.path.exists(path)
# does path name exist and is it a file?
isfile = os.path.isfile(filepathname)
# does path name exist and is it is directory?
isdir = os.path.isdir(filepath)

Command-Line Arguments
The input() function allows you to get input from the user using the keyboard at any point in your program. Often, though, it is more convenient to the user to provide input directly after the program name in a command line. Most command-line utilities have options and data to be used in its process; for example:
python mycopy.py thisfile.txt thatfile.txt
This might be a program that makes a copy of one file to another.
The arguments are captured in the sys.argv list from the sys module. Here is some code that demonstrates how to capture the command-line arguments (command.py):
import sys
nargs=len(sys.argv)
print('%d argument(s)' % (nargs))
n=0
for a in sys.argv:
    print('  arg %d is %s' % (n,a))
    n+=1
Let’s try running our program with three arguments:
D:\LeanPython>python command.py arg1 arg2 arg3
4 argument(s)
  arg 0 is command.py
  arg 1 is arg1
  arg 2 is arg2
  arg 3 is arg3
Note that the first (element 0) argument is always the name of the program itself.

USING MODULES

Once you have more than a hundred (or several hundred) lines of code in one Python file, it can be a little messy to manage all the functions and classes in the same place. Splitting your code over two or more module files that each cover one aspect of the functionality can simplify matters greatly.
The features and functions in the standard library (and other libraries that you might download and use from time to time) are made available to your programs as modules using the import statement.
Whether you are using your own home-grown modules or the standard libraries, the mechanism for including the code is the same.
Importing Code from a Module
The import statement has this format: import modulename [as name]
Thisstatementimportsthemodulemodulename.Theoptional'as name'partallows you to reference that module with a different name in your code. If this statement works without error, then all of the functions and classes in that module are available for use.
Modules Come from the Python Path
WhenPythonencountersanimport modulenamestatement,itlooksforafilecalled modulename.py to load.1 It doesn’t look just anywhere. Python has an internal variable called the Python path. You can see what it is by examining the sys.path variable.
The following interaction shows the path on a Windows machine.
>>> import sys
>>> sys.path
['', 'C:\\Windows\\SYSTEM32\\python34.zip', 'c:\\Python34\\DLLs',
'c:\\Python34\\lib', 'c:\\Python34', 'c:\\Python34\\lib\\site-packages']
>>>

The Python path is a list of directories that is set up by the Python installation process, but you can also access and change the path to suit your circumstances.
When you install other libraries (e.g., from PyPI) the path might be updated. If you keep all your Python code in one place (in the same, current directory), you will never need to change the Python path. You only need to worry about the Python path if you are dealing with many modules in different locations.
Creating and Using Your Own Modules
Let’s suppose that you have a module with Python code called mod1.py; the name of the module in your code will be mod1. You also have a program file called testmod.py. Let’s look at some example code in each file.
This is mod1.py: def hello():
    print('hello')
writtenby='Paul'
class greeting():
    def morning(self):
        print('Good Morning!')
    def evening(self):
print('Good Evening!')
Now, suppose we have a test program mod1test1.py:
import mod1 as m1
print(writtenby)
m1.hello()
print('written by', m1.writtenby)
greet = m1.greeting()
greet.morning()
greet.evening()
Now, you can see in line 1 that we have imported mod1 as m1. This means that
the code in module mod1 is referenced using the m1 prefix. If we had just imported the module, we would use the prefix mod1. When we run this code, we get the following result:
D:\LeanPython\programs>python mod1test1.py
hello
written by Paul
Good Morning!
Good Evening!

Let’s look at another test file (mod1test2.py). from mod1 import greeting,hello,writtenby
hello()
hello.writtenby='xxx'
print('written by', hello.writtenby)
print(writtenby)
greet = greeting()
greet.morning()
greet.evening()
In this case we have imported the function and class using this format:
from module import function1, function2...
When we run this code, we get the following result:
D:\LeanPython\programs>python mod1test2.py
hello
written by xxx
Paul
Good Morning!
Good Evening!
You can see that the import format allows us to drop the prefix for the imported functions.
We now import only what we want and we also can name the imported functions and classes without the prefix. We could also have used the format:
from module import *
In this alternative we import all the functions and classes from the module. The result would have been the same for mod1test2.py; there would be no need for prefixes.
When we import from the standard libraries, which often have a large number of functions and classes, it is more efficient to work this way.
■ Note: In general, name your imported modules and import only what you need; that is, avoid "import *".
  
OBJECT ORIENTATION

What Is Object Orientation?
The professional approach to programming has shifted away from designing systems with a hierarchy of features defined in functions toward an object-oriented (OO) approach. We look here at how Python fully supports object orientation.
In this book, we can only give a flavor of how objects are used. We work through an example and introduce some of the most basic concepts. We use some OO concepts in our explanation so you need a basic understanding of OO to work through this section.
In OO design, systems are composed of collaborating sets of well-defined objects. Rather than one piece of functionality making use of another function, one object sends a message to another object to achieve some goal. The message is in effect a function call, but the function (usually called a method) is associated with the object in question and the behavior of the method depends on the nature of the object.
You have already come across objects in many places. In fact, in Python everything is an object; we just haven’t elaborated on this OO view of the world. For example, a string has several useful methods:
newstring = text.upper()  # uppercase the string
newstring = text.lower()  # lowercase the string
newstring = text.split('\n')  # split lines
The string functions return a new variable—the new object—sometimes called an instance2 of the string class. The object (the new string) is the output of the method called on the original string.
1Object orientation is a big topic. You can see an overview of OO programming at http://en.wikipedia.org/wiki/Object-oriented_programming.
2When you create a new object from a class definition, that object is sometimes called an instance and the create process called instantiation. We use the word object, though, in our description.

In more complex objects, the object itself has attributes or properties that we can set and get.3 We might create a person object, for example. The functions or methods that a person object allows would include a new or create method as well as various set methods and get methods; for example:
fred=customer(name='Fred') # create new customer
fred.setAge(49)            # change age to 49
fred.gender='Male'         # Fred is male
cdate=fred.getCreateDate() # get the creation date
age = fred.getAge()        # get Fred's age
del fred # Fred no longer wanted L
In the preceding example, you can see there were some get and set methods that get and set Fred’s attributes, like his age and creation date. His age and creation date cannot be accessed directly except through these simple get and set functions.
There was one attribute that could be examined directly, though: fred.gender. It wasn’t a method because there were no parentheses associated when we referenced it. We can access that attribute directly and we can set it just like any other variable through an assignment.
Creating Objects Using Classes
In our Python code, a new object is defined by referring to a class. In the same way that we can create an int(), a list(), and str() types, we can define our own more complex objects using a class definition.
A class definition is a template for a new object. It defines the mechanism and data required to create a new instance of that class, its attributes (both private and public), and the methods that can be used to set and get attributes or change the state of the object.
Note that we are not recommending this as a perfect implementation of a person class; it is just an example to illustrate the use of class definitions, object attributes, and methods.
The module that defines the person class is people.py:
1   from datetime import datetime
2
3   class person(object):
4       "Person Class"
5       def __init__(self,name,age,parent=None):
6           self.name=name
7           self.age=age
8           self.created=datetime.today()
9           self.parent=parent
10          self.children=[]
3It is a design choice as to whether we hide attributes and make them available only through methods (private attributes) or expose them to the outside world (public).

11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
• •
•
•


print('Created',self.name,'age',self.age)
def setName(self,name):
    self.name=name
    print('Updated name',self.name)
def setAge(self,age):
    self.age=age
    print('Updated age',self.age)
def addChild(self,name,age):
    child=person(name,age,parent=self)
    self.children.append(child)
    print(self.name,'added child',child.name)
def listChildren(self):
    if len(self.children)>0:
        print(self.name,'has children:')
        for c in self.children:
           print('  ',c.name)
    else:
        print(self.name,'has no children')
def getChildren(self):
    return self.children
Line 1 imports the datetime and printing modules we’ll need later.
Line 3 starts the class definition. We have used the generic object type, but classes can subclassed and inherit the attributes and methods of another parent class.
Lines 5 through 11 creates a new object. Python doesn’t need a “new” method: When the object is created, Python looks for an __init__() method to initialize the object. The arguments passed through the creation call are used here to initialize the object attributes.4
The two methods in lines 13 through 19 update the object attribute’s name and age.
 4Note that the first argument to all of the methods in the class is 'self', the object itself. This argument is used internally in the class and is not exposed to the code that calls these methods, as you'll see in the test that follows. The "self." attributes are public.

 • In lines 21 through 24, the addChild method creates a new person who is a child of the current person. The children objects are stored in an attribute children, which is a list of the person objects for each child.
• In lines 26 through 32, the listChildren method prints out the names of the children for this person.
• In lines 34 and 35, the getChildren method returns a list containing the children of this person.
 ■ Note
behavior. This instrumentation code in the class is there to show what's going on inside.
Class methods would not normally print information messages to describe their
 We wrote a program that tests the person class called testpeople.py. To show the output inline, I pasted the code into the interpreter. The embedded comments should explain what’s going on.
1   >>> from people import person
2   >>> #
3   ... #   create a new instance of class person
4   ... #   for Joe Bloggs, age 47
5 ... #
6   ... joe=person('Joe Bloggs',47)
7   Created Joe Bloggs age 47
8   >>> #
9   ... #   use the age attribute to verify
10  ... #   Joe's age
11  ... #
12  ... print("Joe's age is",joe.age)
13  Joe's age is 47
14  >>> print("Joe's full name is ",joe.name)
15  Joe's full name is  Joe Bloggs
16  >>> #
17  ... #   add children Dick and Dora
18  ... #
19  ... joe.addChild('Dick',7)
20  Created Dick age 7
21  Joe Bloggs added child Dick
22  >>> joe.addChild('Dora',9)
23  Created Dora age 9
24  Joe Bloggs added child Dora
25  >>> #
26  ... #   use the listChildren method to list them
27  ... #
28  ... joe.listChildren()

29  Joe Bloggs has children:
30 Dick
31 Dora
32 >>> #
33  ... #   get the list variable containing Joe's children
34  ... #
35  ... joekids=joe.getChildren()
36  >>> #
37  ... #
38  ... #
39  ... #
40  ... #
41  ... print("** Joe's attributes **")
42  ** Joe's attributes **
print Joe's details.
NB the vars() function lists the values
of the object attributes
43  >>> print(vars(joe))
44  {'age': 47, 'children': [<people.person object at 0x021B25D0>, <people.
    person object at 0x021B2610>], 'name': 'Joe Bloggs', 'parent': None,
    'created': datetime.datetime(2014, 4, 4, 8, 23, 5, 221000)}
45  >>> #
46  ... #   print the details of his children
47  ... #   from the list we obtained earlier
48  ... #
49  ... print("** Joe's Children **")
50  ** Joe's Children **
51  >>> for j in joekids:
52  ...     print(j.name,'attributes')
53  ...     print(vars(j))
54  ...
55  Dick attributes
56  {'age': 7, 'children': [], 'name': 'Dick', 'parent': <people.person
    object at 0x021B2590>, 'created': datetime.datetime(2014, 4, 4, 8, 23,
    5, 229000)}
57  Dora attributes
58  {'age': 9, 'children': [], 'name': 'Dora', 'parent': <people.person
    object at 0x021B2590>, 'created': datetime.datetime(2014, 4, 4, 8, 23,
    5, 231000)}
59  >>>
• Line 1 imports the module we need.
• Line 6 creates a person by the name of Joe Bloggs.
• Lines 12 through 15 print Joe Bloggs’s details.
• Lines 19 through 24 add two children to Joe’s record. Note that the person class adds new person objects for each child.
• Line 28 calls the joe.listChildren() method to list the details of Joe’s children.

• Line 35 uses the joe.getChildren() method to obtain a list of
Joe’s children objects.
• Lines 41 through 43 use the vars() function to collect the attributes of the joe object. You can see all of the variables defined for the object, including a list of Joe’s children.
• Lines 51 through 53 loop through the joekids list printing the attributes of the children objects.
The preceding narrative gives you a flavor of how OO works in the Python language. OO is a large and complex topic that requires careful explanation.

The Python implementation of OO differs in some respects from other languages such as Java, for example. Python has a rather more “relaxed” attitude to OO, which makes some things easier for the programmer, but does mean that the programmer needs to be a little more careful in his or her coding. It is up to you to decide which approach is best.

TESTING YOUR CODE

Modularizing Code and Testing It: (Most programs are split into modules that are separately tested by the programmer. This testing is usually called unit or component testing.)

So far, we have explained how to make use of the features of Python to create software that has some purpose and hopefully, value. When you write a little code, the natural thing to do then is to try it out, or test it.
The programs I have used to illustrate Python features run without any intervention, or require some user input via the input() function. As you get better at programming, you will become more ambitious and create larger programs. Then you realize that testing becomes more difficult, and more important. Splitting programs into functions and modules will make testing and debugging easier, as I said earlier.
Test-Driven Development
As your programs get bigger and more complicated, the chances of making a mistake or making a change that has an unwanted side effect increase. Should we run all of our previous tests every time we make a change then? It would be helpful, but doesn’t the thought of running the same tests again and again bore you? Of course it might.
The test-driven development (TDD) approach for programming is gaining popularity. This is how it works:
• Developers write their (automated) tests first, before they write code.
• They run their tests and watch them fail, then add or correct code to make them pass.
• When their tests pass, they look for opportunities to improve the design of their code. Can you think of why?
TDD might not always be the best approach, but when it comes to writing larger programs it is best to modularize your code. When it comes to writing and testing classes and functions, using a unit test framework to create automated tests makes a lot of sense.

The unittest Framework
In this chapter, I provide a brief introduction of how the unittest framework [20] can be used to test Python modules.
Suppose we need to write a function that performs simple arithmetic. The function is passed two numbers and an operator, which could be any of '+', '-', '*', or '/' to simulate addition, subtraction, multiplication, or division. It is as simple as that. Our function call might look like this:
result, msg = calc(12.34, '*', 98.76)
result would be the outcome of the calculation, or None if an error occurred. msg would contain a string version of the result or an error message if the calculation fails for some reason.
The line of code that called the calc function in this example looks like a test doesn’t it? It is, except we haven’t checked that the outputs (result and msg) are correct. In this case we would expect that:
• result would have the value 1218.6984.
• msg would have the value '1218.6984'.
Here is a possible implementation of the calc function in file calc.py:
def calc(a, op, b):
    if op not in '+-/*':
        return None, 'Operator must be +-/*'
    try:
        if op=='+':
            result=a+b
        elif op=='-':
            result=a-b
        elif op=='/':
            result=a/b
        else:
            result=a*b
    except Exception as e:
        return None,e.__class__.__name__
    return result,str(result)
The calc function does very little checking. It does no checking of the numeric values of the two number arguments a and b. After that, it attempts the calculation but traps any exceptions that occur, passing the name of the exception back in msg.

Now, to create a set of tests for the calc function, we have created a testcalc.py file
as follows:
1   import unittest
2 import calc
3#
4 # define the test class 5#
6   class testCalc(unittest.TestCase):
7
8
9
10
11
12
13
14
15
16
17
18
19  #
20  #
21  #
22  TestSuite = unittest.TestSuite()
23  #
24  #   add tests to the suite
25  #
26  TestSuite.addTest(testCalc("testSimpleAdd"))
27  TestSuite.addTest(testCalc("testLargeProduct"))
28  TestSuite.addTest(testCalc("testDivByZero"))
29  #
30  #   create the test runner
31  #
32  runner = unittest.TextTestRunner()
33  #
34  #   execute the tests
35  #
36  runner.run(TestSuite)
• Line 1 imports the unittest module that we will use to test the calc function.
• Line 2 imports the calc module (the module to be tested).
• Line 6 defines the class (testCalc) that defines the tests.

• Lines 8 through 18 define three tests. The format of each is similar.
• Each test has a unique name (normally test...).
• It calls the function to be tested in some way.
• It performs an assertion to check correctness (we cover assertions further later).
• Line 22 defines the test suite that will be run.
• Lines 26 through 28 add tests to the test suite (note that we can
create multiple test suites with different selections of test).
• Line 32 defines the test runner.
• Line 36 runs the tests.
When we run the test we get this:
D:\LeanPython\programs>python testcalc.py
...
----------------------------------------------------
Ran 3 tests in 0.001s
OK
The three dots appear as you run the tests, and represent the successful execution of each test. If a test had failed, we would have seen a Python error message indicating the exception and line number in the program where the failure occurred.
All this code just to run a few tests might seem a little excessive. Perhaps it looks a bit wordy, but there is purpose in each call. Note, however, that once it is set up, if I want to add a new tests, I create a new test call (e.g., lines 8–10) and add the test to the suite (e.g., line 26). Once you are set up, therefore, creating large numbers of tests is easy. The calc function is a rather simplistic example. More realistic (and complex) classes and functions sometimes require 20 or 30 or even hundreds of tests.
■ Note: Programmers who offer their modules as open-source libraries often include a large suite of tests with their modules.2
  
Assertions
The key to good testing is the choice of inputs or stimuli applied to your code
(the function call; e.g., line 9) and the check that is performed on the outcome. The checks are implemented as assertions. The unittest module provides around 20 different assertion variations. Examples include the following:
• assertEquals. This variation asserts exact equality between two values (the result and your predicted result).
• assertTrue. Is an expression true?
• assertIn. Is a value in a sequence?
• assertGreaterEqual. Is one value greater than or equal to another?
More Complex Test Scenarios
The unittest framework has many more features. Examples are setup() and teardown() methods in the TestCase class. These methods are called automatically, just before
and just after each test case, to perform a standard setup (of variables, data, or the environment) to allow each test to run correctly. The teardown process tidies up after the test (if necessary).
■ Note We have now covered the basic elements of the Python language and explored the unittest module for testing. Now, let's look at using some popular libraries to do something useful.

Accessing the Web


Python has standard libraries that enable programmers to write both clients and servers that both use and implement Internet services such as electronic mail, File Transfer Protocol (FTP), and, of course, web sites.
In this chapter we look at how it is possible to use Python to access web sites and services. Suppose you wanted to download a page from a web site and save the HTML that was retrieved. The user needs to enter a URL for the site. Perhaps you want to be able to add a query string to the URL to pass data to the request, and you want to then display the response or save it to disk.
You would design your program to work in stages, of course:
1. Ask the user for a URL.
2. Ask for the query string to append to the URL.
3. Ask whether to save to disk.
The listing of program webtest.py is shown here.
1   import requests
2   from urllib.parse import urlparse
3
4   url=input('Web url to fetch:')
5   urlparts=urlparse(url)
6   if urlparts[0]=='':
7       url=''.join(('http://',url))
8
9   qstring=input('Enter query string:')
10  if len(qstring)>0:
11      url='?'.join((url,qstring))
12
13  save=input('Save downloaded page to disk [y/n]?')
14
15  print('Requesting',url)
16

17 try:
18      response = requests.get(url)
19      if save.lower()=='y':
20          geturl=response.url
21          urlparts=urlparse(geturl)
22          netloc=urlparts[1]
23          if len(netloc)==0:
24              fname='save.html'
25 else:
26              fname='.'.join((netloc,'html'))
27          print('saving to',fname,'...')
28          fp=open(fname,'w')
29          fp.write(response.text)
30          fp.close()
31 else:
32          print(response.text)
33  except Exception as e:
34
    print(e.__class__.__name__,e)
Let’s walk through this program.2
• Lines 1 and 2 import required modules (requests and urlparse).
• Lines 4 through 7 get a URL from the user. If the user doesn’t include the http:// part of the URL, the program adds the prefix.
• Lines 10 through 12 ask the user for a query string and append it to the URL with a ? character.
• Lines 14 through 16 ask the user if he or she wants to save the output to a file, then print the full URL to be requested.
• Lines 18 through 40 do most of the work; any exception is trapped by lines 34 and 35.
• Line 19 gets the URL and saves the response in response.
• Lines 20 through 31 create a file name based on the URL to the
web site (or uses save.html) and saves the output to that file.
• Line 33 prints the response content to the screen.
When I ran this program, this is what I saw:
D:\LeanPython\programs>python webtest.py
Web url to fetch:uktmf.com
Enter query string:q=node/5277
Save downloaded page to disk [y/n]?y

Requesting http://uktmf.com?q=node/5277
saving to uktmf.com.html ...
d:\LeanPython\programs>
The contents of the downloaded page were saved in uktmf.com.html.
The requests library is very flexible in that you can access the HTTP “post” verb using requests.post().
You can provide data to post commands as follows:
data = {'param1': 'value 1','param2': 'value 2'}
response = request.post(url,data=data)
Where web sites or web services require it, you can provide credentials for authentication and obtain the content as JSON data. You can provide custom headers to requests and see the headers returned in the response easily, too.
The requests module can be used to test web sites and web services quite comprehensively.

SEARCHING

Searching for Strings
Searching for text in strings is a common activity and the built-in string function find() is all you need for simple searches. It returns the position (offset) of the find or –1 if not found.
>>> txt="The quick brown fox jumps over the lazy dog"
>>> txt.find('jump')
20
>>> txt.find('z')
37
>>> txt.find('green')
-1
More Complex Searches
There are often circumstances when the search is not so simple. Rather than a simple string, we need to look for a pattern and extract the information we really want from the matched text. Suppose for example, we wanted to extract all the URLs in links on a web page. Here are some example lines of HTML text from a real web page.
1   <link rel="alternate" type="application/rss+xml" title="RSS: 40 newest
    packages" href="https://pypi.python.org/pypi?:action=packages_rss"/>
2   <link rel="stylesheet" media="screen" href="/static/styles/screen-
    switcher-default.css" type="text/css"/>
3   <li><a class="" href="/pypi?%3Aaction=browse">Browse&nbsp;packages</a>
    </li>
4   <li><a href="http://wiki.python.org/moin/CheeseShopTutorial">PyPI
    Tutorial</a></li>
There is quite a lot going on in the text here.
• Line 1 refers to an RSS feed.
• Line 2 has an href attribute, but it refers to a Cascading Style Sheets (CSS) file, not a link.

• Line 3 is a true link but the URL is relative; it doesn’t contain the
web site part of the URL.
• Line 4 is a link to an external site.
How can we hope to use some software to find the links that we care about? Well, this is where regular expressions come in.
Introducing Regular Expressions1
Regular expressions2 are a way of using pattern matching to find the text we are interested in. Not only are patterns matched, but the re module can extract the data we really want out of the matched text.
Many more examples could be written, and in fact there are whole books written about regular expressions (e.g., [16], [17]). There are many web sites, but the most useful is probably http://www.regular-expressions.info.
■ Note A regex is a string containing both text and special characters that define a pattern that the re functions can use for matching.
Simple Searches
The simplest regex is a text string that you want to find in another string, as shown in Table 10-1.
Table10-1. FindingaSimpleString
    Regex
jumps
The Queen
Pqr123
String Matched
jumps
The Queen
Pqr123
   Using Special Characters
There are special characters, listed in Table 10-2, that influence how the match is to be performed.
1The full documentation of the Python re module can be found at https://docs.python.org/3/ library/re.html. Regular expressions are an advanced topic in any programming language. 2Often, regular expression is shortened to regex.

Table10-2. UsingSpecialCharacters Symbols Description
literal Match a literal string
re1|re2 Match string re1 OR re2
. Match any single character (except \n)
^ Match start of string
$ Match end of string
* Match 0 or more occurrences of preceding regex
+ Match 1 or more occurrences of preceding regex
? Match 0 or 1 occurrences of preceding regex
{m,n} Match between m and n occurrences of the preceding regex (n optional)
[...] Match any character from character class
[x-y] Match any character from range
[^...] Do not match any character from character class
Example
Jumps
Yes|No
J.mps
^The
well$
[A-Z]*
[A-Z]+
[a-z0-9]?
[0-9]{2,4}
[aeiou]
[0-9],[A-Za-z]
[^aeiou]

       There are a number of special characters, listed in Table 10-3, that can be matched, too. Table10-3. SearchingwithSpecialCharacters
   Special Character
\d \w \s
Description
Match any decimal digit
Match any alphanumeric character Match any whitespace character
Example
BBC\d
Radio\w+
The\sBBC
    Table 10-4 gives some examples of regular expressions and the strings that they would match.
Table10-4. RegularExpressionsandMatchingStrings
  Regex
smith|jones
UNE..O
^The
end$
c[aiou]t
[dg][io][gp]
[a-d][e-i]
String(s) Matched
smith, jones
AnytwocharactersbetweenUNandO;e.g.,UNESCO, UNEzyO, UNE99O Any string that starts with The
Any string that ends with end
cat, cit, cot, cut
dig, dip, dog, dop, gig, gip, gog, gop
2 chars a/b/c/d followed by e/f/g/h/i
     
Finding Patterns in Text
Finding substrings in text is fine, but often we want to find patterns in text, rather than literal strings. Suppose we wanted to extract numeric values, phone numbers, or web site URLs from text. How do we do that? This is where the real power of regular expressions lies.
Here is an example regex:
\s[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}[\s]
Can you guess what it might find? It is a regex for finding e-mail addresses in text. At first glance, this looks pretty daunting, so let’s break it down into its constituent parts.3 First, the regex refers only to uppercase letters (to reduce the length of the regex), so this assumes that the string to be searched has already been uppercased.
There are six elements to this regex:
  1 \s
2   [A-Z0-9._%+-]+
3 @
4   [A-Z0-9.-]+
5 \.
6 [A-Z]{2,4}
7 [\s\.]
Leading whitespace One or more characters @ character
A-Z, 0-9.-
Dot character
2 to 4 text characters Whitespace or full stop
 Obviously, you need to know the rules for the pattern you search for and there are specific rules for the construction of e-mail addresses.
Here is the file remail.py.
1 import re # The RegEx library 2#
3   # our regular expression (to find e-mails)
4   # and text to search
5#
6   regex = '\s[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}[\s]'
7   text="""This is some text with x@y.z embedded e-mails
8   that we'll use as@example.com
9   some lines have no email addresses
3Note that this e-mail finder regex is not perfect. It would not find an address at the start of a string and it would ignore e-mail addresses with more than four characters in the trailing element
(e.g., '.mobile').

10  others@have.two valid email@addresses.com
11  The re module is awonderful@thing."""
12  print('** Search text ***\n'+text)
13  print('** Regex ***\n'+regex+'\n***')
14  #
15  #   uppercase our text
16  utext=text.upper()
17  #
18  #   perform a search (any emails found?)
19  s = re.search(regex,utext)
20  if s:
21      print('*** At least one email found "'+s.group()+'"')
22  #
23  #   now, find all matches
24  #
25  m = re.findall(regex,utext)
26  if m:
27 28
• •
• •
•
for match in m:
    print('Match found',match.strip())
Line 1 imports the modules we need.
Lines 6 through 13 define the text string to search and the regex we will use, then print them both.
Line 16 uppercases the text.
Lines 19 through 21 perform the simple search for the first (any) e-mail and print the result. Note that a match contains leading and trailing whitespace.
Lines 25 through 28 find all matches in the text and print the results.
Note that the regex matches the e-mail address and the whitespace boundaries. In Line 21 we print the match including the trailing newline, but in line 28 we strip off the spare characters.
What do we get when we run this code? Here is the result.
D:\LeanPython\programs\Python3>python remail.py
** Search text ***
This is some text with x@y.z embedded emails
that we'll use as@example.com
some lines have no email addresses
others@have.two valid email@addresses.com
The re module is awonderful@thing.
** Regex ***
\s[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}[\s]
***

*** At least one email found " AS@EXAMPLE.COM
"
Match found AS@EXAMPLE.COM
Match found OTHERS@HAVE.TWO
Match found EMAIL@ADDRESSES.COM
Capturing Parentheses
One more aspect we should mention is the use of parentheses. They can be searched for, like any other character, but they can also be used to delineate substrings that are matched, and the re module can capture these substrings and place them in a list returned by the search process. These so-called capturing parentheses feature in the following example and provide the URLs we want to extract from a page of HTML.
Finding Links in HTML
The following program downloads a single web page using the urllib library. The text of the downloaded HTML content is then searched using a complicated regular expression that extracts text links and provides the URL and the text of the link as seen by the user.
This program is called regex.py.
1   import urllib.request
2   import re         # The RegEx library
3#
4 # this code opens a connection to the leanpy.com website 5#
6   response = urllib.request.urlopen('http://leanpy.com')
7   data1 = str(response.read())           # put response text in data
8#
9 # our regular expression (to find links)
10 #
11 regex = '<a\s[^>]*href\s*=\s*\"([^\"]*)\"[^>]*>(.*?)</a>' 12 #
13 # compile the regex and perform the match (find all)
14 #
15 pm = re.compile(regex)
16 matches = pm.findall(data1)
17 #
18 #
19 #
20 #
21 #
22 for m in matches:
23      ms=''.join(('Link: "',m[0],'" Text: "',m[1],'"'))
24 print(ms)

The output of this program is shown here.
1   D:\LeanPython\programs>python re.py
2   200 OK
3   Link: "http://leanpy.com/" Text: "Lean Python"
4   Link: "#content" Text: "Skip to content"
5   Link: "http://leanpy.com/" Text: "Home"
6   Link: "http://leanpy.com/?page_id=33" Text: "About Lean Python"
7   Link: "http://leanpy.com/" Text: "<img src="http://leanpy.com/wp-
    content/uploads/2014/04/cropped-LeanPythonHeader.jpg" class="header-
    image" width="950" height="247" alt="" />"
8   Link: "http://leanpy.com/?p=1" Text: "The Lean Python Pocketbook"
9   Link: "http://leanpy.com/?p=1#respond" Text: "<span class="leave-
    reply">Leave a reply</span>"
10  Link: "http://leanpy.com/wp-content/uploads/2014/04/
    OnePieceCover1-e1396444631642.jpg" Text: "<img class="wp-image-17
    alignleft" alt="OnePieceCover" src="http://leanpy.com/wp-content/
    uploads/2014/04/OnePieceCover1-e1396444631642-633x1024.jpg" width="305"
    height="491" />"
11  Link: "http://leanpy.com/?cat=3" Text: "Lean Python Book"
12  Link: "http://leanpy.com/?tag=book" Text: "Book"
13  Link: "http://leanpy.com/?p=1" Text: "<time class="entry-date"
    datetime="2014-04-02T12:06:06+00:00">April 2, 2014</time>"
14  Link: "http://leanpy.com/?author=1" Text: "paulg"
15  Link: "http://leanpy.com/?p=1" Text: "The Lean Python Pocketbook"
16  Link: "http://leanpy.com/?cat=3" Text: "Lean Python Book"
17  Link: "http://leanpy.com/wp-login.php?action=register" Text: "Register"
18  Link: "http://leanpy.com/wp-login.php" Text: "Log in"
19  Link: "http://leanpy.com/?feed=rss2" Text: "Entries <abbr title="Really
    Simple Syndication">RSS</abbr>"
20  Link: "http://leanpy.com/?feed=comments-rss2" Text: "Comments <abbr
    title="Really Simple Syndication">RSS</abbr>"
21  Link: "http://wordpress.org/" Text: "WordPress.org"
22  Link: "http://wordpress.org/" Text: "Proudly powered by WordPress"
You can see that the program identifies all the links, but isn’t yet as smart as we might like.
• Line 4: This link uses a bookmark to the same page.
• Line 7: The link text is actually an image (do we need to worry
about that?).
Perhaps you could improve on the regex used, as an exercise.

DTABASES


Every application makes use of some form of (persistent) storage. We have looked at plain text files already. In this chapter we consider how a database, in particular a relational database, can be accessed and used by Python programs.
Python provides standard functions to access all of the popular databases. There are many open source and commercial database products and each one has its own adapter that allows Python to connect to and use data held in it. For our purposes, we use the SQLite database because it requires no other installed software.
SQLite
SQLite is a very lightweight serverless tool. The core Python product includes the SQLite adapter, allowing us to demonstrate the most important database features. SQLite behaves in the same way as bigger systems, but has low (near-zero) administrative overhead. A consequence of this is that SQLite can be used for development or prototyping and migrating to a more sophisticated database can be done later. For our purposes, SQLite provides all the features we require.
Database Functions
These are the key SQLite database functions we will be using:
# open (or create) a database file and return
# the connection
conn = sqlite3.connect(filename)
# executes a SQL statement
conn.executescript(sql)
# return a cursor
cursor = conn.cursor()
1This chapter presumes a knowledge of the relational database model and simple Structured Query Language (SQL) commands.

# execute the SQL query that returns rows of data
cursor.execute(sql)
# returns the data as a list of rows
rows = cursor.fetchall()
Connecting and Loading Data into SQLite
Here is an example program that creates a new database, a single table, inserts some data, performs a query, and attempts to insert a duplicate row (dbcreate.py).
1 import os
2   import sqlite3
3
4 db_filename='mydatabase.db' 5#
6 # if DB exists - delete it 7#
exists = os.path.exists(db_filename)
if exists:
8
9
10
11  #
12  #   connect to DB (create it if it doesn't exist)
13  #
14  conn = sqlite3.connect(db_filename)
15  #
16  #   create a table
17  #
18  schema="""create table person (
19    id integer primary key autoincrement not null,
20    name text not null,
21 dob date,
22    nationality text,
23    gender text)
24 """
25  conn.executescript(schema)
26  #
27  # create some data
28  #
29  people="""insert into person (name, dob,nationality,gender)
30  values ('Fred Bloggs', '1965-12-25','British','Male');
31  insert into person (name, dob,nationality,gender)
32  values ('Santa Claus', '968-01-01','Lap','Male');
33  insert into person (name, dob,nationality,gender)
34  values ('Tooth Fairy', '1931-03-31','American','Female');
35  """
36  conn.executescript(people)

37  #
38  #   execute a query
39  #
40  cursor = conn.cursor()
41  cursor.execute("select id, name, dob,nationality,gender from person")
42  for row in cursor.fetchall():
43
44
45  #
46  #
47  #
48  try:
49      dupe="insert into person (id, dob,nationality,gender) \
50      values (1,'1931-03-31','American','Female');"
51      conn.executescript(dupe)
52  except Exception as e:
53
• •
• •
• •
• •
•
print('Cannot insert record',e.__class__.__name__)
Lines 1 and 2 import the modules we need.
Lines 4 through 10 delete an old database file if one exists (be careful not to use the database created in this program for anything useful!).
Line 14 creates the database file.
In lines 18 through 25, the schema is a set of commands (a SQL script) that will create a new table.
Line 26 executes the SQL script to create the new table.
In lines 29 through 36 a new script is defined that includes the SQL commands to insert three records in the new table.
Line 37 executes the script.
In lines 40 through 44, to execute a query, you need to create a cursor, then execute the query using that cursor. This establishes the query content but doesn’t fetch the data. The cursor. fetchall() provides an iterable list of rows that are assigned to named variables, which are then printed.
Lines 48 through 53 set up an insert of a row and the try...except clauses catch errors on the insert. The insert SQL omits the name field deliberately to trigger an exception.
id, name, dob,nationality,gender = row
print("%3d %15s %12s %10s %6s" % (id, name, dob,nationality,gender))
attempt to insert a person with no name
The output from this program is shown hee.
D:\LeanPython\programs>python dbcreate.py
1 Fred Bloggs
2 Santa Claus
3 Tooth Fairy
1965-12-25
 968-01-01
1931-03-31
 British   Male
     Lap   Male
American Female
Cannot insert record IntegrityError

The exception caused by the insert statement on line 52 is triggered because the name field is not supplied (and must be not null).
In the following listing (dbupdate.py), we are passing two arguments to the program and using those in a SQL update command to change the nationality of a person.
1   import sqlite3
2 import sys
3#
4   #   arguments from command line
5   #   use: python dbupdate.py   1  Chinese
6#
7   db_filename = 'mydatabase.db'
8   inid = sys.argv[1]
9   innat = sys.argv[2]
10 #
11  #   execute update using command-line arguments
12  #
13  conn = sqlite3.connect(db_filename)
14  cursor = conn.cursor()
15  query = "update person set nationality = :nat where id = :id"
16  cursor.execute(query, {'id':inid, 'nat':innat})
17  #
18  #   list the persons to see changes
19  #
20  cursor.execute("select id, name, dob,nationality,gender from person")
21  for row in cursor.fetchall():
22 23
• •
id, name, dob,nationality,gender = row
print("%3d %15s %12s %10s %6s" % (id, name, dob,nationality,gender))
Lines 8 and 9 get the data from the command line: inid and innat.
Lines 13 through 16 do most of the work. Lines 13 and 14 set up the cursor. Line 15 is SQL as before, but the values to be used for the fields in the SQL (id and nat) are parameterized using the colon notation (:id and :nat). Line 16 executes the query and provides the actual values of the parameters using a dictionary as thesecondargumenttothecall{'id':inid, 'nat':innat}.
The output is shown here.
D:\LeanPython\programs>python dbupdate.py 1 Chinese
1 2 3
Fred Bloggs
Santa Claus
Tooth Fairy
1965-12-25
 968-01-01
1931-03-31
 Chinese   Male
     Lap   Male
American Female
The colon notation and dictionary can be used to parameterize any SQL call

(source) LEAN PYTHIN : PAUL GERRARD
