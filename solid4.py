# Принцип разделения интерфейсов
#class SmartHouse():
#    def turn_on_light(self):
#        pass

#    def turn_on_music(self):
#        pass

#    def heat_food(self):
#        pass


class Light():
    def turn_on_light(self):
        print("Свет включен")

class Food():
    def heat_food(self):
        print("Еда начала разогреваться")

class Music():
    def turn_on_music(self):
        print("Включаю подборку ваших любимых песен")

        