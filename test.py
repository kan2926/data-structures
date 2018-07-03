def find_max_length_of_matching_parentheses(brackets):
    st = []
    s_len_list=[]
    for i,c in enumerate(brackets):
        if c == '(':
            st.append(c)
        elif c == ')':
            if st:
                st.pop()
                s_len_list.append(i+1)
            else:                
                s_len_list.append(0)
                pass
    print(st)
    print(s_len_list)
    
    if len(st) == 0 and len(s_len_list) > 0:
        return(max(s_len_list))
    else:
        return(max(s_len_list) - len(st))
    
if __name__ == "__main__":
    try:
        brackets = str(input('Enter string: '))
    except:
        brackets = None
    res = find_max_length_of_matching_parentheses(brackets);
    print('balanced parenthesis T or F: ',res)
