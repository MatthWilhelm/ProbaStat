# Tests d'hypothèses statistiques

On peut résumer une approche scientifique selon le schéma suivant:
- théorie: énoncé d'une hypothèse.
- prédiction; on utilise la théorie pour prédire (et décrire) des résultats;
- expérience: récolte de données pour tester la prédiction;
- observation: **Non-rejet**, modification ou rejet de l'hypothèse.

La statistique reproduit ce cadre:
- hypothèse **ur les paramètres $ \theta $ d'un modèle statistique**;
- récolte de données;
- **Non-rejet ou rejet** de l'hypothèse: est-ce que l'écart entre prédiction et données est « significatif »? .

```{warning}
En science comme en statistique, le non-rejet d'une hypothèse n'est pas équivalent à une confirmation!
Par exemple
- La théorie de la gravité de Newton ne peut pas être rejetée par l'expérience à des échelles « humaines ». Mais on la sait désormais fausse pour des échelles très petites ou très grandes.
- Il est prouvé qu'il existe des énoncés logiques indécidables dont on ne peut pas savoir s'ils sont vrais ou faux (théorème d'incomplétude, par ex.).
```

## Hypothèse nulle et hypothèse alternative

```{prf:definition} Hypothèse nulle et hypothèse alternative
:label: hyp_nulle_alt
Étant donné un modèle $ F_\theta $, nous voulons décider entre deux théories:
- $ H_0 \subset \Theta $ l'hypothèse nulle, représentant le cas « normal, attendu » .
- $ H_1 \subset \Theta$ l'hypothèse alternative, représentant une alternative « surprenante, inattendue ».
Ce sont des hypothèses concernant le paramètre $ \theta $. On a nécessairement $H_0 \cap H_1 = \emptyset$. Par contre, il est possible que $H_0 \cup H_1 \neq \Theta.$
```

````{prf:example} 
:label: ex_test_hyp1
On fait passer à 14 sujets un test de dextérité avant et après qu'ils aient consommé 100ml de vin. Leur temps de réaction au test avant et après leur absorption de vin sont présentés dans le tableau suivant. Un score élevé signifie un ralentissement dans les réflexes.
```{figure} latex/PDFSVG/tab4_stat.svg
---
name: tab4_stat
width: 95%
---
```
On voudrait savoir si cette quantité d'alcool  ralentit les réflexes.     
```{admonition} Solution
:class: dropdown
A ce stade du cours, on n'a pas encore les outils pour faire un test d'hypothèse. Essayons de travailler avec les IC. D'abord, nous devons choisir un modèle. Par exemple, on pourrait modéliser les différences comme étant des variables Gaussienne: $ X_1, \dots, X_{14} \stackrel{idd}{\sim} (\mu,\sigma)$.
    Ces $n=14$ observations ont pour moyenne empirique et variance empirique:
\begin{gather*} \bar{x}_n = 3.5, \quad  s^2= 12.58 \approx 3.55^2.\end{gather*}
La question de départ devient alors: est-ce que $\mu = 0$?

L'intervalle de confiance de Student à $0.95$ \% pour $\mu$ est donc:
\begin{align*}
        \left[3.5 - \frac{2.16 \cdot  3.55}{\sqrt{14}} , 3.5 - \frac{2.16 \cdot 3.55}{\sqrt{14}} \right]     =
        \left[1.38, 5.62 \right],    
    \end{align*}
où $\mathbb{P}(-2.16 \leq T \leq 2.16) = 0.95,$ si $T \sim t_{13}$ (attention au nombre de degrés de libertés, $n-1$). L'intervalle des valeurs est donc entièrement composé de valeurs positives. Cette observation **suggère** (sur la base de cet échantillon et avec cette hypothèse) qu'il y a un effet de ralentissement.
    
En pratique, un test d'hypothèse à $5\%$ révèlerait effectivement l'existence d'un effet significatif.
```
````

Comment choisir entre les deux hypothèses? 
- Nous tirons un échantillon $X_1,\ldots,X_n$ de la population, donc: 
\begin{gather*} X_1,\ldots,X_n \stackrel{idd}{\sim} \mbox{Vraie Distribution.} \end{gather*}
- Il faut utiliser l'\'echantillon pour prendre notre d\'ecision.  
**Comment?**   

- Soit $T=T(X_1,...,X_n)$ une statistique prenant typiquement des valeurs ``petites'' sous l'hypothèse nulle $H_0$, c'est-à-dire **si l'hypothèse nulle est vérifiée**.
- Si on observe une valeur plutôt « extrême » de $T$ (« extrême »  dans la direction de l'alternative), l'évidence est contre $H_0$.

```{admonition} Règle de décision
:class: tip
Notre règle de décision sera:
- Rejeter $H_0$ si la valeur observée de $T$ est assez extrême (au-dela d'une **valeur critique**).
- Ne pas rejeter $H_0$ si la valeur observée de $T$ n'est pas assez extrême.
```

Examinons quelles sont les erreurs possibles.

```{figure} latex/PDFSVG/tabSmiley_stat.svg
---
name: tab4_stat
width: 95%
---
```

Erreur de type 1 = grave: on a rejeté $ H_0 $ alors qu'elle était vraie.

Erreur de type 2 = moins grave: on a conservé $ H_0 $ alors qu'elle est fausse.

Il y a une asymétrie entre ces deux types d'erreurs. Par exemple, si votre filtre de spam jette à la poubelle un email important, c'est une catastrophe.    

## Type de tests

```{prf:definition} Types de tests
:label: type_tests
Dans ce cours, nous allons essentiellement considérer le cas bilatéral:
\begin{gather*} H_0: \theta = \theta_0  \text{ versus }H_1: \theta \neq \theta_0. \end{gather*}
Il existe aussi des paires unilatérales:
\begin{gather*} \quad\underset{\mbox{paires unilatérales}}{\underbrace{\left\{\begin{array}{c}H_0:\mu=\mu_0 \\H_1:\mu> \mu_0\end{array}\right\}\quad\mbox{ou}\quad\left\{\begin{array}{c}H_0:\mu=\mu_0 \\H_1:\mu< \mu_0\end{array}\right\}}}.
 \end{gather*}
 ```

````{prf:example} Test bilatéral
:label:  ex_test_bilateral
Soit $X_1,...,X_n\stackrel{idd}{\sim}\mathcal{N}(\mu,\sigma^2) $ un échantillon aléatoire, et considérons la paire:
\begin{gather*} \left\{\begin{array}{c}H_0:\mu=\mu_0 \\H_1:\mu\neq \mu_0\end{array}\right\}.\end{gather*}
Cette paire est donc bilatérale. 
Considérons la statistique de test: $T=\dfrac{\overline{X}-\mu_0}{S/\sqrt{n}}$
- Si $H_0$ est vraie, alors $T\stackrel{H_0}{\sim}t_{n-1}$ et $T$ sera « petites », proche de 0.
- Nous considérons donc comme valeurs extrêmes (« extrême » est interprété en utilisant $H_1$) celles qui sont « loin » de 0.
- Nous allons rejeter $H_0$ si $|T|$ est assez grand,i.e. si $|T|>v^*$, où $v^*$ est la valeur critique.
 On appelle ce test le test de Student.

````

````{prf:example} Test unilatéral
:label: ex_test_unilateral
Soit $X_1,...,X_n \stackrel{idd}{\sim} \mathcal{N}(\mu,\sigma^2) $ un échantillon aléatoire, et considérons la paire:
\begin{gather*} \left\{\begin{array}{c}H_0:\mu=\mu_0 \\H_1:\mu< \mu_0\end{array}\right\}.\end{gather*}
Considérons la statistique de test: $T=\dfrac{\overline{X}-\mu_0}{S/\sqrt{n}}$
- Si $H_0$ est vraie, alors $T\stackrel{H_0}{\sim}t_{n-1}$.
- Nous considérons comme des valeurs extrêmes (interprété en utilisant $H_1$) celles qui sont  « loin » de 0.
- Mais « loin »  en direction de l'hypothèse alternative!
- Alors, nous allons rejeter $H_0$ si $T$ est **assez négative**, $T<v_*$.
````

```{figure} PDFSVG/plot_unilateral.svg
---
name: plot_unilateral
width: 95%
---
```
## Cadre Statistique

### Signification statistique

Nous voulons choisir une règle de décision de telle sorte à limiter la probabilité d'erreur de type I, c'est à dire:
\begin{gather*} \mathbb{P}[\mbox{Rejet de }H_0|H_0\mbox{ est vraie}]\leq \alpha,\end{gather*}
où $\alpha$ est une petite valeur (typiquement $\alpha=0.05$), le **niveau de signification du test**.  

- Nous choisissons la valeur critique en exigeant $\mathbb{P}[\mbox{Rejet de }H_0|H_0\mbox{ est vraie}]= \alpha$, la limite supérieure tolérée pour la probabilité d'erreur de type I.
- C'est-à-dire, nous devons trouver une **valeur critique** telle que
\begin{gather*}\mathbb{P}[T\mbox{ est au-delà de la valeur critique}|H_0\mbox{ est vraie}]= \alpha.\end{gather*}

Reprenons le cas du test de Student. 
Nous allons rejeter $H_0$ si $|T|=\left|\frac{\overline{X}_n-\mu_0}{S/\sqrt{n}}\right|$ est **assez grande**, c'est à dire $|T|>v^*$.

Choix de la valeur critique: il faut respecter le niveau de signification, ainsi,
\begin{align*}
& \mathbb{P}[\mbox{Rejet de }H_0|H_0\mbox{ est vraie}]= \alpha\\
\Longleftrightarrow\quad& \mathbb{P}[|T|>v^*|H_0\mbox{ est vraie}]= \alpha\\
\Longleftrightarrow\quad& \mathbb{P}[T\leq -v^*\mbox{ ou }T\geq v^*|H_0\mbox{ est vraie}]= \alpha
\end{align*}
ce qui implique
\begin{gather*}
v^*=t_{n-1;1-\alpha/2},
\end{gather*}
où $t_{n-1;1-\alpha/2}$ est le quantile $(1-\alpha/2)\%$ de la loi de Student $t_{n-1}$.

### La valeur $p_{obs}$

Au lieu d'utiliser des valeurs critiques pour décider entre $H_0$ et $H_1$, nous pouvons utiliser une autre approche, basée sur la notion de **la valeur $p_{\rm obs}$** (appelée **$p$-valeur**).
- La valeur $p_{\rm obs}$ est la probabilité d'obtenir une valeur de la statistique de test, aussi extrême ou plus extrême encore que celle que nous avons observé (dans la direction de l'alternative) si $H_0$ était vraie.
- Mathématiquement, si nous avons observé $T=t_{\rm obs}$
    * Cas bilatéral: $p_{\rm obs}=\mathbb{P}[|T| > t_{\rm obs}|H_0]$
    * Cas unilatéral à gauche: $p_{\rm obs}=\mathbb{P}[T \leq t_{\rm obs}|H_0]$
    * Cas unilatéral à droite: $p_{\rm obs}=\mathbb{P}[T > t_{\rm obs}|H_0]$
Des valeurs $p_{\rm obs}$ « assez petites » s'opposent à $H_0$ (ils démontrent que la realité observée serait très improbable si notre hypothèse était vraie).


Comment décider le rejet ou non de l'hypothèse nulle en utilisant la $p_{\rm obs}$?

- Nous suivons la même approche que nous avons établie avec le **niveau de signification**.
    * Nous choisissons une probabilité  $\alpha$ maximale d'erreur de type I que nous allons tolérer:
    \begin{gather*}\mathbb{P}[\mbox{Rejet de }H_0|H_0\mbox{ est vraie}]\leq \alpha,\end{gather*}
    par exemple $\alpha=0.05$.
    * Notre règle de décision sera: **Rejeter $H_0$ si $p_{\rm obs}\leq \alpha$**
    * La probabilité d'erreur de type I en utilisant cette règle de décision est exactement $\alpha$.
    * Cette approche est **équivalente** à l'approche des valeurs critiques.

```{figure} PDFSVG/plot_bilateral.svg
---
name: plot_bilateral
width: 95%
---
```

```{admonition} Compte-rendu: les éléments d'un test
- Une <font color="red">hypothèse nulle</font> $H_0$ à tester, contre une alternative $H_1$.  
- Une <font color="red">statistique de test</font> $T$, choisie de telle sorte que des valeurs "extrêmes" de $T$ (en direction de $H_1$) suggèrent que $H_0$ est fausse. La valeur observée de $T$ est $t_{\rm obs}$.  
- Un <font color="red">niveau de signification</font> $\alpha$, qui est le plafond pour l'erreur de type I (rejet de $H_0$ quand $H_0$ est vraie) que nous allons tolérer.
- Des <font color="red">valeurs critiques</font>, telles que quand $T$ tombe au-delà de ces valeurs, nous rejetons $H_0$ en faveur de $H_1$. Les valeurs critiques sont choisies pour respecter le niveau de signification $\alpha$.

 <font color="blue">Au lieu de l'approche basé sur les valeurs critiques, nous pouvons utiliser l'approche équivalente basé sur la valeur $p_{\rm obs}$:</font>
- Une <font color="red">valeur $p_{\rm obs}$</font> donnant la probabilité d'observer  une valeur de $T$ aussi extrême ou plus extrême que $t_{\rm obs}$ sous $H_0$. On rejette alors $H_0$ en faveur de $H_1$ quand $p_{\rm obs}\leq \alpha$.
```

## La statistique de test $T$

- On est libre de choisir $T$, de telle sorte que plus sa valeur est grande,  plus l'indication contre $H_0$ est forte.
- Le choix de $T$ dépend de l'**hypothèse alternative** $H_1$ --- ce que l'on imagine possible, si $H_0$ est fausse.
-  Plus $H_1$ est précise, plus on peut choisir une statistique $T$ appropriée.

```{prf:example} 
:label: ex_test_hyp2
Supposons que l'on lance une pièce $n$ fois indépendamment et que l'on considère que si on obtient « pile », cela vaut 1, et 0 sinon. On observe $k$ piles. Quelle est la probabilité que la pièce soit effectivement équilibrée? Comparons différentes hypothèses alternatives.

Soient $X_1, \dots, X_{n}$ les variables modélisant le lancer.    
Soit:
\begin{gather*}T = \frac{1}{n}\sum_{i=1}^{n}X_i  - \frac{1}{2}. \end{gather*}
Considérons en en premier temps la paire $H_0: p = \frac{1}{2}$ contre $H_1: p \neq \frac{1}{2} $. 
Soit $\alpha = 0.05$ le niveau de signification requis. Alors, la valeur critique doit satisfaire
\begin{align*}
    \alpha & = \mathbb{P}(\left|T\right| > v^* | H_0) = \mathbb{P}\left(\left|\frac{1}{n}\sum_{i=1}^{n}X_i  - 1/2\right| > v^*\right) 
    \\
    & = 1 - \mathbb{P}\left(n(- v^* + 1/2) \leq \sum_{i=1}^{n}X_i \leq n( v^* + 1/2) \right)\\
    &= 1 -  F_X\left(n( v^* + 1/2) \right) + F_X\left(n(- v^* + 1/2) +1  \right).
    \end{align*}

où $X= \sum_{i=1}^{n}X_i$ suit, sous $H_0$, une loi binomiale $\mathcal{B}(n, p_0 = \frac{1}{2}).$ 
On détermine alors le seuil critique comme étant la valeur $v^*$ qui satisfait cette équation. 

On s'intéresse à présent à la paire d'hypothèses
$H_0: p = \frac{1}{2}$ contre $H_1: p > \frac{1}{2} $. Alors, la valeur critique doit satisfaire
\begin{align*}
    \alpha & = \mathbb{P}(T > v^* | H_0) = \mathbb{P}\left(\frac{1}{n}\sum_{i=1}^{n}X_i  - 1/2 > v^*\right) 
    \\
    & = 1 - \mathbb{P}\left[\sum_{i=1}^{n}X_i \leq n( v^* + 1/2) \right]\\
    &= 1 -  F_X\left[n( v^* + 1/2) \right]\\
    & \Leftrightarrow F_X^{-1}(1- \alpha) = n( v^* + 1/2) \Leftrightarrow \frac{1}{n}\left[F_X^{-1}(1- \alpha)\right] - \frac{1}{2}=v^*.
    \end{align*}  
    
Supposons à présent que l'on observe $n= 30$ lancers dont $k = 19$ « piles », autrement dit, on a $\sum_{i=1}^n x_i = k$ et donc $T = k/n - 1/2$. On veut tester l'hypothèse  $H_0: p = \frac{1}{2}$ contre $H_1: p > \frac{1}{2} $. On calcule alors la $p-$valeur suivante:
\begin{gather*}p_{\rm obs}=\mathbb{P}[T > t_{\rm obs}|H_0] = 0.049 < 0.05.\end{gather*}

En effet, en posant $X \sim \mathcal{B}(n, 1/2),$ on a:
\begin{align*}
\mathbb{P}(T > t_{\rm obs}|H_0) & =  \mathbb{P}\left( \frac{1}{n} \sum_{i= 1}^n X_i - 1/2 > \frac{1}{n} \sum_{i= 1}^n x_i - 1/2\right) \\
& = 1 - \mathbb{P}\left( \sum_{i= 1}^n X_i  \leq  k  \right) = 1- F_X\left(k\right).  \\
\end{align*}  
  
Supposons à présent que l'on teste l'hypothèse  $H_0: p = \frac{1}{2}$ contre $H_1: p \neq \frac{1}{2} $. De manière similaire, on obtient alors
\begin{align*}
p_{\rm obs} &= \mathbb{P}(\left|T\right|> t_{\rm obs}|H_0)   =1 - \mathbb{P}\left( \left|\frac{1}{n} \sum_{i= 1}^n X_i - 1/2\right| \leq  \frac{k}{n} - 1/2\right) 
\\ 
& = 1 - \mathbb{P}\left( -\frac{k}{n} + 1/2 \leq  \frac{1}{n} \sum_{i= 1}^n X_i - 1/2 \leq  \frac{k}{n} - 1/2\right)\\
& = 1 - \mathbb{P}\left( n - k \leq  \frac{1}{n} \sum_{i= 1}^n X_i\leq k\right)\\
& = 1-  F_X\left(k\right) + F_X\left(n- k +1\right).  \\
& = 0.230 > 0.05

\end{align*}

```

```{prf:remark}
:label: test_hyp_remarque1
On a donc une $p-$valeur inférieure au seuil de 5\% dans le cas où on teste l'hypothèse $H_1: p > 1/2$ mais pas dans le cas $H_1: p \neq 1/2$.
- L'hypothèse alternative conditionne donc notre rejet ou pas de l'hypothèse nulle.
- On pourrait en conclure que choisir $H_1: p > 1/2$ est plus judicieux. Mais il s'agirait **d'une faute scientifique grave!**
- L'hypothèse nulle, l'hypothèse alternative ainsi que la statistique de test doivent être choisis **avant** de récolter les données!
```

```{admonition} $p-$hacking
L'une des fraude scientifique les plus fréquentes consiste à faire ce que l'on appelle du *$p-$hacking*, qui consiste à faire plusieurs tests différents jusqu'à trouver quelque chose de statistiquement significatif. Dans l'exemple que nous avons considéré, en regardant les données (19 piles), on pourrait penser que la pièce est biaisée vers pile et donc choisir de tester $H_0: p = \frac{1}{2}$ contre $H_1: p > \frac{1}{2} $. Cependant, ce choix se révèle être *conditionnel aux données observées*: notre choix de l'hypothèse alternative est influencé par les données observées. Il s'agit d'une erreur de raisonnement.
```

Il existe des méthodes pour tenir compte du fait que plusieurs tests sont effectués. En particulier:
- correction Bonferroni;
- procédure de Holm-Bonferroni;
- procédure de Benjamini-Hochberg. 

De manière générale, il suffit de rechercher le mot clé « tests multiples ». 
