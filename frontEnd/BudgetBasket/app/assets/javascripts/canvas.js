function sendJson(json){
    // send json to the functions that use it
    drawCanvas(json);
    getTotal(json);
}

function drawCanvas(json){
    // Get coordinates
    var coordinates = json.coordinate_matrix;
    
    var points = Object.keys(coordinates);
    
    
    // Translate coordinates to canvas coordinates
    for(var i = 0; i<points.length; i++){
        console.log("hello");
        var x = coordinates[points[i]].x; 
        var y = coordinates[points[i]].y;
        x = (x+100)* 1.5;
        y = (y+100)* 1.5;
        coordinates[points[i]].x = x;
        coordinates[points[i]].y = y;
        console.log(coordinates[points[i]]);
    }
    
    // Route order
    // var routeOrder = json.routeOrder; // "origin", "store_1"
    var routeOrder = json.route_order;
    var coordinate1;
    var coordinate2;
    for(var i =0; i < (routeOrder.length - 1); i++){
        coordinate1 = coordinates[routeOrder[i]];
        coordinate2 = coordinates[routeOrder[(i+1)]];
        drawLine(coordinate1, coordinate2);
    }
    
}

function getTotal(json){
    var total = json.price_total;
    $('.total p').text(total);
}

// Draw line between 2 coordinate parameters
function drawLine(coordinate1, coordinate2){
    var canvas = document.getElementById("route-map");
    var context = canvas.getContext('2d');
    
    context.beginPath();
    context.moveTo(coordinate1.x,coordinate1.y);
    context.lineTo(coordinate2.x, coordinate2.y);
    context.stroke();
}

// Draw a little circle at a coordinate point
function drawPoint(){
    var canvas = document.getElementById("route-map");
    var context = canvas.getContext('2d');
}