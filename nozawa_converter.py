def nozawa_converter(text):
    nozawa_text = text.replace('ai', 'ee')\
                        .replace('ae', 'ee')\
                        .replace('ei', 'ee')
    return nozawa_text


# word抽出
def extract_word(text, count):
    first = text[count]
    second = text[count+1]
    # print(first, second)

    # 子音list
    consonant = ['a', 'i', 'u', 'e', 'o']
    word = ''

    # 母音
    # nもこの条件に含まれる？
    if first not in consonant:
        # 2番目が子音
        if second in consonant:
            word = first + second
            count += 2
        # 2番目が子音ではない
        # 1番目がnの場合
        else:
            word = first
            count += 1

    # 1番目が子音
    else:
        word = first
        count += 1
    return word, count


# 野沢活用形に変換
# def nozawa_converter(text):
#     word_list = []
#     count = 0
#     while len(text) > count:
#         word, count = extract_word(text, count)
#         word_list.append(word)

#     count = 0
#     new_word_list = []
#     while len(word_list) > count:
#         word = word_list[count]
#         w_list = [w for w in word]

#         # 母音 + 子音の組み合わの文字
#         if len(w_list) >= 2:

#             # 2番目の文字
#             if w_list[1] in ['a', 'e']:

#                 if len(word_list) > count+1:
#                     next_word = word_list[count+1]

#                     # 次の文字がi or e
#                     if next_word in ['i', 'e']:
#                         # second = w_list[1]
#                         new_word = w_list[0] + 'e'
#                         next_word = 'e'

#                         new_word_list.append(new_word)
#                         new_word_list.append(next_word)

#                         count += 2
#                         continue
#             new_word_list.append(w_list[0]+w_list[1])
#             count += 1
#         else:
#             new_word_list.append(w_list[0])
#             count += 1
#     return ''.join(new_word_list)

# 子音a or 子音e  + i or e → 子音e + e（小せぇ「え」）

# test1 = "keitaidenwa"
# test2 = "orawakuwakusuruzo"

# text = nozawa_converter(test1)
# print(text)
