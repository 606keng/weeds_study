#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:doulihang
@file: 示例1-1 一摞有序的纸牌.py
@time: 2021/01/07
@remark：
"""
import collections

# 构建一张纸牌，rank牌的点数，suit牌的花色
from random import choice

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    # spades：黑桃，diamonds：方块，clubs：梅花，hearts：红桃
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        """初始化一副牌"""
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        """获取牌的数量"""
        return len(self._cards)

    def __getitem__(self, position):
        """抽取指定位置的牌"""
        return self._cards[position]

    def __contains__(self, item):
        return item in self._cards


if __name__ == '__main__':
    # 定义一副牌
    deck = FrenchDeck()
    # 获取牌的总张数
    print(len(deck))
    # 抽取第一张牌
    print(deck[0])
    # 抽取随意一张牌，choice从一个序列中随机选取一个元素
    print(choice(deck))
    # 查看最上面的三张牌
    print(deck[:3])
    # 查看全为A的牌
    print(deck[12::13])
    # 查看所有牌
    for card in deck: # doctest: +ELLIPSIS
        print(card)
    # 反向查看所有牌
    for card in reversed(deck): # doctest: +ELLIPSIS
        print(card)
    # 判断Card(rank='3', suit='spades')是否在deck中
    print(Card(rank='3', suit='spades') in deck)
    # 判断Card(rank='16', suit='spades')是否在deck中
    print(Card(rank='16', suit='spades') in deck)