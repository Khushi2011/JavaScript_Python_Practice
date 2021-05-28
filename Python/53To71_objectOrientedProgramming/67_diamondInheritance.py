# If we have a method that is only present in class A and we use class D object to call the method,
# it will go to class A while checking for the method name in all the classes in between and run the method in class A.

# However, if the same method is also present in class B, then it will run the B class method because for class D,
# class B holds a more priority then class A. The reason is that class D is derived from class B which is further
# derived from A. So, the closer relation exists with B than A.

# If the same method is present in class C and B, it may create a little bit of confusion.
# In such cases, our priority is based from left to right, meaning whichever class is on the left side will
# be given more priority, and then we will move towards right one. In this case, the left class is B,
# so the method in B will de be executed first.


class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    def met(self):
        print("This is a method from class B")

class C(A):
    def met(self):
        print("This is a method from class C")

class D(C, B):
    def met(self):
        print("This is a method from class D")#first this will called....if not found then classC will be priority then
#         class B then last class A


a = A()
b = B()
c = C()
d = D()

d.met()
