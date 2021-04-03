#!/usr/bin/env python3
import random


class Attr():
    """ character attribute class """
    def __init__(self, l, h, attack, defense, dexterity, luck, expr):
        self.LV = l
        self.HP = h
        self.attack = attack
        self.defense = defense
        self.dexterity = dexterity
        self.luck = luck
        self.expr = expr

class K_Attr(Attr):
    """ Kuppa's attribute class"""
    def __init__(self):
        Attr.__init__(self, 1, 50, 50, 30, 60, 70, 200)
        self.KI = 20
        self.curr_hp = self.HP
        self.curr_ki = self.KI
        self.curr_exp = self.expr

    def grow(self, expr_pts):
        self.get_expr(expr_pts)
        if self.curr_exp <= 0:
            self.level_up()

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
