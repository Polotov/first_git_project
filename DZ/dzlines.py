with open('rock.txt') as file1:
    list1 = file1.readlines()
    print(len(list1))
    i = 0
    for line in list1:
        print(f'в {i} строке - {len(line)} смволов')
        i += 1