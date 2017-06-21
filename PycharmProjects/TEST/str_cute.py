# coding:utf-8

import re

#1、str.split不支持正则及多个切割符号，不感知空格的数量，比如用空格切割，会出现下面情况。
s1="aa bb  cc"
print s1.split(' ')  ##['aa', 'bb', '', 'cc']

#2、re.split，支持正则及多个字符切割
line="abc aa;bb,cc | dd(xx).xxx 12.12'\txxxx"
print line

##按空格切
print re.split(r' ', line) ##['abc', 'aa;bb,cc', '|', 'dd(xx).xxx', "12.12'\txxxx"]

##加将空格放可选框内[]
print re.split(r'[ ]', line) ##['abc', 'aa;bb,cc', '|', 'dd(xx).xxx', "12.12'\txxxx"]

##按所有空白字符来切割：\s（[\t\n\r\f\v]）\S（任意非空白字符[ ^\t\n\r\f\v]

print re.split(r'[\s]', line) ##['abc', 'aa;bb,cc', '|', 'dd(xx).xxx', "12.12'", 'xxxx']

##多字符匹配
print re.split(r'[;,]', line) ##['abc aa', 'bb', "cc | dd(xx).xxx 12.12'\txxxx"]
print re.split(r'[;,\s]', line) ##['abc', 'aa', 'bb', 'cc', '|', 'dd(xx).xxx', "12.12'", 'xxxx']

##使用括号捕获分组的适合，默认保留分割符
print re.split('([;])', line) ##['abc aa', ';', "bb,cc | dd(xx).xxx 12.12'\txxxx"]

##去掉分隔符，加?:
print re.split(r'(?:;)', line) ##['abc aa', "bb,cc | dd(xx).xxx 12.12'\txxxx"]
print re.split(r'[;]',line)  ##['abc aa', "bb,cc | dd(xx).xxx 12.12'\txxxx"]