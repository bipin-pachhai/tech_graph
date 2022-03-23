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
    f : [g,i],
    g : [h],
    h : [],
    i : [g,k],
    j : [i],
    k : [] 
};


let graph =  new Graph(data, 'a');
let s_graph = new Graph(s_data, 'f');
graph.depthFirstSearch();

console.log(">>>>>>>>>>>>>>>>>>>");
graph.breadthFirstSearch();






