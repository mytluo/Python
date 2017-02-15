def func_prog(args_tuple, *args_func):
    """ func_prog() takes in a 2-tuple and any number of binary function objects
		returns list of return values from executing each function passing in the elements of the tuple as arguments """
    try:
        # assert only 2 elements in tuple
        assert isinstance(args_tuple, tuple)
        assert len(args_tuple) == 2
        res = []
        # for each function in variable arguments, append the result to res
        for f in args_func:
            res.append((args_tuple, f.__name__, f(args_tuple[0], args_tuple[1])))
        return res
    except AssertionError:
        return "first argument must be 2 elements in a tuple"
if __name__ == '__main__':
    import operator, profile
    try:
        print(func_prog((3, 5), operator.__truediv__, operator.__mul__, operator.__pow__, operator.__sub__))
        print(func_prog(('a', 'b'), operator.__concat__))
        print(func_prog((1, 2, 3)))
        print(func_prog((4, 'c'), operator.__mod__))
    except TypeError as e:
        print(e)
