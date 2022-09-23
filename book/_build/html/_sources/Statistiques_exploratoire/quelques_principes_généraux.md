# Quelques principes généraux

## Principes de la statistique

Les étapes d'une analyse statistique peuvent être les suivantes:
1. **question** sur une **population**;
1. création d'une **expérience** visant à collecter un **échantillon utile** de la population;
1. analyse des données: graphique ou qualitative puis statistique (formelle).

La statistique est une science **argumentative**: elle donne une réponse rationnelle aux questions qu'on pose, en se basant sur certaines hypothèses.

## Les dangers de l'échantillonnage

Le raisonnement statistique consiste à extrapoler les propriétés de l'échantillon à l'ensemble de la population.
    
Il est souvent sous-entendu qu'un échantillon représentatif doit être une « version miniature » de la population; c'est parfois désirable, mais pas nécessairement indispensable. Il faut que le lien entre l'échantillon et la population soit connu. 
    
Il faut aussi se demander quelles données sont nécessaires pour répondre à la question et comment nous devons collecter ces données.

````{prf:example}
:label: ex1_principes_generaux
1. Alice veut savoir la préférence entre chocolat et citron pour toute l'EPFL. Elle a demandé à ses amis. Est-ce un bon échantillon?
1. Alice veut savoir si une votation va être acceptée. Elle connaît l'avis de ses amis. Est-ce un bon échantillon?
1. Est-ce que la classe est un échantillon représentatif de la population suisse?
1. Dans un sondage, les sondés peuvent **mentir**, notamment pour des questions sensibles. 
Il faut donc créer une bonne expérience, qui mesure **la bonne variable sur un bon échantillon**. Sinon, toute l'analyse sera faussée par ces erreurs initiales.

```{dropdown} Les échantillons sont-ils représentatifs?
- Les amis d'Alice n'ont sans doute pas été choisis sur leur préférences pour le chocolat ou le citron. Cet échantillon est loin d'être parfait, mais est passable.
- Les amis d'Alice ont très probablement des opinions politiques similaires aux siennes. Cet échantillon est très probablement biaisé.
- La classe est composé de gens jeunes, dans l'enseignement supérieur, déséquilibré entre les deux sexes, etc. C'est un échantillon très biaisé.
```
````

En général, la seule manière d'obtenir des résultats objectifs (ne dépendant pas d'hypothèses supplémentaires) est de tirer **aléatoirement** l'échantillon. Cela pose certains problèmes.
- Il faut avoir une liste exhaustive de la population d'intérêt. Dans de nombreux cas, cela est problématique.
- Parfois, cela pose des problème éthiques. Dans le cas d'une opération orthopédique pour traiter une affection de la hanche, il faudrait avoir un groupe de contrôle (qu'on n'opère pas) et un groupe test et que chacun ignore leur véritable statut. 
Lorsque c'est impossible, on essaie de tirer un échantillon qui a les même caractéristiques connues que la population (échantillonnage par quota). De manière générale: il vaut mieux un petit échantillon représentatif qu'un gros échantillon peu représentatif. Quelques exemples célèbres de mauvais échantillonnages:
- la réélection de Franklin D. Roosevelt en 1936 (échantillon de 2.2 millions de lecteurs du *Literary Digest* vs échantillon par quota de 50000 personnes pour George Gallup). 
- votation sur les minarets (2009);
- élection de D. Trump;
- Brexit.
Parfois, il faut savoir renoncer à faire des prédictions...

## Quantification de l'incertitude

Une estimation (ou prédiction) seule n'a en général pas de valeur. Il est nécessaire qu'elle soit accompagnée d'une **mesure de l'incertitude**. En général, une mesure de dispersion: 
- une variance;
- un intervalle de confiance;
- une majoration de l'incertitude (inégalité de concentration).

Ces concepts sont essentiels à la validité scientifique de toute affirmation. Ils sont aussi nécessaires
à la bonne communication de résultats.
