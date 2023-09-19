

a = input ('я сказав введи текст бо мізинець відріжжу')
while a == 'та':
    with open("tata.txt", "a") as f:
        f.write(a)
    with open("tata.txt", "r") as f:
        f = f.read()
        print(f)
    a = input('давай бистро вводи текст бо салфетками нагодую')

    print('ну ок нагодую салфетками в 3.00')