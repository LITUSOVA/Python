class Exception:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                a = int(input('Введите значения через Enter - '))
                self.my_list.append(a)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка или булево")
                yes_no = input(f'Попробовать еще раз? Ответьте yes или no: ')

                if yes_no == 'yes':
                    print(try_except.my_input())
                elif yes_no == 'no':
                    return f'Вы вышли'
                else:
                    print(f"Недопустимое значение - строка или булево")
                    yes_no = input(f'Попробовать еще раз? Ответьте yes или no: ')

                    if yes_no == 'yes':
                        print(try_except.my_input())
                    elif yes_no == 'no':
                        return f'Вы вышли'
                        pass
        pass


try_except = Exception()
print(try_except.my_input())
