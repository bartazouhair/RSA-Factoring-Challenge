This project 'RSA Factoring Challenge' is done by Glamour Maphanga

Task 0: Factorize all the things! Description This task involves factorizing natural numbers into a product of two smaller numbers. The goal is to factorize as many numbers as possible within a given time limit.

Usage To run the program, use the following command: factors

where is a file containing natural numbers to factor. Each number should be written on a separate line without any additional spaces or characters.

Input The input file should contain valid natural numbers greater than 1. There should be no empty lines or spaces before or after the numbers. The file will always end with a new line. Output The program will output the factorization of each number in the format n=p*q, where n is the original number and p and q are the factors.

Example Suppose we have a file test00 with the following numbers:

4 12 34 128 1024 4958 1718944270642558716715 9 99 999 9999 9797973 49 239809320265259

Running the program with the command ./factors tests/test00 will produce the following output:

4=22 12=62 34=172 128=642 1024=5122 4958=24792 1718944270642558716715=3437888541285117433435 9=33 99=333 999=3333 9999=33333 9797973=32659913 49=77 239809320265259=1548578315485773

Time Limit The program will be terminated after 5 seconds if it hasn't finished execution.

Task 1: RSA Factoring Challenge Description The RSA Factoring Challenge is an advanced version of Task 0. In this task, the objective is to find two prime numbers p and q that multiply together to produce a given number n.

Usage To run the program for the RSA Factoring Challenge, use the following command:

rsa

where is a file containing a single number to factor.

Input The input file should contain a single number to factor. The number should be greater than 1. Output The program will output the factorization of the number in the format n=p*q, where n is the original number and p and q are prime factors.

Example Suppose we have a file rsa-1 with the number '6' :

6 Running the program with the command ./rsa tests/rsa-1 will produce the following output:

6=3*2

Time Limit The program will be terminated after 5 seconds if it hasn't finished execution.

Repository The code for both tasks can be found in the following GitHub repository:

Repository: RSA-Factoring-Challenge

Files:

factors rsa
