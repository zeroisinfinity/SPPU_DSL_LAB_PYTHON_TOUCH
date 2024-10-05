import sys
import itertools
import cProfile
from collections import Counter

my_str =input()

length = len(my_str)


palindrome_final = lambda test_str : all(test_str[cf]==test_str[length-1-cf] for cf in range(0,length//2))
#palindrome2 = 0.0 if len([0.0 for cf in range(0,length//2) if my_str[cf]==my_str[length-cf-1]]) == length//2 else -1.0
#palindrome3 = 0.0 if my_str[:length//2+1][::-1] == my_str[length//2:] else -1.0

count_freq = lambda test_str,char : test_str.count(char)

longest_word = lambda test_str : [test_str for test_str in my_str.split(" ") if len(max(my_str.split(" "),key=len))]

first_index = lambda test_str , sub_test_str : test_str.find(sub_test_str)

occurence = lambda test_str : {word : test_str.split(" ").count(word) for word in test_str.split(" ")}
#occurence = lambda test_str : Counter(test_str.split(" "))

