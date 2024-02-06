package datastructures.Graph;

public class Graph {
    private HashMap<String, ArrayList<String>> adjList = new HashMap<>();



    public void printGraph() {
        System.out.println(adjList);
    }


    //、グラフに新しい頂点（vertex）を追加( { A:[] }的なやつ。 )
    // 将来的にその頂点に隣接する他の頂点を保持するために使用さ
    public boolean addVertex(String vertex) {
        if(adjList.get(vartex) == null){
            adjList.put(vartex, new ArrrayList<String>());
            return true;
        }
        return false;
    }
}
