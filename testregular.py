#测试正则表达式 
#\. 表示小数点
# . 表示任意一个字符
import re

teststrings = '743.5.9'
backslashdot = re.search('\.',teststrings)#匹配小数点
testdot = re.search('.',teststrings)#匹配任意字符
if backslashdot == None:
    print('没有找到小数点')
else:
    searchresult = backslashdot.group(0)
    print('匹配小数点的情况 ',backslashdot)
    print('第1个匹配的小数点是：',searchresult)
    
if testdot == None:
    print('没有找到任意字符')
else:
    searchresult = testdot.group(0)
    print('匹配任意一个字符的情况 ',testdot)
    print('第1个匹配的任意字符是：',searchresult)
    
teststrings2 = '74359L12'
backslashdot2 = re.search('^(\-)?\d+(\.\d{1,2})?$',teststrings2)#带1-2位小数的正数或负数
testdot2 = re.search('^[0-9]+(.[0-9]{1,3})?$',teststrings2)#有1-3位小数的正实数，
#不对，从74359L3 输出匹配来看，点号在这里是任意符合，而不是小数点
testdot3 = re.search('^[0-9]+(\.[0-9]{1,3})?$',teststrings2)#有1-3位小数的正实数，这里才是小数点

if backslashdot2 == None:
    print('没有找到匹配的小数点')
else:
    searchresult = backslashdot2.group(0)
    print('匹配小数点的情况 ',backslashdot2)
    print('第1个匹配的.是：',searchresult)
    
if testdot2 == None:
    print('没有找到任意字符')
else:
    searchresult = testdot2.group(0)
    print('匹配任意一个字符的情况 ',testdot2)
    print('第1个匹配的任意字符是：',searchresult)
    
if testdot3 == None:
    print('没有找到小数点')
else:
    searchresult = testdot3.group(0)
    print('匹配小数点的情况 ',testdot3)
    print('第1个匹配的小数点是：',searchresult)