#/usr/bin/env python
import re

'''
常见字符：
.     默认匹配除\n之外的任意一个字符
+     匹配前面字符出现一次或者多次
?     匹配前一个字符一次或者0次
.+    匹配任意字符任意次
^     匹配字符开头--->同\A
$     匹配以字符结尾--->同\Z
{m}   匹配前面字符出现m次
{n,m} 匹配前面字符出现n次~m次
|     或者
()    分组匹配  re.findall('abc(2)','abccab')
\w    匹配字母 --->[a-zA-Z]
[a-zA-z0-9] 匹配数字和字母----> \W
\d     匹配数字0-9
\D     匹配非数字
\s     匹配空白字符、\t、\n、\r
'''
print(re.match('^wang\d+','wang123zhen123'))
print('匹配到的内容：',re.match('^wang\d+','wang123zhen123').group())
print(re.match('6','wangzhen123'))