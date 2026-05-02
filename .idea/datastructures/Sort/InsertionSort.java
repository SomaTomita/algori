package datastructures.Sort;

import java.util.Arrays;

public class InsertionSort {

    // 元の typo "insettionSort" を insertionSort に修正
    public static void insertionSort(int[] array) {
        // i=1 から始めて、左側 [0..i-1] は既にソート済みという不変条件で進める
        for (int i = 1; i < array.length; i++) {
            int temp = array[i];
            int j = i - 1;
            //　スタートする配列1の値より配列0の方が小さければ。
            while (j > -1 && temp < array[j]) {
                //　手前の値を一つ後ろに。
                array[j + 1] = array[j];
                //　後ろのtempを前に。
                array[j] = temp;
                j--;
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {4, 2, 6, 5, 1, 3};
        insertionSort(arr);
        // 期待値: [1, 2, 3, 4, 5, 6]
        System.out.println(Arrays.toString(arr));
    }
}
