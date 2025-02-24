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

            // Define custom info for each planet
            const planetInfo = {
                'SODA': {
                    orbitFact: "Fizzing with energy! But too much soda can create a gravitational pull on your health.",
                    cosmicTip: "Stay hydrated—alternate soda with water to keep your system in balance! 💧"
                },
                'CHIPS': {
                    orbitFact: "Crunch through the asteroid belt of flavors! Chips are a quick energy boost but can weigh you down.",
                    cosmicTip: "Balance your chip intake with fresh veggies to keep your health in orbit! 🥕"
                },
                'CANDY': {
                    orbitFact: "A sweet meteor shower for your taste buds! But beware of the sugar crash landing.",
                    cosmicTip: "Enjoy candy in moderation and let fruits be your guiding stars! 🍇"
                },
                'SNACKS': {
                    orbitFact: "Snacks orbit your cravings like moons—great for a quick boost but watch out for empty calories.",
                    cosmicTip: "Choose whole grain and nut-based snacks to fuel your cosmic journey! 🌰"
                },
                'PIZZA': {
                    orbitFact: "A universal favorite! Each slice is a galaxy of flavors but can be a black hole for calories.",
                    cosmicTip: "Add veggies and lean proteins to make your pizza a stellar choice! 🍅"
                },
                'BURGER': {
                    orbitFact: "Juicy and delicious, but too many burgers can create a supermassive black hole in your diet.",
                    cosmicTip: "Opt for lean meat and whole grain buns for a lighter orbit! 🍔"
                },
                'ICE CREAM': {
                    orbitFact: "A cool comet of delight! Great for a treat, but too much may freeze your fitness goals.",
                    cosmicTip: "Scoop smaller portions and explore fruit-based desserts! 🍓"
                },
                'ENERGY DRINKS': {
                    orbitFact: "A rocket fuel for your day! But too much can launch your energy into a crash landing.",
                    cosmicTip: "Sip slowly and limit intake to keep your health in orbit! 🚀"
                },
                'SANDWICH': {
                    orbitFact: "A versatile space capsule of flavors! Can be a healthy option depending on the ingredients.",
                    cosmicTip: "Add greens and avoid heavy sauces for a balanced flight! 🥬"
                },
                'FRIES': {
                    orbitFact: "Golden meteors of crunch! Delicious but can add extra gravity to your diet.",
                    cosmicTip: "Bake instead of fry for a healthier trajectory! 🪐"
                }
            };

            // Populate info box content
            const planetData = planetInfo[d.description] || {
                orbitFact: "A unique planet in our nutrient galaxy! Enjoy it mindfully to keep your health in orbit.",
                cosmicTip: "Balance your intake with fresh fruits and water to stay stellar! 🚀"
            };

            infoBox.innerHTML = `
                <h2>${d.description} Planet 🌠</h2>
                <p><strong>Category:</strong> ${d.category}</p>
                <p><strong>Orbit Fact:</strong> ${planetData.orbitFact}</p>
                <p><strong>Cosmic Tip:</strong> ${planetData.cosmicTip}</p>
            `;

            galaxyContainer.appendChild(planet);
            galaxyContainer.appendChild(infoBox);

            console.log(`🪐 Added planet: ${d.description} at (${x}, ${y})`);
        });
    }
});














