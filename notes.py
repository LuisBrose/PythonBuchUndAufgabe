import fractions

if __name__ == "__main__":
    x = fractions.Fraction(1.454165456432132)  # fractions Module
    print(x)
    print(x.limit_denominator(1000))

    y = "abdkfjgiucnglijngjol"  # slice
    print(y[20:1:-1])

    print(hash("abcde") % 10)  # hash value of an object
    print(hash(y) == hash(y))  # better: print(y is y)

    a, *b, c, d = 1, 2, 3, 4, 5, 6
    print(a, b, c, d)

    d = {"a": 1, "b": 1, "c": 1}
    e = {"a": 2, "c": 2, "d": 2}
    d.update(e)  # merge dictionaries
    print(d, d.keys(), d.items(), d.values())  # overview available dict views

    ary = [1, 2, 2, 2, 3, 3, 3, 3, 4]  # set data structure
    my_set = set(ary)
    print(my_set)  # set functions include copy,add,discard and clear: my_set.copy()

    print(bool(my_set))
    my_set.clear()  # bool value of objects: len(collection) == 0/0/None -> False
    print(bool(my_set))  # otherwise -> True

    import copy

    ary2 = [1, 2, 3, [1, 2, 3]]
    copy_ary = []
    copy_ary.clear()
    copy_ary = copy.deepcopy(ary2)
    # deepcopy creates a new compound object and recursively adds the inner elements
    print(copy_ary)

    exec("print" "(123456)")  # execute a statement
    print(eval("5+" "5"))  # evaluate an expression

    for i in range(1, 5):
        print("step", i, sep=": ", end=" completed \t\t")  # custom separator and ending
    print("\r")

    flo = 152131.15466513221185465413
    print(
        f"{flo:.4f}\t" f"{flo:.4e}\t" f"{flo:.2%}\t" f"{flo:n}\n"
    )  # easily format strings all format options: https://www.w3schools.com/python/ref_string_format.asp

    import random

    INT = 10
    for i in range(10):
        print(
            f"{random.randint(2, INT) ** random.randint(2, INT):^20}"  # whitespace format
            f"{random.randint(2, INT) ** random.randint(2, INT):^20}"
            f"{random.randint(2, INT) ** random.randint(2, INT):^20}"
        )

    print(1 if True else 2)  # ternary in python

    list_comprehension = [item + 1 for item in range(10)]  # list comprehension
    print(list_comprehension)



