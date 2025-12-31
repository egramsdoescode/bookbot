# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project! 

BookBot runs a comprehensive report about the text content of the book to include:

- Word Count
- Character Count - Organized from most to least frequent

---
## Requirements

- Python >= 3.10

## Usage

Ensure that you have a book in a plain text file to put into the program and run the following:

```bash
python3 main.py <path_to_file>.txt

```

## Example output:

```text
============ BOOKBOT ============
Analyzing book count at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
o: 24494
i: 23927
n: 23643
s: 20360
r: 20079
h: 19176
d: 16318
l: 12306
m: 10206
u: 10111
c: 9011
f: 8451
y: 7756
w: 7450
p: 5952
g: 5795
b: 4868
v: 3737
k: 1661
x: 691
j: 497
q: 325
z: 235
æ: 28
â: 8
ê: 7
ë: 2
ô: 1
============= END ===============
```
