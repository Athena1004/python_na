#三种方法举例
class Person():
    #1.实例方法
    def eat(self):
        print(self)
        print("Eating")
    #2.类方法，第一个参数一般命名为cls，区别于self
    @classmethod
    def play(cls):
        print(cls)
        print("Playing")
    #3.静态方法，不需要参数
    @staticmethod
    def say():
        print("Saying....")

yueyue = Person()
#1.实例方法
yueyue.eat()
# 2.类方法，
Person.play()
yueyue.play()
#3.静态方法，
yueyue.say()
Person.say()


