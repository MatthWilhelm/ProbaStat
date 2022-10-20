# Probabilités totales et théorème de Bayes

## Probabilités totales

````{prf:theorem} Loi des probabilités totales
:label: prob_tot

Soit $ A $ un événement, et $ B_1 \dots B_n $ une **partition** de $ \Omega $, c'est-à-dire une famille d'ensembles qui satisfait les deux propriétés suivantes:
- $\bigcup_{i=1}^n B_i = \Omega$;
- $B_i \cap B_j = \emptyset$ pour tous $i\neq j$.
On a alors:
    \begin{gather*} \mathbb{P}(A) = \sum_{i=1}^n \mathbb{P}(A \cap B_i) = \sum_{i=1}^n \mathbb{P}(A|B_i) \mathbb{P}(B_i).\end{gather*}  
````

```{figure} latex/PDFSVG/prob_tot_venn.svg
---
name: prob_tot_venn
width: 95%
---
: Probabilités totales: diagramme de Venn
```

La formule des probabilité totale permet de décrire des systèmes plus complexes en deux étapes, en connaissant
- la probabilité de chaque $ B_i $;
- la probabilité de $ A $ sachant chaque $ B_i$.
Dans la pratique, elle est aussi essentielle car d'elle découle la formule d'espérance totale.

````{prf:example}
:label: ex1_prob_tot
Trois machines $M_1,M_2,M_3$ produisent respectivement $1000, 500$ et $500$ tiges de métal. Ces même machines sont imparfaites et produisent respectivement $5\%, 4\%$ et $2\%$ de pièces défectueuses.
Quelle est la probabilité qu'une pièce choisie au hasard parmi les 2000 soit défectueuse?

```{admonition} Solution
:class: dropdown
Les probabilités que la pièce vienne de la machine $ M_i $ sont respectivement données par:

\begin{align*}
        \mathbb{P}(M_1) &= 1000 / 2000 = 1/2; \\
        \mathbb{P}(M_2) &= 500 / 2000 = 1/4;  \\
        \mathbb{P}(M_3) &= 500 / 2000 = 1/4.
\end{align*} 

On peut donc appliquer la formule de la probabilité totale:

\begin{align*}
    \mathbb{P}\left(\text{Pièce défectueuse}\right) &= 0.05 \cdot \frac{1}{2} + 0.04 \cdot \frac{1}{4} + 0.02 \cdot \frac{1}{4} \\
    &= 0.04
\end{align*}
```
````

## Théorème de Bayes

```{prf:theorem} Théorème de Bayes
:label: thm_bayes

Soient $A$ et $B_1 \dots B_n$ tels que les $B_i$ forment une partition de $ \Omega $. Alors on a l'égalité suivante:
\begin{equation*} 
        \mathbb{P}( B_i | A ) = \frac{\mathbb{P}(B_i \cap A)}{\mathbb{P}(A)} = \frac{\mathbb{P}(A|B_i) \mathbb{P}(B_i) }{ \sum_{j=1}^n \mathbb{P}(A|B_j) \mathbb{P}(B_j) }.
\end{equation*}
        
Ce théorème combine la formule de la probabilité conditionnelle et celle des probabilités totales.  
```

````{prf:example}
:label: ex1_bayes
Il y a $ 10 \% $ de chances qu'un patient qui vienne voir le médecin ait un rhume. Il administre donc à chaque patient un test simple de dépistage.
- si le patient est sain, le test a $5\%$ d'être positif;
- si le patient est malade, le test a $100\%$ de chances d'être positif.
Sachant que le test d'Alice est positif, quelle est la probabilité qu'elle soit malade?
```{admonition} Solution
:class: dropdown
On va utiliser la partition: $B_1 =$ « sain »  et $B_2 =$ « malade » et $A =$ « test positif ». On doit donc calculer $\mathbb{P}(B_2 | A)$. On calcule d'abord $ \mathbb{P}(A)$ et on en déduit $\mathbb{P}(B_2 | A)$ à l'aide de la formule de Bayes.
\begin{align*}
        \mathbb{P}(A)     &= \mathbb{P}(A|B_1) \cdot \mathbb{P}(B_1) + \mathbb{P}(A|B_2) \cdot \mathbb{P} (B_2)\\
                    &= 0.05 \times 0.9 + 1 \times 0.1 = \frac{29}{200} = 0.145
\end{align*}

On peut alors calculer:

\begin{align*}
    \mathbb{P}(B_2|A) &= \frac{\Pr(A|B_2) \cdot \mathbb{P}(B_2)}{\Pr(A)} = \frac{\frac{1}{10}}{\frac{29}{200}}  = \frac{20}{29}  \approx 0.69.
\end{align*}
```
````
