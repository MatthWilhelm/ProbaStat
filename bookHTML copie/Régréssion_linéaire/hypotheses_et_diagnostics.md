# Régréssion linéaire: hypothèses et diagnostics

```{math}
\newcommand\corr{\text{Corr}}
\newcommand\cov{\text{Cov}}
\newcommand\var{\text{Var}}
\newcommand\E{\mathbb{E}}
```

\begin{gather*}\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon},
\end{gather*}
où $\boldsymbol{\beta} \in \mathbb{R}^p$ est un vecteur de paramètres, $\boldsymbol{\varepsilon} \in \mathbb{R}^n \sim\mathcal{N}(\mathbf{0}, \sigma^2 \mathbf{I}_n)$ et $\sigma^2 >0$. Rappelons que si $\boldsymbol{\varepsilon}= (\varepsilon_1, \dots, \varepsilon_n)$, on a
\begin{gather*}\boldsymbol{\varepsilon} \sim\mathcal{N}(\mathbf{0}, \sigma^2 \mathbf{I}_n) \Leftrightarrow \varepsilon_1, \dots, \varepsilon_n \stackrel{idd}{\sim} \mathcal{N}(0,\sigma^2).\end{gather*}

D'une certaine manière, tout tient dans l'affirmation que 
\begin{gather*}\varepsilon_1, \dots, \varepsilon_n \stackrel{idd}{\sim} \mathcal{N}(0,\sigma^2).\end{gather*}
On détaille ces hypothèses:
- **linéarité**: une relation linéaire lie la variable réponse et les covariables;
- **homoscedasticité** (même variance): la variance des erreurs est constante;
- **indépendance**: les erreurs sont indépendantes entre elles;
- **normalité**: on suppose que la distribution des erreurs est normale.

Au delà des hypothèses sur les erreurs, on fait une autre hypothèse, sur la structure des covariables:
- **plein rang**: on suppose que les covariables sont indépendantes (au sens de l'algèbre linéaire), c'est-à-dire qu'aucune covariable n'est une combinaison linéaire des autres covariables. Mathématiquement, cela signifie que le rang de la matrice $\mathbf{X}$ est égal à son nombre de colonnes.

Une fois le modèle ajusté, c'est-à-dire qu'on a calculé $\hat{\boldsymbol{\beta}}$, on en déduit **les résidus**
\begin{gather*} e_1 = y_1 - \hat{y}_1, \dots, e_n = y_n - \hat{y}_n.\end{gather*}
Si les hypothèses du modèle linéaire Gaussien sont satisfaites, alors les résidus sont des estimateurs de la variable $\varepsilon \sim \mathcal{N}(0, \sigma^2)$. 

Sous forme vectorielle, on peut écrire $\mathbf{e} = (e_1, \dots, e_n)^\top$ et on a
\begin{gather*}\mathbf{e} = \mathbf{y} - \hat{\mathbf{y}} = \left(\mathbf{I}_n - \mathbf{X}\left(\mathbf{X}^\top\mathbf{X}\right)^{-1}\mathbf{X}^\top \right)\mathbf{y} =\left(\mathbf{I}_n - \mathbf{H}\ \right)\mathbf{y}. \end{gather*}
On définit alors les résidus standardisés comme
\begin{gather*}r_i = \frac{y_i - \hat{y_i}}{s \sqrt{1 - h_{ii}}}. \end{gather*}
Notons que l'on a $\mathbf{H}^2 = \mathbf{H}$ d'où on déduit que 
\begin{align*}
\var(\mathbf{e}) &=  \var\left[\left(\mathbf{I}_n - \mathbf{H}\ \right)\boldsymbol{\varepsilon} \right]  = \left(\mathbf{I}_n - \mathbf{H}\ \right) \var(\boldsymbol{\varepsilon}) \left(\mathbf{I}_n - \mathbf{H}\ \right)^\top \\
&= \sigma^2\left(\mathbf{I}_n - \mathbf{H}\ \right).
\end{align*}

```{prf:property} Résidus
Les résidus satisfont plusieurs propriété.
- Ils sont orthogonaux à la matrice $\mathbf{X}$
\begin{gather*}\mathbf{X}^\top \mathbf{e} =\mathbf{X}^\top  (\mathbf{y} - \mathbf{X}\hat{\boldsymbol{\beta}}) = \mathbf{0}. \end{gather*}
- Ils sont orthogonaux aux valeurs ajustées
 \begin{gather*}\hat{\mathbf{y}}^\top \mathbf{e} = \mathbf{0}.\end{gather*}
```

On va donc voir des moyens graphiques d'examiner d'éventuelles violations de l'hypothèse sur les résidus:
- linéarité: nuage de points des résidus en fonction des covariables;
- homoscédasticité: nuage de points des résidus en fonction des valeurs ajustées;
- indépendance: nuage de point des résidus contre les covariables, graphiques d'auto-corrélation et d'auto-corrélation partielle; 
- normalité: QQ-plot normal. 

## Diagnostic de linéarité

On peut distinguer deux aspects: que la relation entre la variable de réponse et les variables explicatives est bien linéaire et qu'elle ne soit que linéaire.
- Faire un nuage de points de la réponse en fonction de chacune des covariables;
- Faire un nuage de points des résidus en fonction de chacune des covariables.

```{figure} PDFSVG/linearity_diagnostic_exemple.svg
---
name: linearity_diagnostic_exemple
width: 95%
---
Diagnostic de linéarité: exemple
```

```{figure} PDFSVG/linearity_diagnostic_contre_exemple.svg
---
name: linearity_diagnostic_contre_exemple
width: 95%
---
: Diagnostic de linéarité: contre-exemple
```

## Homoscédasticité (variance constante)

L'hypothèse de l'homoscédasticité découle du fait que les erreurs sont identiquement distribuées.
- On peut s'en passer, mais il est alors nécessaire de connaître la structure de la variance;
- En cas d'hétéroscedasticité, les moindres carrés doivent être modifiés et on parle de moindres carrés *pondérés*.

```{figure} PDFSVG/homoscedastic_diagnostic_homo.svg
---
name: homoscedastic_diagnostic_homo
width: 95%
---
: Homoscédastique
```

```{figure} PDFSVG/homoscedastic_diagnostic_hetero.svg
---
name: homoscedastic_diagnostic_heteroo
width: 95%
---
: Hétéroscédastique
```

## Diagnostics d'indépendance

De manière générale, l'hypothèse d'indépendance des résidus est la plus difficile à évaluer. Et l'indépendance peut-être violée de différentes manières. On mentionne deux facteurs importants:
- autocovariance dans le terme d'erreur;
- une partie des résidus est une fonction non-linéaire des variables explicatives.

On parle d'autocovariance lorsque, pour des variables aléatoires $X_1, \dots, X_n$, il existe une fonction $\gamma$ telle que
\begin{gather*}\cov(X_i, X_j) = \gamma(\left|i-j\right|), \quad \forall i,j = 1, \dots, n. \end{gather*}
En général, cette définition est traitée dans le cadre des « série temporelles ». Intuitivement, cela signifie qu'il y a une dépendance entre les observations qui est liée aux indices (ou à leur éloignement), ce qui est typiquement le cas dans les séries temporelles.

L'autocovariance empirique d'un échantillon $x_1, \dots, x_n$ d'observations se calcule de la manière suivante:
\begin{gather*} \hat{\gamma}(h) = \frac{1}{n} \sum_{t = 1}^{n-h}(x_{t + h} - \overline{x}) (x_{t}- \overline{x}). \end{gather*}
L'autocorrélation est définie comme:
\begin{gather*} \rho(h) = \frac{\gamma(h)}{\gamma(0)} \in ]-1,1[.\end{gather*}
L'autocorrélation partielle est une notion plus complexe à définir mais permet de mettre en évidence une dépendance entre des observations.

````{prf:example} Erreurs autocorrélées
Considérons deux modèles presque identiques:
\begin{align}
Y^{(1)} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}^{(1)}, \tag{M1}\\
Y^{(2)} = \mathbf{X}\beta + \boldsymbol{\varepsilon}^{(2)},  \tag{M2}
\end{align}
où on a 
$ \varepsilon^{(1)}_1, \dots, \varepsilon^{(1)}_n \stackrel{idd}{\sim} \mathcal{N}(0,\sigma^2)$, alors que 
$ \varepsilon^{(2)}_1, \dots, \varepsilon^{(2)}_n \sim \mathcal{N}(0,\sigma^2)$ mais **ne sont pas indépendantes**.
Par ailleurs, on a $\boldsymbol{\beta} = (5, -1, 2)^\top$ et $5$ est la valeur de l'ordonnée à l'origine. 

```{figure} PDFSVG/independance_diagnostic_autocorrelation.svg
---
name: independance_diagnostic_autocorrelation
width: 95%
---
: Exemple de diagnostic d'indépendance
```
ACF et PACF des résidus standardisés d'une réalisation du modèle (M1).
```{figure} PDFSVG/ar1_diagnostic_autocorrelation.svg
---
name: ar1_diagnostic_autocorrelation
width: 95%
---
: Contre-exemple de diagnostic d'indépendance
```
ACF et PACF des résidus standardisés d'une réalisation du modèle (M2)
````


## Diagnostic de normalité

On utilise très souvent le QQ-plot (graphique quantile/quantile) pour comparer une distribution empirique par rapport à une distribution théorique $F$ (continue). Soient $x_{(1)}, \dots, x_{(n)}$ un échantillon ordonné et soit $F^{-1}$ le fonction réciproque de $F$, appelée aussi fonction quantile. Alors un QQplot est un nuage de points dont les coordonnées sont
\begin{gather*}(F^{-1}(c_1), x_{(1)}),\dots, (F^{-1}(c_n), x_{(n)}),\end{gather*}
où $c_1, \dots, c_n$ sont donnés par 
\begin{gather*}c_k =  \frac{k - c_0}{n + 1 - 2 c_0 }\approx \frac{k}{n}, \quad c_0 = \frac{3}{8} \text{ si $n$ < 10}, \quad c_0 = \frac{1}{2}, \text{ sinon.} \end{gather*}

Dans le cas où la distribution théorique à laquelle on souhaite comparer notre écahntillon est la loi normale, on a $F^{-1} = \Phi^{-1}, $ la loi quantile de la loi normale standard.

La suite $c_1, \dots, c_n$ peut sembler un peu étonnante. Elle correspond à une approximation de l'espérance  des statistiques d'ordre de la loi normale standard.

Dans ce qui suit, on montre des QQ-plots normaux pour plusieurs échantillons de lois différentes.

```{figure} PDFSVG/QQplot_normal.svg
---
name: QQplot_normal
width: 95%
---
: QQplot d'une réalisation d'une loi normale standard, de taille $n = 50$.
```

```{figure} PDFSVG/QQplot_student.svg
---
name: QQplot_student
width: 95%
---
: QQplot d'une réalisation d'une loi de Student à $\nu = 1$ degré de liberté, de taille $n = 50$.
```

```{figure} PDFSVG/QQplot_Cauchy.svg
---
name: QQplot_Cauchy
width: 95%
---
: QQplot d'une réalisation d'une loi de Cauchy de paramètre de localisation 0 et de localisation $0$, de taille $n = 50$.
```

```{figure} PDFSVG/QQplot_Gamma.svg
---
name: QQplot_GammaQ
width: 95%
---
: QQplot d'une réalisation d'une loi Gamma de paramètre de forme $k = 3$ et d'échelle  $\theta = 1$, de taille $n = 50$.
```

## Hypothèse de rang plein et $R^2$

### Hypothèse de rang plein

Pour vérifier l'hypothèse de plein rang, on peut facilement calculer le déterminant de la matrice 
\begin{gather*}\det\left(\mathbf{X}^\top \mathbf{X}\right) \neq 0 \Leftrightarrow  \text{rang}(\mathbf{X} ) = p.\end{gather*} 

De manière plus pratique, vérifier que le conditionnement de la matrice $\mathbf{X}^\top \mathbf{X}$ est raisonnablement bas permet de s'assurer que le problème n'est pas mal-posé.

### $R^2$

On rappelle la deuxième propriété des résidus, à savoir l'orthogonalité de $\hat{\mathbf{y}}$ et de $\mathbf{e}$. Ainsi, on a
\begin{gather*}\|\mathbf{y} \|^2 =\mathbf{y}^\top \mathbf{y} = (\mathbf{e} + \hat{\mathbf{y}} )^\top (\mathbf{e} + \hat{\mathbf{y}}) = \mathbf{e}^\top\mathbf{e} +  \hat{\mathbf{y}}^\top \hat{\mathbf{y}}. \end{gather*}
Ainsi, on peut décomposer la norme de $\mathbf{y}$ en deux composantes orthogonales, le vecteur de valeurs  ajustées $\hat{\mathbf{y}}$ et le vecteur des résidus $\mathbf{e}$.

L'orthogonalité des résidus et du vecteur de valeurs ajustées mets en lumière qu'il y a une certaine géométrie du problème. De fait, on a:
- Si $\mathbf{X}$ est de plein rang, alors $(\mathbf{X}^\top \mathbf{X} )^{-1}\mathbf{X}$ est une pseudo-inverse de $\mathbf{X}$ (inverse de Moore-Penrose);
- $\mathbf{H}$ est la matrice de projection orthogonale sur l'espace engendré par les colonnes de $\mathbf{X}.$

```{figure} latex/PDFSVG/tab2_regr.svg
---
name: tab2_regr
width: 95%
---
```

A partir de la décomposition de la norme de $\mathbf{y}$, on peut déterminer le *coefficient de détermination* $R^2$, défini comme
\begin{gather*}R^2 = 1 - \frac{\mathbf{e}^\top \mathbf{e}}{(\mathbf{y} - \overline{\mathbf{y}})^\top(\mathbf{y} - \overline{\mathbf{y}}) } =\frac{ \sum_{i = 1}^n (y_i - \hat{y}_i)^2}{\sum_{i = 1}^n (y_i - \overline{y}_i)^2}, \end{gather*}
où $\overline{\mathbf{y}} = \overline{y}\ \mathbf{1}_n\in \mathbb{R}^n$ est le vecteur dont toutes les composantes sont $\overline{y}$.

```{prf:property} $R^2$
- le coefficient de détermination est le rapport entre la variance expliquée et la variance observée;
- il s'agit d'une mesure courante pour évaluer la qualité de l'ajustement du modèle linéaire;
- il souffre de nombreux défauts: monotone dans le nombre de variables (y compris si ces dernières sont absurdes), parfois inférieur à 1 (dans des cas très particulier et seulement si aucune ordonnée à l'origine n'est incluse dans le modèle), etc.
```

## Obsevations influentes

Une idée essentielle de toute modélisation est la « robustesse  » (ou stabilité): si on change un petit peu les données, est-ce que cela change beaucoup les estimations?
- concept similaire à la stabilité en analyse numérique;
- essentiel pour comprendre à quel point les conclusions sont sensibles aux données.


On distingue en général deux catégories distinctes:
- les valeurs aberrantes (outlier);
- les points leviers.

### Valeurs aberrantes

Une valeur aberrante est une valeur qui se situe très loin des autres valeurs observées. Elles ont tendance à « attirer » la droite de régression vers elles.

```{figure} PDFSVG/reg_line_outlier.svg
---
name: reg_line_outlier
width: 95%
---
```

Il y a plusieurs moyens de détecter les valeurs aberrantes:
- en utilisant les nuages de points: les valeurs étant très éloignées des autres sont de potentielles valeurs aberrantes;
- en utilisant les résidus standardisés: les valeurs dont les résidus standardisés sont en dehors de l'intervalle $[-2,2]$ sont de potentielles valeurs aberrantes.
Les résidus standardisés offrent une manière plus méthodique car ils se trouvent sur l'échelle des valeurs d'une loi normale standard. Cependant, ils dépendent de notre modèle.

Il y a plusieurs écoles concernant le traitement à réserver à des valeurs aberrantes. Sans entrer dans la question de savoir s'il est raisonnable de retirer une observation d'un jeu de données, on fera au moins deux remarques.
- La première chose à faire en présence d'une valeur aberrante est de l'examiner de plus près: s'agit-il d'une erreur de mesure? Est-ce que l'on peut confirmer qu'elle a bien été observée ou s'agit-il d'une erreur d'encodage? S'agit-il d'une valeur manquante étonnamment encodée?  
- Les valeurs aberrantes peuvent cacher un aspect insoupçonné et très intéressant d'un phénomène. Il est important de s'y intéresser de plus près si elles ne sont pas le fruit d'une erreur.

### Points leviers

On distingue les *points leviers* des valeurs aberrantes. 
- Les valeurs aberrantes sont en général éloignées du nuage de points dans la direction $y$ (variable réponse).
- Les points leviers sont éloignés du nuage de points dans l'espace des variables explicatives. 
Les points leviers peuvent être difficiles à repérer visuellement.  

On rappelle que l'on a:
\begin{gather*}\var(\mathbf{e}_i) = \sigma^2 (1 - h_{ii}),\end{gather*}
où  $h_{ii}$ est la $i-$ème composante de la diagonale de la matrice 
\begin{gather*}\mathbf{H} = \mathbf{X} \left(\mathbf{X}^\top\mathbf{X}  \right)^{-1}\mathbf{X}^\top.\end{gather*}
Ainsi, si $h_{ii} = 1$, on a nécessairement que $\mathbf{e}_i = 0$. Autrement dit, plus $h_{ii}$ est proche de $1$, plus la droite (ou le plan) de régression va être contrainte à passer proche du point $(x_i, y_i).$

On a aussi que, $\sum_{i = 1}^n h_{ii} = p$.

De manière générale, on utilise la règle suivante: si 
\begin{gather*}h_{ii} > \frac{2p}{n}, \end{gather*}
alors il est important de prêter attention à cette observation particulière car elle a une forte influence sur la régression.

```{figure} PDFSVG/reg_line_leverage_point.svg
---
name: reg_line_leverage_point
width: 95%
---
```

## Distance de Cook

L'influence d'une observation pourrait être évaluée de la manière suivante: comment changerait mon vecteur de paramètres estimés si j'enlevais cette observation? Cette idée est très profonde et conduit à plusieurs concepts:
- la distance de Cook;
- la validation croisée.

```{prf:definition} Distance de Cook
Soit $\hat{\boldsymbol{\beta}}$ le vecteur estimé d'un modèle linéaire et notons $\hat{\boldsymbol{\beta}}_{-j}$ le même vecteur mais estimé sur la base de toutes les observations **sauf la $j-$ème.** On note $\hat{\mathbf{y}}_{-j} = \mathbf{X}\hat{\boldsymbol{\beta}}_{-j}.$
On définit alors la distance de Cook de l'observation $j$ comme
\begin{gather*}C_j = \frac{1}{p s^2} \| \hat{\mathbf{y}} - \hat{\mathbf{y}_{-j}} \|^2.\end{gather*}
On peut montrer que l'on a
\begin{gather*}C_j = r_i^2 \frac{h_{ii}}{p(1-h_{ii})}, \end{gather*}
donc $C_j$ est grand si
- $r_i^2$ est grand;
- si $h_{ii}\approx 1.$
```

```{admonition} Identifier les observations influentes
:class: tip

Il est important de regarder avec une attention particulière les observations pour lesquelles une des propriétés ci-dessous est vérifiée:
- un résidu standardisé $\left|r_i\right|> 2$;
- un levier $h_{ii}>\frac{2p}{n}$; % See Davison, p. 394
- une distance de Cook $C_j > \frac{8}{n-2p}$.
```

```{figure} PDFSVG/cook_distance_2.svg
---
name: coook_distance_2
width: 95%
---
Données et droite de régression (gauche) et distances de Cook correspondantes. La droite en rouge à droite correspond au niveau $y = \frac{8}{n-2p}$.
```

```{admonition} Que faire lorsque l'on a une observation influente
- Examinez les observations problématiques avec une attention particulière;
- Ajustez un modèle avec et sans les observations problématiques et voir si cela change sensiblement ou pas la conclusion;
- Éventuellement retirer les observations problématiques.
```
