# -*- coding: utf-8 -*-
"""ADM-HW1-EG.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hZspjOlfmbZf1qkj6KBSQbe1S2E3dbEr

#Say "Hello, World!" With Python
"""

print("Hello, World!")

"""#Python If-Else

"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if not n % 2 == 0:
    print("Weird")
else:
    if n in range(2,6):
        print("Not Weird")
    if n in range(6,21):
        print("Weird")
    if n > 20:
        print("Not Weird")

"""#Arithmetic Operators

"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
def somma(a,b):
        print(a+b)
def differenza(a,b):
        print(a-b)
def prodotto(a,b):
        print(a*b)
somma(a,b)
differenza(a,b)
prodotto(a,b)

"""#Python: Division

"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a//b)
print(a/b)

"""#Loops"""

if __name__ == '__main__':
    n = int(input())

for i in range(0,n):
    print(i**2)

"""#Write a function

"""

def is_leap(year):
    if year % 4 == 0:
      if year % 100 == 0:
        if year % 400 == 0:
          return True
        else:
          return False
      else:
        return True
    else:
        return False

"""#Print Function

"""

if __name__ == '__main__':
    n = int(input())

l = ""
for i in range(1,n+1):
  l += str(i)

print(l)

"""#List Comprehensions

"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

l = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                l.append([i,j,k])
print(l)

"""#Find the Runner-Up Score!"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
lis = []
for i in arr:
  if i != max(arr):
    lis.append(i)
mas2 = max(lis)
print(mas2)

"""#Nested Lists"""

if __name__ == '__main__':
    rec = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        rec.append([name,score])
rec2=[]
for i in rec:
  rec2.append(i[1])
rec3 = []
for i in rec2:
    if i == min(rec2):
        rec3.append(i)
rec4 = []
for i in rec2:
    if i != rec3[0]:
        rec4.append(i)
names = []
for i in rec:
  if i[1] == min(rec4):
    names.append(i[0])
names.sort()
for i in names:
    print(i)

"""#Finding the percentage"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    def mean(list):
      return sum(list)/len(list)
    for key in student_marks:
      if key == query_name:
        media = mean(student_marks[key])
        print(f"{media:.2f}")

"""#Lists

"""

l = []
for n in range(int(input())):
    command = str(input()).split()
    if command[0] == "append":
        l.append(int(command[1]))
    elif command[0] == "insert":
        l.insert(int(command[1]), int(command[2]))
    elif command[0] == "remove":
        l.remove(int(command[1]))
    elif command[0] == "sort":
        l.sort()
    elif command[0] == "reverse":
        l.reverse()
    elif command[0] == "pop":
        l.pop()
    elif command[0] == "print":
        print(l)

"""#Tuples

"""

if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))

"""#sWAP cASE

"""

def swap_case(s):
    result = ""
    for i in s:
        if i.islower():
            result += i.upper()
        else:
            result += i.lower()
    return result

"""#String Split and Join

"""

def split_and_join(line):
    if isinstance(line,str):
      line1 = line.split(" ")
      line2 = "-".join(line1)
    return line2

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

"""#What's Your Name?

"""

def print_full_name(first, last):
    print("Hello", first, last+"! You just delved into python.")

"""#Mutations"""

def mutate_string(string, position, character):
    string = string[:position]+str(character)+string[position+1:]
    return string

"""#Find a string

"""

def count_substring(string, sub_string):
    count = 0
    start = 0
    while True:
        pos = string.find(sub_string, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1
    return count

"""#String Validators

"""

if __name__ == '__main__':
    s = input()
    for i in s:
        if i.isalnum():
            print(True)
            break
    if not any(i.isalnum() for i in s):
            print(False)

    for i in s:
        if i.isalpha():
            print(True)
            break
    if not any(i.isalpha() for i in s):
            print(False)

    for i in s:
        if i.isdigit():
            print(True)
            break
    if not any(i.isdigit()for i in s):
            print(False)

    for i in s:
        if i.islower():
            print(True)
            break
    if not any(i.islower() for i in s):
            print(False)
    for i in s:
        if i.isupper():
            print(True)
            break
    if not any(i.isupper()for i in s):
            print(False)

"""#Text Alignment

"""

thickness = int(input())
c = 'H'

for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

"""#Text Wrap

"""

def wrap(string, max_width):
    substrings = textwrap.wrap(string, width=max_width)
    for i in substrings:
        if len(i) == max_width:
            print(i)
        if len(i) < max_width:
            return i

"""#Designer Door Mat

"""

n,m=map(int,input().split())
i=0
for i in range(n):
    if i<((n-1)/2):
        print((("."+"|"+".")*(2*i+1)).center(m,"-"))
    elif i==((n-1)/2):
        print("WELCOME".center(m,"-"))
    else:
        print((("."+"|"+".")*(2*((n-1)-i)+1)).center(m,"-"))

"""#String Formatting

"""

def print_formatted(number):
    max_width = len(bin(number)[2:])
    for i in range(1, number + 1):
        decimal = str(i).rjust(max_width)
        octal = str(oct(i)[2:]).rjust(max_width)
        hexadecimal = str(hex(i)[2:]).rjust(max_width).upper()
        binary = str(bin(i)[2:]).rjust(max_width)

        print(decimal, octal, hexadecimal, binary)

"""#Alphabet Rangoli

"""

def print_rangoli(size):
    a=[chr(i) for i in range(97,123)]
    t=1
    l=[]
    ch=a[n-t]
    for i in range(1,n):
        print("-".join(ch).center(1+4*(n-1),"-"))
        l.append("-".join(ch).center(1+4*(n-1),"-"))
        ch=ch[:i]+a[n-t-1]+ch[-i:]
        t+=1
    print("-".join(ch).center(1+4*(n-1),"-"))
    for i in l[::-1]:
        print(i)

"""#Capitalize!

"""

def solve(s):
    l =[]
    for i in s:
        l.append(i)
    l[0] = l[0].upper()
    for i in range(len(l)):
      if l[i] == " ":
        l[i+1] = l[i+1].upper()
    return("".join(l))

"""#The Minion Game

"""

def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    n = len(string)
    for i in range(n):
        if string[i] in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i
    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

"""#Merge the Tools!

"""

def merge_the_tools(string, k):
    i = 0
    while i < len(string):
      substring = string[i:i+k]
      i += k
      result = ""
      seen = set()
      for char in substring:
        if char not in seen:
          result += char
          seen.add(char)
      print(result)

"""#Introduction to Sets

"""

def average(array):
   set1 = set(array)
   mean = sum(set1)/len(set1)
   return mean

"""#No Idea!

"""

n_m =  map(int,input().split())
arr = map(int,input().split())
setA = set(map(int,input().split()))
setB = set(map(int,input().split()))
happy = 0
for i in arr:
  if i in setA:
    happy += 1
  if i in setB:
    happy -= 1
print(happy)

"""#Symmetric Difference

"""

m = int(input())
a = set(map(int,input().split()))
n = int(input())
b = set(map(int,input().split()))
set1 = a.difference(b)
set2 = b.difference(a)
set3 = set1.union(set2)
for i in sorted(set3):
    print(i)

"""#Set .add()"""

n = int(input())
set1 = set()
for _ in range(n):
    country = input().strip()
    set1.add(country)
print(len(set1))

"""#Set .discard(), .remove() & .pop()"""

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    command = list(input().split())
    match command[0]:
        case 'pop':
            s.pop()
        case 'remove':
            if int(command[1]) in s:
                s.remove(int(command[1]))
        case 'discard':
            s.discard(int(command[1]))

print(sum(s))

"""#Set .union() Operation

"""

n = int(input())
s1 = set(map(int, input().split()))
b = int(input())
s2 = set(map(int, input().split()))
print(len(s1.union(s2)))

"""#Set .intersection() Operation

"""

n = int(input())
s1 = set(map(int, input().split()))
b = int(input())
s2 = set(map(int, input().split()))
s3 = s1.intersection(s2)
print(len(s3))

"""#Set .difference() Operation

"""

n = int(input())
s1 = set(map(int, input().split()))
b = int(input())
s2 = set(map(int, input().split()))
s3 = s1.difference(s2)
print(len(s3))

"""#Set .symmetric_difference() Operation

"""

n = int(input())
s1 = set(map(int, input().split()))
b = int(input())
s2 = set(map(int, input().split()))
s3 = s1.symmetric_difference(s2)
print(len(s3))

"""#Set Mutations"""

n = int(input())
a = set(map(int, input().split()))
for _ in range(int(input())):
    cmd = input().split()
    command = cmd[0]
    method = set(map(int, input().split()))
    if command == "intersection_update":
        a.intersection_update(method)
    elif command == "update":
        a.update(method)
    elif command == "symmetric_difference_update":
        a.symmetric_difference_update(method)
    elif command == "difference_update":
        a.difference_update(method)
print(sum(a))

"""#The Captain's Room"""

k = int(input())
room_list = list(map(int, input().split(" ")))
room_set = set(room_list)
for i in room_set:
    room_list.remove(i)
    if i not in room_list:
         print(i)

"""#Check Subset

"""

T = int(input())
for i in range(T):
    a = int(input())
    A = set(map(int, input().split()))
    b = int(input())
    B = set(map(int,input().split()))
    if A <= B:
        print(True)
    else:
        print(False)

"""#Check Strict Superset"""

a = set(map(int, input().split()))
for _ in range(int(input())):
    b = set(map(int, input().split()))
    if not a.issuperset(b):
        print(False)
        exit()
print(True)

"""#collections.Counter()

"""

X = int(input())
l = list(map(int,input().split()))
N = int(input())
earnings = 0
for i in range(N):
    size_price = list(map(int,input().split()))
    if size_price[0] in l:
        l.remove(size_price[0])
        earnings += size_price[1]
    else:
        earnings += 0
print(earnings)

"""#DefaultDict Tutorial

"""

n_m = list(map(int,input().split()))
A = []
for i in range(n_m[0]):
    A.append(input())
B = []
for j in range(n_m[1]):
    B.append(input())
for k in range(len(B)):
    l = []
    trovato = False
    for p in range(len(A)):
        if B[k] == A[p]:
            l.append(p+1)
            trovato = True
    if not trovato:
        print(-1)
    else:
        print(" ".join(map(str,l)))

"""#Collections.namedtuple()

"""

from collections import namedtuple
n = int(input())
columns = input().split()
Student = namedtuple("Student", columns)
sum1 = sum(int(Student(*input().split()).MARKS) for _ in range(n))
average = sum1/n
print(average)

"""#Collections.OrderedDict()

"""

from collections import OrderedDict

N = int(input())
ordered_dictionary = OrderedDict()

for i in range(N):
    nome, prezzo = input().rsplit(' ', 1)
    prezzo = int(prezzo)
    if nome in ordered_dictionary:
        ordered_dictionary[nome] += prezzo
    else:
        ordered_dictionary[nome] = prezzo

for name, price in ordered_dictionary.items():
    print(f"{name} {price}")

"""#Word Order

"""

n = int(input())
words = {}
for _ in range(n):
    word = input()
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

print(len(words))

print(' '.join(map(str, words.values())))

"""#Collections.deque()

"""

from collections import deque
d = deque()
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == 'append':
        d.append(int(command[1]))
    elif command[0] == 'appendleft':
        d.appendleft(int(command[1]))
    elif command[0] == 'pop':
        d.pop()
    elif command[0] == 'popleft':
        d.popleft()
print(' '.join(map(str, d)))

"""#Company Logo

"""

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


if __name__ == '__main__':
    s = sorted(input())
    c = Counter(s).most_common(3)
    for i,j in c:
        print(i,j)

"""#Piling Up!

"""

T = int(input())

for _ in range(T):
    n = int(input())
    blocks = list(map(int, input().split()))

    left = 0
    right = n-1
    last_picked = float('inf')
    is_possible = True

    while left <= right:
        if blocks[left] >= blocks[right]:
            current = blocks[left]
            left += 1
        else:
            current = blocks[right]
            right -= 1

        if current > last_picked:
            is_possible = False
            break

        last_picked = current

    if is_possible:
        print("Yes")
    else:
        print("No")

"""#Calendar Module

"""

import calendar
date_input = input().split()
day = int(date_input[0])
month = int(date_input[1])
year = int(date_input[2])
day_of_week = calendar.weekday(year, day, month)
days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
print(days[day_of_week])

"""#Time Delta"""

import math
import os
import random
import re
import sys
from datetime import date, time, datetime

def time_delta(t1, t2):
    date_format = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, date_format)
    dt2 = datetime.strptime(t2, date_format)
    delta_seconds = int(abs(dt1-dt2).total_seconds())
    return str(delta_seconds)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()

"""#Exceptions

"""

t = int(input())
for i in range(t):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)

"""#Zipped!

"""

N, X = map(int, input().split())
marks = []
for i in range(X):
    marks.append(list(map(float, input().split())))

l = list(zip(*marks))

for j in range(N):
    average = sum(list(l[j]))/X
    print(average)

"""#Athlete Sort"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    for i in sorted(arr, key = lambda x : x[k]):
        print(' '.join(str(y) for y in i))

"""#ginortS

"""

s = str(input())
lower = []
upper = []
odd = []
even = []
for c in s:
    if c.islower():
        lower.append(c)
    elif c.isupper():
        upper.append(c)
    elif c.isdigit():
        if int(c) % 2 != 0:
            odd.append(c)
        else:
            even.append(c)
lower.sort()
upper.sort()
odd.sort()
even.sort()
print(''.join(lower + upper + odd + even))

"""#Map and Lambda Function

"""

cube = lambda x: x**3

def fibonacci(n):
    a = [0, 1]
    if n == 0:
        return []
    if n == 1:
        return [0]
    for i in range(2, n):
        nums = a[-1] + a[-2]
        a.append(nums)
    return a

"""#Detect Floating Point Number

"""

T = int(input())
for i in range(T):
    string = input()
    flag = True
    try:
        float_string = float(string)
        if string.count(".")==0:
            flag = False
    except:
        flag = False

    print(flag)

"""#Re.split()"""

regex_pattern = r"[.,]"

"""#Group(), Groups() & Groupdict()"""

import re
s = input()
r = re.search(r'([a-zA-Z0-9])\1', s)
if r:
    print(r.group(1))
else:
    print(-1)

"""#Re.findall() & Re.finditer()"""

import re
s = input()
r = re.findall(r'(?<=[^aeiouAEIOU])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU])',s)
if r:
    for i in r:
        print(i)
else:
    print(-1)

"""#Re.start() & Re.end()"""

import re
s = input()
k = input()

def results(s, k):
    same = re.finditer(fr'(?=({k}))', s)
    x = [(match.start(1), match.end(1)-1) for match in same]
    return x if x else [(-1, -1)]


if results(s, k):
    for i in results(s, k):
        print(i)
else:
    print((-1, -1))

"""#Regex Substitution"""

import re
n = int(input())
for i in range(n):
  s = input()
  s = re.sub(r"(?<= )&&(?= )", "and", s)
  s = re.sub(r"(?<= )\|\|(?= )", "or", s)
  print(s)

"""#Validating Roman Numerals"""

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

"""#Validating phone numbers"""

import re
n = int(input())
for i in range(n):
    s = input().strip()
    if re.match(r'^[789]\d{9}$', s):
        print("YES")
    else:
        print("NO")

"""#Validating and Parsing Email Addresses"""

import email.utils
import re
n= int(input())
for i in range(n):
    add = email.utils.parseaddr(input())
    check = re.match(r'^[a-zA-Z][\w._-]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$', add[1])
    if check:
        print(email.utils.formataddr(add))

"""#Hex Color Code"""

import re
n = int(input())
for i in range(n):
    CSS = input().strip()
    a = re.findall(r"(#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6})(?=[;),])", CSS)
    if a :
        print(*a, sep="\n")

"""#HTML Parser - Part 1"""

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        self.print_tag_attrs(attrs=attrs)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        self.print_tag_attrs(attrs=attrs)

    def print_tag_attrs(self, attrs):
        [print(f"-> {i[0]} > {i[1]}") for i in attrs]

parser = MyHTMLParser()
parser.feed(''.join([input() for _ in range(int(input()))]))

"""#HTML Parser - Part 2"""

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)

if __name__ == "__main__":
    n = int(input())
    html_content = ""
    for _ in range(n):
        html_content += input() + "\n"

    parser = MyHTMLParser()
    parser.feed(html_content)

"""#Detect HTML Tags, Attributes and Attribute Values

"""

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            [print(f'-> {x[0]} > {x[1]}') for x in attrs]
    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs:
            [print(f'-> {y[0]} > {y[1]}') for y in attrs]

html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

"""#Validating UID"""

import re
check = r"^(?=([A-Z]*[a-z\d]){2})(?=([a-zA-Z]*[\d]){3})(([a-zA-Z0-9])(?!.*\4)){10}$"
t = int(input())
for i in range(t):
    uid = input()
    x = re.match(check, uid)
    if x:
        print("Valid")
    else:
        print("Invalid")

"""#Validating Credit Card Numbers"""

import re
n = int(input())
check = r"(?=[456]\d{3}(-?\d{4}){3}$)(?!.*(.)-?(\2-?){3})"
for i in range(n):
    cr = input()
    x = re.match(check, cr)
    if x:
        print("Valid")
    else:
        print("Invalid")

"""#Validating Postal Codes"""

regex_integer_in_range = r"^([1-9][0-9]{5})$"
regex_alternating_repetitive_digit_pair = r"(?=(.)(.)(\1))"

"""#Matrix Script"""

import math
import os
import random
import re
import sys
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
de = ""
for i in range(m):
    for j in range(n):
        de += matrix[j][i]
print(re.sub(r"(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])", " ", de))

"""#XML 1 - Find the Score"""

def get_attr_number(node):
    total_attributes = len(node.attrib)
    for child in node:
        total_attributes += get_attr_number(child)
    return total_attributes

"""#XML2 - Find the Maximum Depth"""

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if level > maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)

"""#Standardize Mobile Number Using Decorators"""

def wrapper(f):
    def fun(l):
        striped = sorted([i[-10:] for i in l])
        for i in striped:
            print("+91 "+i[0:5]+" "+i[5:])
    return fun

"""#Decorators 2 - Name Directory"""

def person_lister(f):
    def inner(people):
        people.sort(key=lambda x: int(x[2]))
        for person in people:
            yield f(person)
    return inner

"""#Arrays"""

def arrays(arr):
    arr = arr[::-1]
    return numpy.array(arr, float)

"""#Shape and Reshape

"""

import numpy

lst = list(map(int, input().strip().split()))

print(numpy.reshape(lst, (3, 3)))

"""#Transpose and Flatten"""

import numpy

N , M = map(int , input().split())

arr = []

j = 0

for i in range(N):
    if j < M:
        value =list(map(int , input().split()))
        arr.append(value)

array = numpy.array(arr)

print(numpy.transpose(array))
print(array.flatten())

"""#Concatenate"""

import numpy

import numpy

[N, M, P] = list(map(int, input().split(" ")))

arrayN = []
arrayM = []

for i in range(N):
    arrayN.append(list(map(int, input().split(" "))))
for i in range(M):
    arrayM.append(list(map(int, input().split(" "))))

outputArr = numpy.concatenate((arrayN, arrayM))

print(outputArr)

"""#Zeros and Ones"""

import numpy
inp = list(map(int, input().split()))
print(numpy.zeros((inp), int))
print(numpy.ones((inp), int))

"""#Eye and Identity"""

import numpy
numpy.set_printoptions(legacy='1.13')
N, M = map(int, input().split())
print(numpy.eye(N, M, k=0))

"""#Array Mathematics"""

import numpy as np
if __name__ == "__main__":
    N, M = map(int, input().split(" "))
    A = np.array([list(map(int, input().split(" "))) for _ in range(N)])
    B = np.array([list(map(int, input().split(" "))) for _ in range(N)])
    print(A + B)
    print(A - B)
    print(A * B)
    print(A // B)
    print(A % B)
    print(A ** B)

"""#Floor, Ceil and Rint"""

import numpy
import numpy
numpy.set_printoptions(legacy='1.13')
arr = numpy.array(list(map(float, input().strip().split())))
print(numpy.floor(arr), numpy.ceil(arr), numpy.rint(arr), sep='\n')

"""#Sum and Prod"""

import numpy as np
n,m = map(int, input().split())
arr = np.zeros(shape=[n,m], dtype=int)
for i in range(n):
    item = list(map(int, input().split()))
    arr[i] = item
print(np.prod(np.sum(arr, axis=0)))

"""#Min and Max"""

import numpy as np
n, m = [int(num) for num in input().split(' ')]
arr = []
for _ in range(n):
    arr.append([int(num) for num in input().split(' ')])
print(np.max(np.min(arr, axis=1)))

"""#Mean, Var, and Std"""

import numpy
arr = []
j = 0

N , M = map(int , input().split())

for i in range(M):
    if j <= N:
        value = list(map(int , input().split(" ")))
        arr.append(value)
        j+=1
    else:
        print("error!")


my_array = numpy.array(arr)
mean_array = numpy.mean(my_array,axis=1)
print(mean_array)
var_array = numpy.var(my_array,axis=0)
print(var_array)
std_array = numpy.std(my_array , axis=None)
round_std_array = round(std_array , 11)
print(round_std_array)

"""#Dot and Cross"""

import numpy

N = int(input())
a = []
b = []
for i in range(N):
    temp = list(map(int, input().split()))
    a.append(temp)
for i in range(N):
    temp = list(map(int, input().split()))
    b.append(temp)

print(numpy.dot(a, b))

"""#Inner and Outer"""

import numpy as np
A= list(map(int, input().split()))
A=np.array(A)
B= list(map(int, input().split()))
B=np.array(B)
print(np.inner(A,B))
print(np.outer(A,B))

"""#Polynomials"""

import numpy as np
A = np.array(input().split(), float)
print(np.polyval(A, int(input())))

"""#Linear Algebra"""

import numpy as np
rows=[]
s=int(input())
for i in range(s):
    row=(list(map(float, input().split())))
    rows.append(row)
a=np.array(rows)
print(round(np.linalg.det(a), 2))

"""#Birthday Cake Candles"""

#!/bin/python3

import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    return candles.count(max(candles))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

"""#Number Line Jumps"""

import math
import os
import random
import re
import sys

def kangaroo(x1, v1, x2, v2):
    if (x2 > x1 and v2 > v1) or (x2 > x1 and v1 == v2):
        return 'NO'
    elif (x2-x1) % (v1-v2) == 0:
        return 'YES'
    else:
        return 'NO'
        end
    end

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

"""#Viral Advertising"""

#!/bin/python3

import math
import os
import random
import re
import sys

def viralAdvertising(n):
    recipients = 5
    liked = 2
    if n == 1:
        return 2
    if n > 1:
        for i in range(n-1):
            recipients = (recipients // 2)*3
            liked += recipients // 2
        return liked


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

"""#Recursive Digit Sum"""

#!/bin/python3

import math
import os
import random
import re
import sys

def superDigit(n, k):
    def sd(x):
      if len(x)==1: return x
      return sd(str(sum(map(int,str(x)))))

    num = str(sum(map(int,str(n)))*k)
    return sd(num)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

"""#Insertion Sort - Part 1"""

#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    last = arr[n-1]
    i = n-1
    while i > 0 and last < arr[i-1]:
        arr[i] = arr[i-1]
        i -= 1
        print(' '.join(map(str, arr)))
    arr[i] = last
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

"""#Insertion Sort - Part 2"""

#!/bin/python3

import math
import os
import random
import re
import sys

def insertionSort2(n, arr):
    for i in range(1, n):
        num = arr[i]
        j = i - 1
        while j >= 0 and num < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = num
        print(" ".join(map(str, arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)