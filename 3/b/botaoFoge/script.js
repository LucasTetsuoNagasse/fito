const btn1 = document.querySelector("#btn");
let estado = 0;
btn1.addEventListener("mouseover", () => {
  estado++;
  if (estado == 1) {
    btn1.style.transform = "translate(400px, 0)";
  }
  if (estado == 2) {
    btn1.style.transform = "translate(0px, 0)";
    estado = 0;
  }
});