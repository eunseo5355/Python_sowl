class human:

    def __init__(self, name, HP, MP):
        self.name = name
        self.HP = HP
        self.MP = MP

    def meet(self):
        print("안녕하세요")


class player(human):
    AD = 100

    def att(self, enemy):
        if self.MP >= 50:
            enemy.HP -= self.AD - enemy.DP
            self.MP -= 50
            print("공격성공")
            print("플레이어의 마나는", self.MP, "입니다.")
            print("적의 체력은", enemy.HP, "입니다.")
        else:
            print("마나가 적습니다.")

    def meet(self):
        print("반갑습니다")


class npc(human):
    pass


class enemy(human):
    DP = 50


p1 = player("player", 100, 100)
e1 = enemy("enemy", 100, 100)
npc1 = npc("npc", 100, 100)

while True:
    num = input("npc와 만나려면 1, 공격하려면 2 :")
    if num == '1':
        p1.meet()
        npc1.meet()
    elif num == '2':
        p1.att(e1)
        if e1.HP <= 0:
            break

