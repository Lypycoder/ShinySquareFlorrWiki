let petals = ["Air", "Amulet", "Ankh", "Antennae", "Basic", "Basil", "Battery", "Bone", "Bubble", 
    "Bulb", "Bur", "Cactus", "Card", "Carrot", "Chip", "Claw", "Clover", "Coin", "Compass", "Corn", "Cotton", 
    "Cutter", "Dahlia", "Dandelion", "Dice", "Disc", "Ant_Egg", "Beetle_Egg", "Fangs", "Faster", "Grapes", 
    "Glass", "Heavy", "Honey", "Iris", "Jelly", "Leaf", "Light", "Lightning", "Lotus", "Magnet", "Mark", "Missile", 
    "Moon", "Orange", "Pearl", "Peas", "Pincer", "Plank", "Pollen", "Poo", "Powder", "Privet", "Relic", "Rice", "Rock", 
    "Root", "Rose", "Rubber", "Salt", "Sand", "Shell", "Shovel", "Soil", "Sponge", "Square", "Starfish", "Stick", "Stinger", 
    "Blood_Stinger", "Talisman", "Third_Eye", "Tomato", "Uranium", "Web", "Wing", "Yggdrasil", "Yin_Yang", "Yucca"];
function petal_change(petal) {
var petal_pg = document.getElementById(petal)
petal_pg.style.display = "block";
array.forEach(peta => {
    let lpetal = peta.toLowerCase();
    if (lpetal == petal) {
        petal_pg.style.display = "block";
    } else {
        var lpetalid = document.getElementById(lpetal);
        lpetalid.style.display = "none";
    }
});
}
