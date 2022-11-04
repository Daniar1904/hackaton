from products import list_, retrieve_, create_, update, delete_

def main():
    print('Здравствуйте! Вам доступны следующие функции: \n\tLIST - 1\n\tDETAIL - 2\n\tCREATE - 3\n\tUPDATE - 4\n\tDELETE - 5')
    choice = input('Выберите действие (1, 2, 3, 4, 5): ')
    if choice.strip() == '1':
        print(list_())
    elif choice.strip() == '2':
        print(retrieve_())
    elif choice.strip() == '3':
        print(create_())
    elif choice.strip() == '4':
        print(update())
    elif choice.strip() == '5':
        print(delete_())

    answer = input('Хотите продолжить? (yes/no)')
    if answer.lower().strip() == 'yes':
        main()
    else:
        print()
        print('До свидания!')

main()





