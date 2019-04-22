var colors = [];
var coordinates;
var points;
var routeOrder;



function sendJson(json){
    // send json to the functions that use it
    drawCanvas(json);
    displayData(json);
    
}

function drawCanvas(json){
    
    // Get coordinates
    coordinates = json.coordinate_matrix;
    points = Object.keys(coordinates); // list of keys for the coordinate points
    drawLabels(); // Label all the coordinates on the canvas map
    
    // Translate coordinates to canvas coordinates
    for(var i = 0; i<points.length; i++){
        
        var x = coordinates[points[i]].x; 
        var y = coordinates[points[i]].y;
        x = parseInt(x);
        y = parseInt(y);
        
        // Translating where origin is (0,0) and range from (-100,100) to origin (150,150) and range (0, 300)
        x = (x+100) * 1.5;
        y = (y+100) * 1.5;
        
        coordinates[points[i]].x = x;
        coordinates[points[i]].y = y;
    }
    
    // Draw lines according to route
    routeOrder = json.route_order;
    var coordinate1;
    var coordinate2;
    for(var i =0; i < (routeOrder.length - 1); i++){
        coordinate1 = coordinates[routeOrder[i]];
        coordinate2 = coordinates[routeOrder[(i+1)]];
        drawLine(coordinate1, coordinate2);
        drawPoint(coordinate2);
    }
    
}

function displayData(json){
    
    // Shopping List
        // Loop through Stores
    
    for (var i =1; i<(routeOrder.length-1); i++){ // store loop, skipping origin
        // Get current store
        var storeName = routeOrder[i];
        // clone store element to edit
        var clone = $('.store-original').clone();
        clone.removeClass("store-original hidden").addClass("store").attr("id", storeName);
        
        // Add storeName as title
        var title = clone.find(".title");
        title.append(storeName);
        
        // Update color swatch to the corresponding color
        var colorSwatch = clone.find(".color-swatch");
        colorSwatch.css("background-color", colors[(i-1)]);
        
        
        
        var valueList = clone.find(".value-list");
        // Get all ingredients
        var shoppingList = json.shopping_list;
        var ingredientList = Object.keys(shoppingList);
        for(var item = 0; item < ingredientList.length; item++){
            // Add ingredients for that store
            var currentStore = shoppingList[ingredientList[item]].ingredient_store.toString();
            var ingredient = ingredientList[item];
            var value = clone.find(".value-original").clone();
            if(currentStore == storeName.toString()){
                
                value.removeClass("value-original").addClass("ingredient-value").attr("id", ingredient);
                value.text(ingredient);
                
                valueList.append(value);
            }
            clone.append(valueList);
        }
        $('#shopping-list').append(clone);
    }
    
    // Substituted Items
    var subItems = json.substituted_ingredients;
    for(var i=0;i<subItems.length; i++){
        $('#sub-items .value').append(subItems[i].toString() + "</br>");
    }
    // Unavailable Items
    var naItems = json.completely_unavailable_ingredients;
    for(var i=0;i<naItems.length; i++){
        $('#na-items .value').append(naItems[i].toString() + "</br>");
    }
    // Cost of Ingredients
    var itemCost = json.price_ingredients;
    itemCost = twoDecimals(itemCost);
    $('#ingredient-cost .value').text("$" + itemCost);
    
    // Cost of Route
    var gasCost = json.price_route;
    gasCost = twoDecimals(gasCost);
    $('#route-cost .value').text("$" + gasCost);
    
    // Total Price
    var total = json.price_total;
    total = twoDecimals(total);
    $('#total-cost .value').text("$" + total);
}


// Draw line between 2 coordinate parameters
function drawLine(coordinate1, coordinate2){
    var canvas = document.getElementById("route-map");
    var context = canvas.getContext('2d');
    
    context.beginPath();
    context.strokeStyle = "black";
    context.moveTo(coordinate1.x,coordinate1.y);
    context.lineTo(coordinate2.x, coordinate2.y);
    context.stroke();
}

// Draw a little circle at a coordinate point
function drawPoint(coordinate){
    var canvas = document.getElementById("route-map");
    var context = canvas.getContext('2d');
    var color = getRandomColor();
    colors.push(color);
    
    // Colored Circle around coordinate point
    context.beginPath();
    context.moveTo(coordinate.x, coordinate.y);
    context.strokeStyle = color;
    context.arc(coordinate.x, coordinate.y, 7, 0, 2 * Math.PI);
    context.fillStyle = color;
    context.fill();
    context.stroke();
    
    // Black circle for coordinate point
    context.beginPath();
    context.moveTo(coordinate.x, coordinate.y);
    context.strokeStyle = "black";
    context.arc(coordinate.x, coordinate.y, 2, 0, 2 * Math.PI);
    context.fillStyle = "black";
    context.fill();
    context.stroke();
    
    
}
function getRandomColor(){
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    
    return color;
}
function twoDecimals(longNumber){
    var shortNumber = parseFloat(longNumber).toFixed(2);
    
    return shortNumber;
}
function drawLabels(){
    // Draw labels above all coordinate points
    var canvas = document.getElementById("route-map");
    var context = canvas.getContext('2d');
    for (var i =0; i<points.length; i++){
        context.beginPath();
        context.font = "8.5px Georgia";
        var name = points[i];
        var coordinateX = (parseInt(coordinates[points[i]].x) +107) *1.5;
        var coordinateY = (parseInt(coordinates[points[i]].y)+102) *1.5
        context.fillText(name, coordinateX, coordinateY);
        context.stroke();
    }
}
