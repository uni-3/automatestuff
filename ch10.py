# 演習プロジェクト 10.8.1
# バグとしては
# guess=(表, 裏)という文字列に対して、toss=(1, 0)を比較しているので、永遠に当たることはない
# 2回目の入力値をチェックしていない（1回目は表か裏を入力しないと進まないようになっている）
# がある。入力値チェック関数を作った。

import random

# 表か裏が入力されるまで続く
def get_input():
    while True:
        print('表か裏を入力してください:')
        guess = input()
        print('予想は:', guess)
        i_guess = to_index(guess)
        if i_guess != None:
            return i_guess

# guessの値を0: 裏, 1: 表に変換
def to_index(guess):
    if guess == '表':
        return 1
    elif guess == '裏':
        return 0
    return None

print('コインの表裏を当ててください')
toss = random.randint(0, 1) # 0: 裏, 1: 表
guess = get_input()
if toss == guess:
    print('当たり!')
else:
    print('はずれ!もう一回予想して!')
    guess = get_input()
    if toss == guess:
        print('当たり!')
    else:
        print('はずれ...!')