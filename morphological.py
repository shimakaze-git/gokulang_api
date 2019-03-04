#!/usr/bin/python
# -*- coding: utf-8 -*-

import MeCab


DIC_PATH = "/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd"
DIC_PATH = ""


class Morphological:

    def __init__(self, dic_path=DIC_PATH):
        if dic_path:
            self.mecab = MeCab.Tagger('-d '+dic_path)
        else:
            self.mecab = MeCab.Tagger()
        self.mecab.parseToNode('')

        self._surfaces = []

    def tokenize(self, text):
        mecab_nodes = self.mecab.parseToNode(text)

        while mecab_nodes:
            parts = self.parts_decision(mecab_nodes)

            if parts is not None:
                self._surfaces.append(parts)
                # self.surfaces.append(mecab_nodes.surface)
            mecab_nodes = mecab_nodes.next

    def parts_decision(self, mecab_nodes):
        parts = mecab_nodes.feature.split(',')
        if parts[0] != 'BOS/EOS':
            parts_list = [
                # parts[0],
                parts[6],
                parts[7]
            ]
            return parts_list

# text = 'これはテストです。コレはあれです。'
# morphological = Morphological()
# morphological.tokenize(text)

# print(morphological._surfaces)
