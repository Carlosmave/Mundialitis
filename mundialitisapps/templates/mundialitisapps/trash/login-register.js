function validateForm() {
    var x = document.getElementById("rpassword").value;
    var y = document.getElementById("rpassword2").value;
    if (x != y) {
        alert("Las contraseñas no son iguales");
        return false;

    }//else{
    //  var url = "www.google.com"
      //window.location.href = "www.google.com"
      //url2=url.append(/1)
      //window.location(url);
    }
