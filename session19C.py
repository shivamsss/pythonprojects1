# fUNCTION INSIDE A FUNCTION
def func1():
    print("Hello")

    def func2():
        print("Hello2")

    func2()

func1()
print(func1())