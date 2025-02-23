document.addEventListener('DOMContentLoaded', () => {
    console.log("🌌 Nutrient Galaxy Script Initialized!");

    d3.json("data/nutrient_data.json").then(data => {
        console.log("✅ Data loaded:", data);

        const width = window.innerWidth;
        const height = window.innerHeight;

        // Create a Three.js scene
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
        camera.position.z = 200;

        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(width, height);
        renderer.setClearColor(0x1a1a1a, 1);
        document.getElementById('nutrient-galaxy').appendChild(renderer.domElement);

        // Add light to the scene
        const light = new THREE.PointLight(0xffffff, 1);
        light.position.set(100, 100, 100);
        scene.add(light);

        const ambientLight = new THREE.AmbientLight(0x404040);
        scene.add(ambientLight);

        // Procedural planet textures using Three.js MeshStandardMaterial
        const planetColors = ['#3a3a3a', '#6b8e23', '#4682b4', '#8b4513', '#d2691e', '#708090', '#2e8b57', '#b22222'];

        const planets = [];

        data.slice(0, 30).forEach((d, i) => {
            const geometry = new THREE.SphereGeometry(Math.max(20, Math.sqrt(d.calories) * 10), 64, 64);
            const material = new THREE.MeshStandardMaterial({
                color: planetColors[i % planetColors.length],
                roughness: 0.5,
                metalness: 0.3
            });
            const planet = new THREE.Mesh(geometry, material);

            planet.position.x = (Math.random() - 0.5) * 800;
            planet.position.y = (Math.random() - 0.5) * 800;
            planet.position.z = (Math.random() - 0.5) * 800;

            planet.userData = {
                description: d.description,
                category: d.category,
                calories: d.calories,
                protein: d.protein,
                fat: d.fat,
                carbs: d.carbs
            };

            scene.add(planet);
            planets.push(planet);
        });

        // Animation loop
        function animate() {
            requestAnimationFrame(animate);

            planets.forEach(planet => {
                planet.rotation.y += 0.005;
                planet.rotation.x += 0.002;
            });

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

        // Tooltip for displaying planet info
        window.addEventListener('mousemove', (event) => {
            const mouse = new THREE.Vector2(
                (event.clientX / window.innerWidth) * 2 - 1,
                - (event.clientY / window.innerHeight) * 2 + 1
            );

            const raycaster = new THREE.Raycaster();
            raycaster.setFromCamera(mouse, camera);
            const intersects = raycaster.intersectObjects(planets);

            const tooltip = document.getElementById('tooltip');

            if (intersects.length > 0) {
                const { description, category, calories, protein, fat, carbs } = intersects[0].object.userData;
                tooltip.style.display = 'block';
                tooltip.style.left = `${event.pageX + 10}px`;
                tooltip.style.top = `${event.pageY + 10}px`;
                tooltip.innerHTML = `
                    <strong>${description}</strong><br>
                    Category: ${category}<br>
                    Calories: ${calories}<br>
                    Protein: ${protein}<br>
                    Fat: ${fat}<br>
                    Carbs: ${carbs}
                `;
            } else {
                tooltip.style.display = 'none';
            }
        });

    }).catch(error => {
        console.error("❌ Error loading data:", error);
    });
});



