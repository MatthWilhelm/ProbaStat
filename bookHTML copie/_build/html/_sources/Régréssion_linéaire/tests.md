# Régréssion linéaire: tests

## Test de Student

On rappelle que l'on a:
- $ \hat{\boldsymbol{\beta}}\sim \mathcal{N}\left(\boldsymbol{\beta}, \sigma^2\left(\mathbf{X}^\top\mathbf{X}\right)^{-1}\right);$
- $\frac{n-p}{\sigma^2}  S^2 \sim \chi^2_{n-p} $
- $\hat{\boldsymbol{\beta}}$ et $S^2$ sont indépendants.


### Intervalle de confiance pour  $\boldsymbol{\beta}_i$

Ainsi, on a
\begin{gather*}T = \frac{\hat{\boldsymbol{\beta}}_i - \boldsymbol{\beta}_i}{S\sqrt{v_{ii}}} \sim t_{n-p}, \end{gather*}
où $t_{n-p}$ est une variable de Student de $n-p$ de degrés de libertés et où $v_{ii}$ est le ième élément diagonal de la matrice $\mathbf{V} = (\mathbf{X}^\top \mathbf{X})^{-1}$.

On peut construire un intervalle de confiance pour $\boldsymbol{\beta}_i$, basé sur la distribution de Student:
\begin{gather*}\left[\hat{\boldsymbol{\beta}}_i - s_\alpha S \sqrt{v_{ii}},\hat{\boldsymbol{\beta}}_i + s_\alpha S \sqrt{v_{ii}} \right], \end{gather*}
où $s_\alpha$ est le quantile à $1-\frac{\alpha}{2}$ de la loi $t_{n-p}$ et où le niveau de confiance est $1- \alpha $.

### Tester $\beta_i = 0$

A l'aide de la distribution de Student, on peut facilement faire un test d'hypothèse
$H_0: \beta_i = 0$ contre $H_1: \beta_i \neq 0$. En effet, sous $H_0$, on a
\begin{gather*} T = \frac{\hat{\boldsymbol{\beta}}_i}{S\sqrt{v_{ii}}} \sim t_{n-p}.\end{gather*}
Ainsi, pour un niveau de signification fixé $\alpha$, on rejette $H_0$ si 
\begin{gather*}\left|T\right|} = \left|\frac{\hat{\boldsymbol{\beta}}_i}{S\sqrt{v_{ii}}}\right| > t_{n-p; 1-\alpha/2}, \end{gather*}
où $t_{n-p; 1-\alpha/2}$ est le quantile  à $1-\alpha/2$ de la loi de Student à $n-p$ degrés de liberté.

## Modèles emboîtés

On suppose à présent que l'on dispose de $p$ variables mais que l'on soupçonne que seules les $q$ premières (à reparamétrisation près) variables ont réellement une influence sur la variable réponse. 
- L'ajustement sera *toujours* meilleur pour le modèle plein. 
- Est-il possible de tester si cet ajustement est *significativement* meilleur?

Soient $\mathbf{y} = (y_1,\dots, y_n)^\top$ et 
$\mathbf{X} = 
\left[
\mathbf{X}_1
\left| \right. 
\,
\mathbf{X}_2
\right] \in \mathbb{R}^{n\times p}$ et où $\mathbf{X}_1\in \mathbb{R}^{n\times q} $ et $\mathbf{X}_2\in \mathbb{R}^{n\times (p-q)} $. 
On partitionne le vecteur de coefficients de manière similaire
$\boldsymbol{\beta} = 
\left[
\boldsymbol{\beta}_1
\left| \right. 
\,
\boldsymbol{\beta}_2
\right]$, 
où $\boldsymbol{\beta}_1\in \mathbb{R}^{q} $ et $\boldsymbol{\beta}_1\in \mathbb{R}^{p-q}$.

On considère alors les modèle suivants:
```{math}
:label: equ_big_model
\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon} = \mathbf{X}_1\boldsymbol{\beta}_1 +  \mathbf{X}_2\boldsymbol{\beta}_2 + \boldsymbol{\varepsilon}, 
```
et
```{math}
:label:equ_nested_model
\mathbf{y} = \mathbf{X}_1\boldsymbol{\beta}_1  + \boldsymbol{\varepsilon},
```
où $\boldsymbol{\varepsilon}\in \mathbb{R}^n \sim\mathcal{N}(\mathbf{0}, \sigma^2 \mathbf{I}_n)$ et $\sigma^2 >0$.

On voit immédiatement que le modèle [m](equ_nested_model) est un sous-modèle du modèle [M](equ_big_model) il correspond au cas où $\boldsymbol{\beta}_2 = \mathbf{0}_{p-q}$. On dit alors que ces modèles sont emboîtés.

La question initiale peut donc à présent se reformuler de la manière suivante: est-ce que l'on peut tester
|begin{gather*}H_0: \boldsymbol{\beta}_2 = \mathbf{0}_{p-q} \quad \text{ vs }H_1: \boldsymbol{\beta}_2 \neq \mathbf{0}_{p-q}.\end{gather*}
La réponse est affirmative, et cela se fait en utilisant un test $F$.

Soit $\mathbf{H}_1   =
 \mathbf{X}_1\left(\mathbf{X}_1^\top\mathbf{X}_1\right)^{-1}\mathbf{X}_1^\top
$ et 
$\hat{\mathbf{y}}_1 =\mathbf{H}_1 \mathbf{y}.$
Alors on note 
\begin{gather*}\text{SCR}(\hat{\boldsymbol{\beta}}_1) = \| \mathbf{y} -\hat{\mathbf{y}}_1\|^2, \quad \text{SCR}(\hat{\boldsymbol{\beta}}) = \| \mathbf{y} -\hat{\mathbf{y}}\|^2.\end{gather*}
Alors sous $H_0: \boldsymbol{\beta}_2 = \mathbf{0}_{p-q}$, on a
\begin{gather*} F =  \frac{\frac{\text{SCR}(\hat{\boldsymbol{\beta}}_1) - \text{SCR}(\hat{\boldsymbol{\beta}})}{p-q}}{\frac{\text{SCR}(\hat{\boldsymbol{\beta}})}{n-p}} \sim F_{p-q,n-p}.\end{gather*}

````{prf:example} Les données d'Ozone
Voici trois modèles:
\begin{eqnarray*}
y &=& \textcolor{green}{\alpha + \varepsilon},\\
 y &=& \textcolor{red}{\alpha +\beta x + \varepsilon},\\
y &= &\textcolor{blue}{\alpha + \beta x + \gamma x^2 + \delta x^3 + \varepsilon}
\end{eqnarray*}

 Le rouge semble être  bien meilleur que le vert, mais que le rouge et le bleu 
semblent être similaires.  Comment tester ce constat?

```{figure} PDFSVG/JungOzone_fit.svg
---
name: JungOzone_fit
width: 95%
---
```
Comparons le modèle constant $y=\alpha + \varepsilon$ et le modèle linéaire $y=\alpha + \beta x + \varepsilon$.

 Pour tester s'il vaut la peine d'ajouter $\beta x$, on calcule 
\begin{gather*}
F = \dfrac{({\rm SC_{green}} -{\rm SC_{red}}) /1}{ {\rm  SC_{red}}/(n-2)}.
\end{gather*}
Si l'hypothèse nulle $H_0:\beta = 0$ (modèle constant) est vraie alors $F \sim F_{1,n-2}$.
- Données d'ozone: on trouve $F=204.32$, à comparer avec $F_{1,205;0.975}= 5.098$.  

Pour les données d'ozone, pour tester $\gamma=\delta=0$ dans le modèle cubique
\begin{gather*}
 y = \alpha + \beta x + \gamma x^2 + \delta x^3 + \varepsilon,
\end{gather*}
on calcule
\begin{gather*} F = \dfrac{({\rm SC_{red}} -{\rm SC_{blue}}) / (p-q)}{ {\rm  SC_{blue}}/(n-p)},
\end{gather*}
et avec $n=207$, $p=4$, $q=2$, on obtient 
\begin{gather*}
F=\dfrac{(5831.9-5712.2)/(4-2)}{ 5712/(207-4)} = 2.13 \,{{\stackrel{\,H_0\,}{\sim}}}\, F_{2,207-4} = F_{2,203},
\end{gather*}
dont le quantile $95\%$ est $F_{2,203;0.975}= 3.756$. 
````

````{prf:example} L'effet photoélectrique
La loi de l'effet photoélectrique a marqué l'histoire de la physique comme étant une des premières incursion de la physique quantique. Lorsque l'on irradie (éclaire) un métal à une certaine fréquence, certains électrons quittent leur couche de valence. La loi de l'effet photoélectrique postule que la différence de potentiel qui engendre par cette émission d'électron satisfait:
\begin{gather*} V = \frac{h}{e} f - \frac{W_0}{e}, \end{gather*}
où $f$ est la fréquence du rayon incident, $h$ est la constante de Planck, $e$ dénote la charge élémentaire d'un électron, $W_0$ est le travail nécessaire pour permettre l'extraction de l'électron.
La loi de l'effet photoélectrique a marqué l'histoire de la physique comme étant une des premières incursion de la physique quantique.
- observé expérimentalement dès la fin du 19$^{\text{ième}}$ siècle (Hertz, 1887);
- décrit de manière théorique par Einstein en 1905;
- validé expérimentalement par Milikan (1915);
- prix de Nobel de physique pour Einstein (1921).

Postule que la lumière se comporte en quanta.

```{figure} PDFSVG/photo_electric_fit.svg
---
name: photo_electric_fit
width: 95%
---
```
D'après la relation
\begin{gather*}V = \frac{h}{e} f - \frac{W_0}{e}, \end{gather*}
on peut déduire la constante de Planck, et on obtient
\begin{gather*}\hat{h}_{\text{1er ordre}} = 6.41 \times 10^{-34},\quad \hat{h}_{\text{2ème ordre}} = 6.40 \times 10^{-34}.\end{gather*}
On verra plus tard comment construire des intervalles de confiance pour ces valeurs.
La valeur actuelle de $h$ est
\begin{gather*}h = 6.62 \times 10^{-34},\end{gather*}
 et l'écart relatif entre les deux valeurs est de $\sim 3.1\%$.
````
