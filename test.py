class A:
    def __init__(self) -> None:
        pass
    def popka(self):
        global x
        x = 9
        print(x)

class B(A):
    ...
b = B()
print(x)  # 10
b.popka() # 19
print(x)  # 19