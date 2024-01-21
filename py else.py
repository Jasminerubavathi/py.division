Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Explanation 0


 is odd and odd numbers are weird, so print Weird.

Sample Input 1

24
Sample Output 1

Not Weird
Explanation 1


 and  is even, so it is not weird.

Contest ends in 21 hours
Submissions: 81
Max Score: 10
Difficulty: Easy
Rate This Challenge:

    
More
 
1
#!/bin/python3
2
​
3
import math
4
import os
5
import random
6
import re
7
import sys
8
​
9
​
10
​
11
if __name__ == '__main__':
12
    n = int(input().strip())
13
if(n%2)!=0:
14
    print("Weird")
15
else:
16
    if(5>=n>=2):
17
        print("Not Weird ")
18
    elif(20>=n>=6):
19
        print("Weird")
20
    else:
21
        print("Not Weird ")
