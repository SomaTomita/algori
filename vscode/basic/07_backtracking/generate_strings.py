"""
Generate Strings (バックトラッキングの一番やさしい入口)

数 n が与えられる。A と B だけを使って、長さ n の文字列を「全部」作る。

例:
    n = 1 → ["A", "B"]
    n = 2 → ["AA", "AB", "BA", "BB"]
    n = 3 → ["AAA","AAB","ABA","ABB","BAA","BAB","BBA","BBB"]

----------------------------------------------------------------
これがバックトラックだ (最小形):
    1) path に 1 文字足す            ← choose
    2) 残りを再帰で埋める            ← explore
    3) 足した 1 文字を pop して戻す   ← unchoose ★ここが核心★

word_search.py の 2D 盤面より、まずこっち。
盤面も方向も制約も無い。「選択肢を足す → 潜る → 戻す」だけの裸の backtracking。
README.md のトレース表が、verbose=True の出力でそのまま見える。
----------------------------------------------------------------
"""

from __future__ import annotations

# 各位置で選べる文字。ここを ("0","1") にすれば 2 進文字列、
# ("A","B","C") にすれば 3 種類…と、選択肢を変えるだけで応用できる。
ALPHABET = ("A", "B")


def generate(n: int, verbose: bool = False) -> list[str]:
    result: list[str] = []
    path: list[str] = []  # 組み立て中の文字 (全分岐で使い回す 1 個)

    def backtrack(depth: int) -> None:
        # ----- 完成条件: 長さが n に達したら記録して戻る -----
        if len(path) == n:
            word = "".join(path)  # join で文字列を作る = スナップショット (コピー)
            result.append(word)
            if verbose:
                print(f"{'  ' * depth}✓ 完成 → 記録 '{word}'")
            return

        # ----- 選択肢をループ: A を足す / B を足す -----
        for ch in ALPHABET:
            path.append(ch)  # choose
            if verbose:
                print(f"{'  ' * depth}choose   '{ch}'  path='{''.join(path)}'")

            backtrack(depth + 1)  # explore (深く潜る)

            path.pop()  # unchoose ★これがバックトラック★
            if verbose:
                print(f"{'  ' * depth}unchoose '{ch}'  path='{''.join(path)}'")

    backtrack(0)
    return result


# ------------------------------------------------------------
# 動作確認
# ------------------------------------------------------------
def run(n: int, verbose: bool = False) -> None:
    print("=" * 60)
    print(f"n = {n}")
    result = generate(n, verbose=verbose)
    print(f"\n結果 ({len(result)} 個): {result}\n")


if __name__ == "__main__":
    # n=2 を verbose=True にして choose/explore/unchoose のトレースを観察する。
    # 出力の階段状インデントが、そのまま README.md の探索木になっている。
    # 「出力の 1 行ずつ、どのコードが走って path/result に何が入ったか」は
    # ファイル末尾の【実況中継】を 1 行ずつ追うと完全に分かる。
    run(2, verbose=True)

    run(3)  # 結果 (8 個): ['AAA','AAB','ABA','ABB','BAA','BAB','BBA','BBB']


# ------------------------------------------------------------
# 計算量
# ------------------------------------------------------------
"""
時間: O(b^n * n)
    - 葉 (= 完成した文字列) が b^n 個 (b = 選択肢の数, ここでは 2)
    - 各葉で "".join(path) に長さ n 分かかる
    - n=2 → 4 個、n=3 → 8 個、… と指数で増える (全列挙だから当然)

空間: O(n)
    - 再帰スタックの深さ = path の長さ = n
    - 出力 result 自体は別枠 (b^n 個ぶん)
"""

# ------------------------------------------------------------
# 【コールスタック版】 同じ n=2 を「潜る(呼ぶ)/戻る(return)」で追う
#   上の表の 1 行 = この図の 1 命令。なぜ「完成 → 戻ってきた → pop」に
#   なるのか (関数は return すると呼んだ側の続きに戻る) がこれで見える。
# ------------------------------------------------------------
"""
n=2。path=[] result=[] で backtrack(0) を呼ぶところから。

depth 0: backtrack(0) 実行中   path=[]
         len(path)=0 ≠ 2 なので for ループへ
         ┌─ ch='A' → append → path=['A']            ……表: choose 'A'
         │  backtrack(1) を呼ぶ ───┐  ★depth0 停止、depth1 へ潜る
         │                          │
depth 1: │    backtrack(1) 実行中 ◀┘  path=['A']
         │    len=1 ≠ 2 なので for ループへ
         │    ┌─ ch='A' → append → path=['A','A']    ……表: choose 'A'
         │    │  backtrack(2) を呼ぶ ───┐  ★depth1 停止、depth2 へ潜る
         │    │                          │
depth 2: │    │    backtrack(2) 実行中 ◀┘  path=['A','A']
         │    │    len==2 成立！ result に 'AA' 記録    ……表: ✓完成 記録'AA'
         │    │    return ───────────────┐  ★depth2 終了、depth1 に戻る
         │    │                           │
depth 1: │    │  backtrack(2) の次の行 ◀──┘
         │    │  path.pop() → path=['A']             ……表: unchoose 'A'
         │    │  (ch='A' の回、終わり)
         │    └─ ch='B' → append → path=['A','B']    ……表: choose 'B'
         │       backtrack(2) を呼ぶ ───┐  ★潜る
         │                               │
depth 2: │         backtrack(2) 実行中 ◀┘  path=['A','B']
         │         len==2 成立！ 'AB' 記録            ……表: ✓完成 記録'AB'
         │         return ───────────────┐  ★戻る
         │                                │
depth 1: │       path.pop() ◀────────────┘ → path=['A']  ……表: unchoose 'B'
         │       for ループ尽きた → backtrack(1) 終了
         │       return ───┐  ★depth1 終了、depth0 に戻る
         │                  │
depth 0: │  path.pop() ◀───┘ → path=[]               ……表: unchoose 'A'
         │  (ch='A' の回、終わり)
         └─ ch='B' → append → path=['B']             ……表: choose 'B'
            backtrack(1) を呼ぶ ───┐  ★潜る
                                    │
depth 1:      backtrack(1) 実行中 ◀┘  path=['B']
              ┌─ ch='A' → append → path=['B','A']    ……表: choose 'A'
              │  backtrack(2) → 'BA' 記録 → return    ……表: ✓完成 記録'BA'
              │  path.pop() → path=['B']             ……表: unchoose 'A'
              └─ ch='B' → append → path=['B','B']    ……表: choose 'B'
                 backtrack(2) → 'BB' 記録 → return    ……表: ✓完成 記録'BB'
                 path.pop() → path=['B']             ……表: unchoose 'B'
              for ループ尽きた → backtrack(1) 終了 → return
depth 0:    path.pop() → path=[]                      ……表: unchoose 'B'
            for ループ尽きた → backtrack(0) 終了

→ return result = ['AA','AB','BA','BB']

----------------------------------------------------------------
読み方の軸 2 つ:

(1) ★潜る(呼ぶ) と ★戻る(return) は必ずペア。潜った数だけ必ず戻る。
    ネストの深さ = depth そのもの。

(2) ✓完成 の直後は必ず return → 戻った先の path.pop()(unchoose)。
    関数は return すると「呼んだ側の次の行」に戻る、という基本動作。
    再帰では呼んだ側が 1 つ浅い depth の自分自身なので、1 段ずつ
    浅い階層へ戻りながら、戻った先で待つ pop が枝を片付ける。
    → だから表でも「記録」の次の行が必ず unchoose になる。

出る順が 'AA'→'AB'→'BA'→'BB' なのも図で分かる: 外側(depth0)の
ループが 'A'→'B' と 1 歩進む前に、内側(depth1)のループが 'A','B' を
全部回り切る。外が 1 歩進む前に内が回り切る、が backtracking の全体像。
"""
