
# Graphiques

Nous allons présenter comment résumer un jeu de données sous la forme d'un graphique. Un bon graphique permet de <font color="red">présenter efficacement un jeu de données</font>.

Concepts clés:
- histogramme, « boîte à moustaches » (boxplots) et famille;
- notation $ x_{(i)} $ pour variables ordonnées;
- principes d'une bonne représentation graphique.

## Étude d'une variable quantitative

````{prf:example}
:label: example1_etude_quantitative

Le CHUV veut connaitre la fréquence des différents
groupes sanguins en Suisse, pour prévoir des stocks appropriés.
Pour cela, on a mesuré le groupe sanguin de 25 donneurs.

```{figure} latex/PDFSVG/tab1_graphiques.svg
---
name: tab1_graphiques
width: 75%
---
```
**Diagramme en camembert (Pie chart)**:
```{figure} PDFSVG/pie_chart.svg
---
name: pie_chart
width: 65%
---
```

```{warning}
**À éviter**: les comparaisons visuelles sont difficiles. Pas adapté quand les catégories sont déséquilibrées.
```  

**Diagrammes en barres**:
```{figure} PDFSVG/bar_plot.svg
---
name: bar_plot
width: 65%
---
: La hauteur de chaque colonne correspond à la proportion dans l'échantillon du groupe sanguin.
```
````

````{prf:example}
:label: example2_etude_quantitative

Le poids de 92 étudiants d'une école américaine a été
    relevé dans une unité anglaise particulière, le pound.  
    
Les données observées figurent dans le tableau suivant: 
```{figure} latex/PDFSVG/tab2_graphiques.svg
---
name: tab2_graphiques
width: 95%
---
```

On peut transformer une variable continue en variable discrète.
    
On choisit une division en intervalles, et on compte le nombre d'observations correspondant à chaque intervalle. On obtient alors une **table de fréquences**:

```{figure} latex/PDFSVG/tab3_graphiques.svg
---
name: tab3_graphiques
width: 95%
---
```

**Histogramme**:
```{figure} PDFSVG/histogrammes.svg
---
name: histogrammes
width: 75%
---
```
On peut varier le nombre d'intervalles afin de changer le niveau de précision de l'histogramme.
````

Pour certaines données, il est parfois intéressant de les **transformer** avant de les représenter.

```{figure} PDFSVG/Pop_mondiale.svg
---
name: Pop_mondiale_
width: 95%
---
: Population mondiale entre l'an 0 et 2000. L'échelle logarithmique permet de visualiser clairement le taux de croissance. La population en 1200 était de 360 millions. Celle en 1600 de 545 millions.
```

```{admonition} Faire de bon graphes
:class: tip

- toujours avoir un **titre** pour la figure ainsi que des titres et des échelles pour les axes;
- toujours avoir une **description** du graphe;
- choisir des unités claires et intuitives;
- adapter l'échelle au type de graphe. Parfois une **transformation** est nécessaire; certaines **valeurs** ont une **signification particulière** (extrema, etc) et peuvent être mises en évidences.
- Si on a plusieurs graphes similaires, ils doivent avoir **la même échelle** afin de faciliter la comparaison.
- Minimiser les fioritures: on communique de l'information.
```

