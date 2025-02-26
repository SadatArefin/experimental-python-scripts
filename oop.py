class Calculator:
    def __init__(any):
        any.result = 0

    def add(any1, num):
        any1.result += num
        return any1.result

    def sub(any2, num):
        any2.result -= num
        return any2.result
    
    def mul(any3, num):
        any3.result *= num
        return any3.result

calc = Calculator()
print(calc.add(5))
print(calc.sub(3))
print(calc.mul(8))