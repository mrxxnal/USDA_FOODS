document.addEventListener('DOMContentLoaded', () => {
    console.log("🛠️ GSAP & D3 Loaded Successfully!");

    // Initial Fade-In Animation
    gsap.from(".fade-in", {
        duration: 1.2,
        opacity: 0,
        y: 30,
        stagger: 0.15,
        ease: "power3.out"
    });

    // Nutrient Galaxy Visualization
    d3.csv("data/cleaned_data.csv").then(data => {
        console.log("📂 Data loaded successfully:", data);
        
        const svg = d3.select("#data-art")
                      .append("svg")
                      .attr("width", "100%")
                      .attr("height", "500px");
        
        console.log("✅ SVG Element Created:", svg.node());

        // Prepare Data for Visualization
        const nodes = data.map((d, i) => ({
            id: i,
            name: d.description,
            category: d.category,
            value: +d.calories, // Using calories as an example
            protein: +d.protein,
            fat: +d.fat,
            carbs: +d.carbs
        }));

        console.log("🌐 Nodes for Visualization:", nodes);

        const simulation = d3.forceSimulation(nodes)
            .force("charge", d3.forceManyBody().strength(5))
            .force("center", d3.forceCenter(window.innerWidth / 2, 250))
            .force("collision", d3.forceCollide().radius(d => d.value * 0.05))
            .on("tick", () => {
                svg.selectAll("circle")
                    .data(nodes)
                    .join("circle")
                    .attr("r", d => Math.sqrt(d.value) * 1.5)
                    .attr("cx", d => d.x)
                    .attr("cy", d => d.y)
                    .attr("fill", "#ff6f61")
                    .attr("stroke", "#fff")
                    .attr("stroke-width", 2)
                    .on("mouseover", (event, d) => {
                        const tooltip = document.getElementById("tooltip");
                        tooltip.style.display = "block";
                        tooltip.style.left = `${event.pageX + 10}px`;
                        tooltip.style.top = `${event.pageY + 10}px`;
                        tooltip.innerHTML = `
                            <strong>${d.name}</strong><br>
                            Category: ${d.category}<br>
                            Calories: ${d.value}<br>
                            Protein: ${d.protein}<br>
                            Fat: ${d.fat}<br>
                            Carbs: ${d.carbs}
                        `;
                    })
                    .on("mouseout", () => {
                        const tooltip = document.getElementById("tooltip");
                        tooltip.style.display = "none";
                    });
            });
    }).catch(error => {
        console.error("❌ Error loading data:", error);
    });
});