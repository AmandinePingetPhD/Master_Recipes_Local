/// Master Cook - IA de suggestion de recettes - Modif BDD JSON ///
// Javascript Node Js
// Coding Utf-8

/*
Node JS file for JSON BDD Recipes
@author : Amandine Pinget, PhD
*/

class recipes {
    constructor(title, ingredients, instructions, t_recipe, RecipeId) {
        this.title = title;
        this.ingredients = ingredients;
        this.instructions = instructions;
        this.t_recipe = t_recipe;
        this.RecipeId = RecipeId;
        }
}

//Import de la BDD
const fs = require('fs')
let fichier = fs.readFileSync('recipes_raw_result.json')
let recipes = JSON.parse(fichier)

//Affichage
console.log(recipes)

//Tests et classification
switch (recipes.title)
{
    case "Doggie":
    case "Doggy":
    case "Dog Treats":
    case "Dog Biscuits":
    case "Dog Food":
    case "Good Dog":
        console.log('Dog recipe', recipes.RecipeId);
        break;
}

//Modifications / Ajouts 
// let donnees = JSON.stringify(personne)

fs.writeFile('recipe_new.json', donnees, function(erreur) {
    if (erreur) {
        console.log(erreur)}
})
// fs.appendFile

// fs.writeFileSync('personnage2.json', donnees)
// readFileSync : pour obtenir le contenu, puis écrire en ajoutant d’abord l’ancien contenu.
// Ou vous pouvez utiliser la fonction appendFile()
