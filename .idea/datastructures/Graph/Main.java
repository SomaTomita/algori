package datastructures.Graph;

public class Main {

    public static void main(String[] args) {

        Graph myGraph = new Graph();

        // 頂点を追加: A, B, C, D の 4 つ
        myGraph.addVertex("A");
        myGraph.addVertex("B");
        myGraph.addVertex("C");
        myGraph.addVertex("D");

        // 辺を追加: A↔B, A↔C, A↔D, B↔D, C↔D (両方向に登録される)
        myGraph.addEdge("A", "B");
        myGraph.addEdge("A", "C");
        myGraph.addEdge("A", "D");
        myGraph.addEdge("B", "D");
        myGraph.addEdge("C", "D");


        System.out.println("Graph before removeVertex():");
        myGraph.printGraph();

        myGraph.removeVertex("D");

        System.out.println("\nGraph after removeVertex():");
        myGraph.printGraph();

        /*
            EXPECTED OUTPUT:
            ----------------
            Graph before removeVertex():
            {A=[B, C, D], B=[A, D], C=[A, D], D=[A, B, C]}

            Graph after removeVertex():
            {A=[B, C], B=[A], C=[A]}

        */

    }

}