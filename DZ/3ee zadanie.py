def write(filename, mode):
    if mode == 'read':
        file = open(filename)
        print(file1.read())
    elif mode == 'write':
        file1 = open(filename, 'w')
        text = input("введите текст:")
        file1.write(text)


write('spam.txt','write')
