import fractions

if __name__ == "__main__":
    x = fractions.Fraction(1.454165456432132)
    print(x)
    print(x.limit_denominator(1000))

    y = "abdkfjgiucnglijngjol"
    print(y[20:1:-1])

    print(hash("abcde") % 10)

    a, *b, c, d = 1, 2, 3, 4, 5, 6
    print(a, b, c, d)

    d = {"a": 1, "b": 1, "c": 1}
    e = {"a": 2, "c": 2, "d": 2}
    d.update(e)
    print(d, d.keys(), d.items(), d.values())
