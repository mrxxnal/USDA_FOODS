<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.11.5/gsap.min.js"></script>
<script>
    // GSAP animations for smooth elements appearance
    gsap.from(".fade-in", {
        duration: 1.5,
        opacity: 0,
        y: 50,
        stagger: 0.2,
        ease: "power4.out"
    });

    // Hover animation for cards
    document.querySelectorAll('.card').forEach(card => {
        card.addEventListener('mouseenter', () => {
            gsap.to(card, {scale: 1.05, duration: 0.3, ease: "power1.out"});
        });
        card.addEventListener('mouseleave', () => {
            gsap.to(card, {scale: 1, duration: 0.3, ease: "power1.out"});
        });
    });
</script>