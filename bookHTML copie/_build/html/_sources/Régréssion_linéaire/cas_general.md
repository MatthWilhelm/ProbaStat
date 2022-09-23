# Régréssion linéaire: cas général

```{math}
\newcommand\corr{\text{Corr}}
\newcommand\cov{\text{Cov}}
\newcommand\var{\text{Var}}
\newcommand\E{\mathbb{E}}
```

Jusqu'à présent, on a essentiellement chercher à trouver une droite qui passait relativement proche des données, c'est-à-dire qui minimisait l'erreur carrée.

Il s'agit d'un problème d'optimisation, il n'y a *a priori* pas de modèle probabiliste derrière. 

En fait, même si cela n'est pas évident, cela est complètement équivalent à un certain modèle probabiliste, le modèle Gaussien.

```{prf:definition} Distribution normale multivarié
On dit que $\mathbf{X}\in \mathbb{R}^n$ suit une loi normale multivariée d'espérance $\boldsymbol{\mu}\in\mathbb{R}^n$ et de variance $\boldsymbol{\Sigma}\in \mathbb{R}^{n\times n}$ (où $\boldsymbol{\Sigma}$ est symétrique définie positive), notée $\mathbf{X} \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$ si la distribution de $\mathbf{X}$ s'écrit
\begin{gather*}f_{\mathbf{X}}(\mathbf{x}) = \left( 2\pi\right)^{-n/2} \det\left(\boldsymbol{\Sigma}\right)^{-1/2} \exp\left[-\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^\top \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu})\right].\end{gather*}
```

```{prf:remark}
- Si on considère $n$ réalisations indépendantes $X_1,\dots, X_n\stackrel{idd}{\sim} \mathcal{N}(\mu, \sigma^2)$, alors la loi jointe de $\mathbf{X} = (X_1,\dots, X_n)$ est une loi normale multivariée d'espérance $\boldsymbol{\mu} = \mu \mathbf{1}$ et de variance $\boldsymbol{\Sigma} = \sigma^2  \mathbf{I}_n$.
- De manière équivalente, on peut définir une loi normale multivariée comme une transformation affine d'une loi normale standard multivariée:
\begin{align*}
&\mathbf{X}\in \mathbb{R}^n \sim \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})\\
&  \Leftrightarrow \text{Il existe } \mathbf{Z}\in \mathbb{R}^k \sim\mathcal{N}(\mathbf{0}, \mathbf{I}_k),   \mathbf{A}\in \mathbb{R}^{n \times k}, \boldsymbol{\mu} \in \mathbb{R}^n \\
& \text{ tel que } \mathbf{X} = \mathbf{A}\mathbf{Z} + \boldsymbol{\mu}.
\end{align*}
```

```{prf:property} Matrice de variance-covariance
La matrice $\boldsymbol{\Sigma}$ satisfait les propriétés suivantes:
-  $\boldsymbol{\Sigma} = \mathbf{A}\mathbf{A}^\top$;
-  $\boldsymbol{\Sigma}_{ij} = \cov(X_i, X_j)$;
-  $\boldsymbol{\Sigma}_{ij} = 0 \Leftrightarrow X_i, X_j$ sont indépendantes (vrai **uniquement** si $X_i, X_j$ sont des VA Gaussiennes).
```

```{admonition} Loi normal multivariée
- Les courbes de niveau d'une loi normale multivariée sont des ellipsoïdes. Les axes principaux de l'ellipse correspondent aux vecteurs propres de la matrice de variance.
- Soient $X,Y$ variables aléatoires normales (potentiellement multivariée). Alors $X,Y$ sont indépendantes si et seulement si $\cov(X,Y) = 0$ (dans le cas multivarié, il s'agit d'une matrice). Dans ce cas, les axes des courbes de niveaux sont confondus avec les axes de l'ellipse. 
```

```{figure} PDFSVG/Normal_multi.svg
---
name:Normal_multi
width: 95%
---
Deux densités normales multivariées.
```

Dans le graphiques précédent, les axes principaux sont $(1,2)^\top$ et $(1,-2)^\top$ respectivement, mais ils correspondent à des valeurs propres différentes, d'où l'orientation différentes des courbes de niveaux.
L'espérance est l'origine dans les deux cas.

```{prf:definition} Modèle linéaire Gaussien
Soient $\mathbf{y} = (y_1,\dots, y_n)^\top$ et $\mathbf{X} \in \mathbb{R}^{n\times p}$. On appelle modèle linéaire (Gaussien) le modèle suivant:
\begin{equation*}
\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon},
\end{equation*}
où $\boldsymbol{\beta} \in \mathbb{R}^p$ est un vecteur de paramètres, $\boldsymbol{\varepsilon}\in \mathbb{R}^n \sim\mathcal{N}(\mathbf{0}, \sigma^2 \mathbf{I}_n)$ et $\sigma^2 >0$.

- $y$ est appelée la variable d'intérêt, variable de réponse ou variable observée.
- $(x_1, \dots, x_p)$ sont appelés covariables ou variables explicatives, qu'on observe pour chaque occurrence de la variable de réponse. Les covariables sont supposées déterministes. La matrice $\mathbf{X}$ qui contient toutes les covariables est appelée matrice d'expérience ou matrice de design.
- $\varepsilon$ est appelé l'erreur ou le bruit.
- $\boldsymbol{\beta}$ est appelé vecteur des coefficients de régression. 
```

````{prf:example} Constance d'élasticité
Supposons que l'on cherche à estimer la constante d'élasticité d'un ressort. On rappelle que la force exercée par un ressort est approximativement une équation linéaire:
\begin{gather*} F = - k \cdot x, \end{gather*}
où $F$ est la force, $x$ l'élongation et $k$ la constante d'élasticité. On observe les données suivantes:

```{figure} latex/PDFSVG/tab1_regr.svg
---
name: tab1_regr
width: 95%
---
```
```{figure} PDFSVG/ressort_data.svg
---
name: ressort_data
width: 95%
---
: Élongation de ressort [m], en fonction de la masse [kg]. 
```
En utilisant la notation introduite précédemment, on a:
- $(y_1, y_2, \dots, y_6)^\top = (0.0, 0.021, 0.037, 0.056, 0.066, 0.075)^\top$;
- La matrice d'expérience 
\begin{gather*} \mathbf{X} = \begin{pmatrix}
1 & 0.0\\
1 & 0.159 \\
1 & 0.243 \\
1 & 0.357 \\
1 & 0.413 \\
1 & 0.456 \\
\end{pmatrix};
\end{gather*}
- $\boldsymbol{\beta} = (\beta_0, \beta_1)^\top $, qui est à estimer, où $\beta_0$ est l'ordonnée à l'origine.

On a vu que dans l'exemple précédent, on a supposé que le modèle était, M1:
\begin{equation*} y_i = \beta_0 + x_i \beta_1 + \varepsilon_i. 
\end{equation*}
Cependant, l'équation physique décrivant le phénomène ne comprend pas d'ordonnée à l'origine. On pourrait donc plutôt estimer le modèle suivant, M2:
\begin{equation*} y_i = x_i \beta + \varepsilon_i. 
\end{equation*}  

On obtient les valeurs estimées suivantes:
- pour M1: $\beta_0 =-0.002, \beta_1 = 0.166$ (droite en rouge);
- pour M2: $\beta= 0.158$ (droite en noir).

```{figure} PDFSVG/ressort_data_model_fit.svg
---
name: ressort_data_model_fit
width: 95%
---
```
````

Si on suppose que nos observations sont engendrées par un modèle linéaire Gaussien, on a 
\begin{gather*}\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon},\end{gather*}
où $\boldsymbol{\varepsilon} \sim\mathcal{N}(\mathbf{0}, \sigma^2 \mathbf{I}_n)$. En utilisant les propriétés de la loi normale, on obtient:
\begin{gather*}\mathbf{y}  \sim\mathcal{N}(\mathbf{X}\boldsymbol{\beta}, \sigma^2 \mathbf{I}_n).\end{gather*}
Ainsi, on fait l'hypothèse que $\mathbf{y}$ suit un certain modèle probabiliste.  

Comme les paramètres $\boldsymbol{\beta}$ et $\sigma^2$ sont à estimer, on souhaite utiliser notre méthode d'estimation préférée: le maximum de vraisemblance. La vraisemblance des paramètres $(\boldsymbol{\beta}, \sigma^2)$ s'écrit
\begin{align*}
\ell(\boldsymbol{\beta}, \sigma^2; \mathbf{y})& = \log\left\{ \left( 2\pi\sigma^2\right)^{-n/2} \exp\left[-\frac{1}{2\sigma^2}(\mathbf{y} - \mathbf{X}\boldsymbol{\beta})^\top  (\mathbf{y} - \mathbf{X}\boldsymbol{\beta})\right]\right\}\\
& = -\frac{n}{2}\log\left( 2\pi\sigma^2\right) - \frac{1}{2\sigma^2}(\mathbf{y} - \mathbf{X}\boldsymbol{\beta})^\top  (\mathbf{y} - \mathbf{X}\boldsymbol{\beta}).
\end{align*}

Pour maximiser la vraisemblance, on cherche un point stationnaire et on vérifie qu'il s'agit d'un maximum. 
En effet, on a:
\begin{align*}
\frac{\partial \ell(\boldsymbol{\beta}, \sigma^2; \mathbf{y})}{\partial \boldsymbol{\beta}}& =\frac{\partial}{\partial \boldsymbol{\beta}}\left[ - \frac{1}{2\sigma^2}(\mathbf{y} - \mathbf{X}\boldsymbol{\beta})^\top  (\mathbf{y} - \mathbf{X}\boldsymbol{\beta})\right]\\
& = \frac{1}{2\sigma^2}\left( 2 \mathbf{X}^\top \mathbf{y} - 2 \mathbf{X}^\top\mathbf{X} \boldsymbol{\beta}\right).
\end{align*}
On vérifie aisément aussi que 
\begin{gather*}\frac{\partial^2 \ell(\boldsymbol{\beta}, \sigma^2; \mathbf{y})}{\partial \boldsymbol{\beta}^2} = -\frac{1}{\sigma^2} \mathbf{X}^\top\mathbf{X},\end{gather*}
qui est une matrice symétrique définie négative (si $\mathbf{X}$ est de plein rang). Donc la fonction de vraisemblance est une fonction concave de $\boldsymbol{\beta}$ et donc admet un  maximum unique, qui est le point stationnaire. 

En calculant le point stationnaire, on obtient donc aisément
\begin{gather*} 2 \mathbf{X}^\top \mathbf{y} - 2 \mathbf{X}^\top\mathbf{X} \hat{\boldsymbol{\beta}} = \mathbf{0} \Leftrightarrow \hat{\boldsymbol{\beta}}  =\left(\mathbf{X}^\top\mathbf{X}\right)^{-1}\mathbf{X}^\top \mathbf{y}. \end{gather*}
On remarque que $\hat{\boldsymbol{\beta}}$ ne dépend pas de $\sigma^2$. Ainsi, pour calculer $\hat{\boldsymbol{\beta}}$, il n'est pas nécessaire d'estimer $\sigma^2$.

Le contraire n'est pas vrai: pour estimer $\sigma^2$, il est nécessaire d'estimer $\hat{\boldsymbol{\beta}}$.

Le maximum de vraisemblance maximise
\begin{gather*}\hat{\boldsymbol{\beta}} = \arg\max_{\boldsymbol{\beta} \in \mathbb{R}^p}- \frac{1}{2\sigma^2}(\mathbf{y} - \mathbf{X}\boldsymbol{\beta})^\top  (\mathbf{y} - \mathbf{X}\boldsymbol{\beta}),\end{gather*}
et donc
\begin{gather*}
\min_{\boldsymbol{\beta} \in \mathbb{R}^p}(\mathbf{y} - \mathbf{X}\boldsymbol{\beta})^\top  (\mathbf{y} - \mathbf{X}\boldsymbol{\beta})
= \sum_{i = 1}^n (y_i - \hat{y}_i)^2,
\end{gather*}
où $\hat{y}_i = \mathbf{x}_i^\top \hat{\boldsymbol{\beta}},$ et où $\mathbf{x}_i^\top$ est la ième ligne de la matrice $\mathbf{X}$.

Une fois que l'on a calculé $\hat{\boldsymbol{\beta}}$, on peut calculer le vecteur de valeurs ajustées de $\mathbf{y}$, noté $\hat{\mathbf{y}},$ c'est-à-dire les valeurs prédites par notre modèle pour les covariables observées:
\begin{gather*}\hat{\mathbf{y}} = \mathbf{X}\hat{\boldsymbol{\beta}} = \mathbf{X}\left(\mathbf{X}^\top\mathbf{X}\right)^{-1}\mathbf{X}^\top \mathbf{y} = \mathbf{H}\mathbf{y},\end{gather*}
où $\mathbf{H} = \mathbf{X}\left(\mathbf{X}^\top\mathbf{X}\right)^{-1}\mathbf{X}^\top$ est la « hat matrix» et est une matrice symétrique et de projection:
\begin{gather*}\mathbf{H} = \mathbf{H}^\top, \quad \mathbf{H}^2 = \mathbf{H}. \end{gather*}  

Par ailleurs, comme $\hat{\boldsymbol{\beta}}$ est une transformation linéaire d'une variable Gaussienne, on obtient directement que
\begin{gather*}\hat{\boldsymbol{\beta}}\sim \mathcal{N}\left(\boldsymbol{\beta}, \sigma^2\left(\mathbf{X}^\top\mathbf{X}\right)^{-1}\right). \end{gather*}
Ainsi, en utilisant la distribution normale multivariée, on peut construire des intervalles de confiance pour $\hat{\boldsymbol{\beta}}$.

On verra aussi que ce résultat général est une pièce essentielle pour construire des tests de type $\beta_i = 0$, ce qui correspond à tester si la $i-$ème variable est significativement différente de 0. 

On utilise en général l'estimateur non-biaisé suivant:
\begin{gather*}S^2 = \frac{1}{n-p} \sum_{i = 1}^n (y_i - \hat{y}_i)^2 = \frac{1}{n-p} \|\mathbf{y} - \hat{\mathbf{y}}\|^2, \end{gather*}
où $p$ est le nombre de variables explicatives et $n$ le nombre d'observations.

La distribution de $S^2$ est liée à la variance de la manière suivante:
\begin{gather*}\frac{n-p}{\sigma^2}  S^2 \sim \chi^2_{n-p} \end{gather*}  
  
    
Arrêtons-nous pour regarder ce que l'on a fait.
 - On postule un modèle probabiliste pour nos observations $y$ en fonction de variables explicatives $x$. Ce modèle est entièrement caractérisé par un nombre restreint de coefficients.
 - On estime les coefficients caractérisant le modèle en question.

Une fois l'estimation faite, on dispose alors d'une fonction $\hat{f}$ de $x$ qui fournit une approximation de $y$. Autrement dit, pour tout vecteur de covariables $\mathbf{x}^\top$, on peut en déduire une prédiction pour $y$:
\begin{gather*} \hat{y} = \hat{f}(\mathbf{x}) =  \mathbf{x}^\top \hat{\boldsymbol{\beta}} \end{gather*}

