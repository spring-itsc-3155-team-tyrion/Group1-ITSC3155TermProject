function drawCanvas(){
    var canvas = document.getElementById("route-map");
    var context = canvas.getContext('2d');
    
    setTimeout(lineOne, 1000);
    setTimeout(lineTwo, 2000);
    setTimeout(lineThree, 3000);
    
}

function lineOne(){
    var canvas = document.getElementById("route-map");
    var context = canvas.getContext('2d');
    context.beginPath();
    context.moveTo(100, 100);
    context.lineTo(50, 50);
    context.stroke();
}
function lineTwo(){
    var canvas = document.getElementById("route-map");
    var context = canvas.getContext('2d');
    context.beginPath();
    context.moveTo(50, 50);
    context.lineTo(25, 50);
    context.stroke();
}
function lineThree(){
    var canvas = document.getElementById("route-map");
    var context = canvas.getContext('2d');
    context.beginPath();
    context.moveTo(25, 50);
    context.lineTo(75, 75);
    context.stroke();
}