from theme import *
import random
from board import Board
class Utils:
    def __init__(self):
        pass
    def check_letter(self, letter):
        if letter not in "йцукенгшщзхъфывапролджэячсмитьбю":
            return False
        return True
class Game:
    def __init__(self):
          self.attemps = 0
          self.fails = 0
    def start(self):
        utils = Utils()
        board = Board()
        game_play = True
        print("Это игра в висельницу! Правила простые: ты должен угадать слово по буквам."
                'Если много ошибаешься - погибаешь. Удачи!')
        while game_play:
            self.fails = 0
            print("Выбери любую из 5-ти тем:")
            print(*[i for i in word_dict.keys()], sep= ', ')
            fl_check_theme = False
            while fl_check_theme == False:
                theme = input().lower().strip()
                if any([i for i in word_dict.keys() if theme == i]):
                    fl_check_theme = True
                    word = word_dict[theme][random.randint(0, len(word_dict[theme])-1)]
                    word_secret = '*' * len(word)
                    while self.fails < 6 and word_secret != word:
                        print(f'Тема Природа. Слово: {word_secret}')
                        board.draw(self.fails)
                        letter = 'i'
                        while letter not in 'йцукенгшщзхъфывапролджэячсмитьбю':
                            letter = input('Введите русскую букву:').lower().strip()
                            if letter in 'йцукенгшщзхъфывапролджэячсмитьбю':
                                found = False
                                new_word_secret = ""  # Создаем новую строку для обновленного word_secret
                                for i in range(len(word)):
                                    if letter == word[i]:
                                        new_word_secret += letter  # Если буква совпадает, добавляем её
                                        found = True
                                    else:
                                        new_word_secret += word_secret[i]  # Иначе сохраняем то, что уже есть

                                if not found:
                                    print('Такой буквы в слове нет')
                                    self.fails += 1
                                word_secret = new_word_secret
                            else:
                                print('Это не русская буква')
                    if self.fails >= 6:
                        board.draw(self.fails)
                        print('Ты проиграл!')
                    else:
                        print('Ты победил!')
                    next_game = ''
                    while next_game != 'да' and next_game != 'нет':
                        next_game = input('Будешь играть еще? Напиши "Да" или "Нет"').lower().strip()
                        if next_game == 'да':
                            game_play = True
                        elif next_game == 'нет':
                            game_play = False
                else:
                    print('Введите тему правильно')

if __name__ == '__main__':
    game = Game()
    game.start()
