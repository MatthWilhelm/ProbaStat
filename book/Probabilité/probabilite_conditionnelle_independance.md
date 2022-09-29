# Probabilité conditionelle et indépendence

````{prf:definition} Probabilité conditionnelle
:label: prob_cond

La probabilité que l'événement $A$ se réalise peut être modifiée si on sait que l'événement $B$ s'est déja réalisé.
**La probabilité conditionnelle** de A sachant B est définie comme:
\begin{gather*} \mathbb{P}(A | B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}. \end{gather*}
A noter que si $B$ s'est réalisé, on a nécessairement $\mathbb{P}(B) >0$.
````

````{prf:definition} Indépendance conditionnelle
:label: independance

Si le fait que $ B $ ait eu lieu ne change pas la probabilité de l'événement $A$, alors $ A $ et $ B $ sont dits **indépendants**. Dans ce cas, on a:
- $\mathbb{P}(A \cap B ) = \mathbb{P}(A) \mathbb{P}(B)$; 
- $\mathbb{P}(A | B )    = \mathbb{P}(A);$
- $\mathbb{P}(B | A )    =\mathbb{P}(B).$
````

````{prf:example} Deux jets d'une pièce
:label: ex1_prob_cond
Quelle est la probabilité d'avoir pile au 2ème jet, sachant qu'on a déja fait pile au premier?    

```{admonition} Solution
:class: dropdown
Si on modélise les deux lancers de la pièce comme indépendants, et chaque lancer comme équiprobable, alors la probabilité de faire pile au deuxième lancer sachant qu'on a déjà fait pile au premier est:

\begin{align*}
        \mathbb{P}( \text{Pile au 2ème} | \text{Pile au 1er}) &= \mathbb{P} ( \text{Pile au 2ème} ) \\
    &= 1/2
\end{align*} 
```
````

````{prf:example} Jet de dé
:label: ex2_prob_cond
Est-ce que les événements $\{2,4\}$ et $\{2,4,6\}$ sont indépendants?
```{admonition} Solution
:class: dropdown
Les événements ne sont pas indépendants. Pour le vérifier, calculons sous une hypothèse d'équiprobabilité: 
\begin{align*}
        \mathbb{P}( \{2,4\} | \{2,4,6\} ) &= 2/3 \\
        \mathbb{P}( \{2,4\} )             &= 2/6 \neq 2/3
\end{align*}
```
````

````{prf:definition} Indépendance entre $n$ évènement
:label: independance_mult

On peut généraliser l'indépendance à $n$ événements: $ A_1 \dots A_n $ sont indépendants si pour tout sous-ensemble $ \{i_1, \dots, i_k\} \subset \{1,\dots, n\} $:
\begin{gather*} \mathbb{P} \left( \bigcap_{j=1}^k A_{i_j} \right) = \prod_{j=1}^k \mathbb{P}(A_{i_j} ). \end{gather*}
````

````{prf:example} Système redondant
:label: ex3_prob_cond
Un système contient $n$ composants qui fonctionnent en parallèle: le système fonctionne si au moins un composant fonctionne. On suppose que les pannes des composants sont des événements indépendants.
- Quelle est la probabilité que le système fonctionne si chaque composant $i$ a une probabilité $p_i$ de tomber en panne? 
- Quelle serait la probabilité si le système était monté en série?
```{admonition} Solution
:class: dropdown
Soient $A_1, \dots, A_i,\dots, A_n$ les événements « Le $i$ième composant tombe en panne ». Alors pour que le système tombe en panne, il faut 
- dans le cas du système en parallèle, que tous les composants tombent simultanément en panne. La probabilité de cet événement est donc
\begin{gather*} \mathbb{P}(\bigcap_{i =1 }^n A_i) = \prod_{i = 1}^n \mathbb{P}(A_i) = \prod_{i = 1}^n p_i .\end{gather*}
- dans le cas du système en série, qu'au moins un composant tombe en panne, ce qui correspond à l'événement $\bigcup_{i =1 }^n A_i$.
On peut alors calculer la probabilité de cet événement en utilisant les lois de De Morgan:
\begin{align*}
    \mathbb{P}(\bigcup_{i =1 }^n A_i) & = 1- \mathbb{P}\left[\left(\bigcup_{i =1 }^n A_i)^c \right)\right] = 1- \mathbb{P}\left(\bigcap_{i =1 }^n A_i^c\right) \\
&= 1- \prod_{i = 1 }^n \left[1- \mathbb{P}\left( A_i \right)\right]  = 1- \prod_{i = 1}^n (1-p_i).
\end{align*}
On note l'utilisation du fait que si $A_1, \dots, A_n$ sont mutuellement indépendants, alors $ A_1^c, \dots, A_n^c$ le sont aussi.
```
````
