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

        data.forEach((d) => {
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

            // Randomly position the planets within the container
            const x = Math.random() * (window.innerWidth - 150);
            const y = Math.random() * (window.innerHeight - 150);
            planet.style.left = `${x}px`;
            planet.style.top = `${y}px`;

            // Add a simple tooltip on hover
            planet.title = `${d.description}\nCategory: ${d.category}\nBrand: ${d.brand}`;

            galaxyContainer.appendChild(planet);

            console.log(`🪐 Added planet: ${d.description} at (${x}, ${y})`);
        });
    }
});







