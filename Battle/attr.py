#!/usr/bin/env python3
import random


class Attr():
    """ character attribute class """
    def __init__(self, l, h, attack, defense, dexterity, luck, expr):
        super(Attr, self).__init__()
        self.LV = l
        self.HP = h
        self.curr_hp = self.HP
        self.attack = attack
        self.defense = defense
        self.dexterity = dexterity
        self.luck = luck
        self.expr = expr
        self.curr_exp = self.expr

    def raise_hp(self, hpp):
        self.HP += hpp

    def raise_all(self, plus):
        self.attack += plus
        self.defense += plus
        self.dexterity += plus
        self.luck += plus

    def raise_stat(self, ad, plus):
        if ad == 'a':
            self.attack += plus
        elif ad == 'd':
            self.defense += plus
        elif ad == 'ad':
            self.attack += plus
            self.defense += plus
        elif ad == 'dx':
            self.dexterity += plus
        elif ad == 'l':
            self.luck += plus


    def get_dmg(self, e_defen, e_luck):
        dmg = (self.attack ** 2) / (self.attack + e_defen)
        if self.luck < e_luck:
            dmg_factor = random.randint(e_luck - self.luck, e_luck) / e_luck
        else:
            dmg_factor = 1 + (random.randint(self.luck - e_luck, self.luck) / self.luck)
        return (round((dmg * dmg_factor) / 10))

    def hit_hp(self, dmg):
        self.curr_hp -= dmg
        if self.curr_hp < 0:
            self.curr_hp = 0


class C19_Attr(Attr):
    """COVID19 Attribute class """
    def __init__(self):
        """initialize the C19_Attr class with default stat """
        super(C19_Attr, self).__init__(1, 36, 30, 10, 15, 15, 0)



class K_Attr(Attr):
    """ Kuppa's attribute class"""
    def __init__(self):
        Attr.__init__(self, 1, 50, 50, 30, 60, 70, 200)
        self.KI = 20
        self.curr_ki = self.KI
        self.MaxCombo = 3

    def grow(self, expr_pts):
        self.get_expr(expr_pts)
        if self.curr_exp <= 0:
            remainder = self.curr_exp
            print("remainder{}".format(remainder))
            self.level_up()
            self.curr_exp += remainder

    def get_expr(self, expr_pts):
        self.curr_exp -= expr_pts

    def level_up(self):
        self.LV += 1
        self.attack += random.randint(4, 8)
        self.defense += random.randint(1, 5)
        self.dexterity += random.randint(2, 7)
        self.luck += random.randint(3, 10)
        self.expr += random.randint(100, 150)
        self.curr_exp = self.expr
