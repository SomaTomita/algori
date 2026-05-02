package datastructures.Recursion;

// 再帰の概念を確認するための学習用ファイル。
// ※ 元の openGitBox の擬似コードはコンパイル不能だったので、
//   クラスでラップして「概念だけ伝わる形」に最小修正している。
public class Ball {

    private boolean isBall;
    private Ball ball;

    // recursion: 「中にボールが入っているまで箱を開け続ける」イメージ
    public Ball openGiftBox() {
        // ベースケース: 箱の中身がボールならそれを返して再帰終了
        if (isBall) return ball;
        // 再帰ステップ: そうでなければもう一度開ける (= 自分自身を呼ぶ)
        return openGiftBox();
    }


    // ----------------------------------------------------------------
    // call stack の例: methodOne → methodTwo → methodThree と呼んだ時、
    // 出力は "Three, Two, One" の順 (後に積まれた呼び出しから先に終わる)
    // ----------------------------------------------------------------
    public static void methodThree() {
        System.out.println("Three");
    }
    public static void methodTwo() {
        methodThree();
        System.out.println("Two");
    }
    public static void methodOne() {
        methodTwo();
        System.out.println("One");
    }

    public static void main(String[] args) {
        // methodOne() を呼ぶと "Three", "Two", "One" の順に出力される
        methodOne();

        // 再帰の典型例: 階乗 (factorial)
        // 4! = 4 * 3 * 2 * 1 = 24
        System.out.println(factorial(4));
    }


    // if int = 4,  4! = 24
    // stack ( 1!, 2!, 3!, 4! )  → First in, last out (FILO)
    public static int factorial(int n) {
        // ベースケース: n == 1 で再帰終了
        if (n == 1) return 1;
        // 再帰ステップ: n * factorial(n-1) で 1 段ずつ縮める
        return n * factorial(n - 1);
    }
}
