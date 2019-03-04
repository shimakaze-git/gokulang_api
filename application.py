#!/usr/bin/python
# -*- coding: utf-8 -*-

# from .morphological import Morphological
from morphological import Morphological
from kakasi_converter import Kakasi
from nozawa_converter import nozawa_converter
from roma_kana_table import RomajiKanaConvertor


class GokulangConverterApplication:
    def __init__(self):
        self.morphological = Morphological()
        self.kakasi_converter = Kakasi()
        self.romaji_kana_convertor = RomajiKanaConvertor()

        self.goku_text = ""

    def get_goku_text(self):
        return self.goku_text

    def kakasi_convert(self, text):
        """
        各単語をローマ字に変換
        text : kana_text
        """
        return self.kakasi_converter.convert(text)

    def nozawa_convert(self, text):
        """
        野沢活用形に変換
        text : kakasi_text
        """
        return nozawa_converter(text)

    def romaji_kana_convert(self, text):
        # romaji_kana_convertor
        """
        ローマ字からひらがなとカタカナを生成
        text : nozawa_text
        """
        hiragana_text, katakana_text = self.romaji_kana_convertor.execute(
            text
        )
        return hiragana_text, katakana_text

    def convert(self, text):
        self.morphological.tokenize(text)

        for surface in self.morphological._surfaces:
            # kana_text = surface[2]
            kana_text = surface[1]
            print(surface, kana_text)

            # 各単語をローマ字に変換
            kakasi_text = self.kakasi_convert(kana_text)

            # 野沢活用形に変換
            nozawa_text = self.nozawa_convert(kakasi_text)

            # ローマ字からひらがなとカタカナを生成
            hiragana_text, katakana_text = self.romaji_kana_convert(
                nozawa_text
            )

            # カタカナと変換後のカタカナが一致していた場合は、
            # 当初の内容に戻す
            if kana_text == katakana_text:
                convert_text = surface[0]
            else:
                convert_text = hiragana_text

            self.goku_text += convert_text


# if __name__ == "__main__":
#     text = '冷静に考えろ、奴は強いぞ'
#     gokulang_converter_app = GokulangConverterApplication()
#     gokulang_converter_app.convert(text)
#     print(gokulang_converter_app.get_goku_text())
