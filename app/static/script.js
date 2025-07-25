document.addEventListener("DOMContentLoaded", function () {
  const startButton = document.getElementById("start-test");
  const textDisplay = document.getElementById("text-display");

  startButton.addEventListener("click", function () {
    fetch("/api/text")
      .then(response => {
        if (!response.ok) {
          throw new Error("Serverdan xatolik javobi keldi");
        }
        return response.json();
      })
      .then(data => {
        const words = data.text.split(" ");
        textDisplay.innerHTML = ""; // Eski matnni tozalash

        words.forEach(word => {
          const span = document.createElement("span");
          span.textContent = word;
          textDisplay.appendChild(span);

          // Oraliq qo‘shish
          const space = document.createTextNode(" ");
          textDisplay.appendChild(space);
        });
      })
      .catch(error => {
        textDisplay.innerHTML = `<div class="text-danger">❌ Xatolik yuz berdi: ${error.message}</div>`;
        console.error("Fetch xatosi:", error);
      });
  });
});
