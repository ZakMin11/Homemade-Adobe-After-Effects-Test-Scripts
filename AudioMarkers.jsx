var comp = app.project.activeItem;
var layer = comp.selectedLayers[0];
//alert(comp.duration + " " +  comp.frameRate); // 300 10 30
//alert(layer.property("Effects").property("Both Channels").property("Slider").valueAtTime(3, false));
comp.markerProperty.setValueAtTime(1, new MarkerValue("asdf"));
//var audioAmp = layer.audio.audioAmplitude;
var max = 10;
var min = layer.property("Effects").property("Both Channels").property("Slider").valueAtTime(0, false);
const fs = require('fs');
var data = "";
for (var i = 1; i<= comp.duration*comp.frameRate; i++ ){
    var frameTime = i/comp.frameRate;
    var prev  = i-1/comp.frameRate
    var audioLevel = layer.property("Effects").property("Both Channels").property("Slider").valueAtTime(frameTime, false);
    var audioLevelPrev = layer.property("Effects").property("Both Channels").property("Slider").valueAtTime(prev, false);
    data += audioLevel + ", ";
    //if (audioLevel/audioLevelPrev>7){
      //  alert(audioLevel);

    //}
    /*if (audioLevel>max){
        max = audioLevel;
    }
    else if (audioLevel < min){
        min = audioLevel;
    }*/
    //var audioLevel = layer.audio.audioLevels.valueAtTime(frameTime, false);
    
}
fs.writeFile('/Users/zakmineiko/Documents', 'AudioLevels.txt', data);
alert(max + "   +   "  + min )



