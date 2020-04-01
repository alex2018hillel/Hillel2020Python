def example():
    try:
        for i in range(10):
            yield 100 + i
    except Exception as e0:
        yield e0
    else:
        yield 'ok'
    finally:
        print("Finish")

gen = example()
print(next(gen))  # 100
print(next(gen))  # 101
print(next(gen))  # 102
print(gen.throw(Exception('Exception!')))  # Exception!
gen.close()                                # Finish