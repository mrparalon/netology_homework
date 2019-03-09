def adv_print(value, start='', in_file = False, **kwargs):
    value = start + value
    if 'max_line' in kwargs:
        max_line = kwargs['max_line']
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
    adv_print(value, start='New Test ', max_line = 9, in_file=True)