// Get the modal
var modal = document.getElementById("myModal");
var buscar = document.getElementById("buscar");
var registro = document.getElementById("registro");
var buscarA = true;
var control = document.getElementById("control");
var home = document.getElementById("home");
var visiBtn = document.getElementById("visita");
var retBtn = document.getElementById("return");
var vConfBtn = document.getElementById("visiConfirm");
var regBtn = document.getElementById("registrar");
var navB = document.getElementById("navD");
var navC = document.getElementById("consulta");




// Get the button that opens the modal
var btn = document.getElementById("srch");
var btn2 = document.getElementById("rgst");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function () {
  if (!buscarA) {
    btn2.style.backgroundColor = "cornflowerblue";
    registro.style.display = "none";
    btn.style.backgroundColor = "lightskyblue";
    buscar.style.display = "block";
    buscarA = true;
  }
  //modal.style.display = "block";
}

// When the user clicks on the button, open the modal
btn2.onclick = function () {
  if (buscarA) {
    btn.style.backgroundColor = "cornflowerblue";
    buscar.style.display = "none";
    btn2.style.backgroundColor = "lightskyblue";
    registro.style.display = "flex";
    buscarA = false;
  }


  //modal.style.display = "block";
}

visiBtn.onclick = function () {
  home.style.display = "none";
  control.style.display = "flex";
  //navB.style.display = "none";
  navC.style.display = "block";
}

vConfBtn.onclick = function () {
  home.style.display = "block";
  control.style.display = "none";
  //navB.style.display = "block";
  navC.style.display = "none";
}

retBtn.onclick = function () {
  home.style.display = "block";
  control.style.display = "none";
  //navB.style.display = "block";
  navC.style.display = "none";
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
window.onclick = function (event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

//Fecha actual en control 
window.addEventListener('load', function () {
  var today = new Date().toISOString().split('T')[0];
  document.getElementsByName('fecha')[0].value = today;
});


function suma() {
  const peso = parseFloat(document.getElementById("peso").value);
  const talla = parseFloat(document.getElementById("talla").value);
  const imc = peso / Math.pow(talla / 100, 2);
  document.getElementById("imc").value = imc.toFixed(2);
}


var antP = document.getElementById("antecedentes");
var idP = document.getElementById("identificacion");
var diagP = document.getElementById("diagnostico");
var sigBtn = document.getElementById("siguiente");
var canBtn = document.getElementById("anterior");
var antA = false;
var diagA = false;
let loginForm = document.getElementById("registro");

canBtn.onclick = function () {
  if (antA) {
    antP.style.display = "none";
    idP.style.display = "flex";
    antA = false;
    canBtn.classList.remove("anterior");
    sigBtn.classList.remove("siguiente");

  }
  else if (diagA) {
    diagP.style.display = "none";
    antP.style.display = "flex";
    diagA = false;
    antA = true;
    sigBtn.classList.remove("confirmar");
    sigBtn.innerHTML = "Confirmar";
  }
}

//Validacion de Registro
document.getElementById("siguiente").addEventListener("click", function(event){
  // Detener la propagación del evento
  event.stopPropagation();

  // Obtener los valores de los campos obligatorios
  var fechaNac = document.querySelector("input[name='fechaNac']").value;
  var sexo = document.querySelector("select[name='Sexo']").value;
  var entidad = document.querySelector("input[name='entidad']").value;
  var domicilio = document.querySelector("input[name='domicilio']").value;
  var telefono = document.querySelector("input[name='telefono']").value;

  // Verificar si los campos obligatorios están completos
  if(fechaNac === "" || sexo === "" || entidad === "" || domicilio === "" || telefono === "") {
    // Si alguno de los campos obligatorios está vacío, mostrar un mensaje de error y evitar que se envíe el formulario
    alert("Por favor complete todos los campos obligatorios.");
    event.preventDefault();
  } else {
    // Si todos los campos obligatorios están completos, enviar el formulario y cambiar la pantalla que se muestra al usuario
    if (antA) {
      antP.style.display = "none";
      diagP.style.display = "flex";
      antA = false;
      diagA = true;
      sigBtn.classList.add("confirmar");
      sigBtn.innerHTML = "Registrar Paciente";
    }
    else if (!diagA) {
      idP.style.display = "none";
      antP.style.display = "flex";
      antA = true;
      sigBtn.classList.add("siguiente");
      canBtn.classList.add("anterior");
    }
    else {
      loginForm.submit();
    }
  }
});

/*
loginForm.addEventListener("submit", (e) => {
  e.preventDefault();
  alert("Ensure you input a value in both fields!");
  loginForm.submit();
});/*/