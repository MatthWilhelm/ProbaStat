# Boxplot

Le **boxplot** (ou boîte à moustache pour les puristes) est un type de représentation graphique particulier, très apprécié des statisticiens. Il permet:
- la visualisation de l'asymétrie;
- la comparaison facile de jeux de données;
- la visualisation de valeurs aberrantes.

Les cinq valeurs suivantes donnent un bonne description d'une variable: 
\begin{equation*}
    \text{minimum, $\hat{q}(25\%)$, médiane, $\hat{q}(75\%)$, maximum}.
\end{equation*} 
 
 Cette liste est à la base de la **boîte à moustaches**.

```{figure} PDFSVG/Boxplot_weight.svg
---
name: Boxplot_weight
width: 95%
---
Boxplot du poids des étudiants américains.
```

## Calculs d'une boîte à moustaches

Les bords du rectangle sont donnés par les quartiles. On indique la médiane par une ligne qui sépare la boîte.
Pour les moustaches, on calcule 1.5 fois l'étendue interquartile:
\begin{gather*} C = 1.5 \cdot \text{EIQ} = 1.5 \cdot \big[ \hat{q}(75\%) - \hat{q}(25\%) \big] \end{gather*}
Puis on calcule $ \hat{q}(25\%) - C $ et $ \hat{q}(75\%) + C $.
Typiquement, toutes les valeurs de la variables sont entre ces seuils.

- **Si oui**, on met les limites des moustaches au **minimum** et **maximum**.
- Sinon, on mets les moustaches aux valeurs observées les plus proches des seuils **contenues dans les moustaches** et  on représente **les valeurs exceptionnelles par des points**.
Cela donne, en pratique:
```{figure} latex/PDFSVG/Boxplot_example.svg
---
name: Boxplot_example
width: 95%
---
```

::::{grid}
:gutter: 2

:::{grid-item-card} 
M: Médiane 
:::

:::{grid-item-card} 
$\text{Q}_{.25}$: quantile à 25\%
:::
::::

::::{grid}
:gutter: 2

:::{grid-item-card} 
EIQ:  écart inter-quartile
:::

:::{grid-item-card} 
$\text{Q}_{.25}$: quantile à 75\%
:::
::::

## Comparaison de jeux de données

Les boxplots sont particulièrement utiles pour la comparaison de plusieurs groupes.

```{figure} PDFSVG/Boxplot_weight_gender.svg
---
name: Boxplot_weight_gender
width: 95%
---
Comparaison du boxplot des poids des étudiants hommes et femmes.
```

```{figure} PDFSVG/Boxplots_asymetric.svg
---
name: Boxplots_asymetric
width: 95%
---
Comparaison de boxplot pour des jeux de données symétriques et asymétriques.
```
Pr. Isabelle Bey (SIE - EPFL) a mesuré la concentration d'ozone au Jungfraujoch (noir), et a proposé une modélisation (rouge).

```{figure} PDFSVG/Ozone_Data.svg
---
name: Ozone_Data
width: 95%
---
Ozone au Jungfraujoch entre 1987 et 2005.
```
En comparant les boxplots, on voit que le modèle ne genère pas assez d'observations extrêmes.
```{figure} PDFSVG/Ozone_Boxplot.svg
--- 
name: Ozone_Boxplot
width: 95%
---
Comparaison des boxplots des vraies données et du modèle de l'ozone au Jungfraujoch.
```

```{admonition} Analyse initiale des données
:class: important
La procédure suivante est une bonne manière d'analyser une variable quantitative:
- **représenter graphiquement** les données;
- étudier la **structure** des données: y a-t-il des valeurs extrêmes? Si oui, pourquoi? Doivent-elles être conservées ou exclues?
- Calculer les **synthèses numériques** pour décrire les données;
- éventuellement proposer un **modèle** des données.
**Un modèle est une manière de résumer et de traduire en des termes probabilistes le processus qui a engendré les données.**
