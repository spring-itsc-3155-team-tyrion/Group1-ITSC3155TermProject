function drawCanvas(){
    var canvas = document.getElementById("route-map");
    var context = canvas.getContext('2d');
    context.beginPath();
    context.moveTo(100, 100);
    context.lineTo(50, 50);
    context.stroke();
    
    context.beginPath();
    context.moveTo(50, 50);
    context.lineTo(25, 50);
    context.stroke();
    
    context.beginPath();
    context.moveTo(25, 50);
    context.lineTo(75, 75);
    context.stroke();
}