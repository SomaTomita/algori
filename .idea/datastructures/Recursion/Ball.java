// recursion
public static Ball openGitBox() {
    if(isBall) return ball;
    openGitBox();
}







//call stack
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

methodOne();
// Three, Two, One






// if int = 4,  4! = 24
public static int factorial(int n) {
    if(n == 1) return 1;
    return n * factorial(n-1);
}
//stack ( 1!, 2!, 3!, 4! ) 　　First in, last out