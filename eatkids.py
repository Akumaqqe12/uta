dict = {}
dict.values()

while True:
    name = input('Введите имя\n>>')
    if name == 'stop':
        break
    age = input('Введите возраст\n>>')

    dict[name] = int(age)
    print(dict)

    max_age = 0
    max_name = ''
    for i in dict.keys():
        if int(dict[i]) > max_age:
            max_name = i
            max_age = dict[i]
print(max_age, max_name)