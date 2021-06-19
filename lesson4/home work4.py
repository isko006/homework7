todos = []

while True:
    print('1)добавить задачу')
    print('2)добавить задачу')
    print('3)добавить задачу')
    print('4)добавить задачу')
    print('5)добавить задачу')
    print('6)добавить задачу')
    print('7)добавить задачу')
    print('8)добавить задачу')
    print('9)добавить задачу')
    print('0)показать задачи')
    option = int(input())

    if option == 1:
        if option == 2:
            task = input()
            deadline = input()
            date_added = input()
            todo = [task, date_added, date_added]
            todos.append(todo)
        print('задача добавлена!')

    if option == 2:
        print('-----------------')
    for i in todos :
        print(i[0], i[1], i[2])
        print('-----------------')
