/// Master Cook - IA de suggestion de recettes - Modif BDD JSON ///
// Javascript Node Js
// Coding Utf-8

/*
Node JS file for JSON BDD Recipes
@author : Amandine Pinget, PhD
*/

//Import de la BDD
const fs = require('fs')
let fichier = fs.readFileSync('recipes_raw_result.json')
let recipes = JSON.parse(fichier)

//Affichage
console.log(recipes)

//Modifications / Ajouts 
let donnees = JSON.stringify(personne)

fs.writeFile('personne2.json', donnees, function(erreur) {
    if (erreur) {
        console.log(erreur)}
})
// fs.appendFile

// fs.writeFileSync('personnage2.json', donnees)
// readFileSync : pour obtenir le contenu, puis écrire en ajoutant d’abord l’ancien contenu.
// Ou vous pouvez utiliser la fonction appendFile()
