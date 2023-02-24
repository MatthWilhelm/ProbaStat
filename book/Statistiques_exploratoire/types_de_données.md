# Types de données

Nous allons définir un certain nombre de concepts et de termes reliés à l'analyse de données. Cela nous donnera un premier aperçu de la notion d'aléa. En particulier, on abordera les concepts clés suivants:
- population, échantillon, individu, variable;
- catégories de variables: qualitatives (ordinales/nominales), quantitatives (discrètes/continues).
    
## Population et échantillon

````{prf:definition}
:label: population_echantillon
En statistique, une **population** est l'ensemble sur lequel porte une étude statistique. Un **échantillon** est un sous-ensemble (en général connu) de la population.
````  

Typiquement, on va récolter des données sur un certain nombre **d'individus** de la **population**. On va ensuite analyser **l'échantillon** des individus dont on a obtenu les données.  

On veut étudier une (ou plusieurs) caractéristique que possède chaque individu, une **variable statistique**. Par exemple, le poids de chaque individu dans la population.

````{prf:example}
:label: exemple_population_echantillon
Alice (en section chimie) veut organiser une vente de gâteaux à l'EPFL. Elle voudrait savoir si elle doit plutôt préparer des gâteaux au chocolat ou au citron. Pour cela, elle demande à dix amis en chimie s'ils préfèrent le chocolat ou le citron.
- **population**: les étudiants et employés de l'EPFL;
- **échantillon**: les amis d'Alice
- **individu**: un(e) ami(e) d'Alice
- **variable / donnée**: préférence entre chocolat et citron
````

## Types de variables

On différencie deux types de variables:
- Les variables **qualitatives** qui expriment une caractéristique:
    * **ordinales** (= hiérarchie): « un peu, beaucoup, passionément, à la folie »;
    * **nominales**: « femme, homme »;  
   
- Les variables **quantitatives** qui ont une valeur numérique:
    * **discrètes**: seulement certaines valeurs sont possibles (souvent entières)
    * **continues**: n'importe quelle valeur est possible dans un intervalle.

````{prf:example}
:label: exemple_types_données
Pour les exemples suivants, pensez-vous que ce sont des variables **qualitatives** ou **quantitatives discrètes** ou **quantitatives continues**.  
- vote pendant une élection;
- poids;
- lancer d'un dé;
- quantité de chocolat consommé en une année;
- être gaucher ou droitier;

```{warning}
Il faut souvent considérer ces questions de près, et on peut être surpris.
```

```{admonition} Solution
:class: tip, dropdown
- vote pendant une élection: **qualitatif**
- poids: **quantitatif continu**
- lancer d'un dé: **quantitatif discret**
- quantité de chocolat consommé en une année: **quantitatif continu**
- être gaucher ou droitier: A première vue, **qualitatif** mais on pourrait aussi quantifier le degré de préférence pour la main droite entre $-1$ et $+1$ ce qui rendrait cette variable **quantitative continue**.
```
````
