import sys
from io import StringIO

def adv_print(*args, start='', in_file = False, **kwargs):
    """
    Get max_line and all arguments used in built-in print function as kwargs.
    """
    max_line = kwargs.pop('max_line', False)
    print(kwargs)
    old_stdout = sys.stdout
    value = StringIO()
    sys.stdout = value
    print(*args, **kwargs)
    sys.stdout = old_stdout
    value = value.getvalue()
    value = start + value
    if max_line:
        value = value[:max_line] + '\n' + value[max_line:]
    if in_file:
        if 'filename' in kwargs:
            filename = kwargs['filename']
        else:
            filename = 'output.txt'
        with open(filename, 'w') as f:
            f.write(value)
    print(value)


if __name__ == "__main__":
    value = 'Hello, world!'
    adv_print(value)
    adv_print(value, start="Test")
    adv_print(value, max_line=6)
    adv_print(value, in_file=True, filename='test.txt')
    adv_print(1, 2, 3, ['a', 'v'], start='New Test ', max_line = 9, in_file=True, sep=' 0_0 ', end='XxX')