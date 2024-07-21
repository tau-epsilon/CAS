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
    def converter(obj):
        if isinstance(obj,Symbol):
            return Frac(obj,Symbol('x',1,0))
        else:
            return obj
    def __truediv__(self,other):
        self=Frac.converter(self)
        other=Frac.converter(other)
        return Frac(self.num*other.den,self.den*other.num)
    def __mul__(self,other):
        self=Frac.converter(self)
        other=Frac.converter(other)
        return Frac(self.num*other.num,self.den*other.den)
    def __add__(self,other):
        self=Frac.converter(self)
        other=Frac.converter(other)
        if self.den==other.den:
            num=[self.num,'+',other.num]
            solver(num)
            den=self.den
        else:
            num=[self.num*other.den,'+',other.num*self.den]
            solver(num)
            den=self.den*other.den
        return Frac(num,den)
    def __sub__(self,other):
        self=Frac.converter(self)
        other=Frac.converter(other)
        if self.den==other.den:
            num=[self.num,'-',other.num]
            solver(num)
            den=self.den
        else:
            num=[self.num*other.den,'-',other.num*self.den]
            solver(num)
            den=self.den*other.den
        return Frac(num,den)
    def __str__(self):
        if isinstance(self.num,list):
            st='['
            k=0
            while k<len(self.num):
                st+=str(self.num[k])
                k+=1
            st+=']|'+str(self.den)
            return st
        else:
            return(str(self.num)+'|'+str(self.den))
def remover(arr):
    while(True):
        if "brownMunde" in arr:
            arr.remove("brownMunde")
        else:
            break
def solver(arr):
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
            if isinstance(arr[x+1],Symbol) and isinstance(arr[x-1],Symbol):
                if arr[x+1].post==arr[x-1].post:
                    arr[x+1]=arr[x-1]+arr[x+1]
                    arr[x-1]="brownMunde"
                    arr[x]="brownMunde"
                    remover(arr)
            else:
                arr[x+1]=arr[x-1]+arr[x+1]
                arr[x-1]="brownMunde"
                arr[x]="brownMunde"
                remover(arr)
        x+=1
    x=0
    while(x<len(arr)):
        if arr[x]=='-':
            if isinstance(arr[x+1],Symbol) and isinstance(arr[x-1],Symbol):
                if arr[x+1].post==arr[x-1].post:
                    arr[x+1]=arr[x-1]-arr[x+1]
                    arr[x-1]="brownMunde"
                    arr[x]="brownMunde"
                    remover(arr)
            else:
                arr[x+1]=arr[x-1]-arr[x+1]
                arr[x-1]="brownMunde"
                arr[x]="brownMunde"
                remover(arr)
        x+=1
def printer(arr):
    j=0
    while(j<len(arr)):
        print(arr[j],end='')
        j+=1

arr=[Frac(Symbol('x',3,2),Symbol('x',2,1)),'-',Symbol('x',3,2)]
solver(arr)
printer(arr)