class MyNumbers:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration


liste = MyNumbers(10, 20)

my_iter = iter(liste)

while True:
    try:
        print(next(my_iter))
        print(next(my_iter))
        print(next(my_iter))
    except StopIteration:
        print("Liste bitti.")
        break

# for x in liste:
#     print(x)
