# Tutoriel sur la bibliothèque scikit-learn

Introduction aux outils de machine-learning

## Session 1: Prise en main des modèles 

1. Les différents modèles de références, apprentissage, inférence
2. Introspection légère des modèles
3. Les approches ensemblistes
 
## Session 2: Evaluation(s) et sélection(s)

1. Métriques d'évaluation
    * taux de bonne classification, précision, rappel, f1... Mais aussi ROC
    * validation croisée
2. Sélection de modèles, sélection de caractéristiques
    * procédure à la main
    * grid search

## Session 3: Chaine de traitement

1. Pré-traitement des données
    * données catrégorielles
    * données manquante
2. Construction d'une chaine
    * nature des données d'entrée (en apprentissage puis en inférence)
3. Optimisation de l'ensemble de la chaine
    * retour sur le Grid-search

# Evaluation de l'UE Prog

Le module de programmation sera évalué sous la forme de projet:
* A réaliser en monome ou en binome
* Rendre en Janvier (date à préciser)
    * Une partie du travail est possible dès maintenant
* Basé sur au moins 3 jeux de données permettant de mettre en avant:
    * Différentes tâches supervisées: classification, régression
    * Optimisation des performances (sélection de modèles, de caractéristiques, optimisation des pré-traitement)
        * Présentation des performances de référence par rapport aux performances optimisées
    * Modèles scikit-learn + approches deep-learning
    * Les sources de données sont:
        * kaggle
        * UCI
        * toute autre sources ou API est également valable
        * <p style="color:magenta"> Valider l'intérêt des données et de la tâche avec moi avant de vous lancer</p>

* Présentation et consigens détaillées pour les notebooks à rendre
    * 1 notebook par jeu de données
    * Si vous avez des fonctions partagées entre notebooks, merci d'utiliser des modules
    * Il est tout à fait possible (et souhaitable) de bien présenter les résultats dans le notebook (diagramme bar, tableaux, etc...)
    * Ces résultats **doivent** être accompagnés d'analyses (succinctes mais pertinentes). Ces analyses seront présentées dans des boites distinctives:
    
    ```
    > <span style="color:magenta"> Nous nous attendions à ce que le modèle 1 soit meilleur que le 2 car... </span>
    ```

    > <span style="color:magenta"> Nous nous attendions à ce que le modèle 1 soit meilleur que le 2 car... </span>

