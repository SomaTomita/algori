"""
Frequency Map Pattern (頻度マップ)

配列や文字列の中で、各要素が何回出現するかを数える定番パターン。
キー = 要素、値 = 出現回数。

3 通りの書き方を比較する:
  1. 素の dict + dict.get(k, 0) + 1   ... 最も基礎的
  2. collections.defaultdict(int)      ... 初期化が不要で読みやすい
  3. collections.Counter               ... ワンライナーで最も Pythonic
"""

from collections import Counter, defaultdict


# ------------------------------------------------------------
# 方法1: 素の dict + dict.get()
# ------------------------------------------------------------
def freq_with_dict(s: str) -> dict[str, int]:
    """dict.get(key, default) でキー未登録時のデフォルト値を取得しつつ +1 する。"""
    cnt: dict[str, int] = {}
    # 例: s="hello" の動き
    #   ch='h' → cnt={'h':1}
    #   ch='e' → cnt={'h':1, 'e':1}
    #   ch='l' → cnt={'h':1, 'e':1, 'l':1}
    #   ch='l' → cnt={'h':1, 'e':1, 'l':2}   (既出は +1)
    #   ch='o' → cnt={'h':1, 'e':1, 'l':2, 'o':1}
    for ch in s:
        cnt[ch] = cnt.get(ch, 0) + 1   # 未登録なら 0 + 1 = 1 から始まる
    return cnt


# ------------------------------------------------------------
# 方法2: defaultdict(int)
# ------------------------------------------------------------
def freq_with_defaultdict(s: str) -> dict[str, int]:
    """defaultdict は未登録キーへのアクセスで自動的に int() = 0 を作る。"""
    cnt: dict[str, int] = defaultdict(int)
    for ch in s:
        cnt[ch] += 1                   # KeyError を気にせず += が書ける
    return dict(cnt)                   # 比較しやすいよう dict に戻す


# ------------------------------------------------------------
# 方法3: Counter (最も Pythonic)
# ------------------------------------------------------------
def freq_with_counter(s: str) -> dict[str, int]:
    """Counter は iterable を渡すだけで頻度マップを作ってくれる。"""
    return dict(Counter(s))


# ------------------------------------------------------------
# 動作確認
# ------------------------------------------------------------
if __name__ == "__main__":
    text = "hello world"

    print("方法1 (dict.get):       ", freq_with_dict(text))
    print("方法2 (defaultdict):     ", freq_with_defaultdict(text))
    print("方法3 (Counter):         ", freq_with_counter(text))

    # 出力:
    # 方法1 (dict.get):        {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    # 方法2 (defaultdict):     {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    # 方法3 (Counter):         {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

    # ----- Counter ならではの便利機能 -----
    c = Counter(text)
    print("\nCounter の便利メソッド:")
    print("  most_common(3) =", c.most_common(3))    # 上位3要素
    print("  c['l']         =", c["l"])              # 'l' の出現数
    print("  c['z']         =", c["z"])              # 未登録キーは 0 を返す (KeyError にならない)

    # 出力:
    # Counter の便利メソッド:
    #   most_common(3) = [('l', 3), ('o', 2), ('h', 1)]
    #   c['l']         = 3
    #   c['z']         = 0


"""
計算量:
- 時間: O(n)   ... 入力を 1 回走査するだけ
- 空間: O(k)   ... k = ユニークな要素数 (最悪 n)

使い分けの目安:
- 競技プログラミングや読みやすさ重視なら Counter
- 値を +1 以外の処理 (例: list を append) も混ぜたいなら defaultdict
- 依存を増やしたくない / 教育用に明示したい場合は dict.get
"""
