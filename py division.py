Task
The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

No rounding or formatting is necessary.

Example


The result of the integer division .
The result of the float division is .
Print:

0
0.6
Input Format

The first line contains the first integer, .
The second line contains the second integer, .

Output Format

Print the two lines as described above.

Sample Input 0

4
3
Sample Output 0

1
1.33333333333
Contest ends in 21 hours
Submissions: 73
Max Score: 10
Difficulty: Easy
Rate This Challenge:

    
More
 
1
if __name__ == '__main__':
2
    a = int(inpur("enter the value of a:"))
3
    b = int(inpur("enter the value of a:"))
4
    print(a/b)
5
    print(a//b)