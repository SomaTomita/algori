public static void insettionSort(int[] array) {
    for (int i = 1; i < array.length; i++) {
        int temp = array[i];
        int j = i - 1;
        //　スタートする配列1の値より配列0の方が小さければ。
        while (j > -1 && temp < array[j]) {
            //　手前の値を一つ後ろに。
            array[j+1] = array[j];
            //　後ろのtempを前に。
            array[j] = temp;
            j--;
        }
    }
}