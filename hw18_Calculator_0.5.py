# homework 18 - Calculator 0.4
class MyValidation:
    @classmethod
    def digit_validation(cls, count_msg=''):
        next_step = True
        return_digit = None
        while next_step:
            num = input(f'Please, input the {count_msg} digit\n')
            if num == '':
                return num
            else:
                try:
                    return_digit = float(num)
                    next_step = False
                except ValueError as val_err:
                    print(f'Incorrect input: only digits allowed ({val_err}). Try again')
        return return_digit


class Calculator:
    def __init__(self):
        print('Hello! This is the finest calculator (version 0.5)\n'
              'This version can plus or minus or multiply or divide digits and validate input for digits.'
              )
        self._choice()

    def _choice(self):
        input_msg = ('Please, choose the type of the operation. Input "+" or "-" or "*" or "/" to operate with '
                     'two digits.\nIf you want to sum more than two digits please choose "+++" operation type.\n'
                     )
        input_type = input(input_msg)
        assert input_type in ('+', '-', '*', '/', '+++'), 'Incorrect input the type of the operation!'
        self.operation_type = input_type

    def _add(self) -> str:
        assert self.operation_type == '+', 'Only add ("+") type allowed'
        a = MyValidation.digit_validation('first')
        b = MyValidation.digit_validation('second')
        result: float = a + b
        return f'{a} {self.operation_type} {b} = {result}'

    def _subtract(self) -> str:
        assert self.operation_type == '-', 'Only subtract ("-") type allowed'
        a = MyValidation.digit_validation('first')
        b = MyValidation.digit_validation('second')
        result: float = a - b
        return f'{a} {self.operation_type} {b} = {result}'

    def _multiply(self) -> str:
        assert self.operation_type == '*', 'Only multiply ("*") type allowed'
        a = MyValidation.digit_validation('first')
        b = MyValidation.digit_validation('second')
        result: float = a * b
        return f'{a} {self.operation_type} {b} = {result}'

    def _divide(self) -> str:
        assert self.operation_type == '/', 'Only divide ("/") type allowed'
        a = MyValidation.digit_validation('first')
        b = MyValidation.digit_validation('second')
        if b != 0:
            result: float = a / b
        else:
            result = float("inf")
        return f'{a} {self.operation_type} {b} = {result}'

    def _add_many_num(self) -> str:
        assert self.operation_type == '+++', 'Only add many numbers ("+++") type allowed'
        next_digit = True
        result = 0
        nums = []
        print('Please, input a digits to sum or Enter to start operation')
        while next_digit:
            num = MyValidation.digit_validation()
            if num != '':
                result += num
                nums.append(str(num))
            elif num == '':
                next_digit = False
            else:
                print('Incorrect input')
        result_text = ' + '.join(nums)
        return f'{result_text} = {result}'

    def run(self):
        if self.operation_type == '+':
            return self._add()
        elif self.operation_type == '-':
            return self._subtract()
        elif self.operation_type == '*':
            return self._multiply()
        elif self.operation_type == '/':
            return self._divide()
        elif self.operation_type == '+++':
            return self._add_many_num()
        else:
            pass


if __name__ == '__main__':
    my_calc = Calculator()
    print(f'Result for operation: {my_calc.run()}')
