#Пути к файлам
#path_1 = input ('Путь к первому файлу: ')
#path_2 = input ('Путь ко второму файлу: ')
path_1 = 'F:\\Общая\\003.90(сборка).txt'
path_2 = 'F:\\Общая\\003.90.txt'
path_3 = 'C:\\Users\\mbukin\\Desktop\\test3.txt'

voprosov = 0

#Открываем три файла
with open(path_1, 'r') as file_1, open(path_2, 'r') as file_2, open(path_3, 'w') as file_3:
    #Читаем первые два файла
    file_1_r = file_1.read()
    file_2_r = file_2.read()

    #Создание списков из файлов
    question_section_1 = file_1_r.split('#\n')
    question_section_2 = file_2_r.split('#\n')
    print(len(quest_section_2))
        #Перебор значений из списка
    for section_1 in question_section_1:
        for section_2 in question_section_2:
            sec_1 = section_1.split('\n')
            sec_2 = section_2.split('\n')
            try:
                dlina_1 = len(sec_1[0])
                dlina_2 = len(sec_2[0])
                number_1 = section_1[:dlina_1]
                number_2 = section_2[:dlina_2]
                if section_1[dlina_1:] == section_2[dlina_2:]:                    
                    section_1 = section_1.replace(number_1, number_2)
                    question_section_2.remove(section_1)
                    print('Удалил')
            except ValueError:
                file_3.write('#добавление\n')
                file_3.write(section_1)
                voprosov += 1
    for section_2 in question_section_2:
        file_3.write('#итоговый список\n')
        file_3.write(section_2)
voprosov += len(quest_section_2)
print (voprosov)