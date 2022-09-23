# Variables aléatoires discrètes

Nous allons définir les **variables aléatoires**: concept clé de la probabilité.
- types de variables aléatoires: discrète, continue.
- variables discrètes usuelles: Bernouli, binomiale, Poisson.
- variables continues usuelles: Gaussienne, uniforme, exponentielle;

Après avoir effectué une expérience aléatoire, on s'intéresse davantage à une **fonction du résultat**, plutôt qu'au résultat lui-même.

```{prf:definition} Variable aléatoire
:label: var_aleatoire

**Une variable aléatoire** définie sur un ensemble fondamental $\Omega$ est une fonction de $\Omega$ dans $ \mathbb{R}$ (ou dans un sous-ensemble de $H \subset \mathbb{R}$ ):
\begin{align*}
        X : && \Omega \longrightarrow \mathbb{R}\\
        && \omega \longrightarrow X(\omega),
\end{align*}
où $\omega \in \Omega$. Notez donc que $H$ est l'image de $\Omega$ par $X$.
Une variable peut prendre des valeurs **discrètes** ou **continues**.    Plus généralement, pour $A\subset \mathbb{R}$, on écrit $\{X \subset A\}$ l'événement
\begin{gather*}
    \{\omega \in \Omega \ :\ X(\omega) \in A \}. 
\end{gather*}
```

```{prf:example} Le jeu de Catane
:label: jeu_de_catanne

Au jeu de Catane, on lance deux dés et on fait la **somme**. Ici, on a
\begin{gather*} 
    \Omega = \{(i,j) \  : \  i,j = 1,2,\dots, 6\}, 
\end{gather*}
et la variable aléatoire représentant le jeu de Catane est
\begin{gather*}
    X: \Omega \rightarrow \mathbb{R}, \quad (i,j)\mapsto i + j.
\end{gather*}
```

````{prf:example} 
:label: ex2_var_discrete

Identifions l'ensemble $H$ pour les variables suivantes:
- Nombre de buts dans un match de foot.
- Nombre de grammes de chocolat consommé en un an par Alice.
- Température en Celsius demain matin.

```{admonition} Solution
:class: dropdown
- Nombre de buts
\begin{gather*} H = \mathbb{N}^2.\end{gather*}
Le maximum jamais atteint (match international) est de 31 buts Austalie - Samoa Américaines: 31 - 0;    
- Nombre de grammes de chocolat:
\begin{gather*} H = \mathbb{R}^+.\end{gather*}
- Témprature en Celsius:
\begin{gather*} H = \mathbb{R},\end{gather*}
ou
\begin{gather*} H = [-273.15,+\infty[ .\end{gather*}
```
````

````{prf:definition} Variable discrètes
:label: var_discrete

Une variable aléatoire est **discrète** si elle prend un nombre **fini** ou **dénombrable** de valeurs.
````

```{prf:definition} Fonction de masse/fréquences
:label: fct_masse_var_discrete

Pour une variable discrète $ X $, la fonction:
\begin{gather*} f_X (x_i) := \Pr ( X = x_i ) \end{gather*}
est dite **fonction de masse** (ou fonction de fréquences).
```

Une variable $ X $ est complètement caractérisée par
- les valeurs que $X$ peut prendre, c'est-à-dire $H = \{x_1, \dots,x_k, \dots \}$;
- la liste de probabilités de ces valeurs
\begin{gather*} \Pr(X=x_1), \dots, \Pr(X=x_k), \dots \end{gather*}
$f_X$ définit donc complètement une variable discrète.

```{prf:property} Fonction de masse
:label: prop_fct_masse

La fonction $f_X$ satisfait:
- $0\leq f_X(x_i) \leq 1$ pour tout $i = 1,\dots, n$.
- $f_X(x) = 0$ pour toutes les autres valeurs de $x$.
- $ \sum_{x_i \in H} f_X (x_i) = 1 $
```

`````{prf:example} 
:label: ex3_var_discrete

Calculez la fonction de masse:
- de la somme de deux dés (jeu de Catane);
- du maximum.
````{admonition} Solution
:class: dropdown
\begin{gather*}
    \Omega = \left\{
    \begin{array}{llllll}
    \{1,1\} & \{1,2\} & \{1,3\} & \{1,4\} & \{1,5\} & \{1,6\}\\
    \{2,1\} & \{2,2\} & \{2,3\} & \{2,4\}&\{2,5\}&\{2,6\}\\
    \{3,1\} & \{3,2\} & \{3,3\} & \{3,4\}&\{3,5\}&\{3,6\}\\
    \{4,1\} & \{4,2\} & \{4,3\} & \{4,4\}&\{4,5\}&\{4,6\}\\
    \{5,1\} & \{5,2\} & \{5,3\} & \{5,4\}&\{5,5\}&\{5,6\}\\
    \{6,1\} & \{6,2\} & \{6,3\} & \{6,4\} & \{6,5\} & \{6,6\}
    \end{array}
    \right\}
\end{gather*}

::::{grid}
:gutter: 2

:::{grid-item-card} La somme
```{figure} latex/PDFSVG/tab1_prob.svg
---
name: tab1_prob
width: 95%
---
```
:::

:::{grid-item-card} Le maximum
```{figure} latex/PDFSVG/tab2_prob.svg
---
name: tab2_prob
width: 95%
---
```
:::
::::
````
`````

````{prf:definition} Fonction de répartition
:label: fct_répartition

La **fonction de répartition** $F_x$ d'une variable aléatoire $ X $ est définie par:
\begin{gather*} F_X(x) = \Pr (X \leq x).\end{gather*}
````

```{prf:property} Fonction de répartition
:label: prop_repartition

Toute fonction de répartition a les propriétés suivantes:
- $F_X$ prend ses valeurs dans $ [0,1] $.
- $F_X$ est monotone, croissante (pas nécessairement strictement).
- On a 
\begin{gather*} \lim_{x \rightarrow -\infty}F_X(x) = 0, \quad \lim_{x \rightarrow +\infty}F_X(x) = 1.\end{gather*}
- Si $X$ est une variable aléatoire discrète, alors
\begin{gather*} F_X(x) = \sum_{i \text{ tq } x_i \leq x} \Pr (X = x_i);\end{gather*}
- On a $\Pr(a < X \leq b) = F_X(b) - F_X(a).$
- $F_X$ est continue à droite en $x_i,$ pour tout $x_i \in H$.
```

````{prf:definition} Fonction quantile
:label: fct_quantile
Soit la fonction quantile définie comme
\begin{gather*}
F: ]0,1[ \rightarrow \mathbb{R}, \quad F^{-}(\alpha) = \inf \{t\in \mathbb{R}\ :\ F(t)\geq \alpha \}. 
\end{gather*}
- Si $F_X$ est strictement croissante et continue alors, il existe une fonction réciproque $F^{-1}$ et elle coïncide avec $F^{-}$.
 - Si $F_X$ est seulement continue à droite et croissante, alors la fonction $F^{-}$ est bien définie.
Pour $\alpha\in ]0,1[$, on appelle  $q_\alpha = F^{-}(\alpha)$ le $\alpha-$quantile. 
Par commodité, on va utiliser la notation $F^{-1}$ pour $F^{-}$, y compris lorsque $F$ n'est pas strictement croissante et continue. 
````
```{figure} PDFSVG/quantile_explication.svg
---
name:quantile_expl
width: 95%
---
```

````{prf:example} 
:label: ex3_quantile

Supposons que $X\sim \text{Exp}(\lambda)$. On a alors
\begin{gather*} f_X(x) = \lambda e^{-\lambda x}, \quad x>0.\end{gather*}
Soit $\alpha \in ]0,1[$. Calculez le quantile $q_\alpha$ correspondant.

```{admonition} Solution
:class: dropdown
On a donc 
\begin{gather*} f_X(x) = \lambda e^{-\lambda x }.\end{gather*}
On a alors $F_X(x) =  1-e^{-\lambda x}$ et on déduit fonction quantile en inversant cette fonction:
\begin{gather*}y = 1-e^{-\lambda x} \Leftrightarrow x = - \frac{1}{\lambda}\ln(1-y).   \end{gather*}
Ainsi, 
\begin{gather*}q_\alpha = - \frac{1}{\lambda}\ln(1-\alpha). \end{gather*}
```
````

```{note} Quelques notations
- Les majuscules $ X,Y,Z,T\dots$ désignent des variables aléatoires.
- Les minuscules $x,y\dots$ désignent des valeurs possibles ou des réalisations de $X,Y\dots$.
- La majuscule $F_X$ est la fonction de répartition de $X$.
- La minuscule $f_x$ dénote la fonction de masse ou la densité de $X$.
- On écrit $f,F$ (sans l'indice) s'il n'y a pas de risque de confusion.
- $X \sim F$ veut dire: « la variable aléatoire $X$ suit la loi $F$ » .
- $X \dot{\sim} F$ (point au dessus du tilde) veut dire: « la variable aléatoire $X$ suit **approximativement** la loi $F$ ».
```

````{prf:definition} Variable de Bernouilli
:label: var_bern
Une variable aléatoire de Bernoulli satisfait:
\begin{gather*}
X = \left\{ 
        \begin{array}{cl}
        
            x_1 = 0 & \text{ probabilité }1-p \\ 
            x_2 = 1 & \text{ probabilité } p 
        
        \end{array} \right.
\end{gather*}
On écrit $ X \sim \mathcal{B}(p) $. Sa loi de probabilité est donnée par:
\begin{gather*}
\begin{array}{c|c|c|c}
            X = x_i & 0 & 1&\mbox{Total}\\
            \hline f_X(x_i) =\Pr(X=x_i)& 1-p & p &1
        \end{array}
\end{gather*}
Elle a un paramètre: la probabilité de succès $p$. On peut l'utiliser pour modéliser des expériences qui ont deux issues possibles.
````

````{prf:definition} Variable binomiale
:label: var_bin
On jette une pièce de monnaie $n$ fois indépendamment et $\Pr(\text{Pile}) = p$ est fixée. Soit $ X $ le nombre total de piles obtenus. On dit alors que $X$ suit une **loi binomiale** $X \sim \mathcal{B}(n,p) $. Sa fonction de masse est donnée par
\begin{gather*}
f_X(x) = \binom{n}{x} p^x (1-p)^{n-x} \hspace{1.5cm} x = 0,1 \dots n.
\end{gather*}
La loi binomiale a deux paramètres: le nombre d'essai $n$ et la probabilité de succès $p$. Pour $n=1$, on retrouve une variable de Bernoulli.
````

````{prf:example} Anniversaires mensuels
:label: ex4_bin 

Calculons la loi du nombre de personnes $X$ présentes à ce cours ayant leur anniversaire ce mois ci.    
```{admonition} Solution
:class: dropdown
Pour une personne donnée, la probabilité que son anniversaire tombe un mois donné est $ 1 / 12 $. De plus, pour deux personnes qui n'ont pas de lien de parenté, leurs dates d'anniversaires sont indépendantes.
On peut donc utiliser un modèle Binomial $ \mathcal{B}(n,1/12) $ pour représenter le nombre d'anniversaires dans le mois d'un groupe de $ n $ personnes. 
```
````

```{note} Est-ce bien une fonction de masse?
Il faut vérifier les trois propriétés:
- $0\leq f_X(x_i) \leq 1$ pour tout $i = 1,\dots, n$.
- $f_X(x) = 0$ pour toutes les autres valeurs de $x$.
- $ \sum_{x_i \in H} f_X (x_i) = 1 $
On a trivialement que les propriétés 1 et 2 sont satisfaites. On vérifie aisément la propriété 3:

Il suffit de se souvenir de la formule du binôme de Newton et le résultat est immédiat:
\begin{gather*}
\sum_{x =0}^n  \binom{n}{x} p^x (1-p)^{n-x} = [p + (1-p)]^n = 1.
\end{gather*}
```

```{prf:definition} Variable de Poisson
:label: var_poi
Une **variable de Poisson** a un paramètre $\lambda > 0$:
\begin{gather*} f_X(x) = \frac{\lambda^x}{x!} e^{-\lambda} \hspace{1.4cm} x \in \mathbb{N}.\end{gather*}
Toute les valeurs $ x \in \mathbb{N} $ sont possibles! On écrit $ X \sim \text{Poiss}(\lambda).$
```

Une variable de Poisson peut-être utilisé, par exemple, pour  modéliser:
- nombre d'appels téléphoniques par minute dans une centrale;
- nombre d'avalanches mortelles en Suisse en une année.

```{note} Est-ce bien une fonction de masse?
Il suffit de se souvenir de la de la définition de l'exponentielle et le résultat est immédiat:
\begin{gather*} \sum_{x =0}^\infty  \frac{\lambda^x}{x!} e^{-\lambda} = e^{-\lambda}  \sum_{x =0}^\infty  \frac{\lambda^x}{x!} = e^{-\lambda} e^\lambda = 1. \end{gather*}
```


`````{prf:example} E. Coli.
:label: ex4_poi 

Un échantillon d'eau saine contient 4 E. Coli en moyenne. Trouver la probabilité qu'il en contienne $0,1,2,3,4$. Si on trouve 10 bactéries dans l'échantillon, pensez vous que l'eau soit bonne?    

````{admonition} Solution
:class: dropdown
Le calcul nous donne:
\begin{gather*} f_X(0) = \frac{4^0}{0!}e^{-4} = 0.02, \quad f_X(1) = \frac{4^1}{1!}e^{-4} = 0.07, \text{etc.}
\end{gather*}
qui nous donne la fonction de masse:
```{figure} latex/PDFSVG/tab3_prob.svg
---
name: tab3_prob
width: 95%
---
```
Il est très improbable d'observer 10 bactéries ou plus: $ \Pr(X\geq 10 ) \leq 0.01 $. Une telle observation nous fait donc penser que cette eau est contaminée.
````
`````

Si $X \sim \mathcal{B}(n,p) $ avec $n$ grand et $p$ petit, alors on peut approximer par $ X \dot{\sim}    \text{Poiss}(\lambda = np)$.
Parfois, on appelle ce théorème **la loi des petits nombres**.

`````{prf:example} Les anniversaires
:label: ex5_poi 

Soit $X$ le nombre de personnes qui ont leur anniversaire aujourd'hui.
        Calculez la probabilité que $X=0,1,2,3$ et $X>1$ sous la loi binomiale et son approximation poissonienne.  

````{admonition} Solution
:class: dropdown
On suppose que $p =1/365$ et on a $n=247$.
Le calcul montre qu'on a effectivement des résultats quasi identiques.
Si on arrondit à 0.01, on trouve dans les deux cas la fonction de masses suivante (pour $ n = 247 $):
```{figure} latex/PDFSVG/tab4_prob.svg
---
name: tab4_prob
width: 95%
---
```
On a donc $49\% $ de chances que quelqu'un ait son anniversaire aujourd'hui. Est-ce que c'est le cas?
````
`````

