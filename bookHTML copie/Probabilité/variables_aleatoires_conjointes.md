# Variables aléatoires conjointes

```{prf:definition} Variables aléatoires conjointes
:label: var_conjointes
Soient $X,Y$ deux variables définies sur le même ensemble fondamental. La fonction:
    
\begin{gather*} F_{X,Y}(x,y) = \Pr(X \leq x, Y \leq y) \end{gather*}
        
est la **fonction de répartition conjointe (ou jointe ou simultanée)** de $X$ et $Y$.
On peut aussi considérer que $(X,Y)^\top$ est un vecteur aléatoire, c'est-à-dire une variable aléatoire à deux dimensions.
```


````{prf:definition} Fonction de masse et densité conjointes
:label: fct_masse_dens_conj
On différencie les cas discret et continu.
- **Cas discret**: La loi de probabilité conjointe est complètement caractérisée si on connait les valeurs de la fonction de masse conjointe $f_{X,Y}(x_i,y_j) = \Pr(X=x_i \text{ et } Y=y_j),$ pour tous les couples possibles.
- **Cas continu**: il suffit de connaitre la densité conjointe $f_{X,Y}(x,y)$ de $X,Y$ qui est la fonction qui satisfait:
\begin{gather*}\Pr(X \in A) = \iint_{A} f_{X,Y}(x,y)\ dxdy, \quad \text{ pour tout } A\subset \mathbb{R}^2 \end{gather*}

````

````{prf:theorem} Fonction d'un vecteur aléatoire
:label: fct_vec_aléatoire

Soit $\mathbf{X}= (X_1, \dots, X_m)$ un vecteur aléatoire avec densité jointe $f_{X}(x_1, \dots,x_m) = f_{X}(\mathbf{x})$ et soit $g: \mathbb{R}^m \rightarrow \mathbb{R}^m$ une fonction bijective continûment différentiable, admettant pour fonction réciproque $g^{-1} = h$. Soit $\mathbf{Y} = g(\mathbf{X})$. Alors on a
\begin{gather*} f_Y(\mathbf{y}) = f_X\left(h(\mathbf{y})\right) J_h(\mathbf{y}),  \end{gather*}
où $J_h(\mathbf{y}) $ est le **déterminant** de la matrice jacobienne de $h$, c'est-à-dire
\begin{gather*}J_h(\mathbf{y}) =\left|\begin{pmatrix}
\frac{\partial h_1}{\partial y_1} & \dots & \frac{\partial h_1}{\partial y_m}\\
\vdots & &\vdots \\
\frac{\partial h_m}{\partial y_1} & \dots & \frac{\partial h_m}{\partial y_m}
\end{pmatrix}\right|. \end{gather*} 
````

En fait, la démonstration de cette formule se fait à l'aide de la formule classique de changement de variable. Comme la probabilité est l'intégrale sur un certain domaine de la fonction de densité, on obtient le résultat immédiatement. Pour plus de détails, voir par [exemple](https://swisscovery.slsp.ch/permalink/41SLSP_NETWORK/19n6r1g/alma991026360829705501):
Dalang, R. C. et Conus, D. (2015), *Introduction à la théorie des probabilités*, Lausanne, Suisse: PPUR.

````{prf:definition} Lois marginales: fonction de répartition
:label: fct_repartition_marginale
On appelle **fonction de répartition marginale** les fonctions suivantes:
- **cas discret** $F_X(x) = \sum_{i,x_i \leq x} f_X(x_i) $;
- **cas continu** $F_X(x) = \int_{-\infty}^x f_X(u) du $.
````

````{prf:example} Loi marginale
:label: ex1_var_aleatoire_conj

Soient $X,Y$ des variables aléatoire qui prennent les 5 valeurs $(1,2)$, $(1,4)$, $(2,3), $(3,2)$, (3,4)$ avec probabilités égales. Trouver les lois marginales de $X$ et $Y$.
````

````{prf:definition} Fonction de masse et densité marginales
:label: fct_masse_dens_marginale
Soient $(X,Y)$ deux variables aléatoires avec densité (ou fonction de masse) conjointe $f_{X,Y}(x,y)$.
On appelle :
- **cas discret**: *fonction de masse marginale* $ f_X(x_i) = \sum_j f_{X,Y}(x_i,y_j)  = \Pr(X = x_i)$;
- **cas continu**: *densité marginale* de $X$ la fonction $ f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x,y) dy $.
````

````{prf:definition} Indépendance de variables aléatoires
:label: independance_var_alea
On peut généraliser la notion d'indépendance d'événements à des variables conjointes.
$X,Y$ sont dite **indépendantes** si:
- **cas discret** $ \Pr(X=x_i, Y=y_j) = \Pr(X=x_i) \Pr(Y=y_j) $;
- **cas continu** $ f_{X,Y}(x,y) = f_X(x) f_Y(y). $
Dans les deux cas, on a:
    \begin{gather*} F_{X,Y}(x,y) = F_X(x) F_Y(y). \end{gather*}
````

````{prf:example} Somme de Bernouilli indépendantes
:label: ex2_independance

Considérons $n$ variables de Bernoulli indépendantes $I_1,\dots, I_n,$ avec même probabilité de succès $p$. Quelle est la distribution de la somme de ces variables?    

```{admonition} Solution
:class: dropdown
L'expérience que l'on a décrit pour définir une loi binomiale $\mathcal{B}(n,p)$ consiste en fait exactement à considérer la somme de $n$ variables de Bernoulli \textit{indépendantes} avec chacune probabilité $p$ de succès. Cette somme suit donc une loi binomiale.
    Soient $I_1,\dots, I_n \stackrel{iid}{\sim}\mathcal{B}(p).$ Alors 
\begin{gather*} X = \sum_{i = 1}^n I_i \sim \mathcal{B}(n,p). \end{gather*}
```
````


```{prf:theorem} Fonctions de variables aléatoires indépendantes
:label: fct_var_ind
Soient $X_1, \dots, X_n$ des variables indépendantes (pas nécessairement identiquement distribuées) et $g_1, \dots, g_n$ des fonctions continues. Alors les variables aléatoires $g_1(X_1), \dots, g_n(X_n)$ sont aussi indépendantes.
```

Il existe un résultat plus fort, l'hypothèse de continuité étant trop forte.  

De manière générale, les lois marginales **ne suffisent pas** à caractériser la loi jointe.
Par contre, si $X$ et $Y$ sont indépendantes, les lois marginales suffisent à caractériser la loi jointe. 

**Notation:** On écrit $X_1 \dots X_n \stackrel{iid}{\sim} f$ pour dire que $X_1 \dots X_n$ sont des variables **indépendantes et identiquement distribuées** de densité marginale $f$.

```{prf:remark} Précisions pour les conjointes continues
:label: remarque_1

La loi jointe de variables aléatoires $X,Y$ continues peut être caractérisée par $f_{X,Y}(x,y) $ ou $F_{X,Y}(x,y)$. On a la relation suivante:
\begin{gather*} F_{X,Y}(x,y) = \Pr(X\leq x, Y \leq y) = \int_{-\infty}^x  \int_{-\infty}^y f_{X,Y}(u,v)\ du dv. \end{gather*}
```

```{prf:property} Lois conjointes
:label: propriete_loi_conjointe
On a les propriétés suivantes pour deux variables aléatoires $X,Y$ continues:
- $\displaystyle f_{X,Y}(x,y) \geq 0$;
- $\displaystyle \int_{-\infty}^\infty \int_{-\infty}^\infty f_{X,Y}(u,v)dudv = 1$;
- $\displaystyle f_{X,Y}(x,y) = \frac{\partial^2} { \partial x \partial y} F_{X,Y}(x,y) $;
- $\displaystyle \Pr(a_1 \leq X \leq a_2, b_1 \leq Y \leq b_2) = \int_{a_1}^{a_2} \int_{b_1}^{b_2} f_{X,Y}(u,v) du dv $.
- Plus généralement, pour tout $A\subset \mathbb{R}^2$, on a 
\begin{gather*} \Pr\left( (X,Y) \in A\right) = \iint_{A} f_{X,Y}(u,v)\  du dv .\end{gather*}
```


````{prf:example} 
:label: ex4

Considérons $X_1,X_2 \stackrel{iid}{\sim} \mathcal{N}(\mu,\sigma^2) $. Trouver leur densité conjointe.  
Supposons que $\mu=3, \sigma^2 = 4$. Calculer:
\begin{gather*} \Pr(X_1 \leq 1 \text{ et } -1 \leq X_2 \leq 5) = \dots \end{gather*}    

```{admonition} Solution
:class: dropdown
Leur densité conjointe est le produit des densités marginales (indépendance):
\begin{gather*} f(x_1, x_2) = \frac{1}{2\pi} \frac{1}{\sigma^2} \exp \left( - \frac{(x_1-\mu)^2 + (x_2 - \mu)^2}{2 \sigma^2} \right).\end{gather*}
On calcule la probabilité en utilisant l'indépendance puis en standardisant:
\begin{align*}
        \Pr(X_1 \leq 1\text{ et }-1\leq X_2 \leq 5) = \Pr(X_1 \leq -1) \Pr(-1 \leq X_2 \leq 5).
\end{align*}
On a d'une part
\begin{gather*} \Pr(X_1 \leq 1) = \Pr\left(\frac{X_1-3}{2} \leq -1 \right) = \Phi(-1) = 0.159, \end{gather*}
et par ailleurs
\begin{gather*}       \Pr(-1 \leq X_2 \leq 5) = \Phi(1) - \Phi(-2) = 0.82. \end{gather*}
Et donc $\Pr(X_1 \leq 1\text{ et }-1\leq X_2 \leq 5)  \approx 0.13.$
```
````


````{prf:definition} Densité et fonction de masse conditionnelle
:label: dens_conditionnelle
La densité (ou fonction de masse) conditionnelle de $X$ étant donné $Y=y$ est définie par:
\begin{gather*} f_{X|Y}(x|y) = \frac{f_{X,Y}(x,y)}{f_Y(y)}. \end{gather*}  

Si $ X, Y$ sont indépendantes, alors la densité conditionnelle est égale à la densité marginale $ f_{X|Y}(x,y) = f_X(x). $ Ceci est vrai pour des variables discrètes ou continues.
````

````{prf:example} 
:label: ex4

$X,Y$ ont pour densité conjointe:
\begin{gather*} f_{X,Y}(x,y) = \left\{ \begin{array}{cl} x+y & \text{si } 0<x<1, 0<y<1, \\ 0 & \text{sinon.}    \end{array} \right. \end{gather*}
Calculer les densités marginales de $X$ et $Y$. Est-ce que $X,Y$ sont indépendantes?    

```{admonition} Solution
:class: dropdown
Les densités marginales sont:
\begin{align*}
        f_X(x) &= \int_0^1 (x+y) dy = x + 1/2,          \\
        f_Y(y) &=  y + 1/2.
    \end{align*}
Ces variables ne sont pas indépendantes. En effet, on a 
\begin{align*}
        f_X(x)f_Y(y) = (x+1/2)(y+1/2) \neq (x+y) = f_{X,Y}(x,y).
    \end{align*}
```
````
