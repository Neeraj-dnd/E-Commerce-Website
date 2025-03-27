document.addEventListener("DOMContentLoaded", function () {
    const userToggle = document.getElementById("user-toggle");
    const userMenu = document.getElementById("user-menu");

    // Toggle the dropdown menu when clicking on the user name
    userToggle.addEventListener("click", (e) => {
        e.stopPropagation();  // Prevents event bubbling so it doesn't close immediately
        userMenu.classList.toggle("hidden");  // Toggles visibility of the dropdown menu
    });

    // Close the dropdown if clicked outside
    document.addEventListener('click', (e) => {
        if (!userMenu.contains(e.target) && !userToggle.contains(e.target)) {
            userMenu.classList.add("hidden");  // Close dropdown if clicked outside
        }
    });

    // === GSAP Animations ===
    if (typeof gsap !== "undefined" && typeof ScrollTrigger !== "undefined") {
        gsap.registerPlugin(ScrollTrigger);

        gsap.from(".hero h1", { duration: 1, y: -50, opacity: 0, ease: "bounce" });
        gsap.from(".hero p", { duration: 1.2, x: -50, opacity: 0, delay: 0.5 });
        gsap.from(".cta", { duration: 1.5, scale: 0.5, opacity: 0, delay: 0.8 });
    }

    // === Product Filter Buttons ===
    const filterButtons = document.querySelectorAll(".filter-btn");
    const products = document.querySelectorAll(".product");

    filterButtons.forEach(button => {
        button.addEventListener("click", () => {
            const category = button.getAttribute("data-category");

            // Highlight active button
            filterButtons.forEach(btn => btn.classList.remove("active"));
            button.classList.add("active");

            products.forEach(product => {
                const productCategory = product.getAttribute("data-category");
                const matches = category === "all" || productCategory === category;
                product.style.display = matches ? "block" : "none";
            });
        });
    });
});
