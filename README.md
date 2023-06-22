# Mission

We have sniffed an unsecured network and found numbers that are used to encrypt very important documents. It seems that those numbers are not always generated using large enough prime numbers. Your mission should you choose to accept it, is to factorize these numbers as fast as possible before the target fixes this bug on their server - so that we can decode the encrypted documents.

##  Factorize all the things!

Factorize as many numbers as possible into a product of two smaller numbers.

### Usage: factors <file>
where <file> is a file containing natural numbers to factor.
One number per line
You can assume that all lines will be valid natural numbers greater than 1
You can assume that there will be no empy line, and no space before and after the valid number
The file will always end with a new line
Output format: n=p*q
one factorization per line
p and q don’t have to be prime numbers
See example
You can work on the numbers of the file in the order of your choice
Your program should run without any dependency: You will not be able to install anything on the machine we will run your program on
Time limit: Your program will be killed after 5 seconds if it hasn’t finish
Push all your scripts, source code, etc… to your repository
we will only run your executable factors

Compile C function:
cc -fPIC -shared -o lib_factors_functions.so factors_functions.c

# RSA Factoring Challenge in python
___
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/Innocentsax/standard-readme)

The RSA Factoring Challenge was a challenge set up by RSA Security in 1991 to encourage the development of faster factoring algorithms, which are important for breaking the RSA cryptosystem. The challenge involved factoring a large integer that was the product of two prime numbers, and the prize was $200,000.

<p align="center">
<img src="https://www.packetmania.net/en/2022/01/22/Python-Textbook-RSA/finding-prime-en.jpg">
</p>

**Mission/Objective:**
We have sniffed an unsecured network and found numbers that are used to encrypt very important documents. It seems that those numbers are not always generated using large enough prime numbers. Your mission should you choose to accept it, is to factorize these numbers as fast as possible before the target fixes this bug on their server - so that we can decode the encrypted documents.

### Resources
* [Prime Factorization](https://privacycanada.net/mathematics/prime-factorization/) || [How does HTTPS provide security?](https://stackoverflow.com/questions/3968095/how-does-https-provide-security) || [RSA (cryptosystem)](https://en.wikipedia.org/wiki/RSA_(cryptosystem%29) || [Python File I/O](https://www.programiz.com/python-programming/file-operation) || [Open a File in Python](https://pynative.com/python-file-open/) || [Reading and Writing to text files in Python](https://www.geeksforgeeks.org/reading-writing-text-files-python/)

## General Requirements
* You can choose the language of your choice, though this project was written in python language
* All the files was interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All files ends with a new line
* The first line of all your files should be exactly **#!/usr/bin/env python3**
* There is a **README.md** file, at the root of the folder of the project
* All files are executable
* All coded used the pycodestyle (version 2.8.*)*

## List of files and description:
| S/N   |       Files          |        Description  |
|:-----:|:--------------------:|:-------------------|
|1. | [factors](https://github.com/Innocentsax/RSA-Factoring-Challenge/factors) | To Factorize as many numbers as possible into a product of two smaller numbers.|

### Zouhair BARTA
