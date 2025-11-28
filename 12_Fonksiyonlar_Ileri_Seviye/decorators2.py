import math, time


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(1.6)

        func(*args, **kwargs)

        finish = time.time()
        print(
            "fonksiyon " + func.__name__ + " " + str(finish - start) + " saniye sürdü."
        )

    return wrapper


@calculate_time
def us_alma(a, b):
    print(math.pow(a, b))


@calculate_time
def faktoriyel(number):
    print(math.factorial(number))


@calculate_time
def toplama(a, b):
    print(a + b)


us_alma(2, 3)
faktoriyel(4)
toplama(2, 3)
