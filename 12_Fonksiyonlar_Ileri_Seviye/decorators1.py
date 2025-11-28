def my_decorator(func):
    def wrapper(name):
        print("Fonksiyondan önceki işlemler.")
        func(name)
        print("Fonksiyondan sonraki işlemler.")

    return wrapper


@my_decorator
def say_hello(name):
    print("Hello", name)


say_hello("Utku")
