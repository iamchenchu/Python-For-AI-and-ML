def vectorAddition(v1, v2):
    if len(v1) != len(v2):
        raise ValueError ("Vectors must have same length to perform the task")
    
    c = [v1+v2 for v1, v2 in zip(v1, v2)]
    #c = v1+v2 not working properly 

    return c
print (vectorAddition([8.218, -9.341],[-1.129, 2.111]))
