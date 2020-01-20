def f(a, b):
    
    def f1(c):
        return f2(2)
        
    def f2(d):
        return d
        
    print(f1(1))
    
f(1,2)