# Théorème fondamentaux

```{math}
\newcommand\E{\mathbb{E}}
\newcommand\var{\text{Var}}
\newcommand\cov{\text{Cov}}
\newcommand\corr{\text{Corr}}
```

Quand on définit des systèmes complexes à l'aide de la théorie des probabilités, on obtient souvent des distributions de probabilités particulièrement difficiles à manipuler et à utiliser.

On va présenter deux théorèmes clés qui permettent d'approximer ces probabilités difficiles.
- Inégalité de Tchebychev.
- Loi des Grands Nombres.
- Théorème Central Limite.

## Une première approche expérimentale

Alice veut intégrer l'équipe de basket. Pour cela, elle doit prouver qu'elle est capable de marquer souvent des paniers. Comment pouvons nous mesurer le taux de réussite d'Alice?

Principe de la statistique:
- Proposer un modèle probabiliste de la situation.
  Soit $ X_i $ la variable représentant la réussite du i-ème lancer. Un choix possible: $ X_i \stackrel{idd}{\sim} \mathcal{B}(p) $.
- Trouver une procédure qui, à l'aide des valeurs observées de $ X_1 \dots X_n $, retrouve la valeur des paramètres inconnus. Ici: retrouver le taux de réussite $ p $.

Idée basique: 
    
- Alice lance $ n $ fois.
- On note son taux de réussite dans ces $ n $ lancers.
- **Intuitivement**, ce taux de réussite expérimental va être **proche** de son vrai taux de réussite.
- **Intuitivement**, plus $n$ est grand, plus les deux valeurs devraient être proches.

Si $ X_i \sim \mathcal{B}(p) $ représente le $i$-ème lancer et vaut 1 s'il est réussi, 0 sinon, le nombre total de lancers réussis suit une loi binomiale et est donc
\begin{equation*} S = \sum_{i=1}^n X_i \sim \mathcal{B}(n,p). \end{equation*}
La proportion de lancers réussis est $\displaystyle \overline{X} = \frac{S}{n}. $
    On a alors
\begin{gather*} \E[ \overline{X} ] = \frac{\E[ S ]}{n} = \frac{np}{n}  = p,\end{gather*}
et
\begin{gather*} \var( \overline{X} ) =\frac{ \var(S)}{n^2} =\frac{n p(1-p)}{n^2} = \frac{p (1-p) }{n}.\end{gather*}
Plus $ n $ est grand et plus  $ \overline{X} $ est « certain ».

## Théorèmes fondamentaux

```{prf:theorem} Loi des grands nombres
:label: LGN
Soient $X_1, \dots, X_n, \dots$ une suite de variables aléatoires réelles indépendantes et identiquement distribuées, d'espérance $\E[X_1] = \mu < \infty$ et de variance finie $\var(X_1) = \sigma^2 < \infty$. Pour tout $n \in \mathbb{N},$ soit 
\begin{gather*}\overline{X}_n =\frac{1}{n} \sum_{k = 1}^n X_k.\end{gather*}
Alors pour tout $\varepsilon >0$, on a
\begin{gather*}\lim_{n\rightarrow \infty} \Pr\left(\left| \overline{X}_n - \mu  \right| > \varepsilon\right)  = 0.\end{gather*}
```

```{note}
Une démonstration de ces trois résultats est donnée sur la page du cours. Ici, nous donnons la preuve par soucis de complétude, mais les démonstrations **ne sont pas matière à examen**.

En revanche, les énoncés précis des résultats sont à connaître.
```

```{figure} PDFSVG/Evolving_mean.svg
--- 
name: Evolving_mean
width: 95%
---
: Illustration pour des variables $ X \sim \text{Exp}(1) $.
```


```{prf:proposition} L'inégalité de Markov
:label: Markov
Soit $X$ une variable aléatoire réelle \textbf{positive} de moyenne $\E[X] = \mu < \infty$. Alors pour tout $\varepsilon > 0$, on a:
\begin{gather*} \Pr(X > \varepsilon ) \leq \frac{\E[X]}{\varepsilon}. \end{gather*}
```

```{prf:proposition} L'inégalité de Tchebychev
:label: Tchebychev
Soit $X$ une variable aléatoire réelle de moyenne $\E[X] = \mu < \infty$ et de variance finie $\var(X) = \sigma^2 < \infty$. Alors pour tout $\varepsilon > 0$, on a:
\begin{gather*} \Pr(| X - \mu | > \varepsilon ) \leq \frac{\sigma^2}{\varepsilon^2}. \end{gather*}
```

La LGN ne nous parle pas de la taille des erreurs de $ \overline{X} \approx \mu $. Pour cela, il faut le TCL.
    
Soit $\mu, \sigma^2 $ la moyenne et variance commune des $ X_i $. Considérons la version standardisée de $ \overline{X} $:
    
\begin{gather*} Z_n = \frac{\overline{X}_n - \E[\overline{X}_n] }{ \sqrt{\var\left(\overline{X}_n\right)}} = \sqrt{n} \frac{ \overline{X}_n -\mu}{\sigma}. \end{gather*}
        
La distribution de $ Z_n $ serait très compliquée à calculer exactement (intégrale de dimension n-1 ). Heureusement, la distribution de $ Z_n $ est approximativement simple si le nombre d'observations $ n $ est suffisamment grand.

```{prf:theorem} Théorème central limite
:label: TCL
Soient $X_1, \dots, X_n, \dots$ une suite de variables aléatoires réelles indépendantes et identiquement distribuées de moyennes et de variances communes $\mu$ et $\sigma^2 $ respectivement. Alors, pour $ n \rightarrow \infty$, $ Z_n $ est approximativement Gaussienne, c'est-à-dire qu'on a:
\begin{gather*} \Pr( Z_n \leq z ) \stackrel{n\rightarrow\infty}{\longrightarrow} \Phi(z).\end{gather*}
Donc, pour $ n $ suffisamment grand, 
\begin{gather*}\overline{X}_n \stackrel{\dot}{\sim} \mathcal{N}(\mu, \sigma^2 / n)\end{gather*}
```

```{figure} PDFSVG/convergence_TCL_exp.svg
--- 
name: convergence_TCL_exp
width: 95%
---
: Illustration du TCL pour $ X_i \stackrel{idd}{\sim} exp(1) $. En noir, la vraie fonction de distribution et en rouge son approximation Gaussienne $ \Phi $.
```

```{figure} PDFSVG/convergence_TCL_exp_histo.svg
--- 
name: convergence_TCL_exp_histo
width: 95%
---
: Illustration du TCL pour $ X \sim exp(1) $. Histogramme empirique, vraie densité (bleu) et densité Gaussienne (rouge).
```

````{prf:example}
Soit $ X \sim \mathcal{B}(n,p) $, donner une approximation pour $ \Pr( X \leq r)$.
```{admonition} Solution
:class: dropdown
Une variable Binomiale correspond à une somme de variables de Bernoulli IID. Si $ n $ est suffisamment grand, on peut donc appliquer le TCL.
    
On calcule la probabilité demandée par standardisation
    
\begin{align*}
        \Pr(X \leq r ) &= \Pr(X - n p \leq r - n p) \\
                &= \Pr \left(\frac{X - n p}{\sqrt{n  p  (1-p)}} \leq \frac{r - n  p}{\sqrt{n  p  (1-p)}} \right) \\
                & \approx \Phi \left( \frac{r - n  p}{\sqrt{n  p  (1-p)}} \right)
    \end{align*}
```
````


````{prf:example}
Soit $ X_1 \dots X_n \stackrel{idd}{\sim} \exp(\lambda) $. Donner une approximation pour:
        
\begin{gather*} \Pr(X_1 + \dots + X_n \leq r) \end{gather*}
```{admonition} Solution
:class: dropdown
De nouveau, on a affaire a une somme de variables IID. On peut donc appliquer le TCL. On trouve la moyenne et variance de la loi exponentielle soit par calcul, soit dans le formulaire du cours. En l'occurrence, on a
\begin{gather*}\E[X_1] = \frac{1}{\lambda},\quad \var(X_1) = \frac{1}{\lambda^2} \Rightarrow \sqrt{\var(X_1)} = \frac{1}{\lambda}.\end{gather*}
    
\begin{align*}
        \Pr( X_1 + \dots + X_n \leq r ) &= \Pr(\overline{X}_n - \frac{1}{\lambda} \leq r/n - \frac{1}{\lambda}) \\
                &= \Pr \left(\frac{\overline{X}_n - \frac{1}{\lambda}}{\frac{1}{\sqrt{n}\lambda}} \leq \frac{r - \frac{n}{\lambda}}{\frac{n}{\sqrt{n}\lambda}}  \right) \\
                & \approx \Phi \left( \frac{r - n / \lambda}{\sqrt{n} / \lambda} \right) =  \Phi \left( \frac{\lambda r - n}{\sqrt{n}} \right).
    \end{align*}    
```
````

```{prf:remark} Remarques avancées sur le TCL
:label: remarque_avancee

Le TCL est simultanément le théorème le plus connu et le plus mal compris de la théorie des probabilités.  
    
L'erreur la plus fréquente consiste à croire que tout est Gaussien, à cause du TCL.  
    
TCL, version intuitive: « tout $ S $ obtenue par somme de $ X_i $ **suffisament nombreux** et **suffisament indépendants** (et **tous petits**) est approximativement Gaussien.»
    
La condition d'avoir assez de $ X_i $ est souvent vérifiés. Les hypothèses qui font défaut sont en général l'indépendance ou l'absence de moyenne/variance finie.
```

Les problèmes d'une application aveugle du TCL peuvent être multiples, et il faut y prendre garde.
- moyenne ou variance infinie: certaines variables aléatoires n'ont pas de moyenne finie (Cauchy, par exemple). Dès lors, le TCL ne s'applique pas. En particulier la distribution Gaussienne n'a  pas de « queues lourdes », elle est incapable de quantifier l'incertitude pour des hauts quantiles. 
- indépendance: parfois, l'hypothèse d'indépendance est (fortement) violée et il est dangereux de se fier à une approximation Gaussienne dans ces cas.

````{prf:example} Taille et TCL
:label: ex_taille_tcl
Chez les êtres humains, la distribution de la taille est approximativement Gaussienne.
Proposez une explication intuitive de cette observation basées sur le TCL.
```{admonition} Solution
:class: dropdown
La taille d'une personne est le résultat de plein de causes faibles qui ont toutes des effets aléatoires relativement indépendants. En effet, on peut raisonnablement écrire que la taille $X_i$ d'un individu $i$ peut s'écrire comme 
\begin{gather*} X_i = \mu + \varepsilon_i, \end{gather*}
où $\mu$ est une moyenne globale et $\varepsilon_i$ un écart à la moyenne. Ainsi, selon ce modèle, $\overline{X} \sim \mathcal{N}(\mu, \sigma^2)$ si $\overline{\varepsilon} \sim \mathcal{N}(0, \sigma^2), $ où $\overline{\varepsilon} =1/n \sum_i \varepsilon_i$. Cela peut être justifié si les $\varepsilon_i$ sont indépendants et identiquement distribués, ce qui est vraisemblable. On peut donc appliquer des variantes du TCL de manière raisonnable.   
```
````

````{prf:example} Taille, TCL, et dimorphisme sexuel
:label: ex_taille_tcl_dimorphisme
Chez d'autres animaux, la distribution des tailles n'est pas Gaussienne car les individus mâles et femelles ont des tailles très différentes.  Pourquoi est-ce que l'explication précédente ne s'applique plus ici?
```{admonition} Solution
:class: dropdown
Dans des espèces avec un fort dimorphisme sexuel, le sexe d'un animal joue un role prépondérant sur sa taille. L'influence de cette variable est tellement important que le TCL ne s'applique plus. On aurait plutôt une distribution *bimodale* et où chacun des deux modes pourrait raisonnablement être approximé par une loi normale. 
```
````

```{prf:theorem} TCL de Berry-Esseen
Soient $ X_i $ iid tels que $ \E(X) = \mu $, $ \var(X) = \sigma^2 $ et $ \E(|X-\mu|^3) = \kappa$ et soit 
\begin{gather*} Z_n = \sqrt{n} \frac{\overline{X} - \mu}{\sigma} = \frac{1}{\sigma \sqrt{n}} \sum_{i=1}^n (X_i-\mu).\end{gather*}
Alors, l'erreur de l'approximation Gaussienne est bornée par:
\begin{gather*} | \Pr(Z_n \leq z) - \Phi(z) | \leq \frac{0.5 \kappa}{\sigma^3 \sqrt{n}}.\end{gather*}
```

```{note}
Cette borne est plutôt pessimiste, mais elle est très générale, car ne dépendant pas de la distribution des $X_i$ et n'étant pas asymptotique.
```

````{prf:example} TCL de Berry-Esseen
:label: ex_TCL_de_Berry-Esseen
Pour $ \mu = 0, \sigma = 1, \kappa = 8, n = 10000$, trouvez un intervalle de la forme $]-\infty,a]$ qui contient $ 95\%$ de la probabilité de $ Z_n $
    
\begin{gather*} Z_n = \frac{\sum_{i=1}^n X_i}{\sqrt{n}} \end{gather*}    
    
Comparez à l'approximation Gaussienne naïve.
```{admonition} Solution
:class: dropdown
L'approximation Gaussienne naïve nous donne:
    
\begin{align*}
        \Pr(Z_n \leq a) &= \Phi(a) \\
    \end{align*}
L'approximation Gaussienne naïve nous dit donc de choisir $ a \approx 1.60 $.
Le TCL de Berry-Esseen nous donne à la place:
    
\begin{align*}
        \Pr(Z_n \leq a) &\geq \Phi(a) - \frac{0.5\kappa}{\sigma^3\sqrt{n}} \\
                & \geq \Phi(a) - 0.04
    \end{align*}
    
La valeur naïve $ a \approx 1.60 $ garantie donc uniquement une probabilité de 
$ 0.91 < 0.95 $. Pour garantir une probabilité de 0.95, il faut utiliser $ a^\star = 2.33 $.
NB: cette borne est pessimiste, mais elle montre bien que le décalage entre l'application naïve du TCL et une application avec de bonnes garanties.
```
````

```{prf:definition} Fonction de répartition empirique
:label: fct_repart_empirique
Soient $X_1, \dots X_n \stackrel{idd}{\sim} F$, où $F$ est certaine une fonction de répartition. On appelle
*fonction de répartition empirique* la fonction 
\begin{gather*} F_n(x) = \frac{1}{n} \sum_{i =1}^n \mathbf{1}_{X_i \leq x} = \frac{\text{nb de données $\leq$ x}}{n}.\end{gather*}
```

```{figure} PDFSVG/ECDF_exemple.svg
--- 
name: ECDF_exemple
width: 95%
---
```

Le théorème de Glivenko-Cantelli justifie le fait que l'on étudie une distribution à partir de réalisations indépendentes et identiquement distribuées.


```{prf:theorem} Théorème de Glivenko-Cantelli
Soient $X_1, \dots, X_n, \dots \sim F$ une suite de variables aléatoires réelles indépendantes et identiquement distribuées selon une fonction de répartition $F$, et soit $F_n(x)$ la fonction de répartition empirique. Alors on a:
\begin{gather*}\|F_n - F\|_\infty = \sup_{x \in \mathbb{R}} |F_n(x) - F(x)| \rightarrow 0, \end{gather*}
presque sûrement. 
```  
  

Cette section sur le TCL conclut notre introduction à la probabilité.
    
Nous avons vu:
    
- comment définir un modèle de probabilité:
    * évènements élémentaires + fonction de probabilité;
    * variables aléatoires discrètes ou continues, lois conjointes        
- comment calculer un certain nombre de probabilités complexes:
    * probabilité conditionnelle, probabilités totales, Bayes;
    * calcul de la loi marginale.
- comment résumer une variable par quelques valeurs clés: espérance, variance;
- deux théorèmes sur des sommes de variables IID.
