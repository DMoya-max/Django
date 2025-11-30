// --- Ocultar alertas después de 4 segundos ---
setTimeout(() => {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        alert.classList.remove('show');
        setTimeout(() => alert.remove(), 300);
    });
}, 4000);


// --- Scroll suave hacia las secciones ---
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        const destino = document.querySelector(this.getAttribute("href"));
        if (destino) {
            e.preventDefault();
            destino.scrollIntoView({ behavior: "smooth" });
        }
    });
});
