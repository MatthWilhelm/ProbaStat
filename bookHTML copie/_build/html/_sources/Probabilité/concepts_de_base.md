Nous allons présenter une introduction à **la théorie des probabilités**.
    
C'est le domaine des mathématiques qui concerne l'étude des propriétés des systèmes aléatoires.
    
La plus grande difficulté consiste à réconcilier les notions mathématiques sur l'aléatoire avec les notions intuitives que vous avez déjà.
    
Les intuitions dans ce domaine s'avèrent  **souvent fausses** donc méfiez-vous.

# Concepts de base

Nous allons présenter les bases de la probabilité et discuter les sujets suivants:
- expérience aléatoire;
- ensemble fondamental, événements, événements élémentaires;
- opérations sur les événements: union, intersection, négation;
- fonction de probabilité;
- indépendance;
- quelques formules: probabilité conditionnelle, probabilités totales, théorème de Bayes.

Une partie de ce qui suit est tiré de la référence [suivante](https://swisscovery.slsp.ch/permalink/41SLSP_NETWORK/19n6r1g/alma991026360829705501):Dalang, R. C. et Conus, D. (2015), *Introduction à la théorie des probabilités*, Lausanne, Suisse: PPUR.

## Expérience aléatoire

La théorie des probabilités permet de décrire et de modéliser des **phénomènes aléatoires**.
    
Une **expérience aléatoire** est toute action dont il est impossible de prévoir le résultat avec certitude. On admet généralement qu'une expérience aléatoire peut être répétée indéfiniment dans des conditions identiques: le résultat peut varier d'une réalisation à l'autre.
- jet d'un dé, d'une pièce de monnaie;
- tirage d'une carte;
- service au tennis.

````{prf:definition} Modèles probabilistes
:label: modele_probabiliste

**L'ensemble fondamental** $ \Omega $ est l'ensemble de tous les résultats possibles d'une expérience aléatoire.
Lorsque l'ensemble fondamental est dénombrable, on a $\Omega= \{\omega_1, \dots,\}$ et  $\omega_1, \omega_2, \dots$ sont appellés **événements élémentaires**. 
On appelle « événement » tout sous-ensemble de $\Omega$. Un événement peut réunir plusieurs événements élémentaires.
````

````{prf:example} Exemples d'ensemble fondamentaux
:label: ex1_prob
- Une expérience consiste à tirer une boule dans une urne contenant 12 boules: $\Omega = \{ 1,\dots, 12\}.$
- Une expérience consiste à choisir aléatoirement un nombre dans l'intervalle $[0,1]$. $\Omega = [0,1].$
- Une expérience vise à lancer une pièce de monnaie jusqu'à obtenir « Face »:
    $\Omega = \{$ F, PF, PPF, PPPF,$\dots,\}.$ 
````

````{prf:example} Lancer d'une pièce de monnaie
:label: ex2_piece_monaie
\begin{align*}        
         \Omega &= \{P,F\} \\ 
            A &= \{P \} \text{ est un événement et un événement élémentaire}
\end{align*}
````

````{prf:example} Lancer d'un dé à six faces
:label: ex2_piece_monaie
\begin{align*}        
         \Omega &= \{1,2,3,4,5,6\} \\ 
            A &= \{1 \} \text{ est l'événement « obtenir 1»} \\
            B &= \{2,4,6 \} \text{ est l'événement « obtenir un pair » }
\end{align*}
````

````{prf:definition} Intersection d'évènements
:label: intersection_evenement
L'événement « $A$ **et** $B$ » sera noté: $ A \cap B $ (intersection d'ensembles). On a les propriétés suivantes:
- l'intersection de $A$ et $B$ contient tous les événements qui sont contenus dans $A$ et dans $B$;
- s'il n'y a aucun événement commun, alors l'intersection est l'événement vide: $ \emptyset $;
- l'intersection est une opération symétrique: $ A \cap B = B \cap A. $
````
````{prf:example}  
:label: ex3_intersection_evenement_jet_dé
Lors d'un jet de dé, l'intersection des événements
-  « obtenir un chiffre pair »  **et** « obtenir un chiffre premier »   donne
    \begin{gather*} \{2,4,6\} \cap \{2,3,5\} = \{2\}.\end{gather*}
- « Obtenir un chiffre pair »  **et** « obtenir 3 » est vide:
    \begin{gather*} \{2,4,6\} \cap \{3\} = \emptyset.\end{gather*}
````

````{prf:definition} Union d'évènements
:label: union_evenement
L'événement « $A$ **ou** $B$ »  sera noté: $ A \cup B $ (union d'ensembles). On a les propriétés suivantes:
- l'union contient tous les événements qui sont contenus dans $A$ et de tous ceux qui sont contenus dans $B$;
- l'union est vide $ \emptyset $ seulement si les deux événements $ A, B$ sont vides aussi;
- l'union est une opération symétrique: $ A \cup B = B \cup A$.
````

````{prf:example} 
:label: ex4_union_evenement_jet_dé
Lors d'un jet de dé, l'union des événements «Obtenir un chiffre pair»  **ou** « obtenir un chiffre premier » donne
    
\begin{gather*} \{2,4,6\} \cup \{2,3,5\} = \{2,3,4,5,6\}.\end{gather*}
````

````{prf:definition} Complément d'évènement
:label: complement_evenement
L'événement « **non** $A$ »  sera noté: $ A^c $ (complémentaire de l'ensemble). On a les propriétés suivantes:
- l'événement complémentaire de $A$ contient tous les événements élémentaires qui ne sont pas contenus dans $A$;
- l'événement complémentaire est vide seulement si $ A = \Omega $;
- inversément, on a $ A \cup A^c = \Omega $ et $ A \cap A^c = \emptyset $. 
````

````{prf:example} 
:label: ex5_complement_evenement_jet_dé
 Lors d'un jet de dé, le complémentaire de l'événement«Obtenir un chiffre pair»  **ou** « obtenir un chiffre premier » donne
    
\begin{gather*} \{2,4,6\}^c = \{1,3,5\}.\end{gather*}
````

```{prf:definition} Différences d'évènements
:label: dif_evenement
L'événement « $A$ **mais pas** $B$ »  noté $ A \setminus B = A \cap B^c $ (différence des événements)
- la différence contient tous les événements de $A$ qui ne sont pas dans $B$;
- <font color="red">ATTENTION</font>: la différence n'est pas symétrique;
- $ A \setminus B = \emptyset $ seulement si $ A $ est contenu dans $ B $.
```
```{prf:example} 
:label: ex6_dif_evenement_jet_dé
 lors d'un jet de dé, la différence de l'événement « Obtenir un chiffre pair »  avec l'événement « obtenir un nombre premier » donn    
\begin{gather*} \{2,4,6\} \setminus \{2,3,5\} = \{4,6\}.\end{gather*}
```
## Diagrammes de Venn

Le diagramme de Venn est un outil simple pour visualiser les événements et les opérations entre événements.
- L'ensemble fondamental est représenté comme un rectangle.
- Les événements sont des disques contenus dans le rectangle.

```{figure} latex/PDFSVG/venn1.svg
--- 
name: venn1
width: 95%
---
: intersection $A \cap B$
```

```{figure} latex/PDFSVG/venn2.svg
--- 
name: venn2
width: 95%
---
: union $A \cup B$
```

```{figure} latex/PDFSVG/venn3.svg
--- 
name: venn3
width: 95%
---
: différence $A \setminus B$
```

```{figure} latex/PDFSVG/venn4.svg
--- 
name: venn4
width: 95%
---
: complément $A^c$
```

## Fonction indicatrice

```{prf:definition} Fonction indicatrice
:label: fct_indic
On appelle *fonction indicatrice* de l'événement $A$, notée $\mathbf{1}_A$ la fonction définie comme
\begin{gather*} \mathbf{1}_A(x) = \left\{
    \renewcommand{\arraystretch}{1.5}
            \begin{array}{ll}
            1 & \text{ si }x\in A,\\
            0 & \text{ sinon.}
            \end{array} \right. \end{gather*}
```


```{prf:property} Fonction indicatrice
:label: propriete1_fct_indicatrice 

Soient deux ensembles $A, B \subset \Omega$, dont on note les fonctions indicatrices $\mathbf{1}_A$ et $\mathbf{1}_B$ respectivement. On a alors:
- $\mathbf{1}_{A^c} = 1 -\mathbf{1}_{A}; $ 
- $\mathbf{1}_{A\cap B} = \mathbf{1}_A \mathbf{1}_B; $
- $\mathbf{1}_{A\cup B} =\mathbf{1}_A + \mathbf{1}_B - \mathbf{1}_A \mathbf{1}_B. $
```
On peut ainsi facilement montrer les lois de De Morgan:

```{prf:theorem} Lois de Morgan
:label: loi_morgan

- $(A\cup B)^c = A^c \cap B^c$;
- $(A\cap B)^c = A^c \cup B^c$.
```
## Fonction de probabilité

```{prf:axiom} Fonction de probabilité
:label: axiom1_fct_prob
On appelle fonction de probabilité toute fonction $ \Pr $ qui vérifie:
- $0\leq \Pr(A)\leq 1,$ pour tout $A\subset \Omega$;
- $ \Pr(\Omega) = 1 $;
- Pour toute famille d'événements $\{A_n\}_{n=0}^\infty$ deux à deux disjoints, on a
\begin{gather*} 
\Pr\left(\bigcup_{n=0}^\infty A_n\right) = \sum_{n = 0}^\infty \Pr(A_n) 
\end{gather*}

En réalité, la fonction $\Pr$ n'est pas uniquement définie sur tous les sous-ensembles mais seulement sur les sous-ensemble **mesurables**. Mais il s'agit d'une subtilité mathématique.
```

```{prf:property} Fonction de probabilité
:label: propriete2_fct_prob 
Une fonction de probabilité satisfait les propriétés suivantes:
1. $ \Pr(\emptyset) = 0 $ : la probabilité de l'événement impossible est nulle;
1. pour toute famille finie de $N$ événements $\{A_n\}_{n=0}^N$ deux à deux disjoints, on a
\begin{gather*} 
    \Pr\left(\bigcup_{n=0}^N A_n\right) = \sum_{n = 0}^N \Pr(A_n). 
\end{gather*}
1. $ \Pr(A^c) = 1 - \Pr(A) $;
1. $ \Pr(A \cup B) = \Pr(A) + \Pr(B) - \Pr(A\cap B) $;    
1. $ A \subset B $ implique $ \Pr(A) \leq \Pr(B) $
```

````{prf:proof} 
:label: proof_prop_fct_prob
1. Soit $0 \leq p = \Pr(\emptyset) \leq 1$ (axiome 1). Considérons la famille d'ensembles $A_k = \emptyset$. Puisque $A_i \cap A_j = \emptyset$ pour tous $i,j$, cette famille satisfait l'axiome 3. Ainsi, on a
\begin{gather*}\sum_{k = 1}^\infty \Pr(\cup_{k = 1}^\infty A_k) = \Pr(\emptyset) = p \leq 1.\end{gather*}
Ainsi, puisque la série converge, on a nécessairement
\begin{gather*}\lim_{k \rightarrow \infty} \Pr(A_k) = 0. \end{gather*}
Or, Puisque $A_1 = A_2 = \dots,$ on a nécessairement $p = \Pr(A_1) = \lim_{k \rightarrow \infty} \Pr(A_k) = 0$, d'où le résultat.
1. Soit une famille finie de $N$ événements $\{A_n\}_{n=0}^N$ deux à deux disjoints. Pour $n \geq N + 1$, on définit $A_n = \emptyset$. Alors les événements de la famille ainsi définie $\{A_n\}_{n=0}^\infty$ sont eux aussi deux à deux disjoints. On applique l'axiome 3 et on obtient
\begin{align*}
 \Pr\left(\bigcup_{n=0}^N A_n\right) &= \Pr\left(\bigcup_{n=0}^\infty A_n\right) \stackrel{\text{ax. 3}}{ = } \sum_{n = 0}^\infty \Pr(A_n) \\
 & = \sum_{n = 0}^N \Pr(A_n) + \sum_{n = N+1}^\infty \underbrace{\Pr(A_n)}_{ =  0, \text{ par prop.  1}}  = \sum_{n = 0}^N \Pr(A_n).
 \end{align*}
1. Soit $A$ un événement donné. Par définition, on a $A\cup A^c = \Omega$ et $A\cap A^c = \emptyset$. On considère la famille finie d'événements disjoints $\{A, A^c\}$. D'après 2}, on a alors 
$$1 \stackrel{ax. 1}{ = } \Pr(\Omega) = \Pr(A \cup A^c) = \Pr(A) +  \Pr(A^c),$$
d'où le résultat.
````

La propriété 4 est un cas particulier du plus général
[d'inclusion-exclusion](https://fr.wikipedia.org/wiki/Principe_d'inclusion-exclusion) principe .
Les propriétés 4 et 5 seront montrées aux exercices.

## Evénements équiprobables

````{prf:definition}
:label: evenement_equiprobable

Lorsque $\Omega = \{\omega_1, \dots,\omega_N\}$ est un ensemble fini et sous l'hypothèse **d'équiprobabilité**, tous les événements élémentaires ont la même probabilité. On a alors:
\begin{gather*} \Pr(A) = \frac{ \text{nombre total d'événements élémentaires dans A} }{ \text{nombre total d'événements élémentaires} }.\end{gather*}
````

```{warning}
Attention à ne pas confondre évènements élémentaires et composés!
```

````{prf:example} Deux lancers de pièces
:label: ex7_deux_lancers_de_piece
\begin{gather*} \Omega = \{PP, PF, FP, FF\} \end{gather*}
        
Donner les événements $A =$« au moins un P » , et $B=$« Au moins un F » , $ A \cap B$ et $ A \cup B$.
Trouver les probabilités de ces événements si la pièce est équilibrée, c'est-à-dire si $ \Pr(\{PP\}) = \dots = \Pr(\{FF\}) = 1/4 $ 

```{admonition} Solution
:class: dropdown
Calcul des évènements:

\begin{align*} 
    A             &= \{PP, PF, FP\}       \\
    B             &= \{PF, FP, FF\}       \\
                                        \\
    A \cap B     &= \{PF, FP\}         \\
    A \cup B     &= \{PP, PF, FP, FF\} \\
\end{align*}
```

````

````{prf:example} Événement équiprobables
:label: ex8_evenement_equi
**jet de deux dés**:  Quelle est la probabilité d'obtenir un 7 avec la somme de deux dés?
```{admonition} Solution
:class: dropdown
Sous l'hypothèse, d'équiprobabilité, il faut compter le **nombre de cas favorables** et le **nombre de cas total**. En s'aidant d'un petit tableau, cela devient (encore plus) facile.
On a 36 cas au total, et 6 cas favorables, donc:
\begin{gather*} \Pr( \text{Somme}=7 ) = 6/36 = 1/6 \end{gather*}
```
````

