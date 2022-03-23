class Graph{
    #graph;
    #start_node;
constructor(graph, start){
    this.#graph = graph;
    this.#start_node = start;
}

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

hasPath( src , dst){
    

    



 };

}// end of class

module.exports = Graph;