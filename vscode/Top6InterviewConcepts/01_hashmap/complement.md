# Complement（補数）

> Two Sum で出てくる `target - num`。この「引き算」の正体を単独でまとめたノート。

## 一言でいうと

**いま手に持つ値が、答えになるために “あと必要な相手” の値**。

`a + b == target` のとき、`a` から見た `b` が `a` の **complement（補数）**。式を相手について解くだけ。

```
a + b = target
    b = target - a      ← complement
```

`target - num` は難しいことではなく、**方程式を相手について解いた結果**。

## なぜ O(N) の鍵になるのか

ナイーブ解は 2 つの値を両方ループで持ってきて足し、target と一致するか確かめる → O(N²)。

complement の発想は **片方 (num) だけ持って、もう片方 (need = target - num) を逆算し、それが過去に出たかを hashmap で O(1) 引く**。これで内側ループが丸ごと消える。

- **引き算 = 相手を 1 個だけ逆算** → hashmap で即引ける → O(N)
- **足し算 = 2 個そろえて検算** → そろえる時点で総当たり → O(N²)

だから「足し算かつ O(N)」は原理的に無理。complement（引き算）が O(N²) → O(N) の核心。

## 命名で直感的に

`complement` が抽象的なら、変数名を物語にする。

```python
need = target - num     # 「num が探している相手の値」
```

「num は足して target になる相手を待っている。その値が need」と読める。

## つまずき 3 つ

**1. 登録の順序（自分自身とペアを組まない）**
`need in seen` を **先に** チェックしてから `seen[num] = i`。逆だと自分を相手に返す。
例: `nums=[3,3], target=6` でも、この順序なら正しく `[0,1]`。

**2. 負の数でも成り立つ**
ただの引き算。`target=-8, num=-3 → need=-5`。

**3. 式は必ず `target - num`**
`num - target` と書き間違えやすい。検算: `num + need == target` になるか。

## 他の問題での complement（と、その個数）

「逆算して hashmap で O(1) 引き」は汎用パターン。1 要素あたりに逆算する complement の **個数** は問題で変わる。

| 問題 | 関係 | complement | 個数 |
| ---- | ---- | ---------- | ---- |
| Two Sum | `a + b = target` | `target - num` | 1 |
| Subarray Sum = K | `prefix − 過去prefix = k` | `prefix - k` | 1 |
| Pair with difference | `a − b = k` | `num - k` と `num + k` | **2** |

**なぜ差だけ 2 個か**: 和は対称（`a+b == b+a`）なので相手は一意。差は非対称（`a−b ≠ b−a`）で、num が「大きい側」か「小さい側」か決まらない。だから両取り。

- num が大きい側 → `相手 = num - k`
- num が小さい側 → `相手 = num + k`

## まとめ

- complement = `target - num` = 「足して target になる相手を逆算した値」。
- hashmap で O(1) 引きするから O(N²) → O(N)。足し算（検算）では落ちない。
- 和は complement 1 個、差は 2 個（向きがあるから）。
- `complement` → `need` とリネーム、登録は「チェックしてから」。

関連: このフォルダの `two_sum.py`（実装とトレース）、`concept.md`（Hashmap 全体）。
