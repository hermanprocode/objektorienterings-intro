from typing import MutableMapping

id = 0


class Car():
    '''
    En klass som håller reda på några egenskaper hos en bil.
    '''
    # Metoden __init__, körs alltid då ett objekt skapas

    def __init__(self, brand, color, mileage):
        # Nedanstående variabler kallas för attribut.
        # Alla objekt av klassen Car har egna värden på dessa.
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def get_brand(self):
        '''
        Skriver ut bilmärket
        '''
        print(self.brand)

    def set_brand(self, new_brand):
        '''
        Parameter: new_brand | sträng
        Uppdaterar bilmärket om det existerar. Om det inte existerar
        så tilldelas aktuellt objekt märket enligt parametern.
        '''
        self.brand = new_brand

    def set_color(self, new_color):
        self.color = new_color

    def set_mileage(self, new_mileage):
        self.mileage = new_mileage

    def get_mileage(self):
        return self.mileage


# ----------Huvudprogram----------
# Nu när klassen finns kan vi skapa objekt (variabler) med denna typ.
# Dessa objekt har också tillgång till klassens metoder (funktioner).

a_car = Car('Volvo', 'Blå', 1587)
b_car = Car('BMW', 'Svart', 1864)
c_car = Car('Ferrari', 'Röd', 1687)
d_car = Car('Tesla', 'Vit', 1422)

my_cars = [a_car, b_car, c_car, d_car]

print()

svar = ""
while svar != 5:
    svar = int(
        input("Vilken bil vill du inspektera [1] [2] [3] [4], för att avsluta skriv [5]"))
    if svar >= 1 and svar <= 4:
        svar2 = input(
            f"Du valde bil {svar}\nVilken attribut vill du ta reda på [brand] [color] [mileage]")
        if svar2 == "brand":
            print(my_cars[svar-1].brand)
        elif svar2 == "color":
            print(my_cars[svar-1].color)
        elif svar2 == "mileage":
            print(my_cars[svar-1].mileage)
        else:
            print("felaktigt val lol")
    elif svar == 5:
        print("HEJDÅ")
