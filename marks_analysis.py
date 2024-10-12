from collections import Counter


list_of_marks = [1,2,3,4,5,6,-1,-1]
print(len(list_of_marks))

#avg = lambda test_list : {sum([marks for marks in test_list if marks != -1]) : len(test_list)}
#print(avg(list_of_marks).keys())
#print(list(avg(list_of_marks).keys())[0]/list(avg(list_of_marks).values())[0])

avg = lambda test_list : sum([marks for marks in test_list if marks != -1]) / len(test_list)
print(avg(list_of_marks))

hfreq = lambda test_list : "All are absent" if len([{freq:Counter(test_list)[freq]} for freq in list(Counter(test_list).keys()) if Counter(test_list)[freq] >= max(list(Counter(test_list).values())) and freq != -1 ]) == 0 else ("Everyone's frequency is same" if len([{freq:Counter(test_list)[freq]} for freq in list(Counter(test_list).keys()) if Counter(test_list)[freq] >= max(list(Counter(test_list).values())) and freq != -1 ]) == len(test_list) else [{freq:Counter(test_list)[freq]} for freq in list(Counter(test_list).keys()) if Counter(test_list)[freq] >= max(list(Counter(test_list).values())) and freq != -1 ])
print(hfreq(list_of_marks))
print([{freq:Counter(list_of_marks)[freq]} for freq in list(Counter(list_of_marks).keys()) if Counter(list_of_marks)[freq] >= max(list(Counter(list_of_marks).values())) and freq != -1 ])

absent = lambda test_list : len([ab for ab in test_list if ab == -1])
print(absent(list_of_marks))

lowest = lambda test_list : min([marks for marks in test_list if marks != -1])
print(lowest(list_of_marks))
#print(list_of_marks) #DON'T TAMPER WITH GLOBAL DATA

highest = lambda test_list : max([marks for marks in test_list if marks != -1])
print(highest(list_of_marks))
