# 高阶函数：higher-order function 当一个函数接收另外一个函数当作自己的参数的时候，这个函数就是一个高阶函数

import time


def time_master(func):
    def call_func():
        print('start program')
        start = time.time()
        func()
        stop = time.time()
        print('stop the program')
        print(f'一共耗费{(stop - start):.5f}秒')

    return call_func


def myfunc():
    time.sleep(2)
    print('hello python')


myfunc = time_master(myfunc)
myfunc()

"""
问题：
第10行，func是函数time_master()的参数。出现在这里啥意思？要传入参数吗？有()，是要执行，可是它没被定义啊。
第15行，为啥要返回内函数call_func，而且没有（）?
第三个函数的执行体 time.sleep(2)是模块 import time的指定的写法吗？ 
第23行，啥意思？调用函数myfunc,等同于调用以myfunc为参数的time_func(),为啥time_func()的参数可以变，
  
回答：  
你这四个问题**全是 Python 装饰器/高阶函数的核心难点**，我用**最通俗、最直白、不绕弯**的方式给你讲清楚，保证你一次性看懂！

先把你提到的代码（我还原成标准写法）放这里，方便对照：
```python
import time  # 第3行

# 第5行
def time_master(func):  # 第10行：func 是参数
    def call_func():
        print("开始计时")
        start = time.time()
        
        func()  # 执行传入的函数
        
        end = time.time()
        print("结束计时，耗时：", end - start)
    return call_func  # 第15行：返回内函数

# 第20行
def myfunc():
    time.sleep(2)  # 第三个函数执行体

# 第23行
myfunc = time_master(myfunc)
```

---

# 1. 第10行：`func` 是参数，出现这里啥意思？要传吗？没定义为啥能写？
### 一句话解释：
**`func` 就是一个“占位参数”，代表“待会儿要传进来的那个函数”。**

- 它**不是**提前定义好的函数
- 它**只是一个形参名字**，和 `def add(a,b)` 里的 `a`、`b` 完全一样
- 它的作用：**告诉 time_master，你待会儿要给我传一个函数进来**

### 举个超简单类比：
```python
def 计时器(要计时的动作):
    开始计时
    执行 要计时的动作
    结束计时
```
这里的 **“要计时的动作”** 就是你代码里的 **`func`**。

---

# 2. 第15行：为什么要返回内函数 `call_func()`？
### 一句话：
**为了“包装”原函数，不破坏原函数，还能给它加功能。**

你写的是**高阶函数 + 闭包**，规则是：
- 外层函数 `time_master` 接收一个函数
- 内层函数 `call_func` 做**增强逻辑**（计时）
- **必须返回内层函数**，才能把“增强版函数”交给外面使用
-没有（）是因为只是返回函数，而不是返回call_func的值。引而不发？

### 不返回会怎样？
你调用 `time_master(myfunc)` 后，**什么都拿不到**，计时功能也用不了。

### 返回的目的：
把 **“原来的函数 + 计时功能”打包成一个新函数** 还给你。

---

# 3. `time.sleep(2)` 是模块固定写法吗？
### 是的！
- `time` 是 Python 自带**时间模块**
- `sleep(秒数)` 是它的功能：**程序暂停指定秒数**
- 写法固定：`time.sleep(数字)`

你这里写 `time.sleep(2)` 意思就是：
**让程序停 2 秒，方便测试计时功能。**

---

# 4. 第23行：`myfunc = time_master(myfunc)` 到底啥意思？
这是新手**最最最晕**的地方，我用最简单的话讲：

### 整行意思：
**把 myfunc 这个函数，传给 time_master 包装一下，
然后把包装后的新函数，重新赋值给 myfunc。**

---

## 拆解给你看（超级关键）
### ① 定义时：`def time_master(func)`
`func` 只是**参数名**，代表“要传进来的函数”。

### ② 调用时：`time_master(myfunc)`
这里 `myfunc` 就是**实实在在传进去的函数**。

### ③ 参数名可以变吗？
**完全可以！**
你定义时写 `func`、`f`、`fn`、`xxx` 都行，
调用时传 `myfunc`、`test`、`abc` 也都行。

---

## 最直观的比喻
```python
def 包装(礼物):
    给礼物包一层纸
    return 包好的礼物

礼物 = 包装(礼物)
```
你看：
- `礼物` = 你代码里的 `myfunc`
- `包装` = 你代码里的 `time_master`

**参数名只是占位，传什么就是什么！**

---

# 5. 第23 行执行后发生了什么？（终极真相）
执行前：
```
myfunc = 原来的函数（只 sleep 2秒）
```

执行后：
```
myfunc = 被包装后的新函数（计时 + sleep 2秒）
```

所以以后你调用：
```python
myfunc()
```
实际执行的是：
```
计时开始 → sleep 2秒 → 计时结束
```

---

# 用三句话总结你所有疑问
1. **`func` 是参数占位符，不是提前定义的函数**
2. **返回 `call_func` 是为了得到“包装后的新函数”**
3. **`myfunc = time_master(myfunc)` 就是给函数加计时功能，不改变原函数名字**

---
如果你愿意，我可以**把这段代码改成装饰器写法**（@语法），让代码更简洁、更好懂！"""
