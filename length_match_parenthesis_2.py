def find_max_length_of_matching_parentheses(brackets):
    import re
    brackets = re.sub(r"\s","",brackets)
    s = []
    par = {'(': ')', ')':'('}
    max_len=[]
    d ={}
    cnt=1
    for i in brackets:
        if i == '(':
            s.append(par[i])
        elif i == ')':
            if s:
                n = s.pop()                
                if i != n:
                    s.append(n)
                    s.append(par[i])
                else:
                    max_len.append(cnt)
                    print('found')
            else:
                s.append(par[i])
    if len(s) == len(brackets):
        match_string = 0
    elif len(s) == 0 and len(brackets) >0:
        match_string = len(brackets)
    elif max(max_len) >0:
        match_string = len(brackets) - max(max_len)
    else:
        match_string =  len(s)    
    
if __name__ == "__main__":
    try:
        brackets = str(input('Enter string: '))
    except:
        brackets = None
    res = find_max_length_of_matching_parentheses(brackets);
    print('balanced parenthesis T or F: ',res)
# ((((())(((()
