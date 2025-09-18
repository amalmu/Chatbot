document.addEventListener("DOMContentLoaded", () => {
  const btn = document.getElementById("start-btn");
  
  btn.addEventListener("click", () => {
    btn.innerText = "Loading...";
    btn.disabled = true;

    
    setTimeout(() => {
      window.location.href = "/chatbot/"; 
    }, 1000);
  });
});
