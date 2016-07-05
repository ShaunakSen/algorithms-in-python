Ok .. so we know what bytes are
1 byte = 8 bits

Now each memory or eav=ch byte has an abstraction called address
say byte no 2134, byte no 7633

Computer's main memory performs a Random Access memeory
ie its just as easy to receive byte no 231432423 as it is to recv no 23

each indv byte can be retrieved in O(1) time


In python each unicode char takes in 2 bytes

S       A       M
1 3     4 5     6 7 ------->memory locations

memory addr = start + cellsize * index

Prob:
We have many names say mini, shona ,paddy etc

We want to store them in array
Each cell should have same no of bytes
How to make this? Use an array of object references

0       1       2       3
Mini    Shona .....

each index references an object

backup =list(primes)

primes is an already existing list]
this is shallow copy.. we are not exactly duplicating the objects
we are duplicating a  list that references the same object

counters = [0] * 8

all 8 cells of the list reference the same object ie to 0

we are not actually making 8 integers


Dynamic Array

When we build up a list in python
we dont have to specify size beforehand

how does it work internally?

When list is say 2 elements to 6 elements -> 120bytes
6 -> 12 -> 150bytes
memory increases in chunks

as it finds it is increases it increases space


Anagram check:

1. sort and check if they are same
sorted(str) -> returns a list of sorted indv chars

sortedStr1 = ''.join(sortedList1)

2. maintain a dict

for each letter in str1 count[letter] += 1
for each letter in str2 count[letter] -= 1

Then check which letter has count != 0

zip([1, 2, 4, 5, 6, 8], [1, 2, 4, 5, 6])

[(1, 1), (2, 2), (4, 4), (5, 5), (6, 6)]


1 2 -1 3 -1 10 20 -10 5 100


