Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> phone = {"kim":"1111", "lee":"2222"}
>>> 
>>> phone
{'kim': '1111', 'lee': '2222'}
>>> "kim" in phone
True
>>> "kang" in phone
False
>>> "kang" not in phone
True
>>> "Kim" in phone
False
>>> p = phone
>>> p
{'kim': '1111', 'lee': '2222'}
>>> id(phone), id(p)
(2443863452928, 2443863452928)
>>> a = [1, 2, 3]
>>> b = a
>>> a[0] = 38
>>> a
[38, 2, 3]
>>> b
[38, 2, 3]
>>> id(phone), id(p)
(2443863452928, 2443863452928)
>>> id(a), id(b)
(2443863612672, 2443863612672)
>>> a = [100, 200, 300]
>>> b = a[:]
>>> a[0] = 101
>>> a
[101, 200, 300]
>>> b
[100, 200, 300]
>>> id(a), id(b)
(2443863612928, 2443863611776)
>>> 