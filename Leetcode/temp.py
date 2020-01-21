def f(a, b):
    
    res = []
    def f1(c):
        res.append(1)
        return f2(2)
        
    def f2(d):
        return d
        
    print(f1(1))
    print(res)
    
f(1,2)