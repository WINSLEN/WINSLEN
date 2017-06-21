# coding:utf-8

#字符串连接
##方法1： 用字符串的join方法
a = ['a','b','c','d']
content = '0'
contents = content.join(a)
#print contents ##a0b0c0d

##方法2： 用字符串的替换占位符替换
a = ['a','b','c','d']
content = ''
content = '%s%s%s%s' % tuple(a)
#print content ##abcd

#字符串截取
s = 'ilovepython'
#print s[0],s[-1],s[1:-6] ##i n love

##字符串替换
#字符串替换可以用内置的方法和正则表达式完成。
#1.用字符串本身的replace方法:
a = 'hello word'
b = a.replace('word','python')
#print b ##hello python

#2.用正则表达式来完成替换:
import re
a = 'hello word'
strinfo = re.compile('word')
b = strinfo.sub('python',a)
#print b ##hello python
#re.sub(pattern, repl, string, count=0, flags=0)
#pattern： 是re.compile()方法生成Pattern类型，也就是索要匹配的模式。
#repl ： 可以是一段字符串，或者是一个方法
#string： 需要被匹配和替换的原字符串
#count： 指的是最大的可以被替换的匹配到的字符串的个数，默认为0，就是所有匹配到的字符串。
#flags ： 标志位

#print re.sub("word","python",a) ##hello python


##字符串比较
#cmp方法比较两个对象，并根据结果返回一个整数。cmp(x,y)如果X< Y,返回值是负数 如果X>Y 返回的值为正数。
sStr1 = 'strch'
sStr2 = 'strchr'
#print cmp(sStr1,sStr2) ##-1

##字符串相加
#我们通过操作符号+来进行字符串的相加，不过建议还是用其他的方式来进行字符串的拼接，这样效率高点。
#原因：在循环连接字符串的时候，他每次连接一次，就要重新开辟空间，然后把字符串连接起来，
#再放入新的空间，再一次循环，又要开辟新的空间，把字符串连接起来放入新的空间，
#如此反复，内存操作比较频繁，每次都要计算内存空间，然后开辟内存空间，再释放内存空间，效率非常低。
sStr1 = 'strch'
sStr2 = 'strchr'
newstr = sStr1 + sStr2
#print newstr ##strchstrchr

##字符串查找
#python 字符串查找有4个方法，1 find,2 index方法，3 rfind方法,4 rindex方法。
#1.find()方法：
info = 'abca'
#print info.find('a')##从下标0开始，查找在字符串里第一个出现的子串，返回结果：0

info = 'abca'
#print info.find('a',1)##从下标1开始，查找在字符串里第一个出现的子串：返回结果3

info = 'abca'
#print info.find('333')##返回-1,查找不到返回-1

#2.index()方法：
#python 的index方法是在字符串里查找子串第一次出现的位置，类似字符串的find方法，不过比find方法更好的是，如果查找不到子串，会抛出异常，而不是返回-1
info = 'abca'
#print info.index('a') ##1
#print info.index('33') ##异常error

##字符串分割
#字符串分割，可以用split,rsplit方法，通过相应的规则来切割成生成列表对象
#str.split不支持正则及多个切割符号，不感知空格的数量，比如用空格切割
info = 'name:haha,age:20$name:python,age:30$name:fef,age:55'
content = info.split('$')
print content