# Test du $\chi^2$

```{math}
\newcommand\var{\text{Var}}
\newcommand\E{\mathbb{E}}
```

- Modèle statistique du test $\chi^2$.
- Statistique de résumé.
- Distribution d'échantillonage de $ T $, degrés de liberté.
- Test d'indépendance $\chi^2$.

```{prf:definition} Test du $\chi^2$
:label: test_chi2
Supposons qu'on observe $n$ valeurs dont les **fréquences observées** dans $k$ classes disjointes 
sont notés $o_1,\ldots,o_k$. On note $e_1,\ldots,e_k$ les **fréquences théoriques** correspondantes.
 Soit $H_0$ : "les observations proviennent de la loi
théorique spécifiée".
Une mesure de l'écart entre les deux distributions est donnée
par la **statistique $\boldsymbol{\chi^2}$** 
\begin{gather*}
T= \sum^k_{i=1}\dfrac{(o_i-e_i)^2}{ e_i}\quad\mbox{ et}\quad 
\sum^k_{i=1}o_i = \sum^k_{i=1}e _i= n.
\end{gather*}  

Sous $H_0$, cette statistique $T$ suit approximativement (pour $n$ grand) une distribution $\chi^2_\nu$ où
- $\nu = k-1 $ si les $e_i$ peuvent être
calculés sans avoir à estimer des paramètres inconnus; 
-  $\nu = k-1-c$ si les $e_i$ sont calculés
après avoir estimé $c$ paramètres.
```

```{figure} PDFSVG/ChiSqdensity.svg
---
name: ChiSqdensity
width: 95%
---
: Densité de la loi $\chi^2_\nu$ pour $\nu=1,2,5,10$ (noir, rouge, violet, bleu).
```

```{prf:property} Loi $\chi^2$
:label: prop_loi_chi2
Soient $Z_1,\ldots,Z_\nu \stackrel{idd}{\sim} \mathcal{N}(0,1)$. Alors on définit la loi de $Z_1^2+\cdots + Z_\nu^2 \sim \chi^2_\nu$.
On a les propriétés suivantes:
- Si $X\sim \chi^2_\nu$, alors $X$ prends des valeurs dans $[0,\infty)$. 
- Si $X\sim \chi^2_\nu$, alors $\E(X) = r$ et $\var(X) = 2\nu$.
- Si $X \sim \chi^2_\nu$, alors $X \sim \Gamma\left(\frac{\nu}{2},2\right)$.
- Si $Y_1, \ldots, Y_\nu \stackrel{idd}{\sim} \chi^2$, alors $\sum_{i = 1 }^\nu Y_i \sim \chi^2_\nu$.
```

```{admonition} Remarques
- Recommandation: si besoin, regrouper les données de telle façon que 
les $e_i > 5$ pour $i=1,\ldots,k$. Ceci pour que la convergence de $T$
vers la loi $\chi^2_\nu$ soit le moins déraisonnable possible.
- Aucune alternative précise: on rejette «  rejet de $H_0$ ».
- $H_0$ est rejeté pour les grandes valeurs de la valeur observée 
\begin{gather*}
t_{\rm obs} =  \sum^k_{i=1}\dfrac{(o_i-e_i)^2}{ e_i}
= \sum^k_{i=1}\dfrac{o_i^2}{ e_i}-n.
\end{gather*}
Si $t_{\rm obs}>\chi^2_{\nu ;1-\alpha}$ on rejette
$H_0$, sinon on ne la rejette pas.
```

`````{prf:example} Equilibre du dé
:label: ex_equilibre_dé
$n=60$ jets d'un d\'e ont donn\'e la r\'epartition suivante:
```{figure} latex/PDFSVG/tab5_stat.svg
---
name: tab5_stat
width: 95%
---
```
Testons $H_0$ : « équilibre du dé ».  Prenons $\alpha = 5\%$.
````{admonition} Solution
:class: dropdown
Sous $H_0$ la fonction de masse est
```{figure} latex/PDFSVG/tabEx36.svg
---
name: tabEx36
width: 95%
---
```
où $X$ est le numéro obtenu. Donc
\begin{gather*}
t_{\rm obs} = \sum^6_{i=1}\dfrac{(o_i-e_i)^2}{e_i} = 8.6
\end{gather*}
et $T\stackrel{H_0}{\stackrel{\cdot}{\sim}} \chi^2_r$ avec $r = k-1 = 6 - 1 = 5$ où $k$ = 6 classes (faces). On a $\chi^2_{5 ,0.95} = 11.07 > 8.6 = t_{\rm obs}$ donc on ne rejette pas $H_0$.

````
`````

`````{prf:example}
:label: ex_test_chi2_1
On a mesuré le QI de $ n = 1000 $ personnes. Le QI est fait pour être distribué quasi comme une Gaussienne $ \mathcal{N}(100, 15^2) $.
```{figure} latex/PDFSVG/tab6_stat.svg
---
name: tab6_stat
width: 95%
---
```
Testons au niveau de signification $ \alpha = 5\% $ la distribution du QI.    

````{admonition} Solution
:class: dropdown
Calculons les probabilités de chaque classe sous le modèle Gaussien. On a:
```{figure} latex/PDFSVG/tabEx37_1.svg
---
name: tabEx37_1
width: 95%
---
```
Les valeurs théoriques $e_i$ sont donc:
```{figure} latex/PDFSVG/tabEx37_2.svg
---
name: tabEx37_2
width: 95%
---
```
La statistique de test vaut:
\begin{gather*} T = 13.12. \end{gather*}
On a 6 observations et on a ajusté aucun paramètre. Le degré de liberté est donc $ r = 5$.
Le seuil est: $ \chi^2_{5 ,0.95}= 11.07 < 13.12 $. On rejette donc l'hypothèse nulle  à $5\%$.
````
`````

```{prf:definition} Tableau de contingence
:label: ex_tab_contingence
L'utilité principale du test $\chi^2$ est de tester l'indépendance de deux variables discrètes $ A, B$. Soit $ h $ le nombre de classes de $ A $ et $ k $ celui de $ B $.
On appelle **tableau de contingence** d'un jeu de données le tableau qui répertorie les fréquences d'observation de chaque paire $ A,B $.
\begin{gather*}
\begin{array}{l|cccccc|c}
&&&B&&&&\\ 
\hline A & 1      &      2 & \ldots & j     &\ldots & k      & \Sigma\\
\hline 1 & n_{11} & n_{12} & \ldots & n_{1j}&\ldots & n_{1k} & n_{1.}\\
       2 & n_{21} & n_{22} & \ldots & n_{2j}&\ldots & n_{2k} & n_{2.}\\
  \vdots & \vdots &  \vdots& \vdots & \vdots&\vdots & \vdots & \vdots\\
       i & n_{i1} & n_{i2} & \ldots & n_{ij}&\ldots & n_{ik} & n_{i.}\\
  \vdots & \vdots & \vdots & \vdots & \vdots&\vdots & \vdots & \vdots\\
       h & n_{h1} & n_{h2} & \ldots & n_{hj}&\ldots & n_{hk} & n_{h.}\\
\hline 
  \Sigma & n_{.1} & n_{.2} & \ldots & n_{. j}&\ldots& n_{. k}& n_{..}=n\\
\end{array}
\end{gather*}
```

```{prf:definition} Test d'indépendance
:label: test_indep

On considère l'hypothèse nulle suivante $H_0$: les variables sont indépendantes. Ainsi $H_0$ est équivalente à  
\begin{gather*} \mathbb{P}(A=i, B = j) = \mathbb{P}(A=i) \mathbb{P}(B=j) \end{gather*}
où $ \mathbb{P}(A=i)$ et $ \mathbb{P}(B=j) $ sont estimées dans les données:
\begin{gather*} \mathbb{P}(A=i) \approx \frac{n_{i,.}}{n} \hspace{1.5cm} \mathbb{P}(B=j) \approx \frac{n_{.,j}}{n} \end{gather*}
Donc, la prédiction pour $ n_{i,j}$ est:
\begin{gather*} e_{i,j} = n \times \frac{n_{i,.}}{n} \times \frac{n_{.,j}}{n} = \frac{n_{i,.} n_{.,j} }{n} \end{gather*}
    
On utilise alors la statistique de test    
\begin{gather*} t_{obs} = \sum_{i=1}^k \sum_{j=1}^h \frac{ \left(n_{i,j} -\frac{n_{i,.} n_{.,j} }{n} \right)^2}{\frac{n_{i,.} n_{.,j} }{n}}.  \end{gather*}
Sous certaines hypothèses optimistes, $T \sim \chi^2_{r} $, où le nombre de degrés de liberté $r$ est donné par
\begin{gather*} r = hk - 1 - (h-1) - (k-1) = (h-1)(k-1).\end{gather*}
Donc, pour tester l'indépendance de $ A, B $:
- On construit le tableau de contingence.
- On calcule $ t_{obs}$ à partir du tableau.
- On compare $ t_{obs}$ au quantile d'une loi $ \chi^2_{(h-1)(k-1)} $.
```

On a vu en un premier temps que le test du $\chi^2$ permettait de comparer des fréquences théoriques avec des fréquences empiriques. Comment peut-on en faire un test d'indépendance?

En fait, sous l'hypothèse d'indépendance les lois marginales caractérisent complètement la distribution jointe. Donc
- on estime les lois marginales;
- on compare la réalisation de la loi jointe (le tableau de contingence) avec la loi théorique dérivée des lois marginales et de l'hypothèse d'indépendance.

`````{prf:example} 
:label: ex_test_chi2_2
On a relevé parmi 95 personnes la couleur de leurs yeux (caractère $A$) et celle de leurs cheveux (caractère $B$) et on a obtenu les r\'esultats suivants: 
```{figure} latex/PDFSVG/tab7_stat.svg
---
name: tabEx38
width: 95%
---
```
On désire tester ($\alpha = 0.05$) si la couleur des cheveux est
indépendante de celle des yeux.
````{admonition} Solution
:class: dropdown
Les valeurs attendues sous indépendance sont:
```{figure} latex/PDFSVG/tabEx38.svg
---
name: tabEx38
width: 95%
---
```
La statistique résumé vaut:
    
\begin{gather*} T =  10.71 \end{gather*}
    
Le degré de liberté est $ r = (3-1)(2-1) = 2 $. Le seuil est donc: $ \chi^2_{2 ,0.95}= 5.99 $.
    
On peut donc conclure en rejetant l'hypothèse nulle d'indépendance de la couleur des yeux et de celle des cheveux.
````
`````
