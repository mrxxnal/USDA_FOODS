document.addEventListener('DOMContentLoaded', () => {

    // Initial Fade-In Animation for All Elements with .fade-in Class
    gsap.from(".fade-in", {
        duration: 1.2,
        opacity: 0,
        y: 30,
        stagger: 0.15,
        ease: "power3.out"
    });

    // 🌌 Nutrient Galaxy Visualization
    const width = 800;
    const height = 500;

    const svg = d3.select("#data-art").append("svg")
        .attr("width", width)
        .attr("height", height)
        .style("background", "rgba(0,0,0,0.1)")
        .style("border", "2px solid red"); // Visualize the SVG boundary

    // Load and visualize data
    d3.csv("data/cleaned_data.csv").then(data => {
        console.log("Data loaded successfully:", data); // Check if data loads correctly

        const colorScale = d3.scaleOrdinal(d3.schemeCategory10);

        const tooltip = d3.select("#tooltip")
            .style("opacity", 0)
            .attr("class", "tooltip");

        const nodes = data.map(d => ({
            x: Math.random() * width,
            y: Math.random() * height,
            radius: Math.sqrt(d.calories) * 0.8,
            color: colorScale(d.category),
            description: d.description,
            calories: d.calories,
            brand: d.brand
        }));

        svg.selectAll("circle")
            .data(nodes)
            .enter().append("circle")
            .attr("cx", d => d.x)
            .attr("cy", d => d.y)
            .attr("r", d => d.radius)
            .attr("fill", d => d.color)
            .attr("opacity", 0.8)
            .on("mouseover", (event, d) => {
                tooltip.transition().duration(200).style("opacity", 1);
                tooltip.html(`<strong>${d.description}</strong><br>Calories: ${d.calories}<br>Brand: ${d.brand}`)
                    .style("left", (event.pageX + 10) + "px")
                    .style("top", (event.pageY - 20) + "px");
                gsap.to(event.target, { scale: 1.5, duration: 0.3, ease: "power2.out" });
            })
            .on("mouseout", (event) => {
                tooltip.transition().duration(500).style("opacity", 0);
                gsap.to(event.target, { scale: 1, duration: 0.3, ease: "power2.out" });
            });

    }).catch(error => {
        console.error("Error loading data:", error);
    });

    // Add Button Hover Animation for GitHub Buttons
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