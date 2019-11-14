stroka = input("Введите слово или предложение:")
def fnct_for_string(stroka):
    print(stroka[2])
    print(stroka[1:])
    print(stroka[:5])
    print(stroka[:-2])
    print(stroka[::2])
    print(stroka[1::2])
    print(stroka[::-1])
    print(stroka[-1::-2])
    print(len(stroka))

fnct_for_string(stroka)