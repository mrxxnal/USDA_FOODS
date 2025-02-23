// Import necessary modules
import 'style.css';
import React, { useState, useEffect } from 'react';
import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import axios from 'axios';

const UltimateNutrientGalaxy = () => {
    const [data, setData] = useState([]);
    const planetTextures = [
        '/assets/makemake.png',
        '/assets/jupiter.png',
        '/assets/mercury.png',
        '/assets/mars.png',
        '/assets/pluto.png'
    ];

    useEffect(() => {
        axios.get('data/nutrient_data.json')
            .then((response) => {
                setData(response.data.slice(0, 30)); // Limit to 30 planets
                console.log('✅ Data loaded:', response.data);
                initThreeJS(response.data.slice(0, 30));
            })
            .catch((error) => {
                console.error('❌ Error loading data:', error);
            });
    }, []);

    const initThreeJS = (data) => {
        const width = window.innerWidth;
        const height = window.innerHeight;

        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 2000);
        camera.position.z = 1000;

        const renderer = new THREE.WebGLRenderer({ antialias: true });
        renderer.setSize(width, height);
        renderer.setClearColor(0x1a1a1a, 1);
        document.getElementById('nutrient-galaxy').appendChild(renderer.domElement);

        // Lighting
        const ambientLight = new THREE.AmbientLight(0x888888, 1.5);
        scene.add(ambientLight);

        const light = new THREE.PointLight(0xffffff, 1);
        light.position.set(500, 500, 500);
        scene.add(light);

        const textureLoader = new THREE.TextureLoader();
        const planets = [];

        data.forEach((d, i) => {
            const radius = Math.max(80, Math.sqrt(d.calories) * 10);
            const geometry = new THREE.SphereGeometry(radius, 64, 64);
            const texture = textureLoader.load(planetTextures[i % planetTextures.length]);
            const material = new THREE.MeshStandardMaterial({
                map: texture,
                roughness: 0.8,
                metalness: 0.2
            });

            const planet = new THREE.Mesh(geometry, material);

            planet.position.x = (Math.random() - 0.5) * 2000;
            planet.position.y = (Math.random() - 0.5) * 1000;
            planet.position.z = (Math.random() - 0.5) * 2000;

            scene.add(planet);
            planets.push(planet);
        });

        const controls = new OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;

        const animate = () => {
            requestAnimationFrame(animate);
            planets.forEach(planet => {
                planet.rotation.y += 0.005;
                planet.rotation.x += 0.002;
            });
            controls.update();
            renderer.render(scene, camera);
        };

        animate();

        window.addEventListener('resize', () => {
            const width = window.innerWidth;
            const height = window.innerHeight;
            renderer.setSize(width, height);
            camera.aspect = width / height;
            camera.updateProjectionMatrix();
        });
    };

    return (
        <div>
            <h2 className="galaxy-header">Ultimate Nutrient Galaxy</h2>
            <div id="nutrient-galaxy" style={{ width: '100%', height: '100vh' }}></div>
        </div>
    );
};

export default UltimateNutrientGalaxy;

