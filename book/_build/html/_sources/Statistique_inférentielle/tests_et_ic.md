# Tests et IC

De nombreuses hypothèses concernent la valeur d'un paramètre $\theta$.  
Il y a alors un lien entre les intervalles de confiance pour $\theta$ et  les tests.

Supposons que $H_0$ spécifie que $\theta=\theta_0$, alors:
- si $\theta_0$ n'appartient pas à un IC pour $\theta$ avec coefficient de confiance $1-\alpha$, on rejette $H_0$ au niveau de signification $\alpha$; 
- si l'IC contient $\theta_0$, on garde $H_0$.  

Cette procédure est équivalente  à l'utilisation des statistiques de test des types
\begin{gather*}
T = \frac{\hat\theta-\theta_0}{{\rm sd}(\hat\theta)} \quad \mbox{(test unilatéral)},\quad 
T' = \frac{|\hat\theta-\theta_0|}{{\rm sd}(\hat\theta)}\quad  \mbox{(test bilatéral)},
\end{gather*}
où ${\rm sd}(\hat\theta)$ est la déviation standard de $\hat\theta$.
Les valeurs observées sont 
\begin{gather*}
t_{\rm obs} = \frac{\hat\theta_{\rm obs}-\theta_0}{ {\rm sd}(\hat\theta)},\quad 
t'_{\rm obs} = \frac{|\hat\theta_{\rm obs}-\theta_0|}{ {\rm sd}(\hat\theta)},
\end{gather*}
et on rejette $H_0$ si elles sont grandes par rapport aux lois correspondantes.

```{prf:definition} Test bilatéral et unilatéral
Soient $I, S$ les limites inférieure et supérieure d'un intervalle de confiance pour $\theta$ avec coefficient de confiance $(1-\alpha)$. 
 - Un test de l'hypothèse nulle $H_0:\theta=\theta_0$ est **bilatéral** si l'hypothèse alternative 
est $H_1:\theta\neq\theta_0$.  Dans ce cas on rejette $H_0$ au niveau de signification $\alpha$ si et seulement si
\begin{gather*}
\theta_0\not\in ]I, S[.
\end{gather*}
- Le test est **unilatéral** si l'alternative est soit $H^-_1:\theta<\theta_0$, soit $H^+_1: \theta>\theta_0$.  Alors on rejette $H_0$ au niveau de signification **$\alpha/2$** en faveur de $H^-_1$ , respectivement  $H^+_1$,  si et seulement si
\begin{gather*}
H_1^+:\ \theta_0\not\in ]-\infty, S[,  \quad H_1^-:\ \theta_0\not\in ]I, \infty[.
\end{gather*}
```

````{prf:example} «pile et face »  revisité
En utilisant la méthode du maximum de vraisemblance, calculez l'estimateur de la probabilité $\hat{p}$ correspondante ainsi que l'estimateur de la variance correspondant. En utilisant la distribution normale asymptotique, construisez un intervalle de confiance de Wald à 95\%. Est-ce que cet intervalle contient la valeur $p = \frac{1}{2}$? 

```{admonition} Solution
:class: dropdown
On estime $\hat{p}$ par maximum de vraisemblance et on obtient
\begin{gather*}L(p) = p^{k} (1-p)^{n-k} \Rightarrow \ell(p) = k\ln(p) + (n-k)\ln(1-p). \end{gather*}
On calcule le point stationnaire et on en déduit:
\begin{gather*}\ell'(p)= \frac{k}{p} - \frac{n-k}{1-p}, \Rightarrow \ell'(\hat{p})=0 \Leftrightarrow \hat{p} = \frac{k}{n}. \end{gather*}
On calcule la seconde dérivée, et on obtient:
\begin{align*}
\ell''(p) & = - \frac{k}{p^2} - \frac{n-k}{(1-p)^2}.
\end{align*}

Notons tout d'abord que la seconde dérivée est strictement convexe
\begin{gather*}\ell''(p) = - \frac{k}{p^2} - \frac{n-k}{(1-p)^2} <0.\end{gather*}
Ainsi le point stationnaire est nécessairement un maximum car $0 \leq k \leq n$ et $0<p<1$.

La seconde dérivée évaluée en ce point vaut
\begin{align*}
\ell''(\hat{p}) & =-\frac{k}{(k/n)^2} - \frac{n-k}{(1 - k/n)^2} = - \frac{n^2}{k} - \frac{n^2 (n-k)}{(n-k)^2}\\
& = -n^2\left( \frac{1}{k} + \frac{1}{n-k}\right)  = -\frac{n^3}{k (n-k)}
\end{align*}
Ainsi, on a:
\begin{gather*} \hat{p} \stackrel{\cdot}{\sim} \mathcal{N}\left(p,\frac{k(n-k)}{n^3}\right).\end{gather*}
  
On peut donc calculer un intervalle de Wald (bilatéral), basé sur la distribution normale. En utilisant $k = 19$ et $n = 30$, on obtient
comme intervalle à 95\%
\begin{gather*}\left[\frac{k}{n} + z_{0.025} \sqrt{\frac{k(n-k)}{n^3}}, \frac{k}{n} + z_{0.975} \sqrt{\frac{k(n-k)}{n^3}} \right] = [0.461, 0.806], \end{gather*}
qui contient la valeur $p = \frac{1}{2}.$
```
````

````{prf:example} Compteurs d'électricité
On a contrôlé 10 compteurs d'électricité nouvellement fabriqués.
    
\begin{gather*}\begin{array}{ccccc}
        983,& 1002, & 998, & 996, & 1002,\\
        983, & 994, & 991, & 1005, & 986.\end{array}\end{gather*}
On aimerait savoir s'il y a un écart systématique entre la valeur standard 1000 et les compteurs qui sortent de la fabrication. La moyenne empirique est donnée par
\begin{gather*} \bar x = 994 < 1000. \end{gather*}
Est-ce que c'est un hasard ou une faute de production ?

```{admonition} Solution
:class: dropdown
La moyenne empirique et la variance empirique de ces $n=10$ observations sont:
\begin{align*}
        \bar{x} &= 994  \\
        s^2     &= 64.9 = 8.05^2
    \end{align*}
La valeur attendue est $\mu=1000$. La statistique de Student est donc:
\begin{gather*} t_{\rm obs} = \frac{994 - 1000}{s / \sqrt{n}} = -2.35 \end{gather*}

Si on veut tester la présence d'un écart à $5\%$ bilatéral, le seuil critique est donné par le quantile d'une loi Student à $\nu = 9$ degrés de liberté, qui est donné par
\begin{gather*} t_{9;1-\alpha/2} =  2.262 \end{gather*}
L'écart observé empiriquement est plus important que ce qui est \og tolérable \fg{} au seuil de  $5\%$. En effet, on a  $t_{\rm obs} = -2.35 < t_{9;\alpha/2} = - 2.262$.
On a donc un **écart significatif**: on conclut qu'il est très probable qu'il y ait une faute de production.
```
````

```{prf:definition} Niveaux de confiance et de signification
- Le **niveau de confiance** d'un intervalle est la probabilité que l'intervalle aléatoire contienne la vraie valeur, c'est-à-dire typiquement 95\%, et on le note $1-\alpha$ en général.
- Par ailleurs, **le niveau de signification** d'un test est la valeur tolérée d'erreur de type I, c'est-à-dire typiquement 5\% et que l'on note $\alpha$.
```

````{prf:example} Poids de rats
On étudie chez 20 rats l'effet sur le gain de poids de deux régimes: l'un riche en protéines, l'autre pauvre.
```{figure} latex/PDFSVG/tabEx_stat.svg
---
name: tabEx_stat
width: 95%
---
```
Sous l'hypothèse que ces données sont Gaussiennes, effectuer un test au niveau de signification $5\%$ pour l'hypothèse $ H_0 $: "les régimes sont équivalents" contre $ H_1 $: "les régimes sont différents".

```{admonition} Solution
:class: dropdown
Concrètement, on suppose d'abord que
\begin{gather*}X_1 \stackrel{idd}{\sim} \mathcal{N}(\mu_1, \sigma^2_1), \quad X_2 \stackrel{idd}{\sim} \mathcal{N}(\mu_2, \sigma^2_2). \end{gather*}
On pose 
\begin{gather*}
\left\{\begin{array}{l}
H_0 : \mu_1 = \mu_2\\
H_1 : \mu_1 < \mu_2
\end{array}\right. \quad \alpha = 5\%.
\end{gather*}
On calcule
\begin{gather*}\begin{array}{lll}
\bar x_1 = 83.9 && s_1 = 15.71\\
\bar x_2 = 85.9 && s_2 = 15.02.
\end{array}\end{gather*}
Il nous faut une hypothèse sur les variance. Ici il semble raisonnable de supposer $\sigma_1 = \sigma_2$ inconnues. Vérifions tout d'abord si cette hypothèse est raisonable en utilisant un test $F$:
\begin{gather*}\left\{\begin{array}{l}
H_0 : \sigma_1^2 = \sigma^2_2\\ H_1 : \sigma^2_1 \neq
\sigma^2_2\end{array}\right. \quad \alpha = 5\%.\end{gather*}
On a:
\begin{align*}
&F = \dfrac{S^2_1}{S^2_2} \sim F_{n_1-1,n_2-1}\mbox{ sous } H_0\\
&F_{obs} = \dfrac{s^2_1}{s^2_2}= 1.094\\
&n_1 = n_2 = 10,\quad \alpha = 5\%
\end{align*}

On utilise un test bilatéral basé sur les quantiles: $F_{9,9 ;0.025} = 0.2484$ et $F_{9,9 ;0.975} = 4.0259$, ainsi $H_0$ n'est pas
rejetée et on suppose maintenant $\sigma_1^2 = \sigma^2_2=\sigma^2$.
Revenons au test pour les moyennes, maintenant en supposant les variances égales. On estime $\sigma^2$ en utilisant l'estimateur  
\begin{gather*}
S^2_p = \dfrac{(n_1-1)S_1^2+(n_ 2-1)S^2_2}{n_1+n_2-2}.
\end{gather*}  
Remarquons que le théorème de Cochran (pas mentionné dans ce cours par ailleurs) montre que, si $X_1, \dots, X_n \stackrel{idd}{\sim} \mathcal{N}(\mu, \sigma^2)$, alors on a
\begin{gather*}\sum_{i = 1}^n (X_i - \overline{X})^2 \sim \sigma^2 \chi^2_{n-1}.\end{gather*}
Ainsi 
\begin{gather*} (n_1-1)S_1^2+(n_ 2-1)S^2_2 \sim \sigma^2 \chi^2_{n_1 + n_2 -2},\end{gather*}
et ainsi, la variable
\begin{gather*}
T = \dfrac{\overline{X}_1-\overline{X}_2}{S_p\sqrt{(1/n_1) + (1/n_2)}}\stackrel{H_0}{\sim}t_{n_1 +n_2 -2}.
\end{gather*}

Avec $n_1=n_2 = 10$ on obtient la valeur r\'ealis\'ee $s^2_p = 236.21 = 15.37^2$.
On a $\overline{X}_1 \sim \mathcal{N}(\mu_1,\sigma^2/n_1)$ et $\overline{X}_2 \sim \mathcal{N}(\mu_2,\sigma^2/n_2)$, ainsi sous $H_0 : \mu_1 = \mu_2$ on a 
\begin{gather*}
\overline{X}_1 - \overline{X}_2 \sim \mathcal{N}\left(0,\sigma^2(\frac{1}{n_1} + \frac{1}{n_2}) \right)\Rightarrow \dfrac{\overline{X}_1 - \overline{X}_2}{\sigma\sqrt{1/n_1+1/n_2}} \sim \mathcal{N}(0,1).
\end{gather*}
On considère donc la statistique de test
\begin{gather*}
T = \dfrac{\overline{X}_1-\overline{X}_2}{S_p\sqrt{(1/n_1) + (1/n_2)}}\stackrel{H_0}{\sim}t_{n_1 +n_2 -2}
\end{gather*}
(bien noter les degrés de libertés $n_1 +n_2 -2$). Avec nos données on trouve $t_{\rm obs} = -0.29$.  On a $t_{n_1+n_2-2,\alpha}= - 2.10$, donc puisque $t_{\rm obs} > -2.10$ on ne rejette pas $H_0$.    
```
````
