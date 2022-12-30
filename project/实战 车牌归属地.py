lst=['京A8888','津B6666','吉A7777']
for item in lst:
    area=item[0:1]
    print(item,'归属地',area)

s='HELLOpython,helloJAVA,HELLOphp'
word=input('请输入要统计的字符：')
word1=word.upper()
print('{0}在{1}中一共出现了{2}'.format(word,s,s.upper().count(word1)))