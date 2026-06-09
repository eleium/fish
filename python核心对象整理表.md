

完整版：Python 核心对象整理表（五方面框架）
对象	1. 作用	2. 实现	3. 条件/时机	4. 优先级/顺序	5. 常见坑
__init__					
__new__					
__str__					
__repr__					
__call__	让实例像函数一样可调用	实现 __call__(self, *args, **kwargs)	需要对象保持状态且可调用时（计数器、装饰器）	实例化后调用 obj() 时触发	忘记写 return 会返回 None
__get__	描述符：拦截属性读取	实现 __get__(self, instance, owner)	需要控制属性的读取行为时	属性查找链中优先级高（数据描述符）	不处理 instance is None 会导致类访问报错
__set__	描述符：拦截属性赋值	实现 __set__(self, instance, value)	需要控制属性的赋值行为时（类型校验）	数据描述符，优先级高于实例属性	不实现 __get__ 时仍会被类属性覆盖
__delete__	描述符：拦截属性删除	实现 __delete__(self, instance)	需要控制属性的删除行为时	数据描述符，优先级高于实例属性	容易忘记实现，导致 del 不生效
@staticmethod	定义静态方法	描述符，返回原始函数，不绑定实例或类	方法逻辑与类相关但不需要访问类或实例时	优先级低于实例属性（非数据描述符）	误以为能访问 self 或 cls
@classmethod	定义类方法	描述符，返回绑定类的方法	需要替代构造函数、访问类状态、支持继承多态时	优先级低于实例属性（非数据描述符）	忘记返回 cls(...) 会导致无法创建实例
property	将方法转换为属性访问	描述符（__get__/__set__/__delete__）	需要在获取/设置属性时执行逻辑，又不改变调用语法时	数据描述符，优先级高于实例属性	忘记定义 setter 会导致属性只读
__slots__					
__iter__					
__next__					
__enter__					
__exit__					
__add__					
__sub__					
__len__					
__getitem__					
__setitem__					
__delitem__					
__contains__					
__eq__					
__lt__					
__gt__					
__le__					
__ge__					
__ne__					
__getattribute__					
__setattr__					
__delattr__					
__dir__					
__format__					
__hash__					
__reduce__ / __reduce_ex__					
__subclasses__					
__mro__					
__bases__					
__dict__					
__weakref__					
__module__					
__name__					
__qualname__					
__annotations__					
__defaults__					
__kwdefaults__					
__code__					
__closure__					
__globals__					
__builtins__					
__file__					
__package__					
__path__					
__cached__					
__loader__					
__spec__					
切片 (slice)					
__index__					
上下文管理器 (with)					
__aiter__ / __anext__					
__await__					
协程与 async/await					
这个清单已经包含了 Python 中绝大部分重要的特殊方法和对象。你可以根据自己的学习进度，一项一项地填充。