class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def multiply(self):

        return self.a*self.b
    
def addition (p,m):
    print("addition happen")
    return p+m

if __name__=="__main__":
    print("rishikesh")
    (p ,m )=input("enter p and m ").split()
    t=addition(p,m)
    print(f"this is additon{t}")
    a=int(p);b=int(m)
    obj=A(a,b)
    print(f"this is multiplication :{obj.multiply()}")
