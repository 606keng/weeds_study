def decorateFunction(fun, *a, **k):
    print("调用封闭函数")
    class wrapClass():
        def __init__(self, *a, **k):
            print("准备调用被装饰的类")
            self.wrappedClass = fun(*a, **k)
            self.decorate()  # 针对没有重写定义的方法赋值给wrapClass作为实例变量，本案例中为涉及的为fun2方法

        def fun1(self, *a, **k):
            print("准备调用被装饰类的方法fun1")
            self.wrappedClass.fun1(*a, **k)
            print("调用被装饰类的方法fun1完成")

        def decorate(self):  # 针对没有重写定义的方法赋值给wrapClass作为实例变量
            for m in dir(self.wrappedClass):
                if not m.startswith('_') and m != 'fun1':
                    print(m)
                    # 获取对象属性的值
                    fn = getattr(self.wrappedClass, m)
                    # 检查fn对象是否为可调用的
                    if callable(fn):
                        # 用于设置属性的值，属性如果不存在，则添加新的属性
                        # 将方法fn添加到实例变量中，并命名为m
                        setattr(self, m, fn)
    return wrapClass


@decorateFunction
class wrappedClass:
    def __init__(self, *a, **k):
        print("我是被装饰类的构造方法")
        self.name = a[0]
        if a: print("构造方法存在位置参数：", a)
        if k: print("构造方法存在关键字参数：", k)
        print("被装饰类构造方法执行完毕")

    def fun1(self, *a, **k):
        print("我是被装饰类的fun1方法")

        if a: print("fun1存在位置参数：", a)
        if k: print("fun1存在关键字参数：", k)
        print("我的实例名字为:", self.name)
        print("被装饰类fun1方法执行完毕")

    def fun2(self, *a, **k):
        print("我是被装饰类的fun2方法")
        if a: print("fun2方法存在位置参数：", a)
        if k: print("fun2存在关键字参数：", k)
        print("我的实例名字为:", self.name)


c1 = wrappedClass("doulihang", age=28)
# c1.fun1("gaoyujing",age=25)
c1.fun2("gaokele",age=3)