def func(*args, **kwargs):
    print("Positional arguments:", args)  # *args means : u can give any dynamic number of arguments of same variables
    print("Keyword arguments:", kwargs) # **kwargs means : u can define any number of variables in the method dynamically

func(1, 2, 3, a='foo', b='bar', c =30)

func(1, 2, 3, a1='fooqsq', b1='basqdr', c1 =30)