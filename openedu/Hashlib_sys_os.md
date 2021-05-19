### Encrypting and encoding strings
#********************************************************
import hashlib

h1 = hashlib.md5(b'I love Leisan')

h1.hexdigest()
'2d7d3ad943e767bf6dad96b73727bad5'

h1
<md5 HASH object @ 0x7efe80d44c30>
#**************************

>>> h2 = hashlib.sha512('I love Leisan'.encode())
>>> h2
<sha512 HASH object @ 0x7efe809124d0>
>>> h2.hexdigest()
'c8145539c15c1eeab0add4ff1fdf32980c80548cb3afd4df424dffabc4163fb4e7f7bf94e99341aac5af49b7ef03f753acd0374abfe278c19d2f525f2b995ccd'
>>> h3 = hashlib.sha512(b'I love Leisan')
>>> h3.hexdigest()
'c8145539c15c1eeab0add4ff1fdf32980c80548cb3afd4df424dffabc4163fb4e7f7bf94e99341aac5af49b7ef03f753acd0374abfe278c19d2f525f2b995ccd'
>>> 
#**************************

#********************************************************

>>> pswd = hashlib.md5(input('enter password: ').encode())
enter password: 1234
>>> pswd.hexdigest()
'81dc9bdb52d04dc20036dbd8313ed055'

#**************************
>>> p1 = hashlib.md5(b'P@ssw0rd').hexdigest()
>>> p2 = hashlib.md5(input('enter password: ').encode())
enter password: P@ssw0rd
>>> if p1 == p2.hexdigest(): print('Ok')
... 
Ok
>>> 
#********************************************************


>>> l = 'Лейсан'
>>> l.encode('utf-8')
b'\xd0\x9b\xd0\xb5\xd0\xb9\xd1\x81\xd0\xb0\xd0\xbd'
>>> 
>>> b'\xd0\x9b\xd0\xb5\xd0\xb9\xd1\x81\xd0\xb0\xd0\xbd'.decode('utf-8')
'Лейсан'

>>> l.encode('koi8-r')
b'\xec\xc5\xca\xd3\xc1\xce'
>>>
>>> l.encode('cp1251')
b'\xcb\xe5\xe9\xf1\xe0\xed'

### os, sys


#********************************************************
with open('test1.txt', 'w') as file_to_write:
    with open('test2.txt','r') as file_to_read:
        for line in file_to_read:
            line = line.split()
            line.sort()
            print(line)
            line1 = ' '.join(line)
            print(line1)

            file_to_write.write(line1)
        file_to_read.close()
        file_to_write.close()
#********************************************************

import os

def f1(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir,name)
        #print(path)
        if os.path.isfile(path):
            print(path)
        else:
            f1(path)

f1(os.getcwd())
#********************************************************

>>> os.makedirs('one/two/three')
>>> os.path.exists('one/two/three')
True
#********************************************************

import shutil

>>> os.listdir()
['__pycache__', 'test1.txt', 'test2.txt', 'hw.py', 'one']
>>> os.listdir('one')
['two']
>>> os.listdir('one/two')
['three']
>>> shutil.copy('test1.txt','one/test1.txt')
'one/test1.txt'
>>> os.listdir('one')
['test1.txt', 'two']

#********************************************************
>>> my_hath = '/var/www/html/'
>>> my_file = 'index.html'
>>> fulname = os.path.join(my_hath, my_file)
>>> fulname
'/var/www/html/index.html'

#********************************************************

>>> filenames = os.listdir()
>>> for i in filenames:
	os.path.abspath(i)

	
'/home/marat/Documents/python/openedu1/week3/test/__pycache__'
'/home/marat/Documents/python/openedu1/week3/test/test1.txt'
'/home/marat/Documents/python/openedu1/week3/test/test2.txt'
'/home/marat/Documents/python/openedu1/week3/test/hw.py'
'/home/marat/Documents/python/openedu1/week3/test/one'
#********************************************************


#### HW

import hashlib

a = input().encode()
#a = b'apple'
hashes = ("md5", "sha1", "sha224", "sha256", "sha384", "sha512")

print(type(hashes))
dct = {}
        
for i in hashes:
    #print(i)
    my_hash = hashlib.new(i)
    my_hash.update(a)
    print(i, my_hash.hexdigest())
