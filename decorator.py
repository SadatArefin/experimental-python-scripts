def run_n_times(n):
    """Define a decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@run_n_times(3)
def print_sum(a, b):
    print(a + b)

print_sum(3, 5)

@run_n_times(5)
def print_hello():
    print('Hello!')

print_hello()

def tag(*tags):
  # Define a new decorator, named "decorator", to return
    def decorator(func):
        # Ensure the decorated function keeps its metadata
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
        # Call the function being decorated and return the result
        return func(*args, **kwargs)
    wrapper.tags = tags
    return wrapper
    return decorator

def returns_dict(func):
  # Complete the returns_dict() decorator
  def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    assert type(result) == dict
    return result
  return wrapper