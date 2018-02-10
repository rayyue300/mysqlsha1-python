# Project Title

mysqlsha1-python

## Project Requirement

Given the MySQL password hashes, find the original passwords.

## Prerequisites

Python 2.7
(Does not work in Python 3)

## In-code Parameters
Define the given hashes:
```
dict = {
    'D35DB127DB631E6E27C6B75E8D376B04F64FAF83': 'root',
}
```

Define the range of password length:
```
for length in range(4,10):
```

Define the set of possible characters:
```
'abcdefghijklmnopqrstuvwxyz'
```

## Output
```
iisct C2D24DCA38E9E862098B85BF0AB35CAA52803797
abcdef D5D82EF0B0A344A314E3B3E8D1E78A4697B97A53
```
Long time later:
```
computer 81101DED975D54BD76A3C8EAD293597AE9BB143F
```