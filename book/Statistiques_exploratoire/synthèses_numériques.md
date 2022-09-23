# Synthèses numériques

On va donner des outils pour résumer ou décrire rapidement une variable quantitative.
- notions de centre: **moyenne**, médiane;
- notions de dispersion: **variance** et **écart-type**, étendue interquartile;
- quantiles;

## Caractéristiques d'une variable

Pour des **variables quantitatives**, on s'intéresse à:
- la **tendance centrale**: le milieu des données, une valeur typique, e. g.,  la moyenne et la médiane;
- la **dispersion**: à quel point les données fluctuent autour du centre. e. g., l'écart-type et l'étendue ou écart inter-quartile;
- la **symétrie** ou **asymétrie** autour du centre;
- le cas échéant, le nombre de « bosses » ou **modes**;

````{prf:example} Formes des distributions
:label: ex1_syntheses_numeriques

```{figure} PDFSVG/distributions.svg
---
name: distribution
width: 99%
---
```

::::{grid}
:gutter: 2

:::{grid-item-card} 
Même distribution, mais centres différents: <font color="#FE6F5E">$\mathcal{N}(-1,1)$</font>, <font color="#00CED1">$\mathcal{N}(1,1)$</font>.
:::

:::{grid-item-card} 
Même centre, dispersions différentes: <font color="#FE6F5E">$\mathcal{N}(0,1)$</font>, <font color="#00CED1">$\mathcal{N}(0,3)$</font>
:::
::::

::::{grid}
:gutter: 2

:::{grid-item-card} 
Centres et dispersions différents: <font color="#FE6F5E">$\mathcal{N}(-1,1)$</font>, <font color="#00CED1">$\mathcal{N}(1,3)$.</font>
:::

:::{grid-item-card} 
Distribution symétrique et asymétrique: <font color="#FE6F5E">$\mathcal{N}(0,1)$</font>, <font color="#00CED1">$\Gamma(1,3)$</font>
:::
::::

````

## Mesures de tendance centrale

On va considérer deux mesures de tendance centrale:
- la moyenne
- la médiane

````{prf:definition} Moyenne
:label: moyenne

La **moyenne** (arithmétique) d'une suite de valeurs $x_1, \dots, x_n$ est:
\begin{gather*}
 \bar{x} = \frac{x_1 + \dots + x_n}{n} = \frac{1}{n} \left( \sum_{i=1}^n x_i \right) 
\end{gather*}
````
````{prf:definition} Statistique d'ordre
:label: statistique_d_ordre

On a mesuré une même variable $n$ fois, et on dispose des observations suivantes
\begin{gather*}
 x_1, x_2, \dots, x_n.
\end{gather*}
On peut trier cette série dans l'ordre croissant des valeurs. Les valeurs ordonnées sont notées avec un indice entre parenthèses:
\begin{gather*} x_{(1)} \leq x_{(2)} \leq \dots \leq x_{(n)} \end{gather*}
Ainsi, $ x_{(1)} $ est le minimum,  $ x_{(n)}$ le maximum et $ x_{(i)}$ est la $i$ème plus grande valeur observée. On dit aussi parfois que $ x_{(i)}$ est la $i$ème **statistique d'ordre**.
````

````{prf:definition} Médiane
:label: médiane

La médiane, la valeur qui « coupe les données en deux »: 50\% sont plus petites, et 50\% sont plus grandes.
La médiane est la valeur qui est à la position centrale:
\begin{gather*}
 med = x_{ ( \lceil n/2 \rceil ) } 
\end{gather*}
Il existe aussi une définition symétrique qui est parfois utilisée:
\begin{gather*}
    med(x) =
    \left\{
    \begin{array}{ll}
    x_{ \left( \frac{n+1}{2} \right) }         & \text{si $n$ est impair}, \\
    & \\
    \frac{1}{2}  \Big( x_{\left( \frac{n}{2} \right)}+x_{\left( \frac{n}{2} + 1 \right) } \Big)                                                                 & \text{si n est pair}. \\
    \end{array}
    \right.
\end{gather*}
````
La médiane coupe les données en deux parties égales. On peut
généraliser cette idée en séparant l’échantillon en parties inégales.

````{prf:definition} Quartiles et quantiles
:label: quartiles_et_quantile

Le **quantile d'ordre $\alpha$** coupe (approximativement) les données en $\alpha\%$ et $(1-\alpha)\%$. On calcule $ \lceil n \cdot \alpha \rceil $ et on en déduit
\begin{gather*}  
       \hat{q}(\alpha) = x_{ (\lceil n\alpha \rceil) }.
\end{gather*}
Les **quartiles** correspondent au cas $\alpha = 0.25$ et $\alpha = 0.75$.  La médiane à $\alpha = 0.5$.
````
## Mesures de dispersion

````{prf:definition} L'écart-type et la variance
:label: ecart_type_variance

**L'écart-type** (empirique) de l'échantillon $ x_1, x_2, \dots, x_n$ est :
\begin{gather*}
 s = \sqrt{ \frac{1}{n-1} \sum_{i=1}^n (x_i - \bar{x})^2 } = \sqrt{ \frac{1}{n-1} \left( \sum_{i=1}^n x_i^2 - n \bar{x}^2 \right) }
\end{gather*}  

et la quantité $s^2$ est la **variance** (empirique) de l'échantillon $ x_1, x_2, \dots, x_n$.
````

````{prf:definition} L'étendue (ou l'écart) interquartile
:label: ecart_interquartile
**L'étendue (ou l'écart) interquartile** est définie comme:
\begin{gather*}
 \text{EIQ} = \hat{q}(0.75) - \hat{q}(0.25) 
\end{gather*}
````  

On a vu deux mesures de tendances centrales et deux mesures de dispersion: pourquoi?
    
La plupart du temps, les valeurs données par ces différentes notions vont être proches.
    
La médiane et l'écart interquartile sont moins sensibles aux valeurs aberrantes. C'est une bonne chose car ces valeurs résultent souvent d'une erreur de mesure ou d'un problème dans la collecte des données. On dit de ces mesures qu'elles sont **robustes**.
    
On va se concentrer sur la **moyenne** et **l'écart-type** (et la **variance**) par la suite.
