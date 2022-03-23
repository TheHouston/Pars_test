#Пути к файлам
#path_1 = input ('Путь к первому файлу: ')
#path_2 = input ('Путь ко второму файлу: ')
path_1 = 'F:\\Общая\\test.txt'
path_2 = 'F:\\Общая\\test2.txt'
path_3 = 'C:\\Users\\mbukin\\Desktop\test3.txt'

#Открываем три файла
with open(path_1, 'r') as file_1, open(path_2, 'r') as file_2, open(path_3, 'w') as file_3:
    #Читаем первые два файла
    file_1_r = file_1.read()
    file_2_r = file_2.read()

    #Создание списков из файлов
    quest_section_1 = file_1_r.split('#\n')
    quest_section_2 = file_2_r.split('#\n')

        #Перебор значений из списка
    for section_1 in quest_section_1:
        for section_2 in quest_section_2:
            sect_1 = section_1
            sect_2 = section_2
            try:
                number_1 = sect_1[:15]
                number_2 = section_2[:15]
                if sect_1[15:] == sect_2[15:]:
                    section_1 = section_1.replace(number_1, number_2)
                    quest_section_2.remove(section_1)
            except ValueError:
                #continue
                file_3.write('#\n')
                file_3.write(section_1)
    for section_2 in quest_section_2:
        file_3.write('#\n')
        file_3.write(section_2)