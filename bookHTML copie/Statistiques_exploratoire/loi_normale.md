# Loi normale

## Variable aléatoire

Une *variable aléatoire* $X$ peut être vue comme le résultat d'une expérience aléatoire. On en verra la définition formelle plus tard. Lorsque l'expérience aléatoire en question peut prendre des valeurs dans $\mathbb{R}$, on parle variable continue et on y associe une fonction de densité $f_X:\mathbb{R} \rightarrow\mathbb{R}$ qui satisfait:
\begin{gather*}
    P(X \in [a,b]) = \int_a^b f_X(x) \ dx,
\end{gather*}
où $P(X \in [a,b])$ est la probabilité que $X$ prenne une valeur qui soit dans l'intervalle $[a,b]$. 
On peut interpréter $f_X(x) \ dx$ comme la probabilité que la variable $X$ prenne une valeur dans le voisinage de $x$. 

````{note} Une première intuition du concept de fonction de densité
On peut voir la densité comme une version *normalisée* d'un histogramme lorsque $n\rightarrow \infty$ et $h \rightarrow 0$ (la largeur de bande).
```{figure} PDFSVG/hist_to_dens.svg
---
name: hist_to_dens
width:95%
---
```
````

````{prf:example} Exemples de variables aléatoires continues
:label: ex1_loi_normale
- la proportion de jeunes filles dans les classes du canton: il s'agit d'une valeur $p \in [0,1]$, qui a tendance à être proche de $0.5$ et qui peut théoriquement prendre n'importe quelle valeur entre $[0,1]$;
- la taille des enfants d'une même classe d'âge et de même sexe (e.g. fille de 1 an): il s'agit d'une valeur comprise grossièrement entre 69cm et 79cm, pouvant prendre n'importe quelle valeur ([Courbes de croissance, Société Suisse de Pédiatrie](https://cdn.paediatrieschweiz.ch/production/uploads/2020/05/Perzentilen_2012_09_15_SGP_f.pdf)).
````

## Loi normale ou loi Gaussienne

En guise de première rencontre avec une **variable aléatoire**, on va commencer par présenter l'une des plus commune: la loi Gaussienne (ou de Gauss ou loi normale). On va voir les aspects suivants:
- la densité Gaussienne;
- les rôles de la moyenne et de la variance;
- la définition des fonction $ \phi $ et $ \Phi $.

````{prf:definition} Varibale aléatoire normale
:label: my-definition

Une variable aléatoire $X$ suit une **loi normale** (ou Gaussienne) $ \mathcal{N}(\mu,\sigma^2)$ si et seulement si elle admet pour densité la fonction
\begin{gather*} f_X(x; \mu, \sigma) = \frac{1}{(2\pi\sigma^2)^{1/2}} \exp \left( -\frac{(x-\mu)^2}{2 \sigma^2}\right). \end{gather*}
La densité est caractérisée par deux paramètres: la moyenne $ \mu$ et la variance $ \sigma^2 $ (on appelle $\sigma >0$ l'écart-type).
````

````{admonition} Différence entre variable aléatoire et échantillon
:class: important
Il est fréquent (on le reverra constamment) de faire l'hypothèse que des observations
$ x_1,\dots,x_n $ sont les *réalisations* de variables aléatoires $X_1, \dots, X_n$.
- $ x_1,\dots,x_n $ est l'échantillon observé; aucune de ces valeur n'est aléatoire.
- $X_1, \dots, X_n$ sont des variables aléatoires qui modélisent le comportement observé. 

En général, et dans ce cours, on s'efforcera d'utiliser les minuscules pour des variables observées et les majuscules pour les variables aléatoires.`
````

````{prf:example} Exemple de loi normale: nombre d'anneaux d'ormeaux
:label: ex2_loi_normale

```{figure} PDFSVG/hist_abalone.svg
---
name: hist_abalone
width: 95%
---
Histogramme du nombre d'anneaux d'ormeaux (coquillage) et la distribution normale estimée.
```
````

## Propriétés de la loi normale
- La majorité des observations d'une « population Gaussienne » est proche du centre $\mu$
- Plus précisément, on a la règle « 68-95-99.7 »:
\begin{gather*}  \mathcal{N}(\mu,\sigma^2) \Rightarrow \left\{
                    \begin{array}{l r l}
                    68\% & \mbox{ des observations sont dans } & [\mu\pm \sigma],\\
                    95\% & \mbox{ dans }                       & [\mu \pm 2\sigma],\\
                    99.7\% &\mbox{ dans }                      & [\mu \pm 3\sigma].\end{array} \right.
\end{gather*}

Dans le cas des diamètres d'ormeaux, on a:
\begin{equation*}
\begin{array}{lll}
        77.5\% &\mbox{ dans }&[\bar x \pm s]\\
        94.9\% &\mbox{ dans }&[\bar x \pm 2 s]\\
        98.5\% &\mbox{ dans }&[\bar x \pm 3s].
\end{array}
\end{equation*}

## Standardisarion

Pour pouvoir comparer les lois normales, on a recours à la **standardisation**.
Si $ x $ est une observation issue d'une densité de moyenne $ \mu $ et d'écart-type $ \sigma $, alors la valeur standardisée de $ x $ est:
    
\begin{gather*} z = \frac{ x - \mu }{ \sigma } \end{gather*}
    
Pour le nombre d'anneaux des ormeaux, la moyenne empirique (qui est un estimateur de $\mu$)  est $ \bar{x} = 9.93 $ et l'écart-type (qui est un estimateur de $\sigma$) $ s = 3.22 $.

La standardisation permet de se ramener de n'importe quelle Gaussienne à celle qui a moyenne 0 et variance 1: $ \mathcal{N}(0,1) $.

On la dénomme **distribution normale centrée réduite** ou **standard**. Sa densité est donc:
\begin{gather*} \phi(z) = \frac{1}{\sqrt{2\pi}} \exp \left( -\frac{z^2}{2} \right). \end{gather*}

Par définition, son intégrale donne la proportion d'observations qui tombent dans un intervalle donné:
\begin{gather*} \Phi(z) = \int_{-\infty}^z \phi(t) dt, \hspace{1 cm} z \in \mathbb{R}.\end{gather*}

Par définition de l'intégrale, on a:
 \begin{gather*} \int_{z_1}^{z_2} \phi(z) dz = \Phi(z_2) - \Phi(z_1),\end{gather*}
et par symétrie de la fonction $\Phi(z)$:
\begin{gather*} \Phi(-z) = 1 - \Phi(z).\end{gather*}
Pour connaitre la valeur de $ \Phi(z) $, on peut se référer à une table.

```{figure} latex/PDFSVG/tab1_loi_normale.svg
---
name: tab1_loi_normale
width: 95%
---
Extrait de la table de $ \Phi $ du formulaire du cours.
```

On appelle *fonction quantile* la fonction réciproque de la fonction $\Phi,$ que l'on note $\Phi^{-1}.$
Par définition, elle satisfait:
\begin{gather*}\Phi(z) = y \Leftrightarrow z = \Phi^{-1}(y). \end{gather*}
De manière plus concrète, pour une valeur (probabilité) $p\in ]0,1[$ donnée, le quantile correspondant satisfait la relation
\begin{gather*}\Pr (X\leq z) = p, \end{gather*}
où $X$ est une réalisation d'une loi normale standard (on verra plus loin la définition précise d'une variable aléatoire).
On peut montrer que la fonction quantile de la loi normale satisfait la propriété suivante:
\begin{gather*}\Phi^{-1}(z) = - \Phi^{-1}(1-z). \end{gather*}

Dans ce cours, on utilisera parfois la notation $\ln$, parfois la notation $\log$ en fonction de mon humeur. Cependant ces notations ont la même signification et dénotent toutes deux
**le logarithme népérien** (en base $e$). Si on utilise une autre base, celle-ci sera notés **explicitement** en indice:  $\log_{10}$ par exemple. 
