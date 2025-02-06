import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import Lenis from "@studio-freight/lenis";

gsap.registerPlugin(ScrollTrigger);

// 🔹 Smooth Scroll Setup
const lenis = new Lenis({
  smooth: true,
  lerp: 0.1, 
  infinite: false,
});

function smoothScroll() {
  lenis.on("scroll", () => ScrollTrigger.update());
  gsap.ticker.add((time) => lenis.raf(time * 1000));
  gsap.ticker.lagSmoothing(0);
}

smoothScroll();

// 🔹 3D Parallax Scroll Effect
gsap.utils.toArray(".parallax").forEach((layer) => {
  gsap.to(layer, {
    yPercent: -15,
    ease: "none",
    scrollTrigger: {
      trigger: layer,
      start: "top bottom",
      scrub: true,
    },
  });
});

// 🔹 Magnetic Button Effect (For Smooth Hover)
const buttons = document.querySelectorAll(".magnetic-button");

buttons.forEach((button) => {
  button.addEventListener("mousemove", (e) => {
    const { left, top, width, height } = button.getBoundingClientRect();
    const x = e.clientX - left - width / 2;
    const y = e.clientY - top - height / 2;
    gsap.to(button, { x: x * 0.3, y: y * 0.3, duration: 0.3 });
  });

  button.addEventListener("mouseleave", () => {
    gsap.to(button, { x: 0, y: 0, duration: 0.3 });
  });
});