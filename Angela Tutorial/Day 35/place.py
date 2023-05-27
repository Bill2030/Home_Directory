def divide(x,y):
    try:
        result = x// y
        print("The answer is", result)
    except Exception as e:
        print("The error is ", e)
x = divide(9,3)
y = divide(3,0)





