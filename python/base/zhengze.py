import re

pattern1="cat"
pattern2="bird"
string="dog runs to cat"
#print(pattern1 in string)
#print(pattern2 in string)

print(re.search(pattern1,string))
print(re.search(pattern2,string))

print('\n')
ptn=r"r[au]n"
print(re.search(ptn,"dog runs to cat"))

print('\n')
print(re.search(r"r[A-Z]n","dog runs to cat"))
print(re.search(r"r[a-z]n","dog runs to cat"))
print(re.search(r"r[0-9]n","dog runs to cat"))
print(re.search(r"r[0-9a-z]n","dog runs to cat"))

print('\n')
print(re.search(r"r\dn","run r4n"))#\d 数字
print(re.search(r"r\Dn","run r4n"))#\D非数字

#\s 所有空白符  \S所有非空白符
print('\n')
print(re.search(r"r\sn","r\nn r4n"))
print(re.search(r"r\Sn","r\nn r4n"))

print('\n')
match = re.search(r"(\d+), Date: (.+)", "ID: 021523, Date: Feb/12/2017")
print(match.group())
print(match.group(1))
print(match.group(2))

print('\n')
match1=re.search(r"(?P<id>\d+), Date: (?P<date>.+)", "ID: 021567, Date: July/11/2019")
print(match1.group('id'))
print(match1.group('date'))

print('\n')
print(re.findall(r"r[ua]n","run ran ren"))

print('\n')
print(re.sub(r"r[au]ns","catches","dog runs to cat"))

print('\n')
print(re.split(r"[,;.]","a;b,c.d;e"))
      
