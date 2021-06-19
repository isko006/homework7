eng_to_rus = {
    'dog': 'собака',
    'cat': 'кошка',
    'book': 'книга',
    'table': 'стул'

}

rus_to_eng = {
    'собака': 'dog',
    'кошка': 'cat',
    'книга': 'book',
    'стул': 'table'
}


while True :
    lang = input('язык для перевода ')

    if lang == 'eng':
        word = input('слово для перевода')
        try:
            print(eng_to_rus [word])
        except KeyError:
             print('такого слова нету,русский')
             option = input()
             if option == 'yes':
                 eng_to_rus[word] = input(f'перевод для слова {word} ')
    if lang == 'rus':
        word = input('слово для перевода ')
        try:
            print(rus_to_eng[word])
        except KeyError:
             print('такого слова нету, хотите добавить?')