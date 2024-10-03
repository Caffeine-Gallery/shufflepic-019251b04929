import { backend } from 'declarations/backend';

async function changeBackground() {
    try {
        const imageUrl = await backend.getRandomImageUrl();
        document.body.style.backgroundImage = `url(${imageUrl})`;
    } catch (error) {
        console.error("Error fetching random image:", error);
    }
}

document.getElementById('changeBackground').addEventListener('click', changeBackground);

// Set initial background
changeBackground();
