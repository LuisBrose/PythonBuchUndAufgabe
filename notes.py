import fractions

if __name__ == "__main__":
    x = fractions.Fraction(1.454165456432132)  # fractions Module
    print(x)
    print(x.limit_denominator(1000))

    y = "abdkfjgiucnglijngjol"  # slice
    print(y[20:1:-1])

    print(
        hash("abcde")
    )  # hash value of an object                                                         !not in book!
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
    )  # easily format strings, all format options: https://www.w3schools.com/python/ref_string_format.asp

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

    def any_params(*params):  # varying parameter amount
        for p in params:
            print(p, end=" -> ")
        print("\r")

    any_params(2, 4, 6, 4, 7, 5, 4, 2, 1, 5)

    def default_param_values(width=1, height=1):  # assign default parameter values
        print(width, "x", height, " cube created")

    default_param_values()  # no need to specify param values -> default values
    default_param_values(2, 2)

    g_scope = None

    def local_scope():
        global g_scope  # variable is part of global scope instead of local
        g_scope = "something"

    res = map(
        (lambda param1, param2: param1 + param2), [1, 2, 3], [1, 2, 3]
    )  # create a simple anonymous/lambda function
    print(set(res))

    import sys

    print(list(sys.argv))  # access command line arguments

    def docstring_demonstration(random_min: int, random_max: int):
        """Generate a pseudo random number
        :param random_min: the smallest possible value
        :param random_max: the largest possible value
        :return: int between random_min and random_max
        """
        return random.randint(random_min, random_max)

    print(
        docstring_demonstration(1, 10)
    )  # hover to fetch documentation             !not in book!

    # Python allows inheriting from multiple classes directly
    class MultipleInheritance(ImportError, ImportWarning):
        pass

    import time

    t = time.localtime()
    print(
        "Heute ist der ",
        f"{t.tm_mday:02d}.{t.tm_mon:02d}",  # manual formatting
        ".",
        t.tm_year,
        " um ",
        f"{t.tm_hour:02d}:{t.tm_min:02d} Uhr",
        sep="",
    )
    print(
        "Heute ist der ",
        time.strftime("%d.%m.%Y", t),  # easily format using strftime formatting
        " um ",
        time.strftime("%H:%M Uhr", t),
        sep="",
    )

    print(time.mktime(t))  # time since Epoch

    import threading

    def go_to_sleep(sec: int):
        print(f"Sleeping Thread: {threading.get_ident()}")
        time.sleep(sec)
        print(
            f"Thread {threading.get_ident()} is slowly waking up after napping for ",
            sec,
            "s",
            sep="",
        )

    sleeping_thread = threading.Thread(
        target=go_to_sleep, args=[docstring_demonstration(2, 6)]
    )  # create a sleeping thread

    sleeping_thread.start()

    print(f"Main Thread: {threading.get_ident()}")

    import collections

    deque = collections.deque([1, 2, 3])  # deque => double-ended queue
    print(deque[0], deque[1], deque[2], sep=" <-> ")
    deque.pop()
    deque.appendleft(5)
    print(deque[0], deque[1], deque[2], sep=" <-> ")

    import re

    lorem = (
        "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut "
        "labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et "
        "ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem "
        "ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et "
        "dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. "
        "Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
    )
    print(re.findall("Lorem", lorem))  # regex in python
    print(re.findall(".rem", lorem))
    print(re.findall("[ue]m", lorem))
    print(re.findall("[a-z]m", lorem))

    try:
        my_file = open("notes_out/text.txt", mode="a")
    except Exception as e:
        print("An Error occurred: ", e)
        sys.exit(0)
    my_file.write("Test \n")
    my_file.close()

    try:
        my_file = open("notes_out/text.txt")  # mode r is default
    except Exception as e:
        print("An Error occurred: ", e)
        sys.exit(0)
    my_file.seek(1)  # traverse the file by 1 byte
    print(my_file.readlines())  # read to list of strings
    my_file.close()

    try:
        my_file = open("notes_out/data.csv", mode="w")  # read from csv
    except Exception as e:
        print("An Error occurred: ", e)
        sys.exit(0)
    data_tuples = [("Erik", 20, "m"), ("Max", 25, "m"), ("Anna", 19, "w")]
    for tup in data_tuples:
        my_file.write(f"{tup[0]};{tup[1]};{tup[2]}\n")
    my_file.close()

    try:
        my_file = open("notes_out/data.csv")  # read from csv
    except Exception as e:
        print("An Error occurred: ", e)
        sys.exit(0)
    result = my_file.read()
    my_file.close()
    result_lines = result.split(chr(10))
    data_tuples_read = []
    for line in result_lines:
        if line:
            data_tuples_read.append(tuple(line.split(";")))
    print(data_tuples_read)

    import pickle

    try:
        my_file = open("notes_out/serialized.bin", "wb")  # serialize to binary file
    except Exception as e:
        print("An Error occurred: ", e)
        sys.exit(0)
    my_dictionary = {"a": "a", "b": "b", "c": "c", "d": "d"}
    pickle.dump(my_dictionary, my_file)
    my_file.close()

    try:
        my_file = open("notes_out/serialized.bin", "rb")  # read serialized from binary
    except Exception as e:
        print("An Error occurred: ", e)
        sys.exit(0)
    print(pickle.load(my_file)["c"])
    my_file.close()

