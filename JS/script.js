// Get the modal
var modal = document.getElementById("myModal");
var buscar = document.getElementById("buscar");
var registro = document.getElementById("registro");
var buscarA = true;
var control = document.getElementById("control");;
var home = document.getElementById("home");
var visiBtn = document.getElementById("visita");
var retBtn = document.getElementById("return");
var vConfBtn = document.getElementById("visiConfirm");
var regBtn = document.getElementById("registrar");
var navB = document.getElementById("navD");




// Get the button that opens the modal
var btn = document.getElementById("srch");
var btn2 = document.getElementById("rgst");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  if(!buscarA){
    btn2.style.backgroundColor = "cornflowerblue";
    registro.style.display = "none";
    btn.style.backgroundColor = "lightskyblue";
    buscar.style.display = "block";
    buscarA=true;
  }
  //modal.style.display = "block";
}

// When the user clicks on the button, open the modal
btn2.onclick = function() {
  if(buscarA){
    btn.style.backgroundColor = "cornflowerblue";
    buscar.style.display = "none";
    btn2.style.backgroundColor = "lightskyblue";
    registro.style.display = "flex";
    buscarA=false;
  }


  //modal.style.display = "block";
}

visiBtn.onclick = function(){
  home.style.display = "none";
  control.style.display = "flex";
  //navB.style.display = "none";
}

vConfBtn.onclick = function(){
    home.style.display = "block";
    control.style.display = "none";
    //navB.style.display = "block";
  }

  retBtn.onclick = function(){
    home.style.display = "block";
    control.style.display = "none";
    //navB.style.display = "block";
  }

  regBtn.onclick = function(){
    home.style.display = "none";
    control.style.display = "flex";
    //navB.style.display = "none";
  }

/*btn.onmouseover = function(){
  this.style.backgroundColor = "lightskyblue";
}
btn.onmouseout = function(){
  this.style.backgroundColor = "cornflowerblue";
}

btn2.onmouseover = function(){
  this.style.backgroundColor = "lightskyblue";
}
btn2.onmouseout = function(){
  this.style.backgroundColor = "cornflowerblue";
}*/


// When the user clicks on <span> (x), close the modal


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}



function calcular(){
  try{           
        var a = parseFloat(document.getElementById("hdl").value) ;
        var b = parseFloat(document.getElementById("ldl").value) ;
        
        document.getElementById("total").value = a + b; 
        } catch(e){}
}


function suma(){
  try{           
          var p = parseFloat(document.getElementById("peso").value) ;
          var e = parseFloat(document.getElementById("estatura").value) ;
        
          document.getElementById("imc").value = p/(e*e); 
        } catch(e){}
}