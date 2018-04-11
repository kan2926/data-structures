def find_max_length_of_matching_parentheses(brackets): 
    s = []
    par = {'(': ')'}
    cnt = 0
    sub_cnt = 0
    sub_cnt_list=[0]
    for i in brackets:
        if i == '(':
            cnt +=1
            s.append(par[i])
            if sub_cnt >0:
                sub_cnt_list.append(2*sub_cnt)
                sub_cnt = 0
        elif i == ')':
            if s:
                cnt += 1                
                sub_cnt += 1
            else:
                cnt = 0
    if len(sub_cnt_list) == 1 and sub_cnt ==1:
        sub_cnt_list.append(2*sub_cnt)
    print(cnt, sub_cnt_list)
    if cnt == sum(sub_cnt_list):
        print('all balanced', sub_cnt_list)
    return max(sub_cnt_list)                      
    
if __name__ == "__main__":
    try:
        brackets = str(input('Enter string: '))
    except:
        brackets = None
    res = find_max_length_of_matching_parentheses(brackets);
    print('balanced parenthesis T or F: ',res)
# ((((())(((()
