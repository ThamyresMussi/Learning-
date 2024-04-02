def exer1 (a):
    return sum (a), sum(a)/len(a)

def fun2 (a,b,c):
    for i in range (len(a)):
        if a[i]==b:
           a[i]=c
    return a
print (fun2 ([ 'banana', 'morango', 'maça'], 'maça', 'banana'))

def fun3 (x):
    for i in range (1, x+1):
        print("*" * i)
            
