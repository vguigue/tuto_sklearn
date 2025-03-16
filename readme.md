# Tutoriel sur la bibliothèque scikit-learn

Introduction aux outils de machine-learning

## Session 1: Prise en main des modèles 

1. Les différents modèles de références, apprentissage, inférence
2. Introspection légère des modèles
3. Les approches ensemblistes
 
## Session 2: Evaluation(s) et sélection(s)

1. Métriques d'évaluation
    * taux de bonne classification, précision, rappel, f1... Mais aussi ROC
2. Validation croisée
    * Différents usage 

## Session 3: Sélection de modèle, sélection de caractéristiques

1. Sélection de modèles
    * procédure à la main
    * grid-search
2. Sélection de caratctéristiques


## Session 3: Chaine de traitement

1. Pré-traitement des données
    * données catrégorielles
    * données manquante
2. Construction d'une chaine
    * nature des données d'entrée (en apprentissage puis en inférence)
3. Optimisation de l'ensemble de la chaine
    * retour sur le Grid-search
    * Optuna

## Session 4: Visualisation de données

1. Rappels sur l'ACP
2. Projections linéaires
3. Projections non linéaires
4. Interface interactive

# Evaluation de l'UE : le machine learning en pratique

Le module de programmation sera évalué sous la forme de projet:
* A réaliser en monome ou en binome
* Rendre le 31 mars 2025
* Basé sur au moins 2 jeux de données permettant de mettre en avant:
    * Différentes tâches supervisées: classification, régression *(Idéalement 1 problème de chaque, mais ce n'est pas obligé. Si vos données sont très différentes, vous pouvez traiter deux problèmes de classification ou de régression)*
    * Optimisation des performances (sélection de modèles, de caractéristiques, optimisation des pré-traitement)
        * Présentation des performances de référence par rapport aux performances optimisées
        * Courbe de performances par rapport aux réglages: montrer que vous savez choisir les bonnes approches et les régler
    * Illustrer + analyser vos résultats comme pour les expliquer à un expert métier *Phrases explicatives, choix des métriques, illustration d'ensemble etc...*
    * Les sources de données sont:
        * [Kaggle](https://www.kaggle.com)
        * [UCI](https://archive.ics.uci.edu/datasets)
        * [UCR (pour les séries temporelles simples)](https://www.cs.ucr.edu/~eamonn/time_series_data/)
        * [Data gouv](https://www.data.gouv.fr/fr/)
        * toute autre sources ou API est également valable
        * 🟥 Valider l'intérêt des données et de la tâche avec moi avant de vous lancer 🟥

* Présentation et consigens détaillées pour les notebooks à rendre
    * 1 notebook par jeu de données
    * Si vous avez des fonctions partagées entre notebooks, merci d'utiliser des modules
    * Il est tout à fait possible (et souhaitable) de bien présenter les résultats dans le notebook (diagramme bar, tableaux, etc...)
    * Ces résultats **doivent** être accompagnés d'analyses (succinctes mais pertinentes). Ces analyses seront présentées dans des boites distinctives pour que je ne puisse pas manquer vos commentaires:
    
    ```
    <span style="color:magenta"> Nous nous attendions à ce que le modèle 1 soit meilleur que le 2 car... </span>
    ```
    * Voua ajouterez une boite à la fin du notebook présentant une courte prise de recul par rapport aux expériencesen abordant par exemple:
        - les principales difficultés rencontrées
        - l'apport du machine learning (aurait-on pu faire les mêmes analyses à la main?)
        - des idées d'applications connexes à valeur économique, sociale ou solidaire qui seraient envisageables avec les mêmes techniques
        - ...
