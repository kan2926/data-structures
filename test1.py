s_len_list = [4,5,6,10,11]
d = dict()
i=0
for j in range(len(s_len_list)-1):
    d.setdefault(i,[])        
    d[i].append(s_len_list[j]) 
    while s_len_list[j+1] - s_len_list[j] == 1 and j < len(s_len_list)-1:
        d[i].append(s_len_list[j+1])
        j += 1
    i += 1
print(d)
