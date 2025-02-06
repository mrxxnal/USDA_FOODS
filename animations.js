import gsap from "gsap";
import Lenis from "@studio-freight/lenis";

const lenis = new Lenis({
  smooth: true,
  lerp: 0.1,
});

// Animation function for fade-in effects
function animateSections() {
  gsap.from(".section", {
    opacity: 0,
    y: 50,
    duration: 1.2,
    stagger: 0.3,
    ease: "power2.out",
  });
}

// Trigger animations on scroll
lenis.on("scroll", () => {
  animateSections();
});

lenis.start();