// GSAP Animation Script
document.addEventListener('DOMContentLoaded', () => {

    // Initial Fade-In Animation for All Elements with .fade-in Class
    gsap.from(".fade-in", {
        duration: 1.2,
        opacity: 0,
        y: 30,
        stagger: 0.15,
        ease: "power3.out"
    });

    // Hover Animation for Cards with .card Class
    document.querySelectorAll('.card').forEach(card => {
        card.addEventListener('mouseenter', () => {
            gsap.to(card, {
                scale: 1.08,
                duration: 0.3,
                ease: "power2.out",
                boxShadow: "0px 15px 25px rgba(0, 0, 0, 0.2)",
                backgroundColor: "#ff6f61",
                color: "#fff"
            });
        });
        card.addEventListener('mouseleave', () => {
            gsap.to(card, {
                scale: 1,
                duration: 0.3,
                ease: "power2.out",
                boxShadow: "0px 10px 20px rgba(0, 0, 0, 0.1)",
                backgroundColor: "#ffffff",
                color: "#2c3e50"
            });
        });
    });

    // Bouncy Animation for Section Divider
    gsap.from(".section-divider", {
        duration: 1,
        opacity: 0,
        scale: 0.9,
        ease: "elastic.out(1, 0.75)",
        delay: 0.5
    });

    // Smooth Reveal Animation for Images
    gsap.from(".topic-image", {
        duration: 1.2,
        opacity: 0,
        scale: 0.95,
        ease: "power2.out",
        stagger: 0.1
    });

    // Button Hover Animation for GitHub Buttons
    document.querySelectorAll('.github-button').forEach(button => {
        button.addEventListener('mouseenter', () => {
            gsap.to(button, {
                backgroundColor: "#e67e22",
                scale: 1.05,
                duration: 0.2,
                ease: "power1.out"
            });
        });
        button.addEventListener('mouseleave', () => {
            gsap.to(button, {
                backgroundColor: "#333",
                scale: 1,
                duration: 0.2,
                ease: "power1.out"
            });
        });
    });

});