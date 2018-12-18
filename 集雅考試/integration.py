# Please try to add 1~3 line of code to finish the integration

# ========================解題========================
def anonymous(x):
    return x**2 + 1    #目標方程式
    
def integrate(fun, start, end):
    step = 0.1
    intercept = start
    area = 0
    while intercept < end:
        intercept += step
        ''' your work here '''
        area += anonymous(intercept)*step   # 積分就是求面積
        ''' my work end '''
    return area

print(integrate(anonymous, 0, 10))