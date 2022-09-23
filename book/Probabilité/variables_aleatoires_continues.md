# Variables aléatoires continues

````{prf:definition} Variable aléatoire continue
:label: var_cts

Une variable aléatoire est dite continue si elle peut prendre des valeurs sur un ensemble non-dénombrable, en général un sous-ensemble de l'ensemble des nombres réels.
````

Par exemple:
- le poids d'un être humain;
- le temps chronométré d'un 100m;
- la pression atmosphérique.

````{prf:definition} Fonction de densité
:label: fct_dens
Soit $X$ une variable aléatoire réelle continue. La fonction de densité de $X$, notée $f_X(x)$ satisfait
\begin{gather*} \mathbb{P}(X \in A) = \int_A f_X(u) du, \end{gather*}
pour tout $A\subset \mathbb{R}$. En particulier, pour tout $a<b, a,b\in \mathbb{R}$, on a
\begin{gather*} \mathbb{P}(X \in [a,b]) = \int_a^b f_X(u) du. \end{gather*}
````

```{prf:property} Fonctions de densité
:label: prop_fct_dens
On a les deux propriétés essentielles suivantes:
- On a les deux propriétés essentielles suivantes:
\begin{gather*}f_X(x) \geq 0, \quad \int_{-\infty}^{\infty} f_X(u) du = 1.\end{gather*}
- avec $A = [a,a]$, on trouve:
\begin{gather*} \mathbb{P}(X=a) = \int_a^a f_X(u) du = 0; \end{gather*}
- la fonction de répartition est une primitive de la densité:
\begin{gather*} F_X(a) = \mathbb{P}(X\leq a) = \int_{-\infty}^a f_X(u) du \end{gather*}
- En tout point où $f_X(x)$ est continue:
\begin{gather*} f_X(x) = F_X'(x).\end{gather*}
```

```{warning}
$f_X(x)$ peut être plus grand que $1$!
```

````{prf:example}
:label: ex1_loi_unif

On choisit au hasard un nombre réel dans l'intervalle $[0,1]$ de manière équiprobable. Soit $X$ le résultat de cette expérience. Quelle est la densité de $X$ ?
Soient $0<a<b<1$. Calculez:
\begin{gather*} \mathbb{P}(a \leq X \leq b) = \dots \end{gather*}
```{admonition} Solution
:class: dropdown
Pour trouver la réponse, considérons l'histogramme construit avec un grand nombre de données qui suivraient la loi décrite.
    
Cet histogramme serait parfaitement plat sur l'intervalle $[0,1]$. En effet, si il y avait une bosse, cela correspondrait à une zone favorisée et violerait l'hypothèse d'équiprobabilité.
    
La densité est donc une fonction plate sur $ [0,1] $ et vaut $ 0 $ ailleurs. La seule solution possible est:
\begin{gather*} f(x) = \mathbf{1}_{[0,1]}(x). \end{gather*}
On peut alors calculer l'intégrale entre $ a $ et $ b $:
\begin{gather*} \int_a^b f(x) = b-a. \end{gather*}
```
````


```{prf:definition} Loi uniforme
:label: loi_unif
La **loi uniforme** $ X \sim U(a,b)$ pour $ a < b $:
        
\begin{gather*} f_X(x) = \left\{ 
                \begin{array}{cc}
                    1/(b-a) & \text{si }a\leq x \leq b, \\
                    0        & \text{sinon.} \\
                \end{array}        \right. \end{gather*}
```

```{prf:definition} Loi exponentielle
:label: loi_exp
La **loi exponentielle** $X \sim \exp(\lambda)$ pour $\lambda > 0$:
        
\begin{gather*} f_X(x) = \left\{ 
                \begin{array}{cc}
                    \lambda \exp(-\lambda x) & \text{si }x\geq 0, \\
                    0        & \text{sinon.} \\
                \end{array}        \right.  \end{gather*}
```

```{prf:definition} Loi normale
:label: loi_normale
La **loi normale** $X \sim \mathcal{N}(\mu,\sigma^2)$:        
\begin{gather*} f_X(x) = \frac{1}{(2\pi \sigma^2)^{1/2}} \exp \left( -  \frac{(x-\mu)^2}{2\sigma^2}  \right). \end{gather*}
Si $ X \sim \mathcal{N}(\mu,\sigma^2)$ alors $ Z = (X-\mu) / \sigma \sim \mathcal{N}(0,1)$ (standardisation). On a déja vu la densité $ \phi $ et la fonction de répartition $ \Phi $ de $Z$. 
```

````{prf:definition} Loi Gamma
:label: loi_gamma
La **loi** $\Gamma$: $X \sim \Gamma(k,\theta)$:        
\begin{gather*} f_X(x) = \frac{x^{k-1}}{\Gamma(k) \theta^k} \exp(- x/\theta), \quad x \geq 0, \end{gather*}
où $k$ et $\theta$ sont appelés respectivement paramètres de forme et d'échelle (scale and shape).
````


````{prf:example} Temps d'attente
:label: ex2_temps_attente

Le métro arrive toutes les 12 minutes. Si j'arrive à un moment au hasard, quelle est la probabilité que j'attende: 
- plus de 8 minutes? 
- moins de 2 minutes? 
- entre 3 et 6 minutes?    

\begin{gather*} \mathbb{P}(a \leq X \leq b) = \dots \end{gather*}
```{admonition} Solution
:class: dropdown
On peut représenter mon temps d'attente par une loi uniforme: si j'arrive complètement au hasard au métro, il n'y pas de raisons pour que la distribution ait un biais quelconque. Sous cette hypothèse, on trouve la densité:
\begin{gather*} f(x) = \mathbf{1}_{[0,12]}(x). \end{gather*}
On a alors:
\begin{align*}
            \mathbb{P} (X \geq 8) &= 1 / 3, \\
            \mathbb{P} (X \leq 2) &= 1 / 6, \\
            \mathbb{P} (3 \leq X \leq 6) &= 1 / 4.
    \end{align*}
```
````

````{prf:example} Chute de pluie
:label: ex2_chute_pluie

La probabilité qu'il pleuve pendant une journée est de 0.2. S'il pleut, la quantité de pluie suit une loi exponentielle de paramètre $\lambda = 0.05$, exprimée en millimètres. Trouver la probabilité qu'il pleuve plus de 2mm.
```{admonition} Solution
:class: dropdown
Il faut utiliser ici la formule de la probabilité totale, car on connaît la loi conditionnelle de $X$ les jours de pluie. On utilise la partition $B_1 = $« jour de pluie » et $B_2 = $« jour sans pluie ». On a alors
\begin{align*}
        \mathbb{P} (X \geq 2mm) &= \mathbb{P}  (X \geq 2 | B_1) \mathbb{P}  (B_1) +  \underbrace{\Pr(X \geq 2 | B_2)}_{= 0} \mathbb{P}  (B_2)\\
        = \mathbb{P}  (X \geq 2) &= 0.2 \cdot \int_2^\infty \lambda \exp(-\lambda x) dx \\
            &= 0.2 \cdot \exp( - 0.05 \cdot 2 ) \\
            &\approx 0.180
    \end{align*}
```
````

````{prf:example} Chute de pluie 2
:label: ex3_chute_pluie

Supposons que la quantité de pluie qui tombe pendant une année suit une loi normale $ \mu = 140cm $ et $ \sigma^2 = 16cm^2 $. Quelle est la probabilité qu'il tombe entre 135 et 150 cm ?
```{admonition} Solution
:class: dropdown
Il faut standardiser la probabilité demandée pour trouver la réponse:
    
\begin{align*}
                \mathbb{P} (135 \leq X \leq 150) &= \mathbb{P} (-5 \leq X - \mu \leq 10) \\
        &= \mathbb{P} (-1.25 \leq \frac{X-\mu}{\sigma} \leq 2.5) \\
        &= \Phi(2.5) - \Phi(-1.25)           \\
        &= \Phi(2.5) - \bigg( 1 - \Phi(1.25) \bigg)
\end{align*}
On utilise enfin le formulaire du cours pour $ \Phi $ et on trouve:
\begin{gather*} \mathbb{P} (135 \leq X \leq 150) = 0.994 + 0.89 - 1 = 0.884. \end{gather*}
```
````
