class Symbol:
    def __init__(self, var, pre, post):
        self.var = var
        self.pre = pre
        self.post = post

    def __div__(self, other):
        return Symbol(self.var, self.pre / other.pre, self.post - other.post)

    def __mul__(self, other):
        return Symbol(self.var, self.pre * other.pre, self.post + other.post)

    def __add__(self, other):
        return Symbol(self.var, self.pre + other.pre, self.post)

    def __sub__(self, other):
        return Symbol(self.var, self.pre - other.pre, self.post)

    def __str__(self):
        return(str(self.pre)+self.var+str(self.post))
class Frac:
    def __init__(self,num,den):
        self.num=num
        self.den=den
    def __truediv__(self,other):
        return Frac(self.num*other.den,self.den*other.num)
    def __mul__(self,other):
        return Frac(self.num*other.num,self.den*other.den)
    def __add__(self,other):
        if self.den==other.den:
            num=self.num+other.num
            den=self.den
        else:
            num=(self.num*other.den)+(other.num*self.den)
            den=self.den*other.den
        return Frac(num,den)
    def __sub__(self,other):
        if self.den==other.den:
            num=self.num-other.num
            den=self.den
        else:
            num=(self.num*other.den)-(other.num*self.den)
            den=self.den*other.den
        return Frac(num,den)
    def __str__(self):
        return(str(self.num)+'|'+str(self.den))
def remover(arr):
    while(True):
        if "brownMunde" in arr:
            arr.remove("brownMunde")
        else:
            break
arr=[Frac(Symbol('x',3,2),Symbol('x',2,1)),'*',Frac(Symbol('x',3,2),Symbol('x',3,5))]
x=0
while(x<len(arr)):
    if arr[x]=='/':
        arr[x+1]=arr[x-1]/arr[x+1]
        arr[x-1]="brownMunde"
        arr[x]="brownMunde"
        remover(arr)
    x+=1
x=0
while(x<len(arr)):
    if arr[x]=='*':
        arr[x+1]=arr[x-1]*arr[x+1]
        arr[x-1]="brownMunde"
        arr[x]="brownMunde"
        remover(arr)
    x+=1
x=0
while(x<len(arr)):
    if arr[x]=='+':
        if arr[x+1].post==arr[x-1].post:
            arr[x+1]=arr[x-1]+arr[x+1]
            arr[x-1]="brownMunde"
            arr[x]="brownMunde"
            remover(arr)
    x+=1
x=0
while(x<len(arr)):
    if arr[x]=='-':
        if arr[x+1].post==arr[x-1].post:
            arr[x+1]=arr[x-1]-arr[x+1]
            arr[x-1]="brownMunde"
            arr[x]="brownMunde"
            remover(arr)
    x+=1
i=0
while(i<len(arr)):
    print(arr[i],end='')
    i+=1