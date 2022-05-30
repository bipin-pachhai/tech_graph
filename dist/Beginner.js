"use strict";
let id = 5;
let n_name = "Bipin PACHHAI";
let isWorking = true;
let x = "FreeStyle Works";
let arr_ids = [1, 2, 3, 4, 5];
let arr = [1, true, 'No Way'];
//Tuples
let person = [1, "This works here", true];
//Tuple Array
let employee;
employee = [
    [1, "Brad"],
    [2, "Ranch"],
    [3, "Sed"]
];
//Union
let pid;
pid = "Whatever";
//Enum
var Direct;
(function (Direct) {
    Direct[Direct["Up"] = 0] = "Up";
    Direct[Direct["Down"] = 1] = "Down";
    Direct[Direct["Left"] = 2] = "Left";
    Direct[Direct["Right"] = 3] = "Right";
})(Direct || (Direct = {}));
console.log(Direct.Left);
let user = {
    id: 0,
    name: "Bipin Pachhai"
};
//Type Assertion
let cid = 1;
let customerID = cid;
//functions
function addNum(x, y) {
    return x + y;
}
function log(message) {
    console.log(message);
}
const honda = {
    id: 334,
    make: "Honda",
    totalmiles: 1000000,
    vin: "1HJK230222TDG"
    //mileage optional
};
const add = (x, y) => x + y;
