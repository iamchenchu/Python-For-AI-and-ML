def function(n):
    return lambda a : n-a

result = function(20)
print(result(10))
print(result(20))
print(result(-20))