from Task2.convertToDictionary import convert_to_dictionary


def task2_arguments():
    print("Convert to dictionary with 5 parameters")
    print(convert_to_dictionary(first_name='Иван', last_name='Иванов', patronymic_name='Иванович',
                            age=30, gender='Мужчина'))

    print("Convert to dictionary with 4 parameters")
    print(convert_to_dictionary(first_name='Иван', last_name='Иванов', patronymic_name='Иванович',
                            age=30))

    print("Convert to dictionary with 3 parameters")
    print(convert_to_dictionary(first_name='Иван', last_name='Иванов', patronymic_name='Иванович'))
