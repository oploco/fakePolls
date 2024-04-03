document.addEventListener("DOMContentLoaded", function() {
  const value = document.querySelector("#vSpinner");
  const input = document.querySelector("#parametro_spinner");
  value.textContent = input.value;

  input.addEventListener("input", (event) => {
    value.textContent = event.target.value;
  });
});