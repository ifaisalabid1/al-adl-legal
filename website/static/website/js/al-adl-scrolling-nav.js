addEventListener("scroll", (event) => {
    if (window.scrollY > 100) {
        var element = document.getElementById("alAdlAltNav");
        element.classList.add("top-nav-collapse");
    }
    else {
        var element = document.getElementById("alAdlAltNav");
        element.classList.remove("top-nav-collapse");
    }
});
