# Estimation de paramètres

```{math}
\newcommand\var{\text{Var}}
\newcommand\E{\mathbb{E}}
```

Pour estimer les paramètres d'un modèles à partir des données, plusieurs méthodes peuvent être utilisées:
- méthode des moments;
- méthode du maximum de vraisemblance.

```{prf:definition} Estimateur
:label: estmiateur
On commencé par faire l'hypothèse d'un modèle $F_\theta$, complètement caractérisé par un paramètre (éventuellement un vecteur) $\theta$.

Cela signifie que pour connaître notre modèle, il suffit de connaître $\theta$.

Un estimateur $\hat{\theta}$  de notre paramètre $\theta$ est une valeur dépendant de $X_1, \dots, X_n$ telle qu'elle estime la valeur de $\theta$ qui a engendré $X_1, \dots, X_n$. 

Comme $\hat{\theta}$ dépend des variables aléatoires $X_1, \dots, X_n$, c'est bien une variable aléatoire.
```

```{admonition} Notations
L'estimateur d'un paramètre donné est généralement noté avec le même symbole surmonté d'un chapeau. Par exemple, si on veut estimer $\theta$, on utilisera la notation  $\hat{\theta}$ pour en désigner un estimateur. Le « chapeau » signifie grossièrement que c'est une statistique (une variable aléatoire donc) dont le but est d'estimer le paramètre $\theta$. Il s'agit d'une notation: cela ne dit rien quant aux propriétés de l'estimateur en question.
```


## Méthode des moments

```{prf:definition} Méthode des moments
:label: meth_moment
Probablement la plus intuitive et la plus ancienne des méthodes d'estimation. Étant donné un modèle $F_\theta$, on peut calculer *les moments* de la distribution $F_\theta$, donnés par
\begin{gather*} m_k := \E[X^k]. \end{gather*}
Supposons que l'on ait $X_1, \dots,X_n \stackrel{idd}{\sim} F_\theta $. La loi des grand nombres justifie asymptotiquement que l'on utilise
\begin{gather*} \hat{m}_k = \frac{1}{n} \sum_{i = 1}^n X_i^k,\end{gather*}
comme estimateur de $m_k$. Finalement, puisque $m_k$ dépend directement de $\theta$, alors on estime $\hat{\theta}$ tel que $\hat{m}_k  = m_k$.
```

````{prf:example} Méthode des moments
:label: ex1_moment
Supposons que l'on observe $x_1,\dots,x_n$, que l'on modélise comme des réalisations d'une loi normale, de paramètres $\mu$ et $\sigma^2$ respectivement. On pose donc $X_1, \dots, X_n \stackrel{idd}{\sim} \mathcal{N}(\mu, \sigma^2)$.

En utilisant la méthode des moments, estimer les paramètres $\mu$ et $\sigma^2$ caractérisant la distribution normale. On rappelle que pour une variable $X\sim\mathcal{N}(\mu, \sigma^2),$ on a
\begin{gather*}\E[X] = \mu,\quad \var(X) = \sigma^2 \Leftrightarrow  \E[X^2] = \sigma^2 + \mu^2.  \end{gather*}

```{admonition} Solution
:class: dropdown

On pose
\begin{gather*}
\hat{m}_1 =\frac{1}{n} \sum_{i = 1}^n X_i = \overline{X},\quad \hat{m}_2 = \frac{1}{n} \sum_{i = 1}^n X^2_i. 
\end{gather*}
Les conditions $\hat{m}_1 = m_1$ et $\hat{m}_2= m_2$ donnent lieu au système suivant:
\begin{gather*}
\left\{
\begin{array}{ll}
\hat{m}_1 &=\hat{\mu}  \\
\hat{m}_2 &= \hat{\sigma}^2 + \hat{\mu}^2
\end{array}
\right.
\Leftrightarrow
\left\{
\renewcommand{\arraystretch}{1.5}
\begin{array}{ll}
\hat{\mu} &=\hat{m}_1 \\
\hat{\sigma}^2 &= \hat{m}_2 -\hat{m}_1^2.
\end{array}
\right.
\end{gather*}
```
````

````{prf:example} Méthode des moments
:label: ex2_moment
Supposons que l'on observe $x_1,\dots,x_n$, que l'on modélise comme des réalisations d'une loi Gamma, de paramètres de forme et d'échelle $k$ et $\theta$ respectivement. On pose donc $X_1, \dots, X_n \stackrel{idd}{\sim} \Gamma(k, \theta)$.
En utilisant la méthode des moments, estimer les paramètres $k$ et $\theta$ caractérisant la distribution Gamma. On rappelle que pour une variable $X\sim\Gamma(k,\theta),$ on a
\begin{gather*}\E[X] = k\theta,\end{gather*}
ainsi que
\begin{gather*} \var(X) = k\theta^2 \Leftrightarrow  \E[X^2] = k\theta^2 + k^2\theta^2= \theta^2 k(k +1 ) .  \end{gather*}
```{admonition} Solution
:class: dropdown

On pose
\begin{gather*}
\hat{m}_1 =\frac{1}{n} \sum_{i = 1}^n X_i = \overline{X},\quad \hat{m}_2 = \frac{1}{n} \sum_{i = 1}^n X^2_i. \end{gather*}
Les conditions $\hat{m}_1 = m_1$ et $\hat{m}_2= m_2$ donnent lieu au système suivant:
\begin{gather*}
\left\{
\begin{array}{ll}
\hat{m}_1 &= \hat{k}\hat{\theta}, \\
\hat{m}_2 &= \hat{\theta}^2 \hat{k}(\hat{k} +1 ),
\end{array}
\right.
\Leftrightarrow
\left\{
\renewcommand{\arraystretch}{2}
\begin{array}{ll}
\hat{\theta} &=\dfrac{\hat{m}_2 -\hat{m}_1^2}{\hat{m}_1}, \\
\hat{k} &= \dfrac{\hat{m}_1^2 }{\hat{m}_2 -\hat{m}_1^2 }.
\end{array}
\right.
\end{gather*}
```
````


## Méthode du maximum de vraisemblance

Cette méthode est **extrêmement générale**.

```{prf:definition} Vraisemblance
:label: vraisemblance
Soient $ X_1 \dots X_n \stackrel{idd}{\sim} f(x;\theta)$. La **vraisemblance** est la fonction de $ \theta $:
\begin{gather*} L(\theta) = \prod_{i=1}^n f(X_i; \theta).\end{gather*}
Formellement, la fonction de vraisemblance est une **fonction aléatoire**, elle dépend de l'échantillon aléatoire $X_1 \dots X_n$.
```

Si on fait l'hypothèse que $ x_1 \dots x_n$ est un échantillon observé que l'on modélise par $ X_1 \dots X_n \stackrel{idd}{\sim} f(x;\theta) $, alors $L(\theta) $ est simplement l'évaluation de la densité jointe au point $(x_1,\dots,x_n)$, c'est-à-dire
\begin{gather*}L(\theta) = f_{X_1,\dots,X_n}(x_1,\dots,x_n; \theta). \end{gather*}
Autrement dit, de manière informelle, elle représente la « probabilité de l'événement » 
\begin{gather*}\mathbb{P}(X_1 = x_1, \dots, X_n = x_n),\end{gather*}
comme fonction de $\theta$.  
(Attention, puisqu'il s'agit de densités, cette probabilité est nulle.)

Si on considère **un modèle**, c'est-à-dire que l'on s'intéresse à la vraisemblance et non à une **réalisation**, alors on écrit
\begin{gather*}L(\theta) = f_{X_1,\dots,X_n}(X_1,\dots,X_n; \theta), \end{gather*}
et il s'agit d'une **fonction aléatoire**, puisqu'elle dépend des variables aléatoires $X_1, \dots, X_n$.

```{prf:definition} Estimateur du maximum de vraisemblance
:label: est_max_vraisemblance
Soit $L:\Theta \rightarrow \mathbb{R}$ une fonction de vraisemblance. Alors 
**l'estimateur du maximum de vraisemblance**, noté $\hat{\theta}_{ML} $ satisfait
\begin{gather*} L\left(\hat{\theta}_{ML}\right) \geq L(\theta), \quad \forall \theta\in \Theta. \end{gather*}}
Autrement dit, $\hat{\theta}_{ML}$ représente le paramètre le plus vraisemblable étant donné une famille de distributions $f_\theta$ et des données $X_1,\dots, X_n.$
```

Il est plus facile de maximiser $ \ell(\theta) = \log[ L(\theta) ] $. On appelle la fonction $\ell$ la fonction de **log-vraisemblance**. On procède en général de la manière suivante:
- On calcule $\ell$, la fonction de  log-vraisemblance du modèle.
- On calcule la dérivée: $ \ell'(\theta) $.
- On résout l'équation $ \ell'(\theta) = 0 $ (peut être fait numériquement).
- On vérifie qu'il s'agit bien d'un maximum.

````{prf:example} Estimation par maximum de vraisemblance
Supposons que $ X_1, \dots, X_n \stackrel{idd}{\sim} \exp(\lambda)$, de paramètre inconnu $ \lambda \geq 0$:
\begin{gather*} f(x; \lambda) = \lambda \exp(-\lambda x), \hspace{1cm} x\geq 0.
\end{gather*}
Calculer $ \hat{\lambda}_{ML}$.

```{admonition} Solution
:class: dropdown
Dans cet exemple, la log-vraisemblance est donnée par
\begin{gather*} \ell(\lambda) = \sum_{i=1}^n \bigg( \log(\lambda) - \lambda X_i \bigg) = n \log(\lambda) - n \lambda \overline{X}.\end{gather*}
Calculons les dérivées:
\begin{align*}
        \ell'(\lambda)  &=\frac{n}{\lambda} - n \overline{X} \\
        \ell''(\lambda) &= - \frac{n}{\lambda^2} < 0,
    \end{align*}
et la fonction de log-vraisemblance est donc concave et tout point stationnaire est un maximum global. 
Ce maximum global est:
\begin{gather*} \frac{n}{\hat{\lambda}_{ML}} = n \overline{X} \Leftrightarrow \hat{\lambda}_{ML}     = \frac{1}{\overline{X}} .\end{gather*}
De plus, $ J\left(\hat{\lambda}_{ML}\right) $ est donnée par
\begin{gather*} J\left(\hat{\lambda}_{ML}\right) = - \left( -\frac{n}{\hat{\lambda}_{ML}^2}\right) = n \overline{X}^2.\end{gather*}
On en déduit la variance asymptotique:
\begin{equation*}\var(\lambda_{ML}) = \frac{1}{n}\frac{1}{\overline{X}_n^2}. \end{equation*}
```
````

```{prf:theorem} Distribution asymptotique de $\hat{\theta}_{ML}$
:label: dist_asymp
Sous des hypothèses de régularité, l'estimateur $\hat{\theta}_{ML} $ est asymptotiquement Gaussien, centré sur $ \theta$ et sa variance est donnée par moins l'inverse de la seconde dérivée de $ \ell(\theta) $, évaluée en $\theta = \hat{\theta}_{ML} $. Autrement dit, on a 
\begin{equation*} \hat{\theta}_{ML} \stackrel{\cdot}{\sim} \mathcal{N} \left(\theta, \frac{1}{J(\hat{\theta}_{ML})} \right), \quad J(\theta) = - \frac{\partial^2}{\partial \theta^2} \left[  \ell(\theta) \right]. 
\end{equation*}
$J(\theta)$ est appelé l'*information observée*. 
```

```{figure} PDFSVG/log_like_estimators.svg
---
name: log_like_estimators
width: 95%
---
: Fonctions de vraisemblances pour $N = 50$ échantillons de taille $n =40 $ chacun. Les points en rouge sont les maxima et le segment vertical représente la vraie valeur $\theta = 0$. En bleu, on voit la distribution normale dont les moments correspondent aux maxima.
```

```{figure} PDFSVG/QQplot_log_like_estimators.svg
---
name: QQplot_log_like_estimators
width: 95%
---
: QQ-plot des estimateurs de maximum de vraisemblance correspondants.
```

Le choix d'un bon estimateur est un choix en général complexe.
    
Dans le cadre du cours, nous allons voir des situations courantes et décrire de bons estimateurs pour ces situations.
    
**Utilisez les estimateurs du cours dans ces situations courantes**
    
Connaître les méthodes des moindres carrés et du maximum de vraisemblance vous permet de déterminer des estimateurs si vous êtes confrontés à des **nouvelles situations non-couvertes dans le cours**.

Dans bon nombre de situations, on peut utiliser une méthode d'estimation « clés en main ». Cependant, ces solutions sont parfois plus ardues à utiliser qu'on ne le pense. Plusieurs aspects peuvent être délicats:
- **identifiabilité :** parfois, plusieurs modèles très différents peuvent représenter de manière également performante des données. S'il y en a un, lequel est le bon?
- **optimisation :** la plupart des méthodes (dont le maximum de vraisemblance et les moindres carrés) reposent sur une procédure d'optimisation. Dans ce cas, des questions d'existence, d'unicité et de convergence des algorithmes d'optimisation entrent en ligne de compte.

En résumé, tout est plus facile lorsque l'on cherche à optimiser une fonction convexe (ou concave): l'optimum existe, il est unique et des algorithmes efficients existent pour approcher la solution. Si ce n'est pas le cas, il faut prendre garde!

En particulier, il faut faire attention aux points suivants:
- vérifier les questions de convergences de l'algorithme d'optimisation. En particulier, étudier la sensibilité de l'estimation à la valeur de départ de l'algorithme. En général, il est judicieux d'utiliser une méthode facile pour avoir un point de départ proche de la valeur optimale, en utilisant par exemple la méthode des moments.
- bien réfléchir au bien-fondé de l'estimation en utilisant les connaissances que l'on a du sujet. Se poser la question de la pertinence de la distribution résultante pour les $X_i$. Éventuellement on peut recourir à des méthodes différentes pour voir se elles donnent des résultats semblables.   


````{prf:example} Application de la distribution asymptotique de $\hat{\theta}_{ML}$
Supposons que le temps (en secondes) nécessaire $X$ pour résoudre un Rubik's cube a pour fonction de densité
\begin{gather*}
f_X(x;\theta)= \frac{1}{\delta \sqrt{2\pi}}  \frac{1}{x}   \exp \left \{ - \frac{1}{2\delta^2}\left(\ln x - \theta\right)^2 \right  \}, \quad
0<x<\infty, \quad \theta\in \mathbb{R},
\end{gather*}
où $\delta> 0$ est un paramètre fixé, considéré comme connu. On suppose qu'on observe un échantillon $X_1, \dots, X_n \stackrel{idd}{\sim} f_X$.
Déterminez l'estimateur du maximum de vraisemblance de $\theta$, $\hat \theta_{\text{ML}}$ et en calculer la variance asymptotique de l'estimateur du maximum de vraisemblance.

```{admonition} Solution
:class: dropdown
On calcule tout d'abord la fonction de vraisemblance $L(\theta)$ et on a
\begin{align*}
L(\theta)& = \prod_{i = 1}^n f_{X_i}(x_i;\theta)= \frac{1}{\delta \sqrt{2\pi}}  \frac{1}{x_i}   \exp \left \{ - \frac{1}{2\delta^2}\left[\ln x_i - \theta\right]^2 \right\}\\
& =(\delta \sqrt{2\pi})^{-n} \prod_{i = 1}^{n}\frac{1}{x_i}  \exp\left\{\sum_{i = 1}^n -\frac{1}{2\delta^2} \left[\ln(x_i) - \theta\right]^2 \right\},
\end{align*}
et la fonction de log-vraisemblance est donc
\begin{gather*}\ell(\theta) = -n \ln(\delta \sqrt{2\pi}) -\sum_{i = 1}^n \ln(x_i) - \sum_{i = 1}^n \frac{1}{2\delta^2} \left[\ln(x_i) - \theta\right]^2. \end{gather*}

La dérivée de la fonction de log-vraisemblance est donnée par
\begin{gather*}\ell'(\theta) = - \sum_{i = 1}^n \frac{1}{2\delta^2} \left[\ln(x_i) - \theta\right] \cdot 2 \cdot (-1) =  \sum_{i = 1}^n \frac{1}{\delta^2} \left[\ln(x_i) - \theta\right].\end{gather*}

L'estimateur $\hat \theta_{\text{ML}}$ est un point stationnaire et satisfait
\begin{align*}
& \ell'(\hat \theta_{\text{ML}}) = 0 \Leftrightarrow \sum_{i = 1}^n \frac{1}{\delta^2} \left[\ln(x_i) - \hat \theta_{\text{ML}}\right] = 0 \Leftrightarrow  \frac{1}{\delta^2} \sum_{i = 1}^n \ln(x_i)  =  \frac{1}{\delta^2} n \hat \theta_{\text{ML}}\\
& \Leftrightarrow \frac{1}{n}\sum_{i = 1}^n \ln(x_i) = \hat \theta_{\text{ML}}.
\end{align*}

Finalement, la fonction de log-vraisemblance est concave car
\begin{gather*}\ell''(\theta) = \frac{-n}{\delta^2} < 0. \end{gather*}
Ainsi, $\hat \theta_{\text{ML}}$ est un maximum global et donc l'estimateur du maximum de vraisemblance.

En utilisant le théorème sur la distribution asymptotique de l'estimateur du maximum de vraisemblance, on a
\begin{gather*} \var(\hat \theta_{\text{ML}}) = [-\ell''(\hat \theta_{\text{ML}}) ]^{-1} = \frac{\delta^2}{n}.\end{gather*}
```
````
