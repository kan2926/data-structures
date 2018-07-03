def find_max_length_of_matching_parentheses(brackets):
    pop = False
    open_par =[]
    close_par = []
    sub_len_arr = []
    brackets = brackets.replace(" ","")
    for i,j in enumerate(brackets):
        print(brackets[i])
    for i, j in enumerate(brackets):
        if j == '(':
            if not pop:
                open_par.append(j)
            else:
                pop = False
                if len(sub_len_arr)>0:
                    print(i,'---',i - len(open_par)- max(sub_len_arr))
                    sub_len_arr.append(i - len(open_par)- max(sub_len_arr))
                else:
                    sub_len_arr.append(i - len(open_par))
                open_par = []
                open_par.append(j)
        else:
            if open_par:
                open_par.pop()
                pop = True
            else:
                close_par.append(j)
        print(i ,' --- ', sub_len_arr)
    print(sub_len_arr)
    if len(open_par) == 0 and len(close_par) == 0:
        return len(brackets)
    elif len(sub_len_arr) >0:
        return max(sub_len_arr)
    elif len(open_par) > 0 and len(close_par) == 0:
        return len(brackets) - len(open_par)
                    
            
if __name__ == "__main__":
    try:
        brackets = str(input('Enter string: '))
    except:
        brackets = None
    res = find_max_length_of_matching_parentheses(brackets);
    print('balanced parenthesis T or F: ',res)
