class Hero:

    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def attacking(self, opponent):
        print(self.name + " is attacking " + opponent.name)
        opponent.attacked(self)

    def attacked(self, opponent):
        print(self.name + " is attacked by " + opponent.name)
        damage_received = opponent.attack / self.defense
        print("damage per second : " + str(damage_received))
        self.health = self.health - damage_received

        if self.health < 1:
            self.die(opponent)
            del opponent
        else:        
            print(self.name + " health remaining is : " + str(int(self.health)))

    def attackUp(self, up):
        print(self.name + " attack up to : " + str(up))
        self.attack += up
        print(self.name + " attack now is : " + str(self.attack))

    def gotItem(self, item):
        print(self.name + " got " + item.name)
        self.attackUp(item.attack)

    def die(self, opponent):
        print(self.name + " is died by " + opponent.name)
