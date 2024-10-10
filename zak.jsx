var comp = app.project.activeItem;


var inpoint = selectedLayer.inPoint;
var outpoint = selectedLayer.outPoint;

var myWindow = new Window("palette", "My Custom Window", undefined, {resizeable: true});


var myButton = myWindow.add("button", undefined, "select, Add markers");


myButton.onClick = function() {
    
    alart(setMarkers(comp.selectedLayers[0]));
    

};
function setMarkers(selectedLayer) {
    return "Markers set";
}

// Show the window
myWindow.show();

