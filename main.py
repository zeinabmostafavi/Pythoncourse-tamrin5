# init

f = open('zeinab_translate/translate.txt')
big_text = f.read()
parts = big_text.split('\n')
words = []
i = 0

while i < len(parts):
    my_dict = {'english': parts[i], 'persian': parts[i+1]}
    words.append(my_dict)
    i += 2


while True:
    print("____________")
    print("1- insert word in dictionary")
    print("2- dictionary english to farsi")
    print("3- dictionary  farsi to english")
    print("4- translation")
    print("5-exit(e)")
    print("____________")

    op = input("please Enter option: ")

    def trans():
        print('enter sentence: ')
        user_string = input()
        user_words = user_string.split(' ')
        for j in range(len(user_words)):
            for i in range(len(words)):
                if words[i]['english'] == user_words[j]:
                    print(words[i]['persian'], end=' ')
                    break
        else:
            print(user_words[j], end=' ')

    def e2f():

        print('enter word :')
        user_string = input()
        for i in range(len(words)):
            if words[i]['english'] == user_string:
                print(words[i]['persian'])
                break

    def f2e():

        print('enter word : ')
        user_string = input()
        for i in range(len(words)):
            if words[i]['persian'] == user_string:
                print(words[i]['english'])
                break

    def insert():
        f1 = open('zeinab_translate/translate.txt', "a")
        english = input('enter english words :')
        f1.write('\n')
        f1.write(english)
        persian = input('enter persian words :')
        f1.write('\n')
        f1.write(persian)
        print("success")
        f1.close()
        words.append({'english': english, 'persian': persian})

    if op == '1':
        insert()
    elif op == '2':
        e2f()
    elif op == '3':
        f2e()
    elif op == '4':
        trans()
    else:
        exit()
