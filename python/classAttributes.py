class MyClass(object):
    defaultVal = []

    def __init__(self, stuff):
        self.stuff = stuff

a = MyClass(2)
b = MyClass("blah")

print("a", a.defaultVal)
print("b", b.defaultVal)

a.defaultVal.append(3)
print("a", a.defaultVal)

b.defaultVal.append(4)
print("b", b.defaultVal)

a.defaultVal = [1]
b.defaultVal = [2]

print("a", a.defaultVal)
print("b", b.defaultVal)

# Those last ones might be a bit of a surprise, but the following code should explain it;

c = MyClass(1)
print(c.__dict__)
print(MyClass.__dict__)

c.defaultVal = [1]
print("after change\n", c.__dict__)
print(MyClass.__dict__)

# So we can see that the #31 is not actually changing the class attribute but it's creating
# a new instance attribute that then "overrides the class one"

# When accessing c.defaultVal python first looks into the instance namespace (__dict__)
# then if not present into the class one. -> .append can actually change the mutable class
# attribute whereas the assignment would "hide/override" the class attribute
# (note that the class attribute is still there, unchanged)


