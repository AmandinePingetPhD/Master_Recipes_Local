//// Node JS file for JSON BDD Recipes

//Import de la BDD
const fs = require('fs')
let fichier = fs.readFileSync('recipes_raw_result.json')
let recipes = JSON.parse(fichier)

//Affichage
console.log(recipes)

//Modifications / Ajouts 
let donnees = JSON.stringify(personne)

// fs.appendFile

// fs.writeFileSync('personnage2.json', donnees)
// readFileSync : pour obtenir le contenu, puis écrire en ajoutant d’abord l’ancien contenu.
// Ou vous pouvez utiliser la fonction appendFile()
