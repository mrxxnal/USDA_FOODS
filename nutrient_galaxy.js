document.addEventListener('DOMContentLoaded', () => {
    console.log("🌌 Super Simple Nutrient Galaxy Initialized!");

    // Load the JSON data
    fetch('data/planet_data.json')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log("✅ Data loaded:", data);
            createNutrientGalaxy(data.slice(0, 10));
        })
        .catch(error => console.error("❌ Error loading data:", error));

    function createNutrientGalaxy(data) {
        const galaxyContainer = document.getElementById('nutrient-galaxy');
        galaxyContainer.innerHTML = ''; // Clear any existing elements

        const planetImages = {
            'SODA': 'assets/moon.png',
            'CHIPS': 'assets/jupiter.png',
            'CANDY': 'assets/makemake.png',
            'SNACKS': 'assets/mars.png',
            'PIZZA': 'assets/mercury.png',
            'BURGER': 'assets/makemake.png',
            'ICE CREAM': 'assets/moon.png',
            'ENERGY DRINKS': 'assets/jupiter.png',
            'SANDWICH': 'assets/mercury.png',
            'FRIES': 'assets/mars.png'
        };

        data.forEach((d, index) => {
            const planet = document.createElement('img');
            const imgSrc = planetImages[d.description] || 'assets/default.png';
            planet.src = imgSrc;
            planet.alt = d.description;
            planet.className = 'planet';

            const planetSize = 450; // Make the planets 3x bigger (150px * 3)

            // Check if the image loads correctly
            planet.onerror = () => {
                console.error(`❌ Image failed to load: ${imgSrc}`);
                planet.src = 'assets/default.png'; // Fallback to default
            };

            // Alternate left and right positioning with structured vertical spacing
            const x = (index % 2 === 0) ? '5%' : '45%'; // Alternate between left and right
            const y = `${0 + index * 25}%`; // Vertically space planets evenly

            planet.style.left = x;
            planet.style.top = y;

            // Add a simple tooltip on hover
            planet.title = `${d.description}\nCategory: ${d.category}\nBrand: ${d.brand}`;

            // Create an info box next to each planet and make it always visible
            const infoBox = document.createElement('div');
            infoBox.className = 'info-box';
            infoBox.style.left = (index % 2 === 0) ? '35%' : '75%';
            infoBox.style.top = `calc(${y} + 50px)`;

            // Populate info box content
            infoBox.innerHTML = `
            <h2>${d.description} Planet 🌠</h2>
            <p><strong>Category:</strong> ${d.category}</p>
            <p><strong>Orbit Fact:</strong> The ${d.description} planet is a true taste supernova! Enjoy its boost but don't let your cravings pull you into a black hole.</p>
            <p><strong>Cosmic Tip:</strong> Keep your nutrition in orbit—balance ${d.description.toLowerCase()} with fresh fruits and water! 🚀</p>
        `;

            galaxyContainer.appendChild(planet);
            galaxyContainer.appendChild(infoBox);

            console.log(`🪐 Added planet: ${d.description} at (${x}, ${y})`);
        });
    }
});














