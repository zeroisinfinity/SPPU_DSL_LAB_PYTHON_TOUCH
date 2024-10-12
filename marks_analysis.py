from collections import Counter


list_of_marks = list(range(80, 1, -1)) + [80,79]
print(len(list_of_marks))

#avg = lambda test_list : {sum([marks for marks in test_list if marks != -1]) : len(test_list)}
#print(avg(list_of_marks).keys())
#print(list(avg(list_of_marks).keys())[0]/list(avg(list_of_marks).values())[0])

avg = lambda test_list : sum([marks for marks in test_list if marks != -1]) / len(test_list)
print(avg(list_of_marks))

#hfreq = lambda test_list : "All are absent" if len([{freq:Counter(test_list)[freq]} for freq in list(Counter(test_list).keys()) if Counter(test_list)[freq] >= max([Counter(test_list)[pov] for pov in list(Counter(test_list).keys()) if pov != -1 ]) and freq != -1 ]) == 0 else ("Everyone's frequency is same" if len([{freq:Counter(test_list)[freq]} for freq in list(Counter(test_list).keys()) if Counter(test_list)[freq] >= max([Counter(test_list)[pov] for pov in list(Counter(test_list).keys()) if pov != -1 ]) and freq != -1 ]) == len([pov_len for pov_len in test_list if pov_len != -1]) else [{freq:Counter(test_list)[freq]} for freq in list(Counter(test_list).keys()) if Counter(test_list)[freq] >= max([Counter(test_list)[pov] for pov in list(Counter(test_list).keys()) if pov != -1 ]) and freq != -1 ])
#print([Counter(list_of_marks)[pov] for pov in list(Counter(list_of_marks).keys()) if pov != -1 ])
#print([{freq:Counter(list_of_marks)[freq]} for freq in list(Counter(list_of_marks).keys()) if Counter(list_of_marks)[freq] >= max([Counter(list_of_marks)[pov] for pov in list(Counter(list_of_marks).keys()) if pov != -1 ]) and freq != -1 ])
hfreq = lambda test_list : "All are absent" if not [freq for freq in Counter(test_list) if freq != -1] else "Every marks' frequency is 1" if len(set(Counter(test_list).values())) == 1 else [{key:value} for key,value in Counter(test_list).items() if value >= max(Counter(test_list).values()) and key != -1]
print(hfreq(list_of_marks))
#print([Counter(list_of_marks)[pov] for pov in list(Counter(list_of_marks).keys()) if pov != -1 ])
#print([{freq:Counter(list_of_marks)[freq]} for freq in list(Counter(list_of_marks).keys()) if Counter(list_of_marks)[freq] >= max([Counter(list_of_marks)[pov] for pov in list(Counter(list_of_marks).keys()) if pov != -1 ]) and freq != -1 ])

absent = lambda test_list : len([ab for ab in test_list if ab == -1])
print(absent(list_of_marks))

lowest = lambda test_list : min([marks for marks in test_list if marks != -1])
print(lowest(list_of_marks))
#print(list_of_marks) #DON'T TAMPER WITH GLOBAL DATA

highest = lambda test_list : max([marks for marks in test_list if marks != -1])
print(highest(list_of_marks))
