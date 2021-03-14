# -*- coding: utf-8 -*-
# Nola

import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])  # 返回具有命名字段的元组的新子类 表示一张牌

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)  # ♣->♦->♥->♠ 2-A 花色和大小从小到大 0(2梅花色)-51(A黑桃色) 花色大小映射


def spades_high(card):
    """
    纸牌升序
    :param card:
    :return:
    """
    rank_value = FrenchDeck.ranks.index(card.rank)  # 获取纸牌大小index
    return rank_value * len(suit_values) + suit_values[card.suit]  # 纸牌大小index * 4色 + 花色权重 2clubs=0 2diamonds=1


class FrenchDeck(object):
    # ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] 13
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()  # ['spades', 'diamonds', 'clubs', 'hearts'] 4

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


if __name__ == '__main__':
    # namedtuple用法
    Point = collections.namedtuple('Point', ['x', 'y'])
    print(Point.__doc__)  # docstring   Point(x, y)
    p = Point(11, 22)
    print(p[0] + p[1])  # 使用index
    x, y = p  # 像元组一样解包
    print(x, y)
    print(p.x, p.y)  # 使用字段名获取对应值
    d = p._asdict()  # 转为dict  OrderedDict([('x', 11), ('y', 22)]) 11 22
    print(d, d['x'], d['y'])
    print(Point(**d))  # dict打包为新子类  Point(x=11, y=22)
    print(p._replace(x=100))  # 类似str替换  Point(x=100, y=22)
    print('@.@ '*20 + "\n"*2)

    # 得到一个纸牌对象
    beer_card = Card('7', 'diamonds')
    print(beer_card)  # Card(rank='7', suit='diamonds')
    print('@.@ ' * 20 + "\n"*2)

    # len函数查看一叠牌有多少张
    deck = FrenchDeck()
    print(len(deck))  # 52
    print('@.@ ' * 20 + "\n"*2)

    # 使用__getitem__方法从一叠牌中抽取特定的一张牌
    print(deck[0])  # 第一张  Card(rank='2', suit='spandes')
    print(deck[-1])  # 最后一张  Card(rank='A', suit='hearts')
    print('@.@ ' * 20 + "\n" * 2)

    # 使用python内置函数random.choice随机抽取一张牌
    print(choice(deck))  # Card(rank='9', suit='hearts')
    print(choice(deck))  # Card(rank='3', suit='diamonds')
    print('@.@ ' * 20 + "\n" * 2)

    # 抽取最上面3张
    print(deck[:3])
    # 只看牌面是A的牌
    print(deck[-4:])
    print(deck[48:])
    print('@.@ ' * 20 + "\n" * 2)

    # 仅仅实现__getitem__方法，这一摞牌就编程可迭代了
    for card in deck[:5]:
        print(card)
    print('@.@ ' * 20 + "\n" * 2)

    # 反迭代reverse list
    for card in reversed(deck):
        if card.rank == "K":
            break
        print(card)
    print('@.@ ' * 20 + "\n" * 2)

    # in运算符可用在FrenchDeck类上，因为它是可迭代的
    print(Card('Q', 'diamonds') in deck)
    print(Card('S', 'diamonds') in deck)
    print('@.@ ' * 20 + "\n" * 2)

    # spades_high函数对牌进行升序排序 标准库中sorted函数自增可根据指定key自增排序 reverse参数为True倒序
    for card in sorted(deck[:8], key=spades_high, reverse=True):
        print(card)
    # Card(rank='3', suit='spades')
    # Card(rank='3', suit='hearts')
    # Card(rank='3', suit='diamonds')
    # Card(rank='3', suit='clubs')
    # Card(rank='2', suit='spades')
    # Card(rank='2', suit='hearts')
    # Card(rank='2', suit='diamonds')
    # Card(rank='2', suit='clubs')
    print('@.@ ' * 20 + "\n" * 2)





