class Graph{
    #graph;
    #start_node;
constructor(graph, start){
    this.#graph = graph;
    this.#start_node = start;
}
// Time : O(E), Space : O(n)
depthFirstSearch(){
    const stack = [ this.#start_node];

    while(stack.length > 0){
        const current = stack.pop();
        console.log(current);
        this.#graph[current].forEach(element => {
            stack.push(element);
            
        });
    }

};

dfsRecursive(){
    this.depthFirstSearchRecursiveHelper(this.#start_node);
};

depthFirstSearchRecursiveHelper(source_node){
    console.log(source_node);
    for(let neighbor of this.#graph[source_node]){
        depthFirstSearchRecursive(neighbor);
    }
};
// Prints the graph in Breadthfirstsearch order
breadthFirstSearch(){
    const queue = [this.#start_node];
    while(queue.length > 0){
      const curr = queue.shift();
      console.log(curr);
      for(let neighbor of this.#graph[curr]){
          queue.push(neighbor);
      }
    }
};

// using BFS technique
hasPath(src, dst){
    const queue = [src];

    while(queue.length > 0){
        const current = queue.shift();
        if(current === dst) return true;
        for(let neighbor of this.#graph[current]){
            queue.push(neighbor);
        }
    return false;
}
};

//Recursive DFS
hasPathRecursive(src, dst){
    if(src === dst){ return true;}
    for(let neighbor of this.graph[src]){
        if(hasPathRecursive(neighbor, dst) === true){ return true;}
    }
    return false;
};

undirectedPathExists( src, dst){
   const visited_set = new Set();
    return pathCheckHelper(src , dst, visited_set);
};

pathCheckHelper(src, dst, visited){
    if(src === dst){
        return true;
    }
    if(visited.has(src)) return false;

    visited.add(src);

    for(let neighbor of this.graph[src]) {
        if(pathCheckHelper(neighbor, dst, visited) === true) return true;
    }
    return false;     
};

// Build Adjacency list of graph from edges
buildAdjGraphData(edges){
    // Graph created should   be undirected
    const graph_data = {};
    for(let edge of edges ){
        const [a, b] = edge;
        if(!(a in graph_data)){
            graph_data[a] = [];
        }
        if(!(b in graph_data)){
            graph_data[b] = [];
        }

        graph_data[a].push(b);
        graph_data[b].push(a);
    }
    console.log(graph_data);
    return graph_data;


};

}// end of class

module.exports = Graph;