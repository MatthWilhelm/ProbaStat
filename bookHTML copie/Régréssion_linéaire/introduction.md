# Introduction

La **régression** concerne la dépendance d'une variable sur d'autres variables.  
Variables et notations:
- $y$ : la variable d'interêt, appelée la **variable de réponse**, et on la considère comme variable 
aléatoire;
- $x_1,\ldots, x_n$: les autres variables, les **covariables** (variables explicatives), on les considère comme fixes (non aléatoires).

On s'intéresse entre autres à :
- l'**estimation** d'une relation éventuelle entre $y$ et les $x_j$;
- la **prédiction** des valeurs futures de $y$ sachant les $x_j$ correspondantes.

````{prf:example} Réaction chimique
Prof. Christophe Holliger (SIE): on essaye de d\'eterminer les paramètres cinétiques d'une « reductive dehalogenase dechlorinating tetrachloroethene (PCE) ».  Ceci dépend de la concentration du substrat, et la vitesse de la réaction peut être exprimée par l'équation de Michaelis--Menten
\begin{gather*}
y = \dfrac{ \gamma_0 x}{ \gamma_1 + x},
\end{gather*}
où $x$ est la concentration de PCE, $\gamma_0$ est la vitesse maximale, et $\gamma_1$ est la concentration quand $y=\gamma_0/2$. Comment estimer $\gamma_0$ et $\gamma_1$?
```{figure} PDFSVG/PCE_Data.svg
---
name: PCE_Data
width: 95%
---
```
````

````{prf:example} Ozone atmosphérique
Prof. Isabelle Bey (SIE): observations de la concentration de l'ozone au Jungfraujoch,
de janvier 1987 à décembre 2005 (qqs valeurs manquantes), et résultats d'une 
modélisation.
Soit $y$ les données réelles et $x$ les résultats du modèle.
```{figure} PDFSVG/Ozone_Data.svg
---
name: Ozone_Data
width: 95%
---
```

```{figure} PDFSVG/Ozone_obs_vs_model.svg
---
name: Ozone_obs_vs_model
width: 95%
---
```

```{figure} PDFSVG/Jura_Data_Ni_vs_Co.svg
---
name: Jura_Data_Ni_vs_Co
width: 95%
---
```
````

- On dispose d'un ensemble de points
\begin{gather*}
\left(\begin{array}{c}x_1\\ y_1\end{array}\right),\ldots, \left(\begin{array}{c}x_n\\ y_n\end{array}\right)
\end{gather*}
qu'on peut représenter par un "scatterplot" comme ceux d'auparavant.
- Si il y a une **relation linéaire**, on peut utiliser la corrélation pour mesurer la dépendance linéaire entre les variables.
- D'une manière générale, le **problème d'ajustement**
consiste à trouver une courbe $y=\mu(x)$ qui résume « le mieux
possible »  le nuage de points. La fonction $\mu(x)$ dépend de
paramètres qu'il faut estimer. **Comment**?

## Moindres carrés

Les écarts verticaux entre les données $y_j$ et la courbe $\mu(x_j)$ sont 
\begin{gather*}
y_j-\mu(x_j),\quad j=1,\ldots, n.
\end{gather*}
- On cherche les paramètres de la fonction $\mu(x)$ telle que la **somme des carrés** des écarts
verticaux 
\begin{gather*}
\sum^n_{j=1}[y_j - \mu(x_j)]^2
\end{gather*}
soit minimale.
- L'ajustement est dit **linéaire** si $\mu(x) = \alpha + \beta x$. Dans ce cas, il faut minimiser
\begin{gather*}
{\rm SC}(\alpha,\beta) = \sum^n_{j=1}[y_j-\mu(x_j)]^2 = \sum^n_{j=1}[y_j - (\alpha + \beta x_j)]^2.
\end{gather*}

En fait, en minimisant la somme des carrés, on minimise **une distance** entre les $y_j$ et $\mu(x_j)$. Les ingrédients minimaux nécessaires sont
- une forme paramétrique pour $\mu(x_j)$: par exemple une droite, un polynôme ou autre;
- une métrique pour mesurer la distance entre $y_j$ et $\mu(x_j).$

Dans la pratique, on utilise le carré de la différence, mais bien d'autres distances peuvent être utilisées, avec d'autres propriétés.

```{figure} PDFSVG/residuals.svg
---
name: residuals
width: 95%
---
: illustration des résidus \& Shiny app
```

```{prf:theorem} Estimateur des moindres carrés
Soient $(x_1,y_1),\ldots, (x_n,y_n)$ issues d'un rélation $y=\alpha+ \beta x$ et telles que au moins deux des $x_j$ soient différents.  Alors les **estimateurs de moindres carrés** de $\alpha$ et $\beta$ sont 
\begin{gather*}
\hat\alpha = \overline y - \hat\beta\overline x, \quad \hat\beta = \dfrac{\sum^n_{j=1}(x_j-\overline x)y_j}{ \sum^n_{i=1}(x_j-\overline x)^2}.
\end{gather*}
```

```{prf:definition} Droite des moindres carrés et résidus
La droite $\hat\alpha + \hat\beta x$ s'appelle la **droite des moindres carrés**, la **valeur ajustée** qui correspond à $(x_j,y_j)$ est $\hat y_j= \hat\alpha + \hat \beta x_j$, et la différence 
\begin{gather*}
r_j = y_j-\hat y_j = y_j-(\hat\alpha + \hat\beta x_j)
\end{gather*}
 s'appelle un **résidu**.
```

````{prf:example} Ozone atmosphérique
- Il y a $n=207$ paires (observation, modèle) = $(y_j,x_j)$, et 21 valeurs de $x$ sans valeur observée
- A partir des $n$ paires complètes on trouve la droite des moindres carrés
\begin{gather*}
\hat y = \hat\alpha +\hat\beta x = -5.511 + 1.069 x.
\end{gather*}
- Pour une paire (observation, modèle) = (?, $x_+)$, on peut remplacer la valeur manquante par la valeur ajustée correspondante: 
\begin{gather*}
\hat y_+ = \hat\alpha + \hat\beta x_+.
\end{gather*}
```{figure} PDFSVG/Ozone_obs_vs_model_with_pred.svg
---
name: Ozone_obs_vs_model_with_pred
width: 95%
---
La ligne rouge montre la meilleure estimation d'une relation linéaire entre $y$ et $x$. Les points bleus correspondent aux valeurs observées manquantes prédites par la droite de régression.
```
````
