document.getElementById("diabetes-form").addEventListener("submit", async function (e) {
  e.preventDefault();

  const formData = new FormData(e.target);
  const jsonData = Object.fromEntries(formData.entries());

  const response = await fetch("https://diabetes-detector.onrender.com", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(jsonData)
  });

  const result = await response.json();
  localStorage.setItem("prediction_result", JSON.stringify(result));
  window.location.href = "result.html";
});
