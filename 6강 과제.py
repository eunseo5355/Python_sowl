class human:

    def __init__(self, name, HP, MP):
        self.name = name
        self.HP = HP
        self.MP = MP

    def meet(self):
        print("name: %s" % self.name)
        print("HP: %d" % self.HP)
        print("MP: %d" % self.MP)
        print("안녕하세요")


class player(human):
    def __init__(self, name, HP, MP, AD):
        super().__init__(name, HP, MP)
        self.AD = AD

    def att(self):
        enemy.HP = int(self.AD) - int(enemy.DP)


class npc:
    def meet(self):
        print("반갑습니다")


class enemy(human):
    DP = None

    def __init__(self, name, HP, MP, DP):
        super().__init__(name, HP, MP)
        self.DP = DP

    def getEnemyDP(self):
        return self.DP

    def getEnemyHP(self):
        return self.HP


p1 = player("eunseo", 100, 100, 50)
e1 = enemy("aaa", 70, 30, 20)
hi = npc()

while int(e1.getEnemyHP()) != 0:
    num = int(input("1 또는 2 입력:"))
    if num == 1:
        p1.meet()
        hi.meet()
    elif num == 2:
        p1.att()
        print(e1.getEnemyHP())
