
def hasMatchingParantheses(strExpression):
    open_par = tuple('({[')
    close_par = tuple(')}]')
    mapping_par = dict(zip(open_par, close_par))
    s = []
    for i in strExpression:
        if i in open_par:
            s.append(mapping_par[i])            
        elif i in close_par:
            if not s or i != s.pop():
                return False
    return True          
        
    
if __name__ == "__main__":
    try:
        strExpression = str(input('Enter string: '))
    except:
        strExpression = None
    res = hasMatchingParantheses(strExpression);
    print('balanced parenthesis T or F: ',res)
