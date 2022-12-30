import os
import itertools
from unrar import rarfile
from datetime import datetime
from string import digits, ascii_letters, punctuation

symbols = ''
path_to_archive = ''


def brute_archive():
    print('***Привет!***')

    path_to_archive = input('Введите путь к архиву: ')
    if not os.path.exists(path_to_archive):
        print('Некорректно введены данные!')
        return

    try:
        password_length = input('Введите длину предполагаемого пароля,'
                                'от скольки до скольки символов, например 5 - 7: ')
        password_length = [int(item) for item in password_length.split('-')]
    except:
        print('Некорректно введены данные!')
        return

    print('Если пароль содержит только цифры, введите: 1')
    print('Если пароль содержит только латинские буквы, введите: 2')
    print('Если пароль содержит цифры и латинские буквы, введите: 3')
    print('Если пароль содержит цифры, буквы и спецсимволы введите: 4')

    try:
        choice = int(input(': '))
        if choice == 1:
            symbols = digits
        elif choice == 2:
            symbols = ascii_letters
        elif choice == 3:
            symbols = digits + ascii_letters
        elif choice == 4:
            symbols = digits + ascii_letters + punctuation
        else:
            print('Некорректно введены данные!')
            return

    except Exception as e:
        print(e.args[0])
        return

    # подбор пароля
    start_time = datetime.now()
    print(
        f'Начато в {start_time}')
    for pass_len in range(password_length[0], password_length[1] + 1):
        for password in itertools.product(symbols, repeat=pass_len):
            password = ''.join(password)
            print(password)
            try:
                with rarfile.RarFile(path_to_archive, 'r',
                                     pwd=password) as myrar:
                    end_time = datetime.now()
                    print(f'Пароль {password} подобран!')
                    print(f'Окончено в {end_time}, \n'
                          f'затрачено времени {end_time - start_time}')
                    return
            except Exception as e:
                print(e.args[0])


def main():
    brute_archive()


if __name__ == '__main__':
    main()
