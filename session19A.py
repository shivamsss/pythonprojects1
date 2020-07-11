#generators in python
#yield in python

def Hello():
    print("This is Hello")
    return "heya"
Hello()
print(Hello())
result = Hello()
print(result)

print("=========================================================")

def Helloagain():
    print("This is hello again")
    yield "hey1"
    yield "hey2"
    yield "hey3"
    yield "hey4"
print(Helloagain())
result1 = Helloagain()
print(result1)
print(next(result1))