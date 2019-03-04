from application import GokulangConverterApplication


if __name__ == "__main__":
    text = '見えない'
    # text = 'もう帰ります'
    # text = '冷静に考えろ、奴は強いぞ'
    text = 'FF外から失礼します'
    gokulang_converter_app = GokulangConverterApplication()
    gokulang_converter_app.convert(text)
    print(gokulang_converter_app.get_goku_text())
