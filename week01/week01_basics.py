"""
week01_basics.py

『独習Python（2020年版）』第1〜3章の理解度チェックに対する解答コード。
問題文は含まず、自作コードのみ掲載しています。
"""

#第1章最終問題
name = '山田'
print(name)

#第2章最終問題
name = '山田'
#宣言した変数を破棄
del name
#タブキーのエスケープ文字\t
txt = 'みかん\tかき\tりんご'
print(txt)
#入れ子リスト
data = [
    ['あ','い','う','え','お'],
    ['か','き','く','け','こ'],
]
print(data)
#フォーマット文字列
name = '鈴木'
print(f'こんにちわ、{name}さん')
#要素を持ったリスト末尾取得
data = [1,2,3,4,5]
print(data[4])

#第3章最終問題
i = 0
#変数を2減らす
i -= 2
print(i)
#decimal型の変数を生成する。
import decimal
d = decimal.Decimal('0.5')
#リストのアンパック
x, y, *z=2, 4, 6, 8, 10
print(x,y,z)
#変数m, nの中身を入れ替える。
m = 10
n = 5
m, n= n, m
print(m,n)
#条件式を論理演算子を使わずに表す。
x = 10
print(10 <= x <= 50)
