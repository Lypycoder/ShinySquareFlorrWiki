(function() {
    'use strict';
 
    // Function to obtain all ultras
    function getAllUltras() {
        // Assuming there's a global game object with a method to get ultras
        if (window.game && typeof window.game.obtainUltra === 'function') {
            const ultras = ['ultra1', 'ultra2', 'ultra3']; // List all ultras here
            ultras.forEach(ultra => {
                window.game.obtainUltra(ultra);
            });
            alert('All ultras have been obtained!');
        } else {
            console.error('Game object or obtainUltra method not found.');
        }
    }
 
    // Adding a button to the game interface for obtaining all ultras
    function addButton() {
        const btn = document.createElement('button');
        btn.innerHTML = 'Get All Ultras';
        btn.style.position = 'fixed';
        btn.style.top = '10px';
        btn.style.right = '10px';
        btn.style.zIndex = 1000;
        btn.addEventListener('click', getAllUltras);
        document.body.appendChild(btn);
    }
 
    // Wait for the game to load
    window.addEventListener('load', () => {
        addButton();
    });
})();