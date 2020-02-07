def FizzBuzz():
    for fizzbuzz in range(1, 100):
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            print("FizzBuzz")
            continue
        elif fizzbuzz % 3 == 0:
            print("Fizz")
            continue
        elif fizzbuzz % 5 == 0:
            print("Buzz")
            continue
        print(fizzbuzz)
FizzBuzz()
# http://www.blog.pythonlibrary.org/2019/09/18/python-code-kata-fizzbuzz/
