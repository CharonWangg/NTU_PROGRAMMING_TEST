# Question 1 # Dynamic Organization

def findOperations(m,n,sumNum):
    sumMin = n + sum(range(2,m+1))
    diffNum = sumNum - sumMin
    res = diffNum % (n - 1)

    if diffNum != 0:
        if res == 0:
            lineNum = int(diffNum/(n-1))
        else:
            lineNum = int(diffNum/(n-1)) + 1
            res = n - 1 - res
    else:
        lineNum = 0

    if lineNum > 1:
        operations = 'D'*(lineNum-1) +'R' * res + 'D' + 'R' * (n - 1 - res) + 'D' * (m - 1 - lineNum)
    else:
        operations = 'R'*res + 'D'*lineNum + 'R'*(n-1-res) + 'D'*(m-1-lineNum)
    print(operations)

findOperations(90000,100000,5994891682)
