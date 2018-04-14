# PythonYSL

- Introduction
- Summary
    - open 函数使用
    - with 语句
    - except 语句

## Introduction
This is a learning project.

## Summary

### open 函数使用

```

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

Character Meaning

'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)
'U'       universal newline mode (deprecated)
```

### with 语句

```py
with open("/tmp/foo.txt") as file:
    data = file.read()
```

1. 用with后不管with中的代码出现什么错误，都会进行对当前对象进行清理工作。例如file的file.close()方法，无论with中出现任何错误，都会执行file.close（）方法。
2. 其次with只有特定场合下才能使用，这个特定场合只的是那些支持了上下文管理器的对象，这些对象包括：
```py
file
decimal.Context
thread.LockType
threading.Lock
threading.RLock
threading.Condition
threading.Semaphore
threading.BoundedSemaphore
```

那么什么是上下文管理器：
- 这个管理器就是在对象内实现了两个方法：`__enter__()` 和`__exit__()`
- `__enter__()`方法会在with的代码块执行之前执行，`__exit__（）`会在代码块执行结束后执行。
- `__exit__()`方法内会自带当前对象的清理方法。

```py
# -*- coding: utf-8 -*-

class WithObject(object):
    def __init__(self):
        print("__init__")
        pass

    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("__exit__")
        pass

    def hello(self):
        print("hello, with")

with WithObject() as wo:
    wo.hello()

```
### except 语句

```py
try:
    diction = p.load(f)
    print(diction)
except Exception as e:
    print(Exception, e)
```