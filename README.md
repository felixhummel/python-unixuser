# Using `__matmul__` for fun and profit

```
>>> from unixuser import User, Host
>>> unixuser = User('alice') @ Host('example.com')
>>> str(unixuser)
'alice@example.com'
```

