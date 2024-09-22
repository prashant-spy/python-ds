class A:
    def rk(self):
        print("in class A")


class B(A):
    def rk(self):
        print("In class B")


class C(A):
    def rk(self):
        print("In class C")


class D(B, C):
    pass


r = D()
r.rk()
print(D.__mro__)
