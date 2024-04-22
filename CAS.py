class Symbol:
    def __init__(self, var, pre, post):
        self.var = var
        self.pre = pre
        self.post = post

    def __truediv__(self, other):
        return Symbol(self.var, self.pre / other.pre, self.post - other.post)

    def __mul__(self, other):
        return Symbol(self.var, self.pre * other.pre, self.post + other.post)

    def __add__(self, other):
        return Symbol(self.var, self.pre + other.pre, self.post)

    def __sub__(self, other):
        return Symbol(self.var, self.pre - other.pre, self.post)

    def __str__(self):
        return(str(self.pre)+self.var+str(self.post))


def is_operator(obj):
    operators = "+-*/%<>=!&|^~"
    if obj in operators:
        return True
    return False

arr = [Symbol('x', 2, 3), '*', Symbol('x', 3, 4)]
arr2 = []
for x in arr:
    y = arr.index(x)
    if not isinstance(x,Symbol):
        if x == '/':
            arr2.append(arr[y - 1] / arr[y + 1])
        elif x == '*':
            arr2.append(arr[y - 1] * arr[y + 1])
        elif x == '+':
            arr2.append(arr[y - 1] + arr[y + 1])
        elif x == '-':
            arr2.append(arr[y - 1] - arr[y + 1])

for z in arr2:
    print(z)
