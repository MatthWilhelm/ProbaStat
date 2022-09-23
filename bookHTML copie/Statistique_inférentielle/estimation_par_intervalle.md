# Estimation par intervalle

```{math}
\newcommand\E{\mathbb{E}}
```

On a vu qu'une des raisons d'utiliser le formalisme des probabilités était de traiter de manière systématique les données comme aléatoires. Cela permet non seulement de faire des estimations mais aussi et surtout de **quantifier l'incertitude** liée à ces estimations. On va donc voir l'estimation par intervalle.

## Estimation par intervalle

L'estimation par intervalle essaye de donner une réponse plus complète que simplement un estimateur $ \hat{\theta} $.
- définition de l'intervalle de confiance;
- intuition: « **Intervalle compatible avec les données** »;
- l'intervalle est aléatoire alors que $ \theta $ ne l'est pas;
- niveau de confiance, niveau de signification;
- intervalle de Wald, intervalle de Student.

La notion **d'intervalle de confiance** est une notion d'**intervalle compatible avec les données**. Attention: la définition précise n'est pas nécessairement intuitive.
    
Au lieu d'estimer le paramètre $\theta$ seulement par un nombre $\hat\theta$, on préfère donner un intervalle aléatoire qui couvre $\theta$ avec une grande probabilité}.

```{prf:definition} Estimation par intervalle
:label: est_int
Mathématiquement, un intervalle de confiance est tel que dans $ (1 - \alpha) \% $ du temps, il contient la vraie valeur du paramètre inconnu $ \theta $. $1- \alpha $ est appelé le **niveau de confiance** de l'intervalle.

Plus précisément, un intervalle est défini par deux statistiques $ I, S $ qui donnent les bornes de l'intervalle. $ I, S$ définissent **un intervalle de confiance à $ (1-\alpha)\% $** si:
\begin{gather*}\Pr( I \leq \theta \leq S ) = 1 - \alpha, \end{gather*}
pour tout $\theta \in \Theta$.    
```

Considérons un estimateur $\hat{\theta} $ de $\theta$, et supposons qu'il existe une fonction $T=q(\hat\theta,\theta)$ dont la loi est connue et ne dépend pas de $\theta$ (s'appelle un **pivot**).

Soient $a$ et $b$ tels que 
\begin{gather*}
\alpha_1 = \Pr(T< a),\quad \alpha_2 = \Pr(T > b),
\end{gather*}
avec $\alpha_1 + \alpha_2 = \alpha$ (souvent $\alpha_1=\alpha_2$).  On a alors
\begin{gather*}
\Pr(a \leq T \leq b) = \Pr(T\leq b) - \Pr(T< a) = (1-\alpha_2)-\alpha_1= 1-\alpha, 
\end{gather*}
et si on peut isoler $\theta$, on peut trouver des variables aléatoires $I, S$ telles que 
\begin{gather*}
\Pr(I \leq \theta \leq S) = 1-\alpha.
\end{gather*}

````{prf:example} Pivot: moyenne et espérance pour une loi normale

Soient $ X_1 \dots X_n \stackrel{idd}{\sim} \mathcal{N}(\mu,\sigma^2) $, où $\sigma$ est supposé connu. Trouvez un pivot pour l'espérance $\mu$ en fonction de la moyenne empirique $\overline{X}$ et en déduire un intervalle de confiance au niveau $1-\alpha,$ pour $\alpha\in ]0,1[$.
```{admonition} Solution
:class: dropdown
On sait que $\overline{X} \sim \mathcal{N}(\mu, \frac{\sigma^2}{n}).$ Ainsi, en utilisant les propriétés de la loi normale, on a:
\begin{gather*}q(\overline{X}, \mu) := \sqrt{n} \frac{\overline{X} - \mu}{\sigma} \sim \mathcal{N}(0,1),\end{gather*}
qui est donc un pivot. Ainsi, on peut construire un intervalle au niveau $1-\alpha$
\begin{gather*}
\Pr\left(-z_{1-\alpha/2} \leq \frac{\bar X-\mu}{\sigma/\sqrt{n}} \leq z_{1-\alpha/2}\right) = 1-\alpha,
\end{gather*}
que l'on peut réécrire comme
\begin{gather*}
\Pr\left(\underbrace{\overline{X}-z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}}_{=I} \leq \mu\leq
\underbrace{\overline{X} + z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}}_{=S}\right) = 1-\alpha.
\end{gather*}
Ainsi l'intervalle de confiance sym\'etrique \`a $100(1-\alpha)\%$ pour $\mu$ (avec $\sigma^2$ connu) est 
\begin{gather*}
[I,S] = \left[\overline{X} -z_{1-\alpha/2},\frac{\sigma}{\sqrt{n}},\mbox{ } \overline{X} + z_{1-\alpha/2},\frac{\sigma}{\sqrt{n}}\right].
\end{gather*}
```
````

- $ [I,S] $ est un intervalle aléatoire car $ I,S $ sont des VA.
- La probabilité dans la définition est donc par rapport à la position aléatoire des bornes de l'IC.
- La position de $ \theta $ **n'est pas aléatoire**.
- **Attention** Dire que $\theta \in [I,S]$, avec une probabilité $1-\alpha$, est **incorrect** car ce sont les valeurs $I$ et $S$ qui sont aléatoires.

```{figure} latex/PDFSVG/tab2_stat.svg
---
name: tab2_stat
width: 30%
---
Différents IC pour la même valeur de $\theta$ (ligne rouge)
```

## Intervalle de confiance de Wald

```{prf:definition} IC de Wald
:laebl:ic_wald
Soit $ \hat{\theta} $ un estimateur non-biaisé de $ \theta $, et soit $ v $ sa variance (ou un estimateur de sa variance). Si, asymptotiquement, $ \hat{\theta} $ est approximativement Gaussien, c'est-à-dire si
    \begin{gather*} \hat{\theta} \dotsim \mathcal{N}(\theta, v),\end{gather*}
    alors, on peut construire un IC \textbf{de Wald}:
    \begin{gather*} \left[ \hat{\theta} - s_\alpha \sqrt{v} ,  \hat{\theta} + s_\alpha \sqrt{v}  \right], \end{gather*}
    où le seuil $ s_\alpha $ est tel que:
    \begin{gather*} \Pr( - s_\alpha \leq \eta \leq s_\alpha ) = 1 - \alpha \end{gather*}
    pour $ \eta \sim \mathcal{N}(0,1) $.
```

Dans le cas d'un intervalle de Wald, on fait implicitement l'hypothèse d'un intervalle symétrique autour de $\hat{\theta} $. Ainsi, on a
\begin{gather*}s_\alpha = z_{1 - \alpha/2}, \end{gather*}
où $z_p$ désigne le quantile d'ordre $p$. Par exemple, on a:

```{figure} latex/PDFSVG/tab3_stat.svg
---
name: tab3_stat
width: 95%
---
```

L'intervalle de confiance de Wald est exact dans le cas où $\hat{\theta} \sim \mathcal{N}(\theta, v)$. En pratique, cette condition est rarement satisfaite, mais elle est parfois justifiée en vertu du TCL ou de la convergence de l'estimateur du maximum de vraisemblance. En particulier deux aspects sont à souligner:
- la taille d'échantillon qui justifie l'usage de résultats asymptotiques est rarement atteinte;
- sauf exception, la variance est elle-même une estimation, et la distribution n'est alors pas nécessairement normale.

Malgré ces mises en garde, l'IC de Wald peut être une approximation très raisonnable de la réalité.

```{admonition} Recette générale
On rappelle le résultat suivant:  

**Distribution asymptotique de $\hat{\theta}_{ML} $**       
Sous des hypothèses de régularité, l'estimateur $\hat{\theta}_{ML} $
\begin{gather*} \hat{\theta}_{ML} \stackrel{\cdot}{\sim} \mathcal{N} \left(\theta, \frac{1}{J(\hat{\theta}_{ML})} \right), \quad J(\theta) = - \frac{\partial^2}{\partial \theta^2} \left[  \ell(\theta) \right]. \end{gather*} 
$J(\theta)$ est appelé l'*information observée*. Donc
l'IC pour $\theta$ de niveau $1-\alpha$ a des limites 
$\hat\theta_{ML}\pm z_{1-\alpha/2}J(\hat\theta_{ML})^{-1/2}$.
```

````{prf:example} Estimateur $\hat{\lambda}_{ML}$ pour un modèle exponentiel

Soient $X_1,\ldots, X_n \stackrel{idd}{\sim}\exp(\lambda)$, trouver un intervalle de confiance à $100(1-\alpha)\%$ pour $\lambda$. Pour des données avec $n=25$ et $\overline{X}=40$, trouver un IC à 95\%.
```{admonition} Solution
:class: dropdown
La vraisemblance est
\begin{gather*}
L(\lambda) = \lambda e^{-\lambda X_1}\cdots \lambda  e^{-\lambda X_2}= 
\lambda^n e^{-\lambda(X_1+\cdots + X_n)},
\end{gather*}
donc la log vraisemblance est
\begin{gather*}
\ell(\lambda) = \log L(\lambda)  = n\log\lambda - \lambda (X_1+\cdots + X_n).
\end{gather*}
Ainsi
$\ell'(\lambda) = \frac{n}{ \lambda}- \sum^n_{i=1}X_i$ et on trouve 
\begin{gather*}\ell'(\hat\lambda_{ML}) =0 \Leftrightarrow \hat\lambda_{ML}=\frac{1}{\overline{X}}.\end{gather*}
On vérifie la seconde dérivée 
\begin{gather*} \ell''(\hat\lambda_{ML}) =- \frac{n}{\hat\lambda_{ML}^2}  = - n\overline{X}^2 < 0,\end{gather*}
ainsi $\hat\lambda_{ML}$ est bien un maximum global de $\ell$.
Ainsi $J(\hat\lambda_{ML})=-\ell''(\hat\lambda_{ML})=n\overline{X}^2$, et 
\begin{gather*}
\hat{\lambda_{ML}}\stackrel{\cdot}{\sim} \mathcal{N}\left(\lambda,\frac{1}{n\overline{X}^2} \right).
\end{gather*}
Un IC de niveau $1-\alpha$ pour $\lambda$ a pour limites 
\begin{gather*}\hat\lambda_{ML}\pm z_{1-\alpha/2}\frac{1}{\sqrt{n}\overline{X}}.\end{gather*}

Pour ces données, les bornes d'un IC à 95\% sont $1/40 \pm 1.96(5\cdot 40)^{-1}$. L'intervalle est environ: $[0.0152,0.0348]$.
```
````

````{prf:example} Estimateur $\hat{\lambda}_{ML}$ pour un modèle Poisson

Soient $ X_1 \dots X_n \stackrel{idd}{\sim} Poiss(\lambda) $. Construire un intervalle de confiance pour $ \hat{\lambda} $ ? Quelle est la forme de l'IC de Wald à $95\%$ ?
```{admonition} Solution
:class: dropdown
La log-vraisemblance est:
\begin{align*}
        \ell(\lambda) &= \sum_{i=1}^n \left[ x_i \log(\lambda) - \log(x_i !) - \lambda \right] \\
                    &= \log(\lambda)  n \overline{X}_n - n \lambda - \sum_{i=1}^n \log(x_i !).
    \end{align*}
On calcule les dérivées:
\begin{align*}
        \ell'(\lambda) &= \frac{n \overline{X}_n}{\lambda} - n \\
        \ell''(\lambda) &= - \frac{n \overline{X}_n}{\lambda^2} <0.
    \end{align*}
De nouveau, la log-vraisemblance est systématiquement concave et le point stationnaire est nécessairement un maximum global. On a donc
\begin{gather*}\ell(\hat{\lambda}) = 0  \Leftrightarrow \frac{\overline{X}_n}{\hat{\lambda}} = 1 \Leftrightarrow \hat{\lambda}_{ML} = \overline{X}_n.\end{gather*}
  
On calcule  
\begin{gather*} J \left( \hat{\lambda}_{ML} \right) = -\ell''(\hat{\lambda}),\end{gather*}
d'où on déduit la variance asymptotique
\begin{gather*}      \frac{1}{J \left( \hat{\lambda}_{ML} \right)} = \frac{\overline{X}_n}{n}.\end{gather*}

L'intervalle de confiance de Wald a donc pour limites
\begin{gather*}\overline{X}_n \pm z_{1-\alpha/2} \sqrt{\frac{\overline{X}_n}{n}},\end{gather*}
où $ z_{1-\alpha/2} =  z_{0.975} = 1.96 $. 
```
````

## Intervalle de Student

La distribution $t$ de «  Student » a été introduite à des fins de tests statistiques pour la première fois dans une publication par William S. Gosset. Ce dernier, travaillant pour la brasserie Guinness était interdit de publier autrement que sous un pseudonyme. Il publia donc ses résultats sous le pseudonyme de Student. Il finit sa carrière comme brasseur en chef de Guinness mais décéda 1 mois après, à l'âge de 61 ans.
[référence:](https://pubs.aeaweb.org/doi/pdfplus/10.1257/jep.22.4.199) Ziliak, S. T. (2008), *Guinnessometrics: The Economic Foundation of “Student’s”t*, Journal of Economic Perspectives.

```{prf:definition} Statistique de Student
:label: stat_student
Soient $ X_1 \dots X_n \stackrel{idd}{\sim} \mathcal{N}(\mu, \sigma^2) $ avec **variance inconnue**.

On peut estimer $ \mu, \sigma^2 $ avec:
\begin{equation*}  
\begin{array}{cccl}
            \mu & \approx \hat{\mu} &= \overline{X} & =  \displaystyle{ \frac{1}{n} \sum_{i=1}^n X_i }, \\
            \sigma^2 & \approx \hat{v}  &= S^2     & = \displaystyle{ \frac{1}{n-1} \sum_{i=1}^n (X_i - \overline{X})^2 }. \\
        \end{array} \end{equation*}
Soit la **statistique-T de Student**:
\begin{gather*} T = \frac{\overline{X} - \mu}{ S / \sqrt{n}} \sim t_{n-1}.\end{gather*}
Elle suit une **loi de Student** de $ n-1 $ degrés de liberté.
```

```{prf:definition} Intervalle de Student
:label:int_student
Dans le formulaire, on trouve les seuils $s_\alpha$ tels que:
\begin{gather*} \Pr( -s_\alpha \leq T \leq s_\alpha) = 1 - \alpha, \end{gather*}
    où $s_\alpha$ est le quantile à $1-\frac{\alpha}{2}$ de la loi $t_{n-1}$.
À l'aide de ces valeurs, on peut construire des intervalles de confiance pour $ \mu $ quand la **variance est inconnue**. Ces IC sont de la forme:
\begin{gather*} \left[ \overline{X} - s_\alpha \frac{S}{\sqrt{n}} ,  \overline{X} + s_\alpha \frac{S}{\sqrt{n}}  \right], \end{gather*}
    où $ \alpha $ est la valeur choisie pour le niveau que le niveau de confiance soit $1- \alpha $.
```

````{prf:example} Intervalle de confiance pour les résistances

On suppose que la résistance $X$ d'un certain type d'équipements électriques est distribuée approximativement suivant une loi normale.

Un échantillon de taille $n = 64$ a donné comme moyenne et écart-type empiriques les valeur $\bar x = 5.34\ \Omega $ (ohm) et $S = 0.12\ \Omega$ . Trouver un intervalle de confiance pour $\mu = \E[X]$ au niveau de confiance de 95\%.
```{admonition} Solution
:class: dropdown
On utilise le fait que la statistique de test $T = \frac{\overline{X} - \mu}{ S / \sqrt{n}} \sim t_{n-1}. $ Ici, on prend $\bar{x} = 5.34,$ $n = 64$ et  $S = 0.12$. En utilisant l'outil informatique, on trouve que le quantile 
$t_{n-1; 1-\alpha/2}= t_{63; 0.975} = 2$. On a évidemment $\sqrt{64} = 8$ et l'intervalle de confiance pour $\mu$ est 
\begin{gather*}
\left[ 5.34 - 2 \cdot \frac{0.12}{8}, 5.34 + 2\cdot \frac{0.12}{8}\right] = \left[5.31,5.37\right].
\end{gather*}
```
````

```{prf:remark} 
- Pour augmenter la probabilité que l'intervalle contienne $ \theta $, il faut le rendre plus large. On est alors plus conservatif.
- Pour obtenir un intervalle plus court, on peut soit être moins conservatif, soit augmenter $ n $.
- La notion d'IC a quelques variantes: 
    * IC unilatéraux de la forme $ ]-\infty, S] $ (**intervalle unilatéral à gauche**);
    * IC approximatifs: $ \Pr(I \leq \theta \leq S) \approx 1 - \alpha $, souvent construits avec le TCL.
```

```{figure} PDFSVG/tdensity_IC.svg
---
name: tdensity_IC
width: 95%
---
Distributions $t_\nu$, pour $\nu= 2,5,10$ et distribution normale standard. Les segments représentés en bas sont les « intervalles de confiance » à 95\%.  Les queues de la loi de Student sont plus lourdes que celles de la loi $\mathcal{N}(0,1)$ et la loi $t_\nu$ converge vers une $\mathcal{N}(0,1)$ pour $\nu\rightarrow\infty$.
```
