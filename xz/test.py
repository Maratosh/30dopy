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

