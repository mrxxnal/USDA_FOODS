document.addEventListener('DOMContentLoaded', () => {
    console.log("🌌 Nutrient Galaxy Script Initialized!");

    d3.json("data/nutrient_data.json").then(data => {
        console.log("✅ Data loaded:", data);

        const width = window.innerWidth;
        const height = 600;

        // SVG Container
        const svg = d3.select("#nutrient-galaxy")
            .append("svg")
            .attr("width", width)
            .attr("height", height);

        // Scales for Positioning and Colors
        const xScale = d3.scaleLinear().domain([0, d3.max(data, d => d.calories)]).range([50, width - 50]);
        const yScale = d3.scaleLinear().domain([0, d3.max(data, d => d.protein)]).range([height - 50, 50]);
        const colorScale = d3.scaleOrdinal(d3.schemeSet3);

        // Create Data Circles
        const circles = svg.selectAll("circle")
            .data(data)
            .enter()
            .append("circle")
            .attr("cx", d => xScale(d.calories))
            .attr("cy", d => yScale(d.protein))
            .attr("r", d => Math.max(10, Math.sqrt(d.fat) * 5))
            .attr("fill", d => colorScale(d.category))
            .attr("stroke", "white")
            .attr("stroke-width", 1.5)
            .style("opacity", 0.8)
            .on("mouseover", (event, d) => {
                const tooltip = document.getElementById("tooltip");
                tooltip.style.display = "block";
                tooltip.style.left = `${event.pageX + 10}px`;
                tooltip.style.top = `${event.pageY + 10}px`;
                tooltip.innerHTML = `
                    <strong>${d.description}</strong><br>
                    Category: ${d.category}<br>
                    Calories: ${d.calories}<br>
                    Protein: ${d.protein}<br>
                    Fat: ${d.fat}<br>
                    Carbs: ${d.carbs}
                `;
                gsap.to(event.target, { scale: 1.5, duration: 0.3 });
            })
            .on("mouseout", (event) => {
                document.getElementById("tooltip").style.display = "none";
                gsap.to(event.target, { scale: 1, duration: 0.3 });
            });

        // GSAP Animation
        gsap.fromTo(circles.nodes(), 
            { opacity: 0, y: -50 },
            { opacity: 0.8, y: 0, duration: 1.5, stagger: 0.05, ease: "power2.out" }
        );

    }).catch(error => {
        console.error("❌ Error loading data:", error);
    });
});
