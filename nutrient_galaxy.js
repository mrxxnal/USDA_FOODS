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

            // Alternate left and right positioning with structured vertical spacing
            const index = data.indexOf(d);
            const x = (index % 2 === 0) ? '10%' : '60%'; // Alternate between left and right
            const y = `${10 + index * 20}%`; // Vertically space planets evenly

            planet.style.left = x;
            planet.style.top = y;

            // Create an info box next to each planet
            const infoBox = document.createElement('div');
            infoBox.className = 'info-box';
            infoBox.style.left = (index % 2 === 0) ? '30%' : '80%';
            infoBox.style.top = y;

            galaxyContainer.appendChild(infoBox);

            // Add a simple tooltip on hover
            // Keep the hover tooltip with nutritional info
            planet.title = `${d.description}\nCategory: ${d.category}\nBrand: ${d.brand}`;

            // Show custom content in the info box
            planet.addEventListener('click', () => {
                infoBox.innerHTML = `<h2>${d.description} Planet</h2>
                    <p><strong>Did you know?</strong> This planet is part of our Ultimate Nutrient Galaxy and represents the food category of ${d.category}. Explore more to learn about its unique properties and benefits!</p>`;
                infoBox.style.display = 'block';
            });

            galaxyContainer.appendChild(planet);

            console.log(`🪐 Added planet: ${d.description} at (${x}, ${y})`);
        });
    }
});







