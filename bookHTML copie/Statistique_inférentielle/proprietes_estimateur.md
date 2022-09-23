# Propriétés d'un estimateur

```{math}
\newcommand\EQM{\text{EQM}}
\newcommand\var{\text{Var}}
\newcommand\E{\mathbb{E}}
```

En général on fait l'hypothèse (parfois discutable au demeurant) que l'on observe des réalisations IID d'une distribution caractérisée par un *vrai* paramètre $\theta$. Notre estimateur $\hat{\theta}$ est une variable aléatoire (comme une fonction de variables aléatoires $X_1,\dots,X_n$). On s'intéresse donc à évidemment à la précision de cet estimateur. On va donc évoquer trois caractéristiques d'un estimateur:
- le biais;
- la variance;
- l'erreur quadratique moyenne.

## Biais

```{prf:definition} Biais
Le **biais** d'un estimateur mesure s'il est centré sur la bonne valeur:
    
\begin{gather*} b(\hat{\theta}) = \mathbb{E}( \hat{\theta} ) - \theta \end{gather*}
```

```{admonition} Interprétation
- Si $ b(\hat{\theta}) < 0 $ alors $\hat{\theta} $ a tendance à sous-estimer $\theta$.
- Si $ b(\hat{\theta}) > 0 $ alors $\hat{\theta} $ a tendance à sur-estimer
- Si $ b(\hat{\theta}) = 0 $ alors $\hat{\theta} $ est **non-biaisé**. C'est un indicateur de qualité.
```

## Variance

Un estimateur étant une variable aléatoire, on a donc
\begin{gather*}\var(\hat{\theta}) = \E[ (\hat{\theta} - \E[\hat{\theta} ])^2].\end{gather*}
La variance d'un estimateur est une mesure de la dispersion de l'estimateur autour de son espérance.

```{figure} latex/PDFSVG/tab1_stat.svg
---
name: tab1_stat
width: 95%
---
```
- le biais est représenté par le fait que la moyenne empirique diffère du but: le centre du nuage de points n'est pas le centre de la cible.
- la variance est représentée par la dispersion du nuage de points.

## Erreur quadratique moyenne

```{prf:definition} Erreur quadratique moyenne
:label: EQM
**L'erreur quadratique moyenne** d'un estimateur $ \hat{\theta} $ de $\theta$ est la fonction:
\begin{gather*} \EQM(\hat{\theta}) = \mathbb{E} \left[ (\hat{\theta} - \theta)^2\right] = \var( \hat{\theta} ) + b(\hat{\theta})^2. \end{gather*}
```

On peut utiliser l'EQM ou la variance pour comparer des estimateurs afin d'utiliser seulement le plus efficace. Lorsque l'on considère deux estimateurs non-biaisés, notés $\theta_1$ et $\theta_2$, comparer leurs variances revient à comparer leurs erreurs quadratiques moyennes. Si l'on a
\begin{gather*}\var(\theta_1) \leq \var(\theta_2), \end{gather*}
alors on dit que $\theta_1$ *est plus efficace* que $\theta_2$.

````{prf:example} Moyenne empirique et médiane empirique
Soient $ X_1 \dots X_n \stackrel{idd}{\sim} \mathcal{N}(\mu,\sigma^2) $. On considère $\overline{X}_n$ et $M_n$, la médiane empirique de $X_1,\dots, X_n$.

La médiane $ M_n $ suit approximativement la loi: $ \mathcal{N}\left( \mu , \frac{\pi}{2}\frac{\sigma^2}{n}\right) $.
            
Vaut-il mieux utiliser la moyenne empirique ou la médiane pour estimer $ \mu $ ?

```{admonition} Solution
:class: dropdown
Rappelons que l'on a:
\begin{gather*} \bar{X}_n \stackrel{\cdot}{\sim} \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right)\end{gather*}
et que l'on a 
\begin{gather*} M_n \stackrel{idd}{\sim}  \mathcal{N}\left( \mu , \frac{\pi}{2}\frac{\sigma^2}{n}\right).\end{gather*}
Ainsi les deux estimateurs sont non-biaisés. Il suffit de comparer leurs variances. On a donc
\begin{gather*}\frac{\EQM(\overline{X}_n)}{\EQM(M_n)} = \frac{\sigma^2}{n}\frac{2}{\pi}\frac{n}{\sigma^2} = \frac{2}{\pi}< 1. \end{gather*} 
La médiane empirique a une variance et donc une erreur quadratique moyenne plus importante. Utiliser cet estimateur nous conduit donc **dans cet exemple** à être moins efficace: on va systématiquement commettre des erreurs plus grandes.
```
````
