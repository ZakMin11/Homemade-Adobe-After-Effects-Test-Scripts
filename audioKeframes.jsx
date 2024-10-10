var comp = app.project.activeItem;


var audioLayer = comp.layer(1);

var audioProperty = audioLayer.property("Audio");
var audioKeyframes = audioProperty.property("Audio Levels");

var audioDuration = audioProperty.duration;
alert()
var keyframeFrequency = 0.5;
for (var time = 0; time <= audioDuration; time += keyframeFrequency) {

    // Get the audio value at the current time
    var audioValue = audioProperty.valueAtTime(time, false);
    alert(audioValue);

    // Create a keyframe at the current time with the audio value
    audioKeyframes.addKey(time);
    audioKeyframes.setValueAtTime(time, audioValue[0]);
  }

  // Alert the user when the process is complete
  alert("Audio keyframes created successfully!");


