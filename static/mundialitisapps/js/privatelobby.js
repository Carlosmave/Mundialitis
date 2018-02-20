function entry(){
/*var modal = document.getElementById('id01');
var pepa = String(value);
var lobbypass = document.getElementById('lobbypassword');
var pepe = 'santaclaus';
if(pepa===lobbypass){
    modal.style.display = "none";
}*/

if (document.getElementById('lobbypassword').value === document.getElementById('accesslobby').value){
  modal = document.getElementById('id01');
  modal.style.display = "none"
}else{
}
}


function deletelobby(){
  /*id = document.getElementById('deletelobby').value*/
  location.href = "/deletelobby/" + document.getElementById('deletelobby').value;
}

function joinlobby(){
  location.href = "/joinlobby/" + document.getElementById('joinlobby').value;
}

function goback(){
  location.href="/trivialobbies/";
}

/*function begingame(){
  location.href="/trivia/1-0/"
}*/

/*function choosegamemode(){
  location.href="/triviagamemode/"
}*/

function setupgame(val){
  location.href= "/triviasetup/" + document.getElementById('setup').value + "/" + val;
/*  if (val===1){
  location.href="/triviasetup/" + document.getElementById('setup').value;
  location.href="/triviasetup/" + document.getElementById('setup').value + "/" + val;
}else if(val === 2){
  location.href="/triviasetup/" + document.getElementById('setup').value + "/" + val;
}*/
}

function begingame(val){
  if(val===1){
    location.href="/triviabegin/" + document.getElementById('begin1').value;
  }else if (val === 2){
    location.href="/triviabegin/" + document.getElementById('begin2').value;
  }else if (val === 3){
    location.href="/triviabegin/" + document.getElementById('begin3').value;
  }


}
