from random import choice

words_list = ["собака", "кошка", "змея", "птица", "медведь", "обезьянка"]

def hangman(word):
    # счетчик неправильных ответов
    wrong = 0
    # список со строками
    stages = ["",
              "________      ",
              "|      |      ",
              "|      0      ",
              "|     /|\     ",
              "|     / \     ",
              "|             "
              ]
    # список с символами в переменной word
    rletters = list(word)
    #список строк для отслеживания подсказок для второго игрока
    board = ["__"] * len(word)
    # победил или нет второй игрок
    win = False
    print("Добро пожаловвать на казнь!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введите букву: "
        char = input(msg)
        if char in rletters:
            # получаем индекс угаданной буквы
            cind = rletters.index(char)
            # обновляем наш текущий результат
            board[cind] = char
            # открываем доступ к следующей аналогичной букве
            rletters[cind] = '$'
        else:
            wrong += 1
        # Выводим теущий результат
        print((" ".join(board)))
        # Выводим теущий висельника
        e = wrong + 1
        print("\n".join(stages[0: e]))

        if "__" not in board:
            print("Вы выиграли! Было загадано слово: ")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("Вы проиграли! Было загадано слово: {}.".format(word))

if __name__ == "__main__":
    hangman(choice(words_list))

