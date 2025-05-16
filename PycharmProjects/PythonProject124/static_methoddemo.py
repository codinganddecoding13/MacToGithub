class MethodDemo:

    a = 1

    @classmethod
    def classM(cls):
        print("Class Method. cls.a = ", cls.a)

    @staticmethod
    def staticM():
        print("Static method")

md1=MethodDemo
md1.staticM()
MethodDemo.staticM()