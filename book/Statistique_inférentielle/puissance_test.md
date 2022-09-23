# Puissance d'un test

Nos tests sont construits de tel sorte que $\mathbb{P}(\mbox{ Erreur du type I }) =\alpha$.
La probabilité de ne pas rejeter une fausse hypothèse $H_0$ dépend de $H_1$.  
La **puissance** d'un test est
\begin{gather*}
\pi(H_1) = 1-\mathbb{P}(\mbox{ Erreur du type II }) = 1-\mathbb{P}_{H_1}(\mbox{ Non-rejet de } H_0\ ) .
\end{gather*}
Dans le cas où $H_0:\theta=\theta_0$, et $H_1$ dépend de $\theta$, la puissance s'écrit comme $\pi(\theta)$. Remarques: 

- A $\alpha$ égal on veut la plus grande puissance possible.
- Plus $H_1$ est éloignée de $H_0$, plus la puissance est grande: les grandes différences ont plus de chances d'être détectées.
- La puissance augmente avec $n$.
On veut $\pi(\theta)$ le plus grand possible. En règle générale $\pi(\theta)$ est difficile à calculer.
Illustration avec $H_0:\theta=170$. Gauche: le cas idéal (en général irréalisable). Droite: un cas plus réaliste ($\alpha=0.05$).

```{figure} PDFSVG/Power.svg
---
name: Power
width: 95%
---
```

Il existe énormément de tests différents pour des hypothèses plus ou moins complexes.  
Deux classes importantes de tests sont:
- des tests **paramètriques**, se basant sur un modèle probabiliste paramètrique---par exemple, 
$X_1,\ldots, X_n\stackrel{idd}{\sim} \mathcal{N}(\mu, s^2)$, et $H_0:\mu=0$;
- des tests **nonparamétriques**, se basant sur un modèle probabiliste plus général---par exemple, 
$X_1,\ldots, X_n\stackrel{idd}{\sim} f$, et $H_0:\mathbb{P}(X>0)=\mathbb{P}(X<0)=1/2$, c'est à dire, la médiane de $f$ est 0.  

- L'avantage principal d'un test paramétrique est la possibilité de trouver un test (presque) optimal, 
si les suppositions sous-jacentes sont correctes. Dans le cas contraire, un tel test pourrait être mauvais--par ex., si des valeurs abérrantes sont présentes. 
- Un test nonparamétrique n'a pas forcément ce défaut, mais il est souvent moins **puissant**  qu'un test paramétrique.
  
Il y a en effet généralement un compromis entre flexibilité et efficacité. 
