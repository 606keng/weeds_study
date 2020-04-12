class A:
    param_a = 1
    def get_param(self):
        return self.param_a

a1 = A()
a2 = A()
A.param_a=9
a1.param_a = 4
a2.param_a = 5
A.param_a = 10

print(f'a1.param = {a1.param_a}, a2.param = {a2.param_a}  , A.parame = {A.param_a}')