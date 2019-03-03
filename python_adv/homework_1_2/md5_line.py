from hashlib import md5

def md5_for_line(filename, encoding='utf8'):
    with open(filename, encoding=encoding) as f:
        for line in f:
            encoded_line = line.encode(encoding=encoding)
            yield md5(encoded_line).hexdigest()


if __name__ == '__main__':
    import os
    md5_generator = md5_for_line(os.path.join('files','test_for_hash.txt'))
    for line in md5_generator:
        print(line)