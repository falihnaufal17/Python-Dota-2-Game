from Hero import Hero
from Item import Item

def main():
    # Play
    Axe.gotItem(AbyssalBlade)
    print()
    Axe.attacking(Sniper)
    print()
    Axe.gotItem(BladeMail)
    print()
    Axe.attacking(Sniper)
    print()
    Axe.gotItem(ShadowBlade)
    print()
    Axe.attacking(Sniper)
    print()
    Axe.attacking(Sniper)

# Item Available
ShadowBlade = Item("Shadow Blade", 0, 20, 0)
AbyssalBlade = Item("Abyssal Blade", 0, 40, 0)
BladeMail = Item("Blade Mail", 15, 38, 10)

# Hero
Sniper = Hero("Sniper", 100, 20, 5)
Axe = Hero("Axe", 120, 40, 10)

main()