package datastructures.Graph;

public class Graph {
    private HashMap<String, ArrayList<String>> adjList = new HashMap<>();



    public void printGraph() {
        System.out.println(adjList);
    }


    // グラフに新しい頂点（vertex）を追加( { A:[] }的な。 )
    // 将来的にその頂点に隣接する他の頂点を保持するために使用さ
    public boolean addVertex(String vertex) {
        // vertexがまだグラフに追加されていなければ、頂点に隣接する頂点が追加。
        if(adjList.get(vertex) == null){
            adjList.put(vertex, new ArrrayList<String>());
            return true;
        }
        return false;
    }

    // 頂点1から頂点2へのエッジと、頂点2から頂点1へのエッジの両方を追加
    // ex) {A = [B], B = [A]}
    public boolean addEdge(String vertex1, String vertex2) {
        if (adjList.get(vertex1) != null && adjList.get(vertex2) != null) {
            adjList.get(vertex1).add(vertex2);
            adjList.get(vertex2).add(vertex1);
            return true;
        }
        return false;
    }

    // ex) {A = [B, C], B = [A, C] C = [A, B]}
    // remove("A", "B")
    // →　{A = [C], B = [C] C = [A, B]}
    public boolean removeEdge(String vertex1, String vertex2) {
        if (adjList.get(vertex1) != null && adjList.get(vertex2) != null) {
            adjList.get(vertex1).remove(vertex2);
            adjList.get(vertex2).remove(vertex1);
            return true;
        }
        return false;
    }

    // ex) {A = [B, C, D], B = [A, D] C = [A, D], D = [A, B, C]}
    public boolean removeVertex(String vertex) {
        if (adjList.get(vertex) == null) return false;
        // 他のvertexに紐づく指定されたvertexと同じedgeを消していく。( D = [A, B, C]のA~Cを回す。)
        for (String otherVertex : adjList.get(vertex)) {
            // D=[A, B, C]とあれば ex) vertex Aの中にあるedge Dを消す。
            adjList.get(otherVertex).remove(vertex);
        }
        // vertex Dの本元を消す。
        adjList.remove(vertex);
        // グラフから特定の頂点（例えば"D"）を削除する場合、このループは
        // "D"に隣接するすべてのvertexの隣接リストから"D"を削除。
        // 最初の反復ではotherVertexは"A" ...
        return true;
    }


}
