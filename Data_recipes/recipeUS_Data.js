class recipeUS {
    constructor(title, ingredients, instructions, t_recipe, RecipeId) {
        this.title = title;
        this.ingredients = ingredients;
        this.instructions = instructions;
        this.t_recipe = t_recipe;
        this.RecipeId = RecipeId;
        }
}

/// Switch/Case peut être utile pour classif?
/// Modifier Bdd Json avec Javascript?
/// Ajout du nombre d'ingrédients nécessaires pour la recette pour une recherche avancée? ingrédients.length ?
/// Mise en oeuvre d'une recherche avancée? par nombre d'ingrédients? par plusieurs ingrédients? 
/// Recette avancée par type de plats? à définir? dans t_recipe...
/// Faire une bdd avec les proportions d'ingrédients en grammes/ métric au lieu d'impérial
/// t_recipe à modifier avec le type de recette : Drink / Dish / Desert dans un premier temps puis affiner/détailler