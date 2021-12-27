from time import perf_counter_ns

NS_TO_MICRO = 1000


def solver(fn):
    def wrap(*args, **kwargs):
        start = perf_counter_ns()
        res = fn(*args, **kwargs)
        elapsed_time = perf_counter_ns() - start
        print(f"{fn.__name__}{'-Test' if args[0] else ''}:")
        print(f"Answer is: {res}")
        print(f"Took: {elapsed_time / NS_TO_MICRO} µs\n")
        return res

    return wrap