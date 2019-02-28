class Pet:
    def __init__(self):
        super.__init__()


class Dog(Pet):
    def __init__(self):
        pass

class BulDog:
    count = 1

print (issubclass(Pet, Dog))

#raise ValueError("error")
#raise "ValueError"
#raise ValueError
print (BulDog().get)
