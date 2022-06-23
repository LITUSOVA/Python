my_dict = {}
with open('my_file_6.txt', 'r') as file_6:
    for line in file_6:
        subject, lecture, practice, lab = line.split()
        my_dict[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество занятий по каждому предмету - \n {my_dict}')

