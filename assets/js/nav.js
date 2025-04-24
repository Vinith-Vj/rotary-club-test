
document.addEventListener("DOMContentLoaded", () => {
    const currentPath = window.location.pathname; // Get the current path
    const navbarLinks = document.querySelectorAll("#navbar .nav-link");

    navbarLinks.forEach(link => {
        if (link.getAttribute("data-path") === currentPath) {
            link.classList.add("active");
        } else {
            link.classList.remove("active");
        }
    });
});
