#!/usr/bin/env python
# coding: utf-8

# # Série3 : Correction 
#   ## Exercice 1: 
# 
# On suppose que la taille, en centimètres, d'un homme âgé de 25 ans est une variable aléatoire 
# normale de paramètres $\mu= 176.6$ et $\sigma^2=63.84$. 
# 
# 1\) Quelle est la probabilité que la taille d'un homme de 25 ans choisi au hasard soit supérieure à 170cm?

# In[ ]:


from scipy import stats as st
import numpy as np

mu = 176.6
sigma_square = 63.84

# Calculer cette probabilité en utilisant directement la fonction de répartition 
# d'une loi normale de moyenne 176.6 et de variance 63.84

prob =  1 - st.norm.cdf(170,loc = mu,scale = np.sqrt(sigma_square))

# Calculer cette probabilité en normalisant notre observation et en utilisant la 
# fonction de répartition d'une loi normale standardisé
normalisation = (170 - mu)/np.sqrt(sigma_square)
prob_ = 1 - st.norm.cdf(normalisation)


# 2\) Sachant que l'homme choisi mesure plus de 180cm, quelle est la probabilité qu'il mesure plus de 192cm?  
# a\) Calculer $\mathbb{P}(\{X > 192\} \bigcap \{X > 180\})$:  
# 
# **Solution**: 
# Comme $\{X > 180\} \subset \{X > 192\}$, on a $\mathbb{P}(\{X > 192\} \bigcap \{X > 180\}) = \mathbb{P}(X > 192)$
# 

# In[ ]:


########### Solution Python: ##########

prob_up =  1 - st.norm.cdf(192,loc = mu,scale = np.sqrt(sigma_square))


# b\) Calculer $\mathbb{P}(X > 180)$:

# In[ ]:


########### Solution Python: ##########

prob_sub =  1 - st.norm.cdf(180,loc = mu,scale = np.sqrt(sigma_square))


# c\) En déduire la valeur de la probabilité $\mathbb{P}(X > 192 | X > 180)$:

# In[ ]:


########### Solution Python: ##########

prob_cond = prob_up/prob_sub


# 3\) Quel est la taille $x$ pour laquelle il y a $5$% de chance d'observer plus grande que $x$, c'est-à-dire $x$ tel que $\mathbb{P}(X>x) = 0.05$ avec $X\sim\mathcal{N}(\mu,\sigma^2)$.

# In[ ]:


########### Solution Python: ##########

quantile = st.norm.ppf(0.95,mu,np.sqrt(sigma_square))
quantile


# ## Exercice 2: 
# 
# On considère une variable aléatoire réelle $X$ avec espérance $\mu$ et variance $\sigma^2 < \infty$. Soit $X_1, \dots, X_n$ un échantillon iid de $n$ variables aléatoires avec la même loi que $X$.
# On définit $\overline{X}=  \frac{1}{n}\sum_i^n X_i $ et $\hat{\sigma}^2 = \frac{1}{n}\sum_i (X_i - \overline{X})^2$ des estimateurs empiriques des deux premiers moments de $X$.
# 
# 1) a) Soit directement en markdown, soit à la main, calculer $\mathbb{E}[\overline{X}]$ et $\mathbb{E}[\hat{\sigma}^2]$:
# 
# **Solution**: 
# Calcul de $\mathbb{E}[\overline{X}]$:  
# \begin{align*}\mathbb{E}[\overline{X}] &= \mathbb{E}[\frac{1}{n}\sum_i^n X_i] \\
# &= \frac{1}{n}\mathbb{E}[\sum_i^n X_i] \\
# &= \frac{1}{n}\sum_i^n\mathbb{E}[ X_i] \\
# &= \frac{1}{n}\sum_i^n \mu = \mu 
# \end{align*}  
# 
# Calcul de $\mathbb{E}[\hat{\sigma}^2]$:
# \begin{align*}
# \mathbb{E}[\hat{\sigma}^2] &= \mathbb{E}[\frac{1}{n}\sum_i (X_i - \overline{X})^2] \\
# &= \frac{1}{n}\mathbb{E}[\sum_i (X_i - \overline{X})^2] \\
# &= \frac{1}{n}\mathbb{E}[\sum_i (X_i^2 - 2*X_i*\overline{X} + \overline{X}^2)] \\
# &= \frac{1}{n}\left( \mathbb{E}[\sum_i X_i^2] - 2 \overline{X}\mathbb{E}[\sum_i X_i] + \mathbb{E}[\sum_i \overline{X}^2]\right) \\
# &= \frac{1}{n}\left( \sum_i\mathbb{E}[ X_i^2] - 2\sum_i\mathbb{E}[ \overline{X} X_i] + \sum_i\mathbb{E}[\overline{X}^2]\right) \\
# &= \mathbb{E}[X_i^2] - 2 \mathbb{E}[\overline{X}^2] + \mathbb{E}[\overline{X}^2]
# \end{align*}
# Ce qui nous donne:
# \begin{equation*}
# \mathbb{E}[\hat{\sigma}^2] = \mathbb{E}[X_i^2] -  \mathbb{E}[\overline{X}^2] =  (\sigma^2 + \mu^2) - (\mu^2 + \frac{\sigma^2}{n}) = \frac{n-1}{n}\sigma^2
# \end{equation*} 
#   
# b) En déduire un estimateur non-biaisé de $\sigma^2$.
# 
# **Solution**:  
# Comme l'espérence est linéaire, on a que l'estimateur $\hat{\sigma}^2_{non-biaisé} = \frac{n}{n-1} \hat{\sigma}^2$ est non-biaisé. Effectivement, on a:
# \begin{equation*}
# \mathbb{E}[\hat{\sigma}^2_{non-biaisé}] = \frac{n}{n-1} \mathbb{E}[\hat{\sigma}^2] = \sigma^2 \end{equation*} 
# 
# 
# 2) Proposer une méthode pour estimer l'espérance et la variance si nous avions un échantillon $X_1, \dots, X_n$ de grande taille.
# 
# **Solution**:  
# 
# Comme nous venons de le montrer dans les questions précédentes, l'estimateur $\overline{X}$ est non-biaisé pour le paramètre $\mu$, donc une façon naturelle d'estimer $\mu$ si nous avons à disposition un grand nombre d'observation est de poser $\hat{\mu} = \overline{X}$. De la même façon, nous avons deux estimateur du paramètre $\sigma^2$:
# - $\hat{\sigma}^2$
# - $\hat{\sigma}^2_{non-biaisé}$  
# 
# L'estimateur $\hat{\sigma}^2_{non-biaisé}$ étant non-biaisé, nous préfèrerons celui-ci, dans le cadre de cet exercice, pour estimer $\sigma^2$. Avec un grand nombre d'observation à notre disposotion, nous estimerons donc $\sigma^2$ par $\hat{\sigma}^2_{non-biaisé} = \frac{1}{n-1}\sum_i (X_i - \overline{X})^2$. Cependant, nous verrons plus tard qu'il n'est pas toujours préférable de choisir un estimateur non-biaisé. En effet, il sera des fois mieux de choisir un estimateur avec un peu de biais mais une variance moindre, ce compromis entre le biais et la variance sera étudié à travers l'erreur quadratique moyenne (EQM).  
# 
# 3) Nous allons maintenant tester cela en générant un grand nombre de variables aléatoires pour une variable étudiée en cours (une variable suivant la loi Beta par exemple):  
# a) Générer $n = 10000$ observations de la loi que vous avez choisi.

# In[ ]:


########### Solution Python: ##########

from scipy import stats as st

n = 10000
a = 5.5
b = 3.14

X = st.beta.rvs(a,b,size=n)


# a\) Calculer la moyenne et la variance de la loi que vous avez choisi pour les paramètres que vous avez fixé.
# 
# **Solution**:  
# On rappelle une variable aléatoire $X\sim\text{Beta}(a,b)$, on a $\mathbb{E}[X] = \frac{a}{a +b}$ et $\text{Var}[X] = \frac{a - 1}{a + b -2}$.
# 

# In[ ]:


mean = a/(a+b)
var = a*b/((a+b)**2*(a+b+1))


# 1\) Faire un plot de l'évolution de l'estimation de la moyenne en fonction du nombre $m = 1, \cdots, n$ d'obervations utilisé dans l'estimation. Faire aussi apparaître la vrai valeur de la moyenne sur ce plot.

# In[ ]:


from matplotlib import pyplot as plt
import numpy as np

# Plot de l'évolution de l'estimation de la moyenne
fig, (ax1) = plt.subplots(1, 1,figsize = (6,4))
ax1.plot(np.arange(1,n+1),np.divide(np.cumsum(X),np.arange(1,n+1)))
ax1.hlines(mean,1,n,colors="r")
ax1.set_title("Plot de l'évolution de l'estimation de la moyenne")
ax1.set(xlabel='Nombre de variable utilisé dans l\'estimation',ylabel="Moyenne estimée")
plt.show()


# 2\) Faire un plot de l'évolution de l'estimation de la variance en fonction du nombre $m = 1, \cdots, n$ d'obervations utilisé dans l'estimation. Faire aussi apparaître la vrai valeur de la variance sur ce plot.

# In[ ]:


# Calculer l'estimation de la variance pour chacunes des m premières observations
# Attention: Suivant la fonction utilisée pour estimer la déviation, la définition par défaut de cette fonction peut 
# être différente de celle que nous utilisons (np.std par exemple, pour laquelle il faut utiliser le paramètre ddof = 1)
var_hat = np.zeros(n-1)
for i in range(1,n):
    var_hat[i-1] = np.std(X[:i+1],ddof=1)**2



# Plot de l'évolution de l'estimation de la variance
fig, (ax1) = plt.subplots(1, 1,figsize = (6,4))
ax1.plot(np.arange(2,n+1),var_hat)
ax1.hlines(var,1,n,colors="r")
ax1.set_title("Plot de l'évolution de l'estimation de la variance")
ax1.set(xlabel='Nombre de variable utilisé dans l\'estimation',ylabel="Variance estimée")
plt.show()


# ## Exercice 3: Estimation de Monte-Carlo
# 
# Considérer un domaine quelconque (mesurable, de mesure non-nulle) $D\subset [0,1]^2\subset \mathbb{R}^2$. Soit $X\sim f_X$ un variable aléatoire de densité $f_X$ telle que $D\subset \text{supp}(f_X)$ (le support de $f_X$, c'est-à-dire l'ensemble pour lequel $f_X >0$) et soit $Y = \mathbf{1}_{\{X\in D\}}$. 
# 
# 1) Donner la distribution de $Y$ en fonction de $X$.
# 
# **Solution**:
# 
# \begin{equation*}
# Y = \left\{ \begin{array}{ll}
# 1 & \text{ si $X\in D$} \\
# 0 & \text{ sinon}.
# \end{array} \right. = 
# \left\{ \begin{array}{ll}
# 1 & \text{ avec probabilité }\Pr(X\in D) \\
# 0 & \text{ avec probabilité } 1 - \Pr(X\in D).
# \end{array} \right.
# \end{equation*}  
# 
# 2) Calculer l'espérance de $Y$. 
# 
# **Solution**:
# 
# On a:
# \begin{equation*}
# \mathbb{E}[Y]= \mathbb{E}\left[\mathbf{1}_{\{X\in D\}}\right] = \mathbb{P}\left( X\in D\right) 
# \end{equation*}
# 
# 3) Supposons à présent que $X \sim \mathcal{U}\left([-1,1]^2\right)$ et considérons le disque $D = \{(x,y) \in \mathbb{R}^2: x^2 +y^2 \leq 1\}$.  
# a) Calculer $\mathbb{P}(X\in D)$.
# 
# **Solution**: On a:
# \begin{equation*}
# \mathbb{P}(X\in D) = \iint_{D} f_X(x,y) dx dy = \iint_{D} \frac{1}{4} dx dy = \frac{\pi}{4}
# \end{equation*} 
# 
# b) En supposant qu'on dispose d'un grand échantillon $X_1, \cdots, X_n \stackrel{idd}{\sim} \mathcal{U}\left([-1,1]^2\right)$ proposer une procédure pour estimer la valeure de $\pi$.
# 
# **Solution**: On a vu précédement qu'en définissant la variable aléatoire $Y = \mathbf{1}_{\{X\in D\}}$, on a que $\mathbb{E}[Y] = \mathbb{P}\left( X\in D\right) = \frac{\pi}{4}$. Avec un $n$ observations de la variable aléatoire $X$, on peut donc avoir $n$ observations de la variable aléatoire $Y$ et donc estimer $\mathbb{E}[Y]$ avec plus ou moins de précision en fonction de $n$. On aura alors $\pi \approx 4\overline{Y}$.  
# 
# c) En déduire une estimation de $\pi$ et montrer la convergence de l'estimation sur un plot.

# In[ ]:


from scipy import stats as st
from matplotlib import pyplot as plt
import numpy as np

n = 5000

# Générer un échantillon de n VA unif([-1,1])

X = st.uniform.rvs(size=(n,2),loc=-1,scale=2.)

# Générer la variable aléatoire Y
Y = (np.linalg.norm(X, axis = 1)<=1)

# Évolution de l'estimation de pi
fig, (ax1) = plt.subplots(1, 1,figsize = (6,4))
ax1.plot(np.arange(1,n+1),4*np.cumsum(Y)/np.arange(1,n+1))
ax1.hlines(np.pi,1,n,colors="r")
ax1.set_title("Plot de l'évolution de l'estimation de la moyenne")
ax1.set(xlabel='Nombre de variable utilisé dans l\'estimation')
plt.show()


# 4) Soit une fonction $h\in C^0([0,1]^2)$. À l'aide d'un échantillon de variables $X \sim \mathcal{U}\left([0,1]^2\right)$, en vous inspirant des questions précédentes, donner une estimation de 
# \begin{equation*}
# \int_{[0,1]^2} h(x) \ dx.
# \end{equation*}
# De plus, on rappel la propriété suivante de l'espérance: 
# \begin{equation*}
# \mathbb{E}[h(X)] = \int_{[0,1]^2} h(x,y) f_X(x,y)\ dxdy
# \end{equation*}
# 
# **Solution**:  En utilisant la propriété de l'espérance ci-dessus et en l'associant avec le fait que $f_X(x,y) = 1,\  \forall x,y \in[0,1]$, on obtient que: 
# \begin{equation*}
# \int_{[0,1]^2} h(x) \ dx = \mathbb{E}[h(X)]
# \end{equation*}
# Une façon naturelle d'estimer $\int_{[0,1]^2} h(x) \ dx$ est donc de calculer de transformer l'échantillon $X_1, \cdots, X_n \sim \mathcal{U}\left([0,1]^2\right)$  que nous avons en un échantillon $h(X_1,) \cdots, h(X_n)$, puis d'estimer l'espérance de la variable $h(X)$ par l'estimateur non-biaisé $\overline{h(X)} = \frac{1}{n} \sum_{i=1}^{n}h(X_i)$.
# 
# 5) En considérant la fonction $h(x,y) = e^{x^2+y^2}\in C^0([0,1]^2)$, calculer une approximation de $\int_{[0,1]^2} h(x) \ dx$ et comparé cette valeur à sa vrai valeur qui vaut $\int_{[0,1]^2} h(x) \ dx \approx 2.139350129$.

# In[ ]:


n = 5000
true_value = 2.139350129

# Générer un échantillon de n VA unif([-1,1])

X = st.uniform.rvs(size=(n,2),loc=0,scale=1)

# Écrire la fonction h
def h(X):
    
    val = np.exp(np.linalg.norm(X,axis = 1)**2)
    return val

# Générer la variable aléatoire Y
Y = h(X)

# Plot de l'évolution de l'estimation de la moyenne
fig, (ax1) = plt.subplots(1, 1,figsize = (6,4))
ax1.plot(np.arange(1,n+1),np.cumsum(Y)/np.arange(1,n+1))
ax1.hlines(true_value,1,n,colors="r")
ax1.set_title("Évolution de l'estimation de l'intégrale")
ax1.set(xlabel='Nombre de variable utilisé dans l\'estimation')
plt.show()


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
        
        X = st.uniform.rvs(size=(n,2),loc=-1,scale=2.)
        # Estimation de pi
        
        pi = (np.linalg.norm(X, axis = 1)<=1).mean()*4
        # Calcul de la MSE de l'échantillon
        
        échantillon_estimation[j] = (pi-np.pi)**2
    
    RMSE[i] = np.sqrt(échantillon_estimation.mean())

# Plot du taux de convergence
fig, (ax1) = plt.subplots(1, 1,figsize = (6,4))
ax1.loglog(N,RMSE)
ax1.loglog(N,1./np.sqrt(N),"k")
ax1.set_title("Taux de convergence de la RMSE")
ax1.set(xlabel='n')
plt.show()


# Les applications des méthodes de Monte-Carlo sont nombreuses, cependant elles sont particulièrement utilisées pour calculer des intégrales en dimensions plus grandes que 1 (en particulier, pour calculer des surfaces et des volumes). Elles sont également couramment utilisées en physique des particules, où des simulations probabilistes permettent d'estimer la forme d'un signal ou la sensibilité d'un détecteur. La comparaison des données mesurées à ces simulations peut permettre de mettre en évidence des caractéristiques inattendues, par exemple de nouvelles particules.

# ## Exercice 4: 
# 
# On considère $ 100 $ lancers indépendants d'une pièce de monnaie dont la probabilité de tomber sur face est $ 3/5 $. 
# Soient $ X_i $, $ i \in \{ 1, \ldots, 100 \} $, les variables aléatoires telles que $ X_i=1 $ si on est tombé sur face au $ i^{ème}$ jet et $ X_i=0 $ sinon.
# 
# 1\) Quelle est la loi de $X_i$ pour $i\in\{1, \cdots, 100\}$ ?
# 
# **Solution**: $ X_i \sim \mathcal{B}(3/5) $ pour $ i \in \{ 1, \ldots, 100\} $, c'est-à-dire qu'il s'agit d'une variable de Bernoulli.
# 
# 2\) Quelle est la loi de $ S_{100} = \sum_{i=1}^{100} X_i $?
# 
# **Solution**: $ S_{100} \sim \mathcal{B}(100, 3/5) $, c'est-à-dire qu'il s'agit d'une variable binomiale.
# 
# 3\) Calculez $ \mathbb{P}(S_{100} \leq 60) $.

# In[ ]:


from scipy import stats as st
import numpy as np

n = 100
p = 3./5
prob = st.binom.cdf(60,n,p)
# Afficher le résulat
print(f"La probabilité de faire moins de 60 face est de {prob}")


# 4\) Écrire une fonction qui standardise $S_{100}$ et donnez la loi approximative de la variable standardisée.  
# 
# **Solution**: D'après le théorème central limite, la loi approximative de $ Z_{100} $ est $ \mathcal{N}(0, 1) $.  
# 
# 

# In[ ]:


########### Solution Python: ##########


def standardise(S,n,p):
    Z = (S-n*p)/np.sqrt(n*p*(1-p))#C1
    return Z


# 5\) Approximez la valeur de $\mathbb{P}(S_{100} \leq 60)$ grâce à la question précédente et comparez cette valeur approximative à la valeur exacte.  
# 
# **Solution**:  En utilisant la loi approximative de $ Z_{100} $ on obtient
# $$
# \mathbb{P}(S_{100} \leq 60) = 
# \mathbb{P} \left( \frac{S_{100} - 60}{\sqrt{24}} \leq \frac{60 - 60}{\sqrt{24}}  \right)
# \approx
# \Phi(0) = 0.5,
# $$
# ce qui est proche du résultat exact $ \mathbb{P}(S_{100} \leq 60) = 0.5379$.
# 
# 

# In[ ]:


Z = standardise(60,n,p)
prob_ = st.norm.cdf(Z)
# Afficher le résulat
print(f"L'approximation via le TCL de la probabilité de faire moins de 60 face est de {prob_}")


# ## Exercice 5: 
# 
# Soit $X$ le résultat du jet d'un dé équilibré.
# 
# 1\) Calculez $\mathbb{E}[X]$ et $\text{Var}(X)$

# In[ ]:


from scipy import stats as st
import numpy as np

E_X, V_X = st.randint.stats(1,7)
# Afficher le résultat
print(f"L'espérance de X est: {E_X}\nLa variance de X est: {V_X}")


# 2\) On lance $100$ dés équilibrés de façon indépendante. Calculez approximativement la probabilité la somme des $100$ résultats soit comprise entre $340$ et $360$.

# In[ ]:


########### Solution Python: ##########

n = 100
upper_boundary = 360
lower_boundary = 340

def standardise(S,n,mu,sigma_square):
    Z = (S-n*mu)/np.sqrt(n*sigma_square)#C1
    return Z

prob = st.norm.cdf(standardise(upper_boundary,n,E_X,V_X)) - st.norm.cdf(standardise(lower_boundary,n,E_X,V_X))
print(f"La probabilité que la somme des 100 lancés soit comprise entre 340 et 360 est donc approximativement de {prob}")

