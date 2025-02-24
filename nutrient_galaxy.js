document.addEventListener('DOMContentLoaded', () => {
    console.log("🌌 Super Basic Nutrient Galaxy Initialized!");

    // Load the JSON data
    fetch('data/nutrient_data.json')
        .then(response => response.json())
        .then(data => {
            console.log("✅ Data loaded:", data);
            createNutrientGalaxy(data.slice(0, 5)); // Limit to 20 planets for simplicity
        })
        .catch(error => console.error("❌ Error loading data:", error));

    function createNutrientGalaxy(data) {
        const width = window.innerWidth;
        const height = window.innerHeight;

        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 2000);
        camera.position.z = 1000;

        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(width, height);
        document.getElementById('nutrient-galaxy').appendChild(renderer.domElement);

        // Basic white light
        const light = new THREE.PointLight(0xffffff, 1);
        light.position.set(500, 500, 500);
        scene.add(light);

        const textureLoader = new THREE.TextureLoader();
        const planetTextures = [
            'assets/makemake.png',
            'assets/jupiter.png',
            'assets/mercury.png',
            'assets/mars.png',
            'assets/pluto.png'
        ];

        data.forEach((d, i) => {
            const radius = 150; // Fixed size for simplicity
            const geometry = new THREE.SphereGeometry(radius, 32, 32);
            const texture = textureLoader.load(planetTextures[i % planetTextures.length]);
            const material = new THREE.MeshStandardMaterial({
                map: texture,
                roughness: 0.8,
                metalness: 0.2
            });

            const planet = new THREE.Mesh(geometry, material);

            planet.position.x = (Math.random() - 0.5) * 1000;
            planet.position.y = (Math.random() - 0.5) * 500;
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






