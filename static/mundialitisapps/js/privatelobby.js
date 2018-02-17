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
