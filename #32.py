# 32. Создать класс Годзила. У данного класса должен быть атрибут - объем желудка.
# Написать для данного класса метод поедания людей.
# В данную функцию должен передаваться объем съеденного и соответственно уменьшаться место в желудке.
# Когда Годзила заполнит желудок на 90%, метод должен выводить надпись, что Годзила наелся и больше не может поедать людей.

class Godzilla:

    def __init__(self):
        self.swallowed = 0
        self.stomach_volume = 150

    def om_nom_nom(self, number_of_persons):
        self.number_of_persons = number_of_persons
        self.swallowed = self.swallowed + int(number_of_persons)
        i = self.swallowed/self.stomach_volume*100
        if i < 90:
            print("I need more people!!!")
        elif 90 <= i < 100:
            print("I'm fed up.I can't eat people anymore!!")

godzilla = Godzilla()

godzilla.om_nom_nom(number_of_persons = input("How many of you are here? "))