document.addEventListener('DOMContentLoaded', () => {
    console.log("🌌 Super Basic Nutrient Galaxy Initialized!");

    // Load the JSON data
    fetch('data/planet_data.json')
        .then(response => response.json())
        .then(data => {
            console.log("✅ Data loaded:", data);
            createNutrientGalaxy(data); 
        })
        .catch(error => console.error("❌ Error loading data:", error));

    function createNutrientGalaxy(data) {
        const width = window.innerWidth;
        const height = window.innerHeight;

        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 2000);
        camera.position.z = 1000;

        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        renderer.setSize(width, height);
        document.getElementById('nutrient-galaxy').appendChild(renderer.domElement);

        // Basic white light
        const light = new THREE.PointLight(0xffffff, 1);
        light.position.set(500, 500, 500);
        scene.add(light);

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

        data.forEach((d, i) => {
            const texture = new THREE.TextureLoader().load(planetImages[d.description]);
            const material = new THREE.SpriteMaterial({ map: texture });
            const planet = new THREE.Sprite(material);

            planet.scale.set(200, 200, 1); // Set size of the planet

            planet.position.x = (Math.random() - 0.5) * 1500;
            planet.position.y = (Math.random() - 0.5) * 800;
            planet.position.z = (Math.random() - 0.5) * 1000;

            scene.add(planet);
        });

        function animate() {
            requestAnimationFrame(animate);
            renderer.render(scene, camera);
        }

        animate();

        window.addEventListener('resize', () => {
            const width = window.innerWidth;
            const height = window.innerHeight;
            renderer.setSize(width, height);
            camera.aspect = width / height;
            camera.updateProjectionMatrix();
        });
    }
});







