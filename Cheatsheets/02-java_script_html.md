let nombre = "Juan";      // texto (string)
let edad = 25;            // número (number)
let esVerdad = true;      // verdadero/falso (boolean)
let lista = ["uno", 2, true];  // lista (array)
let objeto = {            // objeto (como una cajita con etiquetas)
    nombre: "Juan",
    edad: 25
};

// Declarar una función
function saludar() {
    alert("Hola!");
}

// Llamar (ejecutar) una función
saludar();  // Aparece el mensaje "Hola!"

// Buscar por ID (el más fácil y confiable)
let miElemento = document.getElementById('mi-id');

// Buscar el primero que coincide con un selector CSS
let primerParrafo = document.querySelector('p');

// Buscar TODOS los que coinciden
let todosLosParrafos = document.querySelectorAll('p');

// Cambiar el texto de un elemento
miElemento.textContent = "Nuevo texto";

// Cambiar el HTML de un elemento (CUIDADO: peligroso si viene del usuario)
miElemento.innerHTML = "<b>texto en negrita</b>";

// Cambiar el estilo de un elemento
miElemento.style.color = "red";
miElemento.style.backgroundColor = "blue";

// Ocultar o mostrar un elemento
miElemento.style.display = "none";    // ocultar
miElemento.style.display = "block";   // mostrar

// Forma 1: en el HTML (la más fácil de entender)
// <button onclick="miFuncion()">Click</button>

// Forma 2: en JavaScript (la más recomendada)
let boton = document.getElementById('mi-boton');
boton.addEventListener('click', function() {
    alert('¡Hiciste clic!');
});

// Una lista de productos
let productos = [
    "Camisa",
    "Pantalón",
    "Zapatos"
];

// Recorrer la lista UNO POR UNO
for (let i = 0; i < productos.length; i++) {
    console.log(productos[i]);  // Muestra cada producto
}

// Versión más moderna (más fácil)
productos.forEach(function(producto) {
    console.log(producto);
});

<!-- Las 10 etiquetas que necesitas HTML-->
<h1>Título</h1>              <!-- Títulos -->
<p>Párrafo</p>               <!-- Párrafos -->
<div>Cajón</div>             <!-- Contenedor genérico -->
<span>Texto en línea</span>  <!-- Texto dentro de una línea -->
<a href="url">Enlace</a>     <!-- Enlaces -->
<img src="imagen.jpg">       <!-- Imágenes -->
<input type="text">          <!-- Campos de texto -->
<button>Botón</button>       <!-- Botones -->
<ul><li>Lista</li></ul>      <!-- Listas -->
<script>código</script>      <!-- Donde va el JavaScript -->