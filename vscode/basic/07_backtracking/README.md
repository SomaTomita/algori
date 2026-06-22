# 07. Backtracking

**DFS + undo** — 一手進めて、ダメなら戻す。

名前を聞いただけで身構える人が多い。難しいからではなく、**核心の直感を誰も説明してくれない**から固まるだけ。Backtracking は新しいアルゴリズムでも魔法でもない。読み終わるころには、どんな backtracking 問題を見ても「どこから手をつけるか」が分かる状態になる。

## まず、ありがちな失敗から

問題。「数 n が与えられる。A と B だけを使って、長さ n の文字列を**全部**作れ」。

最初に思いつくのはネストしたループ。1 文字につき 1 ループ。n=2 ならこう。

```python
# n=2 ならこれで動く…
for c1 in ("A", "B"):
    for c2 in ("A", "B"):
        print(c1 + c2)
```

でも n=10 なら? 10 重ループを手で書くのか。それはプログラムじゃなくて悲鳴。**n ごとに別のプログラムをハードコードはできない**。もっといい方法があるはず。ある。

## たった 1 つの気づき

n=2 で簡単にして、頭の中で組み立ててみる。

空文字列から始める。1 文字目は選択肢が 2 つ。A を足すか、B を足すか。A から進むとまた A か B。B から進んでも A か B。

```
            ""
          /    \
        A        B
       / \      / \
     AA   AB  BA   BB
```

**木ができた**。そして答え `AA, AB, BA, BB` は、その木の**葉っぱ**にすぎない。

ここで問いを丸ごと差し替える。「どうやって全部の文字列を作るか?」ではなく、「**この木をどう辿るか?**」と問う。答えは単純。**DFS**。

これが backtracking の正体。**自分で作りながら DFS する木**、それだけ。

## 普通の DFS と何が違うか

普通の DFS は、木が**最初から与えられている**。あるものを辿るだけ。

backtracking では、木は**目に見えない**。まだ存在しない。**進みながら作る**。各ステップでこう問う。「今、どんな選択ができる?」その選択肢が枝になる。深く潜る。葉に着く。**戻る**。次の枝を試す。この「戻る」部分が backtracking の名前の由来。

では、コードはどうやって「戻る」のか。ここが多くの説明がすっ飛ばすところ。飛ばさない。

## 仕組みの核心: どうやって「戻る」のか

文字列を組み立てていて、A、もう一度 A を足した。path は `AA`。これは正しい答えなので記録する。次は `AB` を試したい。でも path にはまだ `AA` が入っている。`AA` から `AB` にどうやって行く?

**最後の 1 文字を消す**。末尾の A を pop する。path は `A` に戻る。そこに B を足す。path は `AB`。新しい答え。A から始まる全部を探し終えたら、それも pop。path は `""` に戻る。次に B を試す。

```
AA  ──pop A──▶  A  ──add B──▶  AB
```

この `path.pop()` という**たった 1 つの操作**が、全体を動かしている。これが無ければ前に進み続けるだけで、別の枝には永遠に行けない。木は目に見えないまま到達不能になる。

`path.pop()` は後片付けではない。**仕組みそのもの**。直前の状態に戻して、別の選択を試せるようにする装置。

### choose / explore / unchoose

```
[ choose ]              [ explore ]             [ unchoose ]
state: [ A . . ]        state: [ A B . ]        state: [ A . . ]
       ↓ pick B                ↓ recurse                ↑ remove B
       add to path             go deeper                back to before
```

3 段でワンセット。`explore` の後は **必ず** `unchoose`（＝さっきの pop）で元に戻す。

## コードを書く前の 2 つの問い

何か書く前に、2 つだけ答える。

**問い 1. いつ答えが完成するか?（＝記録して深掘りをやめるタイミング）**
AB 問題なら「path の長さが n になったら」。それが完成。記録する。

**問い 2. 今ここから、どんな選択ができるか?（＝枝）**
AB 問題なら、各ステップで「A を足す」か「B を足す」。

この 2 つを言葉で答えられれば、あとはテンプレに流すだけ。

## テンプレート（3 パート）

「完成チェック」「選択肢をループ」「各回のあとで unchoose」。この unchoose（pop）が backtracking。**毎回の再帰呼び出しの直後**に走って、その選択をする前の状態に戻す。

```python
def generate(n):
    result = []
    path = []

    def backtrack():
        # 1. 問い1: 完成したか?
        if len(path) == n:
            result.append("".join(path))   # 記録（path は使い回すので join でコピー相当）
            return
        # 2. 問い2: 今の選択肢をループ
        for ch in ("A", "B"):
            path.append(ch)   # choose
            backtrack()       # explore
            path.pop()        # unchoose ← これが "back"

    backtrack()
    return result
```

一般化するとこの形。`feasible` を再帰の**前**に置けば枝刈りになる（後述）。

```python
def backtrack(state, choices, result):
    if is_complete(state):
        result.append(state.copy())   # COPY! state は使い回しなので
        return
    for choice in choices:
        if not feasible(choice, state):
            continue                  # prune (枝刈り)
        state.add(choice)             # choose
        backtrack(state, choices, result)  # explore
        state.remove(choice)          # unchoose ← これが "back"
```

> **記録は必ずコピー**。`path` / `state` は全分岐で使い回す 1 個のオブジェクト。`result.append(path)` だと後で pop された path への参照が入って壊れる。`"".join(path)`（文字列を作る）や `state.copy()`（複製する）でスナップショットを残す。

## 具体例で 1 ステップずつ動かす

n=2 を最後まで動かす。

| 動き | path | できごと |
|---|---|---|
| choose A | `A` | 長さ1、深掘り |
| choose A | `AA` | 長さ2 → **記録 AA** |
| pop | `A` | A に戻る |
| choose B | `AB` | 長さ2 → **記録 AB** |
| pop | `A` | A に戻る |
| pop | `""` | A の選択肢を使い切った |
| choose B | `B` | 長さ1、深掘り |
| choose A | `BA` | 長さ2 → **記録 BA** |
| pop | `B` | B に戻る |
| choose B | `BB` | 長さ2 → **記録 BB** |
| pop | `B` | B に戻る |
| pop | `""` | 全部探索完了 |

どの pop も、ぴったり 1 歩だけ前の状態に戻している。これが backtracking の全て。結果は `AA, AB, BA, BB`。

## 枝刈り（prune）を入口で

全列挙は指数的に枝が増えるので、**無駄な部分木は再帰に入る前に切る**ほど効く。「この選択は明らかにダメ」と分かるなら、潜る前に `continue` する。`feasible(choice, state)` を再帰呼び出しの**前**に置けば、その先の指数的な部分木がまるごと消える。

潜ってから気づいて return するより、**入る前に切る**方が桁違いに速い。Word Search なら「マスが word の次の文字と違う」時点で即 return が典型。

## なぜ undo（pop）で済ませるのか

state を 1 個だけ使い回して全候補を列挙するため。分岐ごとに state を丸ごとコピーすれば undo は要らないが、毎回 O(N) のコピーが入って重い。`choose → recurse → unchoose` の一手戻しなら**追加メモリは O(深さ)** だけで、同じ state を全分岐で共有できる。これが backtracking が素朴な DFS より「賢い」と言われる理由。

## 計算量

| 種類 | オーダー |
|---|---|
| 純粋な全列挙 | **O(b^d)**（b=分岐数, d=深さ）指数 |
| 順列 Permutations | O(N!) |
| 部分集合 Subsets | O(2^N) |
| Word Search | O(m·n·4^L) |

prune がよく効く実問題では、理論上限よりずっと速く実用速度に収まる。

## 「Backtracking で解ける」と気付くサイン

問題文にこういう言葉が出たら、まず**木を描く**。

| キーワード | 何の木か |
|---|---|
| 「全部生成せよ」generate all | 各位置の選択肢が枝 |
| 「すべての組み合わせ」all combinations | 選ぶ/選ばないが枝 |
| 「ありうる全パターン」return all possible | 状態遷移が枝 |
| 順列 / 部分集合 / パズル / パス探索 | それぞれ選択肢が枝 |

「**最大/最小を 1 つ**」なら DP や貪欲を疑う。「**全部**列挙」なら backtracking。

## 典型問題ジャンル

| ジャンル | 例 |
|---|---|
| 順列 | Permutations, N-Queens |
| 部分集合 | Subsets, Combination Sum |
| パズル | Sudoku Solver, N-Queens |
| パス系 | Word Search, Rat in a Maze |

## まとめ

- Backtracking は新しいアルゴリズムではない。**自分で作りながら DFS する木**。各ノードが途中状態、各枝が選択、各葉が完成した答え。
- 速い/動く理由はただ 1 つ。**unchoose（`path.pop()`）が直前の状態に戻す**から、別の枝を試せる。これが無いと前進し続けるだけ。
- 書く前に 2 つだけ答える。「**いつ完成?**（記録）」「**今どんな選択肢?**（枝）」。
- 「generate all / all combinations / return all possible」を見たら、木を描いて、ループ書いて、unchoose を足す。それで終わり。

## このフォルダ（やさしい順）

1. `generate_strings.py` — **ここから**。上の A/B 文字列の例そのもの。盤面も方向も制約も無い裸の backtracking。`verbose=True` の出力が、上のトレース表と探索木にそのまま対応する。まず choose → explore → unchoose の 3 点セットを目で見て掴む。
2. `word_search.py` — 応用（王道だが難しめ）。2D の board を `#` でマーク（choose）→ 4 方向に再帰（explore）→ 戻す（unchoose）。複数の起点・枝刈り・in-place マークが乗るので、1 が腹落ちしてから読む。
