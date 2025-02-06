import gsap from "gsap";
import Lenis from "@studio-freight/lenis";

// 🔹 Initialize Lenis for smooth scrolling
const lenis = new Lenis({
  smooth: true,
  lerp: 0.1,
});

// 🔹 Fade-In Sections on Scroll
function fadeInSections() {
  gsap.utils.toArray(".section").forEach(section => {
    gsap.fromTo(section, 
      { opacity: 0, y: 50 }, 
      { opacity: 1, y: 0, duration: 1, ease: "power2.out", scrollTrigger: { trigger: section, start: "top 85%", toggleActions: "play none none none" }}
    );
  });
}

// 🔹 Navbar Color Change on Scroll
window.addEventListener("scroll", () => {
  document.querySelector(".navbar").classList.toggle("scrolled", window.scrollY > 50);
});

// 🔹 Floating Effect for Images & Elements
gsap.utils.toArray(".interactive-section").forEach(element => {
  gsap.to(element, { y: -10, duration: 2, repeat: -1, yoyo: true, ease: "power1.inOut" });
});

// 🔹 Parallax Effect on Scroll
gsap.utils.toArray(".parallax").forEach(layer => {
  gsap.to(layer, { yPercent: -10, scrollTrigger: { trigger: layer, start: "top bottom", scrub: true } });
});

// Start Lenis
lenis.on("scroll", fadeInSections);
lenis.start();