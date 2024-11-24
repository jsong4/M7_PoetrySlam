var synthesis = window.speechSynthesis;
var utterance = new SpeechSynthesisUtterance("Hello, Khalil you little cutie!");

function sayIt(){
  if ('speechSynthesis' in window) {
    synthesis.speak(utterance);
  } else {
    console.log('Text-to-speech not supported.');
  }
};

function logVoices(){
    var voices = synthesis.getVoices();
  
    voices.forEach(function (voice) {
      console.log({
        name: voice.name,
        lang: voice.lang
      });
    });
    if ('speechSynthesis' in window) {
        utterance.voice = voices[38];  
        console.log(voices[0]);
        synthesis.speak(utterance);
      }
    
    utterance.pitch = 1.5;
    utterance.rate = 1.3;
    utterance.volume = 1.2;
  }