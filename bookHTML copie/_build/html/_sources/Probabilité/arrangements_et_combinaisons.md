# Arrangements et combinaisons

````{prf:definition} Arrangements
:label: arrangement

Considérons un ensemble de $n$ objets (boules numérotées, par exemple) distincts.
Le nombre **d'arrangements** de $k$ objets (distincts) dans un ordre déterminé est donné par:
\begin{gather*} A^n_k = n \cdot (n-1) \cdot \ldots \cdot (n-k+1) = \frac{n!}{(n-k)!}.\end{gather*}
Dans un arrangement *l'ordre compte*. Autrement dit, on différencie les tirages $(1,2,3)$ et $(1,3,2)$, par exemple. On considère en fait des $k-$tuples (ordonnés, donc).
````

````{prf:definition} Combinaisons
:label: combinaisons

Considérons un ensemble de $n$ objets (boules numérotées, par exemple) distincts. Le nombre *de combinaisons* de $k$ objets (distincts) est donné par:
\begin{gather*} C^n_k = \binom{n}{k} =  \frac{n!}{(n-k)!k!} = \frac{A^n_k}{k!} .\end{gather*}
Dans une combinaison, *l'ordre n'importe pas*. Autrement dit, on ne différencie pas les tirages $\{1,2,3\}$ et $\{1,3,2\}$, par exemple. On considère des sous-ensembles (pas ordonnés, donc).
````

Les coefficients binomiaux se retrouvent dans bien des domaines des mathématiques. Vous les avez surement déjà rencontrés.
- Dans la formule du binôme de Newton:
\begin{gather*} (a + b)^n = \sum_{k=0}\binom{n}{k} a^k b^{n-k}.\end{gather*}
- dans la formule de Stirling;
- dans les problèmes de dénombrements (de probabilité); 
- et dans bien d'autres cas!

````{prf:example} l'Euromillion
:label: ex_arrangement_combinaison
On s'intéresse à la probabilité de gagner à l'Euromillion. Il s'agit
    D'une loterie à deux grilles. Dans la première, il faut choisir, sans remise, 5 numéros choisis entre 1 et 50. Dans la seconde, il s'agit de choisir 2 « étoiles » parmi 12.
Quelle est la probabilité de gagner? 
```{admonition} Solution
:class:
Il s'agit de compter le nombre de combinaisons possibles  de 5 chiffres parmi 50 et de 2 « étoiles » parmi 12. On a alors:
\begin{gather*}\Pr(\text{gros lot}) = \frac{1}{\binom{50}{5} \binom{12}{2}} \approx 7.15\cdot 10^{-9}.\end{gather*}
```
````
