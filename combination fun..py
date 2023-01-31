def combination(n,r):
    expression=[]
    expression.append('(')
    for i in range(r): #numerator
        expression.append(n-i)
        if i != r-1 :
           expression.append('*')  
        else:
            expression.append(')')
            expression.append('/')


    expression.append('(')
    for j in range(r): #denominator
        expression.append(r-j)
        if j != r-1 :
           expression.append('*')  
        else:
            expression.append(')')
    
    output = [str(x) for x in expression]

    return " ".join(output)
        
print(combination(10,5))
