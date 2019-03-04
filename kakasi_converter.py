from pykakasi import kakasi


class Kakasi:
    def __init__(self):
        kakasi_obj = kakasi()  # Generate kakasi instance

        kakasi_obj.setMode("H", "a")  # Hiragana to ascii
        kakasi_obj.setMode("K", "a")  # Katakana to ascii
        kakasi_obj.setMode("J", "a")  # Japanese(kanji) to ascii

        self.conv = kakasi_obj.getConverter()

    def convert(self, text):
        result = self.conv.do(text)
        return result

# text = u"これはひらがなコレハカタカナ漢字"
# text = u"これはひらがなコレハカタカナカンジ"
# text = u"俺は孫悟空です"

# kakasi_converter = Kakasi()
# convert_text = kakasi_converter.convert(text)
# print(convert_text)
