---
header-includes:
  - \usepackage{color}
output:
  pdf_document:
    keep_tex: true
---

# Introduction

## Statistiques: une définition ?

Les mathématiques (du grec *Mathema* $\approx$ apprendre) sont une manière:

- d'exprimer une grande variété de notions complexes avec précision et cohérence.
- de « *légitimer les conquêtes de notre intuition* » (Jacques Hadamard)
        [^citationHadamard]
        : raisonner rigoureusement à partir d'hypothèses, tirer les conclusions correctes d'une observation, d'une expérience, etc.

[^citationHadamard]: La citation exacte est [« La rigueur n’a d’autre objet que de sanctionner et de légitimer les conquêtes de l’intuition »](http://idm-old.math.cnrs.fr/Jacques-Hadamard-passeur.html).

La statistique souffre d'un problème de nomenclature. On a deux « statistiques » (définitions [TLF](http://stella.atilf.fr/Dendien/scripts/tlfiv5/visusel.exe?12;s=467953305;r=1;nat=;sol=1;)):
- « Recueil de données numériques concernant des faits économiques et sociaux »; par exemple des données démographiques (répartition en âge, métiers, etc. de la population), ou économiques (taux de chômage, salaire médian, etc.).  
    «L'ensemble des connaissances que doit posséder un homme d'État », introduit en allemand *Statistik* par l'économiste G. Achenwall (1719-1772) (de l'italien *statista*, homme d'\'Etat).
- « Branche des mathématiques ayant pour objet l'analyse et l'interprétation de données quantifiables.»



<p style="text-align:center">
    <font color="red">Utiliser les maths</font> <br> pour <br> <font color="red">extraire des informations</font> <br> à partir de <br> <font color="red">données</font> <br> en présence <br> <font color="red">d'incertitudes</font> <br>
</p>

Les données sont absolument partout de nos jours.
- OFS: démographie, chômage $\rightarrow$ décisions politiques;
- science: expérience $\rightarrow$ données $\rightarrow$ conclusion;
- utilisation d'internet: « cookies » $\rightarrow$ publicités ciblées.

## Et les probabilités ?

Les probabilités nous aident à appréhender **l'incertitude**; elles permettent de la transcrire en un formalisme mathématique.
- C'est la discipline qui étudie les phénomènes aléatoires (ou *stochastiques*).
- C'est la base indispensable à toute étude mathématiquement rigoureuse de ces phénomènes.

Les probabilités nous donnent **le formalisme** dans lequel on peut comprendre et quantifier l'effet que la présence d'incertitude dans les données a sur notre analyse de ces données.

## Le but de la statistique

L'expérience montre que de nombreuses expériences sont *intrinsèquement* aléatoire: jet de dé, un tirage au sort, une campagne de vaccination.  
D'autres ne le sont peut-être pas intrinsèquement, mais il s'avère impossible de les reproduire exactement: tir au panier, mesure physique etc. Ainsi, *le hasard est une composante essentielle de bien des expériences*.  
La plupart du temps, le but de la statistique est de **comprendre ce hasard**.  

On peut identifier quatres étapes majeures de la démarche statistique:
- planification de l'expérience; (développement théorique du problème, élaboration du plan expérimental);
- collecte des données;
- **analyse des données**;
- présentation des résultats et conclusions / actions;


Ce cours se concentre sur **l'analyse des données**. 
Je conseille fortement la référence [suivante](https://swisscovery.slsp.ch/permalink/41SLSP_NETWORK/1ufb5t2/alma991170199983205501): Cox, D. R.  and Donnelly, C. A. (2011) *Principles of applied statistics*, Cambridge, UK: Cambridge University Press.

- **L'analyse exploratoire des données**: consiste en l'utilisation de méthodes simples, intuitives, essentiellement graphiques. Son objectif est l'identification informelle de la structure d'un jeu de données (tendances, formes, observation atypiques). Elle permet donc de se familiariser avec les données.

L'analyse exploratoire suggère des hypothèses de travail et des modèles, qui sont formalisés et vérifiés dans le second pôle: 
- **L'analyse confirmatoire des données**: elle conduit à des conclusions statistiques à partir de données en utilisant des notions de la théorie des probabilités. Cette partie plus formelle concerne notamment des méthodes de test, d'estimation et de prévision.  

On distingue en général deux grands types d'études: expérimentales et observationnelles. La démarche est fondamentalement différente, ainsi que les conclusions que l'on peut en tirer.  

```{figure} table.svg
---
name: directive-fi
width: 95%
---
```
## Les statistiques dans le monde moderne

Les statistiques sont très présentes autour de nous.
- En science, la statistique est l'outil clé pour obtenir des conclusions scientifiques rigoureuses.
- En politique, les décisions sont basées sur les statistiques qui donnent un aperçu d'une certaine situation.
- Plus généralement, les statistiques sont utilisés pour <font color="red">comprendre l'état présent</font> d'un système ou <font color="red">anticiper son état futur</font>. Par exemple, à l'aide d'un sondage, on peut évaluer l'état de l'opinion publique à un moment donné, et anticiper le résultat d'une élection.

## Structure du cours

Ce cours a pour objectifs formels:
    - d'introduire les bases de la théorie des probabilités;
    - d'introduire les bases de la théorie statistiques.
    
Ce cours est **très, très loin d'être exhaustif** et constitue un aperçu de ce domaine.
Le <font color="red">fil rouge</font> de ce cours consiste à comprendre des données dans différentes situations.
- Statistitique exploratoire: comprendre <font color="red">visuellement</font> des données;
- Probabilités: construire un cadre théorique pour comprendre des données au-delà du visuel. Se constituer une <font color="red">boîte à outils</font>.
- Statistique inférentielle: 
    * Comprendre des données à partir d'un modèle: <font color="red">estimation</font> d'un modèle;
    * Comprendre des données et les confronter à une théorie: <font color="red">tests d'hypothèses</font>;
    * Comprendre des données à l'aide d'autres données: <font color="red">régression</font>. 

Le cours sera divisé en quatre chapitres:
1. **Statistique exploratoire** ($\leq $ 2 semaines) - types de données, étude graphique des variables, synthèses numériques de la distribution, loi normale.
1. **Calcul des probabilités** ($\sim$ 6 semaines) - probabilités d'évènements, variables aléatoires, valeurs caractéristiques, théorèmes fondamentaux.
1. **Idées fondamentales de la statistique** ($\sim$ 4 semaines) - modèles statistiques, estimation de paramètres, estimation par intervalles, tests statistiques, test $\chi^2$ (prononcer khi-carré).
1. **Régression linéaire** ($\sim$ 3 semaines) - introduction, principe des moindres carrés, régression linéaire simple et multiple.

````{admonition} Remarque
* Si vous avez déjà fait de la probabilité, la section probabilité pourrait être redondante avec vos cours précédents. Elle est nécessaire pour les  étudiants qui n'ont pas encore vu ce domaine des mathématiques.
* Ne faites pas l'impasse sur la probabilité. On ne peut pas comprendre la statistique sans comprendre la probabilité.        
* La probabilité et la statistique présentent camparativement peu de difficultés mathématiques (calculs difficiles, etc.) mais des difficultés conceptuelles.
````
