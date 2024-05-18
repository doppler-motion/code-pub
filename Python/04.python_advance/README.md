# Python高级编程知识

----

[TOC]

------

## 第 1 章 装饰器

* 自定义装饰器
* @wraps装饰器
  > * 去掉装饰器外包装，返回本来的函数名
  >   * 未加wraps
  >     > ```python 
  >     > def welcome(fn):
  >     > # @wraps(fn)
  >     >     def wrapper(*args, **kwargs):
        >         print("welcome")
        >         result = fn(*args, **kwargs)
        >         return result
        > 	return wrapper
        > 
        > @welcome
        > def my_fun(msg: str):
        >     print(f"hello {msg}")
        > 
        > my_fun(msg="Jack")
        > print(my_fun)    #  ***<function welcome.<locals>.wrapper at 0x000001AAFFE0DAF0>***
        > ```
  
      * 加wraps
      
        ```python
        from functools import wraps
  
  
  ​      
        def welcome(fn):
            @wraps(fn)
            def wrapper(*args, **kwargs):
                print("welcome")
                result = fn(*args, **kwargs)
                return result
        
            return wrapper
  
  
  ​      
        @welcome
        def my_fun(msg: str):
            print(f"hello {msg}")
  
  
  ​      
        my_fun(msg="Jack")
        print(my_fun)  # ***<function my_fun at 0x000002C04C3DDAF0>***
        ```

  
  ​      
  
* 带参数的装饰器

```python
from functools import wraps


# def welcome(fn):
#     @wraps(fn)
#     def wrapper(*args, **kwargs):
#         print("welcome")
#         result = fn(*args, **kwargs)
#         return result
#
#     return wrapper

def welcome(name):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"welcome {name}")
            result = fn(*args, **kwargs)
            return result

        return wrapper
    return decorator


@welcome("Tom")
def my_fun(msg: str):
    print(f"hello {msg}")


my_fun(msg="Jack")
print(my_fun)
```



## 第 3 章 上下文管理器
* 什么是上下文管理器
  > * 本质上是一个对象
  > * 定义了运行时的上下文
  > * 使用with语句来执行
* with语句  执行上下文管理器
```python
with context_manager as tex_m:
    pass
```
* 上下文管理器的协议
  > * __enter__() -- 安装上下文，返回对象
  > * __exit__() -- 清楚释放对象
* 上下文管理器的应用
  > * 开 关
  > * 锁 释放
  > * 启动 停止
  > * 改变 重置

## 第10章 Mixin（混入） 模式
* 什么是 Mixin模式
  > * 通用功能抽取封装入Mixin类
  > * 需要Mixin类功能的类通过多继承来获取Mixin类的功能
* Mixin实例
```python
class MapMixin:
    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value


class DictMixin:
    def to_dict(self):
        return self.__convert_dict(self.__dict__)

    def __convert_dict(self, attrs: dict):
        result = {}
        for key, value in attrs.items():
           result[key] = self.__convert_value(value)

    def __convert_value(self, value):
        if isinstance(value, DictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self.__convert_dict(value)
        elif isinstance(value, list):
            return [self.__convert_value(v) for v in value]
        elif hasattr(value, "__dict__"):
            return self.__convert_dict(value.__dict__)
        else:
            return value


class Student(MapMixin, DictMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.__dict__)
```

## 第13章  单例模式
* 什么是单例模式
    > * 让一个类只能制造出一个对象
    > * 针对需要共享数据的对象
    >   * 工厂对象
    >   * 数据库连接池对象
    >   * 其他想要共享的对象
* 单例模式的代码实现
  ```python
  # 方法4 元类
  class SingletonMeta(type):
    def __call__(cls, *args, **kwargs):
        if hasattr(cls, "_instance"):
            return getattr(cls, "_instance")
  
        obj = super().__call__(*args, **kwargs)
        setattr(cls, "_instance", obj)
        return obj
  
  # 使用
  class Person(metaclass=SingletonMeta):
    pass

## 第15章 并发编程 -- 线程

*   线程与进程

>   *   进程是操作系统中运行的一个任务
>       *   当前的操作系统基本都支持多进程并发
>       *   进程拥有独立的CPU、内存等资源
>   *   一个线程是一个进程中运行的一个任务
>       *   一个进程可以同时并发多个任务
>       *   线程之间共享进程的CPU、内存等资源

*   创建线程
*   给线程传递参数

## 第16章 并发编程 -- 线程进阶

*   通过继承创建线程

```python
class MyThread(Thread):
    def __init__(self):
        super(MyThread, self).__init__()
        
    def run(self):
        pass
```



*   守护线程

    *   守护线程会在主线程结束时候自动结束
    *   主线程则需要等到所有非守护线程结束才能结束
    *   守护线程一般用于非关键性的线程，比如日志

    ```python
    def task():
        pass
    
    thread = Thread(target=task, daemon=True)
    thread.start()
    ```

    

*   线程安全队列

```python
# queue 模块中的Queue类提供了线程安全队列功能
queue.put(item, block=True)
queue.put(item, timeout=3)
queue.get(block=False)
queue.get(timeout=10)
queue.qsize()
queue.empty()
queue.full()
```



*   生产者消费者线程实例

## 第17章 并发编程 -- 线程锁

*   线程锁

    >   当多个线程在同一时刻访问同一数据时，可能产生数据丢失，覆盖，不完整等问题
