#!/usr/bin/env python
# coding: utf-8

# # Série3
# ## Exercice 1: 
# 
# On suppose que la taille, en centimètres, d'un homme âgé de 25 ans est une variable aléatoire 
# normale de paramètres $\mu= 176.6$ et $\sigma^2=63.84$. 
# 
# 1\) Quelle est la probabilité que la taille d'un homme de 25 ans choisi au hasard soit supérieure à 170cm? 
# 

# In[ ]:


from scipy import stats as st
import numpy as np

mu = 176.6
sigma_square = 63.84

# Calculer cette probabilité en utilisant directement la fonction de répartition 
# d'une loi normale de moyenne 176.6 et de variance 63.84
prob = ...

# Calculer cette probabilité en normalisant notre observation et en utilisant la 
# fonction de répartition d'une loi normale standardisé
normalisation = ... 
prob_ = ... 


# 2\) Sachant que l'homme choisi mesure plus de 180cm, quelle est la probabilité qu'il mesure plus de 192cm?  
# a\) Calculer $\mathbb{P}(\{X > 192\} \bigcap \{X > 180\})$:  
# 
# **Solution**:  
#   
# 

# In[ ]:


# Place your answer here


# b\) Calculer $\mathbb{P}(X > 180)$:

# In[ ]:


# Place your answer here


# c\) En déduire la valeur de la probabilité $\mathbb{P}(X > 192 | X > 180)$:

# In[ ]:


# Place your answer here


# 3\) Quel est la taille $x$ pour laquelle il y a $5$% de chance d'observer plus grande que $x$, c'est-à-dire $x$ tel que $\mathbb{P}(X>x) = 0.05$ avec $X\sim\mathcal{N}(\mu,\sigma^2)$.

# In[ ]:


# Place your answer here


# ## Exercice 2: 
# 
# On considère une variable aléatoire réelle $X$ avec espérance $\mu$ et variance $\sigma^2 < \infty$. Soit $X_1, \dots, X_n$ un échantillon iid de $n$ variables aléatoires avec la même loi que $X$.
# On définit $\overline{X}=  \frac{1}{n}\sum_i^n X_i $ et $\hat{\sigma}^2 = \frac{1}{n}\sum_i (X_i - \overline{X})^2$ des estimateurs empiriques des deux premiers moments de $X$.
# 
# 1) a) Soit directement en markdown, soit à la main, calculer $\mathbb{E}[\overline{X}]$ et $\mathbb{E}[\hat{\sigma}^2]$:
# 
# **Solution**:  
#   
# b) En déduire un estimateur non-biaisé de $\sigma^2$.
# 
# **Solution**:  
#   
# 2) Proposer une méthode pour estimer l'espérance et la variance si nous avions un échantillon $X_1, \dots, X_n$ de grande taille.
# 
# **Solution**:  
#   
# 3) Nous allons maintenant tester cela en générant un grand nombre de variables aléatoires pour une variable étudiée en cours (une variable suivant la loi Beta par exemple):  
# a) Générer $n = 10000$ observations de la loi que vous avez choisi.

# In[ ]:


# Place your answer here


# a\) Calculer la moyenne et la variance de la loi que vous avez choisi pour les paramètres que vous avez fixé.
# 
# **Solution**:  
#   
# 

# In[ ]:


mean = ... 
var = ... 


# 1\) Faire un plot de l'évolution de l'estimation de la moyenne en fonction du nombre $m = 1, \cdots, n$ d'obervations utilisé dans l'estimation. Faire aussi apparaître la vrai valeur de la moyenne sur ce plot.

# In[ ]:


from matplotlib import pyplot as plt
import numpy as np

# Plot de l'évolution de l'estimation de la moyenne
...


# 2\) Faire un plot de l'évolution de l'estimation de la variance en fonction du nombre $m = 1, \cdots, n$ d'obervations utilisé dans l'estimation. Faire aussi apparaître la vrai valeur de la variance sur ce plot.

# In[ ]:


# Calculer l'estimation de la variance pour chacunes des m premières observations
# Attention: Suivant la fonction utilisée pour estimer la déviation, la définition par défaut de cette fonction peut 
# être différente de celle que nous utilisons (np.std par exemple, pour laquelle il faut utiliser le paramètre ddof = 1)
...


# Plot de l'évolution de l'estimation de la variance
...


# ## Exercice 3: Estimation de Monte-Carlo
# 
# Considérer un domaine quelconque (mesurable, de mesure non-nulle) $D\subset [0,1]^2\subset \mathbb{R}^2$. Soit $X\sim f_X$ un variable aléatoire de densité $f_X$ telle que $D\subset \text{supp}(f_X)$ (le support de $f_X$, c'est-à-dire l'ensemble pour lequel $f_X >0$) et soit $Y = \mathbf{1}_{\{X\in D\}}$. 
# 
# 1) Donner la distribution de $Y$ en fonction de $X$.
# 
# **Solution**:  
#   
# 2) Calculer l'espérance de $Y$. 
# 
# **Solution**:  
#   
# 3) Supposons à présent que $X \sim \mathcal{U}\left([-1,1]^2\right)$ et considérons le disque $D = \{(x,y) \in \mathbb{R}^2: x^2 +y^2 \leq 1\}$.  
# a) Calculer $\mathbb{P}(X\in D)$.
# 
# **Solution**:  
#   
# b) En supposant qu'on dispose d'un grand échantillon $X_1, \cdots, X_n \stackrel{idd}{\sim} \mathcal{U}\left([-1,1]^2\right)$ proposer une procédure pour estimer la valeure de $\pi$.
# 
# **Solution**:  
#   
# c) En déduire une estimation de $\pi$ et montrer la convergence de l'estimation sur un plot.

# In[ ]:


from scipy import stats as st
from matplotlib import pyplot as plt
import numpy as np

n = 5000

# Générer un échantillon de n VA unif([-1,1])
X = ...

# Générer la variable aléatoire Y
Y = (np.linalg.norm(X, axis = 1)<=1)

# Évolution de l'estimation de pi
...


# 4) Soit une fonction $h\in C^0([0,1]^2)$. À l'aide d'un échantillon de variables $X \sim \mathcal{U}\left([0,1]^2\right)$, en vous inspirant des questions précédentes, donner une estimation de 
# \begin{equation*}
# \int_{[0,1]^2} h(x) \ dx.
# \end{equation*}
# De plus, on rappel la propriété suivante de l'espérance: 
# \begin{equation*}
# \mathbb{E}[h(X)] = \int_{[0,1]^2} h(x,y) f_X(x,y)\ dxdy
# \end{equation*}
# 
# **Solution**:  
#   
# 5) En considérant la fonction $h(x,y) = e^{x^2+y^2}\in C^0([0,1]^2)$, calculer une approximation de $\int_{[0,1]^2} h(x) \ dx$ et comparé cette valeur à sa vrai valeur qui vaut $\int_{[0,1]^2} h(x) \ dx \approx 2.139350129$.

# In[ ]:


n = 5000
true_value = 2.139350129

# Générer un échantillon de n VA unif([-1,1])
X = ...

# Écrire la fonction h
def h(X):
    val = ...
    return val

# Générer la variable aléatoire Y
Y = ... 

# Plot de l'évolution de l'estimation de la moyenne
...


# 6) Soient $X_1, \cdots, X_n$ une suite variable aléatoire réelles indépendantes et identiquement distribuées de moyennes et de variances communes $\mu$ et $\sigma^2$ finies. On peut reformuler le théorème central limite de la façon suivante:
# \begin{equation*}
# \overline{X}_n - \mu \sim \frac{1}{\sqrt{n}}\mathcal{N}(0,\sigma^2),\ \text{pour $n$ assez grand}
# \end{equation*}
# On a donc que le taux de convergence de la $\text{RMSE} = \sqrt{\mathbb{E}\left[(\overline{X}_n-\mu)^2\right]}$ est de $\sqrt{n} = n^{-\frac{1}{2}}$. En reprenant l'estimation de $\pi$, illustrer le taux de convergence de la RMSE en estimant la racine carrée de l'erreur quadratique moyenne pour plusieurs valeurs de $n$ (par exemple $n\in\{10,20,50,100,200,500,1000\}$) et en générant à chaque fois $m = 100$ échantilons, puis en faire un plot en échelle logarithmique sur l'axe des ordonée. La doite de régression devrait avoir une pente de $-\frac{1}{2}$ car le taux de convergence est de $\sqrt{n}$.

# In[ ]:


N = [10,20,50,100,250,500,1000,2500,5000]
m = 100

RMSE = np.zeros(len(N))

for i,n in enumerate(N):
    échantillon_estimation = np.zeros(m)
    for j in range(m):
        # Générer un échantillon de n VA unif([-1,1])
        X = ...
        # Estimation de pi
        pi = ...
        # Calcul de la MSE de l'échantillon
        échantillon_estimation[j] = ...
    
    RMSE[i] = np.sqrt(échantillon_estimation.mean())

# Plot du taux de convergence
...


# Les applications des méthodes de Monte-Carlo sont nombreuses, cependant elles sont particulièrement utilisées pour calculer des intégrales en dimensions plus grandes que 1 (en particulier, pour calculer des surfaces et des volumes). Elles sont également couramment utilisées en physique des particules, où des simulations probabilistes permettent d'estimer la forme d'un signal ou la sensibilité d'un détecteur. La comparaison des données mesurées à ces simulations peut permettre de mettre en évidence des caractéristiques inattendues, par exemple de nouvelles particules.

# ## Exercice 4: 
# 
# On considère $ 100 $ lancers indépendants d'une pièce de monnaie dont la probabilité de tomber sur face est $ 3/5 $. 
# Soient $ X_i $, $ i \in \{ 1, \ldots, 100 \} $, les variables aléatoires telles que $ X_i=1 $ si on est tombé sur face au $ i^{ème}$ jet et $ X_i=0 $ sinon.
# 
# 1\) Quelle est la loi de $X_i$ pour $i\in\{1, \cdots, 100\}$ ?
# 
# **Solution**:  
#   
# 2\) Quelle est la loi de $ S_{100} = \sum_{i=1}^{100} X_i $?
# 
# **Solution**:  
#   
# 3\) Calculez $ \mathbb{P}(S_{100} \leq 60) $.

# In[ ]:


from scipy import stats as st
import numpy as np

n = 100
p = 3./5
prob = ... 
# Afficher le résulat
...


# 4\) Écrire une fonction qui standardise $S_{100}$ et donnez la loi approximative de la variable standardisée.  
# 
# **Solution**:  
#   
# 

# In[ ]:


# Place your answer here


# 5\) Approximez la valeur de $\mathbb{P}(S_{100} \leq 60)$ grâce à la question précédente et comparez cette valeur approximative à la valeur exacte.  
# 
# **Solution**:  
#   
# 

# In[ ]:


Z = ... 
prob_ = ... 
# Afficher le résulat
...


# ## Exercice 5: 
# 
# Soit $X$ le résultat du jet d'un dé équilibré.
# 
# 1\) Calculez $\mathbb{E}[X]$ et $\text{Var}(X)$

# In[ ]:


from scipy import stats as st
import numpy as np

E_X, V_X = ... 
# Afficher le résultat
...


# 2\) On lance $100$ dés équilibrés de façon indépendante. Calculez approximativement la probabilité la somme des $100$ résultats soit comprise entre $340$ et $360$.

# In[ ]:


# Place your answer here

