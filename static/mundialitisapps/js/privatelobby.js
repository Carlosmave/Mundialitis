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

function deletelobby2(){
  /*id = document.getElementById('deletelobby').value*/
  location.href = "/deletelobbypolla/" + document.getElementById('deletelobby').value;
}

function joinlobby2(){
  location.href = "/joinlobbypolla/" + document.getElementById('joinlobby').value;
}

function deletelobby3(){
  /*id = document.getElementById('deletelobby').value*/
  location.href = "/deletelobbyequipo/" + document.getElementById('deletelobby').value;
}

function joinlobby3(){
  location.href = "/joinlobbyequipo/" + document.getElementById('joinlobby').value;
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

function setupgame2(val){
  location.href= "/pollasetup/" + document.getElementById('setup').value;
/*  if (val===1){
  location.href="/triviasetup/" + document.getElementById('setup').value;
  location.href="/triviasetup/" + document.getElementById('setup').value + "/" + val;
}else if(val === 2){
  location.href="/triviasetup/" + document.getElementById('setup').value + "/" + val;
}*/
}

function setupgame3(val){
  location.href= "/equiposetup/" + document.getElementById('setup').value;
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

function endgame(){
  location.href= document.getElementById('endlobby').value;
}

function optionchecked(val){
  if (document.getElementById('opt1').checked){
      location.href="/pollaprocessing/" + document.getElementById('opt1').value.replace(/ /g, '') + "/" + val;
  }else if (document.getElementById('opt2').checked){
      location.href="/pollaprocessing/" + document.getElementById('opt2').value.replace(/ /g, '') + "/" + val;
  }else if (document.getElementById('opt3').checked){
      location.href="/pollaprocessing/" + document.getElementById('opt3').value.replace(/ /g, '') + "/" + val;
  }

}
str.replace(/hello/g, 'hi');

function previouspolla(val){
  newid=val-1
  location.href="/polladetails/" + newid;
}

function nextpolla(val){
  newid=val+1
  location.href="/polladetails/" + newid;
}

function gopollaindex(){
  location.href="/polla/";
}

function endpolla(){
  location.href="/pollabet/";
}
