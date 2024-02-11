public static void selevctionSort(int[] array) {
    for (int i = 0; i < array.length; i++) {
        int minIndex = i;
        // 一番最初の i を基準にi+1の j が minIndex を探す
        for (int j = i+1; j < array.length; j++) {
            if (array[j] < array[minIndex]) {
                minIndex = j;
            }
        }
        if (i != minIndex) {
            int temp = array[i];
            array[i] = array[minIndex];
            array[minIndex] = temp;
        }
    }
}