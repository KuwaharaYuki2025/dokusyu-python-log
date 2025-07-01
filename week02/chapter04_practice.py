# 練習問題 第4章 学習ログ
# 作成日: 2025/07/01
# 内容: if文、for文、while文などの基礎文法の確認

#練習問題4.1_1問
score = 75
if score >= 90:
    print("優")
elif score >= 70:
    print("良")
elif score >= 50:
    print("可")
else:
    print("不可")

#練習問題4.2_1問
for i in range(1,10):
    for j in range(1,10):
        print(i*j,end = ' ')
    print()

#練習問題4.3_1問
_sum=0
i = 0
while i <= 100:
    i+=1
    if i % 2 != 0:
        continue
    _sum += i

print('合計値は',sum,'です。')

#第4章理解度チェック
#dataの内容を順に出力する。
data = [1,2,3,4,5]
for i in data:
    print(i,end = ' ')

#1~100の値を順に出力する
for i in range(1,101):
    print(i,end = ' ')
    if i % 10 == 0:
        print()

#数値が格納されたリストの10倍した結果をdata2に格納する。
data2 = [i * 10 for i in data]
print(data2)

#dataから値が0以上のものを取り出して、合計値を求める。
print('合計',sum([i for i in data if i >= 0]),'です。')

#numが10以上50未満の時に、numの値を表示する。
num = 20
if 10 <= num < 50:
    print(num)
"""
#第3問
while True:
    try:
        num = input('数字を入力してください:')
        print('1.5倍すると...',float(num) * 1.5)
    except ValueError:
        print('入力値エラーです。')
    else:
        break
"""
#第4問
_sum = 0
for i in range(100,201):
    if i % 2 == 0:
        continue
    _sum += i
print('合計値は',_sum,'です。')

#第5問
interpreted_Languages = ['Python','Perl','Ruby']
compiled_Languages = ['C#','C++','Java']
language = 'C++'
if language in interpreted_Languages:
    print('インタープリタ言語')
elif language in compiled_Languages:
    print('コンパイル言語')
else:
    print('不明')