https://stepic.org/media/attachments/course67/week_2.html  ﻿

n = int(input('enter the number: '))
#c = 1
#while c <= n:
#    print('*' * c)
#    c += 1
###################

stars = '*'
while len(stars) <= n:
    print(stars)
    stars += '*'
#**********************************************************************88
a = int(input('a: '))
b = int(input('b: '))
s = 0
i = a
while i <= b:
     s += i
     i += 1
print(s)
#*********************************************************************
a = int(input('a: '))
b = int(input('b: '))
d = 1
while d % a != 0 or d % b != 0:
    d += 1
print(d)
#***************************************

a = int(input())
b = int(input())
c = int(input())
d = int(input())
for j in range(c, d+1):
    print(' ', '\t', j, end=' ')
print()
for i in range(a, b+1):
    print(i, end=' ')
    for j in range(c, d+1):
        print(' ', '\t', i * j, end=' ')
    print()
    
 a, b, c, d = (int(input()) for x in range(4))
print('', *range(c,d+1), sep='\t')
for x in range(a, b+1):
    print(x, *[y*x for y in range(c, d+1)], sep='\t')   
    
#******************************************************************
import time
import random
import string
s = ''.join(random.choices(string.ascii_uppercase, k=1000))
#slices
start = time.time()
print(s == s[::-1])
print('slices ---- %s sec ----' %(time.time() - start))
#cicle
start = time.time()
is_palinom = True
i = 0
j = len(s) - 1
while i < j:
    if s[i] != s[j]:
        is_palinom = False
    i += 1
    j -= 1
print(is_palinom)
print('cicle  ---- %s sec ----' %(time.time() - start))

#Strings EBAT 
st = 'aaaabbcaa.' # add '.'

s = 1
leng = len(st)
# for a
for i in range(leng-1):
    if st[i+1] == st[i]:
        s += 1
    else:
        print(st[i]+str(s), end='')
        s = 1
#################
a = [int(i) for i in input().split()]
s = 0
for i in a:
    s += i
print(s)

#########################
#a = [int(i) for i in input().split()]
a = [4, 8, 0, 3, 4, 2, 0, 3]
b = []

for i in range(len(a)):
    if len(a) == 1:
        b = a
        break
    elif i == (len(a)-1):
        b.append(a[0]+ a[i-1])
    else:
        b.append(a[i-1] + a[i+1])

for i in b:
    print(i, end=' '
#################################
     

