


var coordinate = new Object();
coordinate.x  = 0;
coordinate.y  = 0;
coordinate.z  = "fudge";

var cell = new Object();
cell.coordinate =  coordinate
cell.alive = false; 

console.log(cell);

var grid = new Object();
grid.cell = cell

console.log(grid)

var initalize = function(grid){

	grid.broken = true;
	console.log(grid);
}
initalize(grid);
initalize(1);