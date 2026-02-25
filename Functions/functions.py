
def outer_func():
    msg = "Hello there!"
    res = ""

    def inner_func():
        nonlocal res
        res = "How are you doing?"
        print(msg)
    
    inner_func()
    print(res)

outer_func()