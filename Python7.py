class Complex:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * j'

    def __add__(self, other):
        if self.b > 0 and other.b > 0:
            if self.a + other.a != 0:
                return f'Сумма двух комплексных чисел равна sum_z = {self.a + other.a} + {self.b + other.b} * j'
            else:
                return f'Сумма двух комплексных чисел равна sum_z = {self.b + other.b} * j'
        elif self.b == 0 and other.b == 0:
            if self.a + other.a != 0:
                return f'Сумма двух комплексных чисел равна sum_z = {self.a + other.a}'
            else:
                return f'Сумма двух комплексных чисел равна sum_z = 0'
        elif self.b + other.b == 0:
            if self.a + other.a != 0:
                return f'Сумма двух комплексных чисел равна sum_z = {self.a + other.a}'
            else:
                return f'Сумма двух комплексных чисел равна sum_z = 0'
        else:
            if self.a + other.a != 0:
                if self.b + other.b > 0:
                    return f'Сумма двух комплексных чисел равна sum_z = {self.a + other.a} + {self.b + other.b} * j'
                else:
                    return (f'Сумма двух комплексных чисел равна sum_z = ' 
                           f'{self.a + other.a} - {abs(self.b + other.b)} * j')
            else:
                if self.b + other.b > 0:
                    return f'Сумма двух комплексных чисел равна sum_z = {self.b + other.b} * j'
                else:
                    return f'Сумма двух комплексных чисел равна sum_z = - {abs(self.b + other.b)} * j'

    def __mul__(self, other):
        return (f'Произведение двух комплексных чисел равно mul_z = '
                f'{self.a * other.a - (self.b * other.b)} + {self.b * other.a} * j')

    def __str__(self):
        if self.b > 0:
            return f'z = {self.a} + {self.b} * j'
        elif self.b == 0:
            return f'z = {self.a}'
        else:
            return f'z = {self.a} - {abs(self.b)} * j'


z_1 = Complex(2, -1)
z_2 = Complex(-2, 1)
print(z_1)
print(z_2)
print(z_1 + z_2)
print((z_1 * z_2))
