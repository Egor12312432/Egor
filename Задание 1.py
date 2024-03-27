f=open('students.csv', encoding='utf8')
a=f.readlines()
f.close()
shapka=a.pop(0)
for i in range(len(a)):
    a[i]=a[i].strip().split(',')
for i in range(len(a)):
    if 'Хадаров Владимир' in a[i][1]:
        print(f'Ты получил:{a[i][-1]}, за проект - {a[i][2]}')
        break
