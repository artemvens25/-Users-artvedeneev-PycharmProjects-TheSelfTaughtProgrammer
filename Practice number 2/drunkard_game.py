from random import shuffle

# данные по картам
class Card:
    suits = ["spades",
             "hearts",
             "clubs",
             "diamonds"]

    values = [None, None, "2", "3",
              "4", "5", "6", "7",
              "8", "9", "10", "Jack",
              "Queen", "King", "Ace"]

    def __init__(self, v, s):
        "suit\value - целые числа"
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        else:
            return False

    def __repr__(self):
        v = self.values[self.value] + " of " + self.suits[self.suit]
        return v


# перетасовка карт и вытаскиваение рандомной карты из колоды
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


# отслеживание карт и количество выигранных игроками раундов
class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.card = None

# сама игра
class Game:
    def __init__(self):
        name1 = input("The name player first: ")
        name2 = input("The name player second: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self,winner):
        w = "{} picks up cards"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = "{} put {}, but {} put {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("GO!")
        while len(cards) >= 2:
            m = "Push X for exit. Push any different button for the start to play"
            response = input(m)
            if response == "X":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.wins)
        win = self.winner(self.p1, self.p2)
        print("The game to the end. {} winner!".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Draw!"

game = Game()
game.play_game()
