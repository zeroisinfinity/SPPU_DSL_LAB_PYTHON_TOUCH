from collections import Counter


list_of_marks = [1,2,3,4,5,6]
print(len(list_of_marks))

#avg = lambda test_list : {sum([marks for marks in test_list if marks != -1]) : len(test_list)}
#print(avg(list_of_marks).keys())
#print(list(avg(list_of_marks).keys())[0]/list(avg(list_of_marks).values())[0])

avg = lambda test_list : sum([marks for marks in test_list if marks != -1]) / len(test_list)
print(avg(list_of_marks))

hfreq1 = lambda test_list : "All are absent" if len([{freq:Counter(test_list)[freq]} for freq in list(Counter(test_list).keys()) if Counter(test_list)[freq] >= max(list(Counter(test_list).values())) and freq != -1 ]) == 0 else ("Everyone's frequency is same" if len([{freq:Counter(test_list)[freq]} for freq in list(Counter(test_list).keys()) if Counter(test_list)[freq] >= max(list(Counter(test_list).values())) and freq != -1 ]) == len(test_list) else [{freq:Counter(test_list)[freq]} for freq in list(Counter(test_list).keys()) if Counter(test_list)[freq] >= max(list(Counter(test_list).values())) and freq != -1 ])
print(hfreq1(list_of_marks))


