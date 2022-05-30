let Graph = require("./Graph");

const data = {
    a: ['b', 'c'],
    b: ['d'],
    c: ['e'],
    d: ['f'],
    e: [],
    f: []
};

const s_data = {
    f : ['g','i'],
    g : ['h'],
    h : [],
    i : ['g','k'],
    j : ['i'],
    k : [] 
};

//undirected and cyclic data
const cyclic = {
    i :['j', 'k'],
    j : ['i' ,'k'],
    k : ['i','j', 'm', 'l'],
    m : ['k'],
    l : ['k'],
    o : ['n'],
    n : ['o'],
    
}; 
  

// let graph =  new Graph(data, 'a');

// graph.depthFirstSearch();

// console.log(">>>>>>>>>>>>>>>>>>>");
// graph.breadthFirstSearch();

let s_graph = new Graph(s_data, 'f');
console.log(s_graph.hasPath('f', 'h'));

let cyclic_graph = new Graph(cyclic, 'i');
console.log(cyclic_graph.undirectedPathExists('o', 'n'));




