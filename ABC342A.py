# これは正規表現の知識の問題
S = input()
for i in range(len(S)):
    if S.count(S[i]) == 1:
        print(i + 1)
# countは対象の文字列の中に括弧内の要素が何個含まれるか数える
#　カウントif関数と同じ役割を果たす