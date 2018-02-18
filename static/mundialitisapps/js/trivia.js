/*function nextquestion(id){
  id = document.getElementById('deletelobby').value
  newid=id+1
  location.href = "/trivia/" + newid + "-0";
}*/

function nextquestion(){
  location.href = "/trivianextquestion/";
}

function backtolobby(){
  location.href = "/trivialobbies/";
}

function optnon(){
  location.href = "/trivialobbies/";
}

/*function process(option, id, ttlscore){
  soption=option.toString();

  var i = 0, length = soption.length;
  for (i; i < length; i++) {
    soption = soption.replace(" ", "");
    soption = soption.replace(",", "");
  }


  option2=soption.replace(" ", "");
  option3=option2.replace(",","");
  pepe1 =
  location.href = "/triviaprocessing/" + soption.toString() + "-" + parseInt(id) + "-" + parseInt(ttlscore) + "/";
}
*/

function process(val){
  /*var part1 = "/triviaprocessing/";*/
  /*qwerty=option.toString();*/

if (val === 1){
  location.href= document.getElementById("optn1").value;
}else if (val === 2) {
  location.href= document.getElementById("optn2").value;
}else if (val === 3) {
  location.href= document.getElementById("optn3").value;
}else if (val === 4) {
  location.href = document.getElementById("optn4").value;
}
}

/*
function opt1on(){
  location.href = "/trivialobbies/";
}

function opt2on(){
  location.href = "/trivialobbies/";
}

function opt3on(){
  location.href = "/trivialobbies/";
}

function opt4on(){
  location.href = "/trivialobbies/";
}
*/
