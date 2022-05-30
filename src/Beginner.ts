let id: number =  5
let n_name : String = "Bipin PACHHAI"
let isWorking : boolean = true
let x: any = "FreeStyle Works"

let arr_ids: number[]  = [1,2,3,4,5]
let arr: any[] = [1, true, 'No Way']


//Tuples
let person: [number, string, boolean] = [1, "This works here", true]

//Tuple Array
let employee : [number, string][] 
employee = [
    [1, "Brad"],
    [2, "Ranch"],
    [3, "Sed"]
]

//Union
let pid: string | number
pid ="Whatever"

//Enum
enum Direct {
    Up,
    Down,
    Left,
    Right,
}

console.log(Direct.Left)

//Object Type
type User = {
    id: number,
    name: string,
}

let user : User = {
    id: 0,
    name: "Bipin Pachhai"
}

//Type Assertion
let cid: any =1
let customerID = cid as number

//functions
function addNum ( x: number, y: number) : number{
    return x+y;
}

function log(message: string | number): void{
    console.log(message);
}

// Interfaces

interface VehicleInterface{
    id: number
    make: string
    totalmiles: number
    vin : string | number
    mileage?: number
}


const honda : VehicleInterface = {
    id: 334,
    make: "Honda",
    totalmiles: 1000000,
    vin: "1HJK230222TDG"
    //mileage optional
}

interface MathFunc{
    (x: number, y: number) : number
}

const add: MathFunc =(x: number, y: number): number =>  x + y 






