def foo(*args, **kwargs):
    print(args)
    print(kwargs)


foo({1, 2}, {1: 10, 2: 20}, x1=10)
foo()


def int_to_str(source_list):
    return list(map(lambda x: str(x),source_list))

nums = [1, 2, 3, 4, 5, 6]

print(int_to_str(nums))

print(list(zip(
  filter(bool, range(3)),
  [x for x in range(3) if x]
)))

def stringify(func):
  return func


@stringify
def multiply(a, b):
  return a * b

print(multiply(10,2))