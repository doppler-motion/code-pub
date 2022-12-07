# python 面向对象
## 第 1 章
* 面向对象的解释
* 类的定义
* 对象的创建
* instance函数
* Python中的类本身也是一个对象

## 第 2 章 类属性
* 什么是类变量
    > * 属于类本身的变量
    > * 所有该类的对象都共享类变量
* 定义类变量
* 取得类变量的值
  > * 直接取值
  > * 使用函数getattr()取值
* 设置类变量的值
  > * 直接赋值
  > * setattr()函数
* 删除类变量
  > * del
  > * delattr() 函数
* 类变量的存储
  > 类变量全部存放在类变量__dict__字典中，但不能直接修改__dict__的内容

## 第 3 章 实例变量与函数
* 实例函数的定义
* 认识__init__函数
  > * 用来初始化对象的实例函数
* 定义实例变量
  > * 在__init__函数中定义
* 实例函数中访问实例变量
* 外部访问实例变量与函数

## 第 4 章 私有属性与函数
* 私有属性与函数的用途
  > * 在封装中，根本目的是防止被外部调用
  > * 但Python没有严格的权限限定符去进行限制
  > * 私有属性定义依赖于命名
  * 封装
    > 将部分属性的访问包起来，以免用户恶意修改
* 如何定义
  > * 通过给属性和函数名称添加 _ 或者 __前缀
* 如何访问

## 第 5 章 类方法与静态方法
* 类方法
  > * 需要用@classmethod装饰器定义
  > * 第一个参数是类本身
  ```python
   class Student:
    @classmethod
      def get_instance(cls):
        return cls
  
    student = Student.get_instance() 

* 静态方法
  > * 使用@staticmethod装饰器来定义
  > * 静态方法只是定义在类范围内的一个函数
  ```python
  class Student:
    @staticmethod
    def say_hello():
      print("hello")
  
  Student.say_hello()

## 第 6 章 常用的特殊方法
* ``` python
  __str__
  # 用于返回一个描述对象的字符串
  # 主要面向用户
* ```python
  __repr__
  # 返回一个描述符对象本身的字符串
  # 主要面向机器或者开发者
* ```python
  __eq__
  # 用于比较两个对象是否一样
  # 使用 == 调用
* ```python
  __hash__
  # 用于实现根据对象生成hash值的逻辑
  # 将对象放入dict或者set中的时候，被调用
* ```python
  __bool__
  # 在对象被bool函数求解的时候返回一个布尔值
  # 如果类没有实现这个方法，那么__len__将会被用户求解布尔值
* ```python
  __del__
  # 对象被垃圾回收前调用
  # 不要依赖于这个方法做一些重要的事情

## 第 11 章 类的继承
* 类继承的定义
  > ```python
  >   class Person
  >     def __init__(self, name):
  >       self.name = name
  >   
  >   class Student(Person):
  >     def __init__(self, name, age):
  >       self.name = name
  >       self.age = age
  
* isinstance()
* issubclass()
  > * 判断一个类是不是另一个类的子类
  
## 第 12 章 方法重写
* 什么是方法重写
  > * 在子类中重新定义父类中的方法
* 方法重写
* 类属性重写
* 调用父类方法



## 第 19 章 __new__方法
* 函数动态参数列表
  ```python
    def execute(*args, **kwargs):
      print(args)
      print(kwargs)
    
    execute("p1", "p2", name="Jack", age=10)

* __new__方法的定义原型
  > * __new__定义在object类当中，所有类的最终父类都是object类
  > * object.__new__(self, *args, **kwargs)
* __new__方法的执行时刻
  > * 构建一个对象的过程
  > > person = Person("Jack")
  > > person = object.__new__(Person, "Jack")
  > > person.__init__("Jack")
  
* __new__方法的最佳实践
  > * 通常情况下，定义了__new__ 就不用在定义__init__方法
