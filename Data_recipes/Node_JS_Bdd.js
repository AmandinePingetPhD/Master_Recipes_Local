//// Node JS file for JSON BDD Recipes

const fs = require('fs')
let fichier = fs.readFileSync('recipes_raw_result.json')
let recipes = JSON.parse(fichier)
console.log(recipes)