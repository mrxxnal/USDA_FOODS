// GSAP Animation Script
document.addEventListener('DOMContentLoaded', () => {

    // Initial Fade-In Animation for All Elements with .fade-in Class
    gsap.from(".fade-in", {
        duration: 1.5,
        opacity: 0,
        y: 50,
        stagger: 0.2,
        ease: "power4.out"
    });

    // Hover Animation for Cards with .card Class
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            gsap.to(card, {
                scale: 1.1, 
                duration: 0.3, 
                ease: "power1.out",
                boxShadow: "0px 20px 30px rgba(0, 0, 0, 0.2)",
                backgroundColor: "#ff6f61",
                color: "#ffffff"
            });
            gsap.to(card.querySelector('h4'), { 
                color: "#ffffff", 
                duration: 0.2 
            });
        });
        
        card.addEventListener('mouseleave', () => {
            gsap.to(card, {
                scale: 1, 
                duration: 0.3, 
                ease: "power1.out",
                boxShadow: "0px 10px 20px rgba(0, 0, 0, 0.1)",
                backgroundColor: "#ffffff",
                color: "#2c3e50"
            });
            gsap.to(card.querySelector('h4'), { 
                color: "#2c3e50", 
                duration: 0.2 
            });
        });
    });

    // Bouncy Animation for Section Divider
    gsap.from(".section-divider", {
        duration: 1.2,
        opacity: 0,
        scale: 0.8,
        ease: "elastic.out(1, 0.5)"
    });

    // Smooth Reveal Animation for Images
    gsap.from(".topic-image", {
        duration: 1.5,
        opacity: 0,
        scale: 0.9,
        ease: "power2.out"
    });

    // Button Hover Animation for GitHub Buttons
    const githubButtons = document.querySelectorAll('.github-button');
    githubButtons.forEach(button => {
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