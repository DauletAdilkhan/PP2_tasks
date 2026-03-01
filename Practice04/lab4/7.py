class rev:
    def __init__(self,a):
        self.a = a
        self.ind = len(a)-1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.ind < 0:
            raise StopIteration
        i = self.a[self.ind]
        self.ind-=1
        return i



a=str(input())

for i in rev(a):
    print(i,end='')
print()