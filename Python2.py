class DivisionByNull:
    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def divide_by_null(dividend, divider):
        try:
            return dividend / divider
        except ZeroDivisionError:
            return f"Деление на ноль недопустимо"


print(DivisionByNull.divide_by_null(100, 0))
print(DivisionByNull.divide_by_null(100, 10))
