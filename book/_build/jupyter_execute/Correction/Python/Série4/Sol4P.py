#!/usr/bin/env python
# coding: utf-8

# # Série4 : Correction 
#   ## Exercice 1: 
# 
# Une entreprise d'automobiles veut publier des informations sur la consommation d'un nouveau modèle de voiture. 
# Pour 12 voitures de ce modèle on mesure la consommation d'essence, en litres, pour parcourir 100 km, et on obtient
# les résultats suivants:
# \begin{gather*}
# 14.60, 11.21, 11.56, 11.37, 13.68, 15.07, 11.06, 16.58, 13.37, 15.98,
# 12.07, 13.22
# \end{gather*}
# 
# 1\) Supposez que la consommation d'essence pour une voiture de ce modèle est une variable aléatoire $ X \sim \mathcal{N}(\mu , 3.5 ) $ avec $ \mu $ inconnu, et que les données récoltées sont indépendantes.  
# a\) Écrire une fonction qui retourne un intervalle de confiance symmétrique à $ (1-\alpha)100\,\% $  pour $ \mu $ dans le cas où l'on connait la variance. (N'hésitez pas à faire des développements à la main ou en markdown avant de vous lancez dans l'implémentatioonde cette fonction)
# 
# 
# **Solution**: 
# Si $X_1,\dots,X_n$ sont iid $\mathcal{N}(\mu,\sigma^2)$, alors
# \begin{gather*}
# Z_n=\sqrt{n}\,\frac{\overline X_n-\mu}{\sigma}\sim \mathcal{N}(0,1).
# \end{gather*}
# On sait que
# \begin{gather*}
# \Pr(-z < Z_n < z) = 2\, \Phi(z) - 1 ,
# \end{gather*}
# pour toute constante $ z > 0 $.
# Donc si on choisit $ z_{1-\alpha/2} = \Phi^{-1}(1-\alpha/2) $
# (le $ (1-\alpha/2)- $quantile de la loi $ N(0,1) $), on obtient que
# \begin{gather*}
# 1-\alpha = \mathbb{P}(-z_{1-\alpha/2} < Z_n < z_{1-\alpha/2}) = \mathbb{P} \left( -z_{1-\alpha/2} < \sqrt{n}\,\frac{\overline{X}_n-\mu}{\sigma} < z_{1-\alpha/2} \right)  = \mathbb{P} \left( \overline{X}_n -\frac{z_{1-\alpha/2}}{\sqrt{n}}\, \sigma < \mu < \overline{X}_n + \frac{z_{1-\alpha/2}}{\sqrt{n}}\, \sigma \right) 
# \end{gather*}
# L'intervalle 
# \begin{gather*}
# \left( \overline{X}_n -\frac{z_{1-\alpha/2}}{\sqrt{n}}\, \sigma , \overline{X}_n + \frac{z_{1-\alpha/2}}{\sqrt{n}}\, \sigma 
# \right)
# \end{gather*}
# couvre donc la vraie valeur de $ \mu $ avec la probabilité $ 1-\alpha $.
# 
# 

# In[ ]:


import pandas as pd
from scipy import stats as st
import numpy as np

def IC_variance_connue(x_bar,sigma_square,n,alpha):
    quantile = st.norm.ppf(1-alpha/2)
    
    IC = pd.DataFrame(data = {"lower_bound":[x_bar-quantile*np.sqrt(sigma_square/n)],"upper_bound":[x_bar  + quantile*np.sqrt(sigma_square/n)]})
    return IC


# b\) Calculez cet intervalle de confiance pour le jeu de donnée fourni.

# In[ ]:


# Importation des données
data = pd.read_csv("consommation.csv")

# Calcul de la moyenne empirique
mean = data.consommation.mean()

n = len(data)
sigma_square = 3.5
alpha = 0.05

IC = IC_variance_connue(mean,sigma_square,n,alpha)
# Afficher cet intervalle
print(f"L'intervalle de confiance à 95% est donc: [{IC.lower_bound[0]:.3f},{IC.upper_bound[0]:.3f}]")


# On va maintenant abandonner l'hypothèse de variance connue (ce qui est plus réaliste).  On considère toujours un modèle normal, mais cette fois on suppose que $ X ~\sim \mathcal{N}(\mu , \sigma^2 ) $ avec $ \mu $ et $ \sigma^2 $ inconnus. Les données récoltées sont toujours considérées indépendantes.
# 
# 2\) Impémentez une fonction qui retourne un intervalle de confiance symmétrique à $ (1-\alpha)100\,\% $  pour $ \mu $ dans le cas où la variance est inconnue. (N'hésitez pas à faire des développements à la main ou en markdown avant de vous lancez dans l'implémentatioonde cette fonction)
# 
# **Solution**: 
# Si $X_1,\dots,X_n$ sont iid $\mathcal{N}(\mu,\sigma^2)$, alors
# \begin{gather*}
# T=\sqrt{n}\,\frac{\overline{X}_n-\mu}{S_n}\sim t_{n-1},
# \end{gather*}
# où $S_n^2=\frac1{n-1}\sum_{i=1}^n(X_i-\overline{X})^2$, et $ t_{\nu} $
# est la loi de Student avec $ \nu $ degrés de liberté. La loi de Student
# est symétrique autour de zéro de la même manière que la loi $ \mathcal{N}(0,1) $.
# On a donc
# \begin{gather*}
# \Pr(-t_{n-1,1-\alpha/2} < T < t_{n-1,1-\alpha/2} =  1 - \alpha, 
# \end{gather*}
# c'est-à-dire que $t_{n-1,\alpha/2} = -t_{n-1,1-\alpha/2}$, et donc
# \begin{gather*}
# ]t_{n-1,\alpha/2}, t_{n-1,1-\alpha/2} [\quad=\quad ]-t_{n-1,1-\alpha/2} , t_{n-1,1-\alpha/2} [.
# \end{gather*}
# 
# On obtient l'intervalle de confiance
# sous la forme
# \begin{gather*}
# \left( \overline{X}_n -\frac{t_{n-1,1-\alpha/2}}{\sqrt{n}}\, S_n ,\ \overline{X}_n + \frac{t_{n-1,1-\alpha/2}}{\sqrt{n}}\, S_n \right).
# \end{gather*}
# 

# In[ ]:


########### Solution Python: ##########


def IC_variance_inconnue(x_bar,sigma_est,n,alpha):
    quantile = st.t.ppf(1-alpha/2,n -1)
    IC = pd.DataFrame(data = {"lower_bound":[x_bar-quantile*np.sqrt(sigma_est/n)],"upper_bound":[x_bar  + quantile*np.sqrt(sigma_est/n)]})
    return IC


# 3\) a\) Calculez un intervalle de confiance à $95\,\% $ pour le jeu de donnée fourni.

# In[ ]:


########### Solution Python: ##########

alpha = 0.05
IC = IC_variance_inconnue(data.consommation.mean(),data.consommation.var(),n,alpha)
print(f"L'intervalle de confiance à 95% est donc: [{IC.lower_bound[0]:.3f},{IC.upper_bound[0]:.3f}]")


# b\) Calculez un intervalle de confiance à $90\,\% $ pour le jeu de donnée fourni.

# In[ ]:


########### Solution Python: ##########

alpha = 0.1
IC = IC_variance_inconnue(data.consommation.mean(),data.consommation.var(),n,alpha)
print(f"L'intervalle de confiance à 90% est donc: [{IC.lower_bound[0]:.3f},{IC.upper_bound[0]:.3f}]")


# c\) Commentez la différence entre ces deux intervalles.
# 
# **Solution**: L'intervalle de confiance à $90\,\% $ est plus étroit que l'intervalle de confiance à $95\,\% $, car son seuil de confiance est plus petit. Plus on veut être confiant qu'un intervalle couvre la vraie valeur de $\mu$, plus cet intervalle doit être large (et vice-versa).   
# 
# 4\) Que l'entreprise peut-elle faire pour obtenir un intervalle de confiance à $ 95\,\% $ plus étroit que celui obtenu?
# 
# **Solution**: Récolter plus de données. Plus on a de données, plus l'incertitude est faible. 
# 
# 

# ## Exercice 2: 
# 
# Une marque de friandises produit des bonbons au chocolat de six couleurs. Le responsable  de la communication affirme que les proportions des différentes couleurs sont de $30\,\%$ pour le brun, $20\,\%$ pour le jaune, $20\,\%$ pour le rouge, $10\,\%$ pour l'orange, $10\,\%$ pour le vert et $10\,\%$ pour le doré. Une expérience réalisée sur un total de $370$ bonbons donne les nombres suivants :
# 
# | Couleur           | Brun | Jaune | Rouge | Orange | Vert | Doré |
# |-------------------|------|-------|-------|--------|------|------|
# | Nombre de bonbons | 84   | 79    | 75    | 49     | 36   | 47   |
# 
# Les données semblent-elles en accord avec l'affirmation du responsable de la communication? Faites un test à un niveau de signification de $5\%$.
# 
# 1\) Proposer une hypothèse nulle et une hypothèse alternative qui permettront de tester l'affirmation du responsable de la communication.
# 
# **Solution**: On va tester 
# \begin{eqnarray*}
# & H_0:&  \text{l'affirmation du responsable de la communication est vraie}, \\ 
# & H_1: & \text{l'affirmation du responsable de la communication est fausse}.
# \end{eqnarray*} 
# Ainsi, si on note $ p_B $ la proportion de brun, $ p_J $ la proportion de jaune, $ p_R $ la proportion de rouge, $ p_O $ la proportion d'orange, $ p_V $ la proportion 
# de vert et $ p_D $ la proportion de doré, on a
# \begin{eqnarray*}
# & H_0: &  \ p_B = 0.3,\ p_J = 0.2,\ p_R = 0.2,\ p_O = 0.1,\ p_V = 0.1,\ p_D = 0.1,  \\
# & H_1: & H_0 \text{ n'est pas vraie.}
# \end{eqnarray*}  
# 
# 2\) Quel test allez-vous utiliser pour tester ces deux hypothèses ? Donnez la statistique $T$ associé à ce test, ainsi que sa loi approximative sous $H_0$. De plus, y a-t-il une/des conditions pour que la convergence de $T$ soit le moins déraisonnable possible ? Si oui, énoncé-la/les et vérifier la/les.
# 
# **Solution**: Il s'agit d'un test d'adéquation. On peut baser la statistique de test sur les différences
# entre les nombres de bonbons des différentes couleurs observés ($ O_i $) et les nombres attendus 
# si $ H_0 $ est vraie ($ E_i $):
# \begin{gather*}
# T=\sum_{i=1}^k \frac{(O_i-E_i)^2}{E_i}, 
# \end{gather*}
# où $ k $ est le nombre de classes.
# Si le nombre d'observations est assez grand et les nombres attendus sont suffisamment élevés (en pratique supérieurs ou égaux à 5), la statistique $ T $ suit approximativement sous $ H_0 $ une loi $ \chi^2 $ dont le nombre de degrés de liberté est égal à
# \begin{gather*}
# (\text{nombre de classes}) - 1 - (\text{nombre de paramètres estimés sous $H_0$}). 
# \end{gather*}
# 
# Dans notre cas, les nombres observés et attendus sont affichés dans la cellule de code suivante. La taille de l'échantillon est grande et tous les nombres attendus $e_i$ sont plus grands que $5$.
# On peut donc utiliser l'approximation de la loi de la statistique $ T $ sous $ H_0 $ par la loi asymptotique (mentionnée ci-dessus). Nous avons 6 classes et aucun paramètre à estimer sous $ H_0 $ (les proportions sous $ H_0 $ sont
# données). Cela donne 5 degrés de liberté pour la loi asymptotique.
# 

# In[ ]:


import pandas as pd

# Vérifier que la/les conditions sont remplies
data = pd.DataFrame(data = {"Couleur": ["Brun" , "Jaune" , "Rouge" , "Orange" , "Vert" , "Doré"],
                           "Nombre_observé": [84   , 79    , 75    , 49     , 36   , 47],
                           "probabilité": [0.3,0.2,0.2,0.1,0.1,0.1]})
data["Nombre_attendu"] = data.Nombre_observé.sum()*data.probabilité

if not False in (data.Nombre_attendu>5):
    print("Tous les nombres d'observations attendus sont supérieur à 5, la conditions est donc remplie.")
else: 
    print("Tous les nombres d'observations attendus ne sont pas supérieur à 5, la conditions n'est donc pas remplie.")


# 3\) Tester l'hypothèse nulle $H_0$ à un seuil de $5\,\%$. Les données semblent-elles en accord avec l'affirmation du responsable de communication ? 
# 
# **Solution**: Il reste à calculer la valeur observée de la statistique de test et la comparer avec une valeur critique. En testant à un niveau de $ 5\, \% $ (ce qui est le niveau standard),la valeur critique est  $ \chi^2_{5; 0.95}=11.07 $. La valeur observée de la statistique de test est 
# \begin{gather*}
# t_{obs} = \sum_{i=1}^6 \frac{(o_i-e_i)^2}{e_i} = 13.54.
# \end{gather*}
# Puisque cette valeur est plus grande que la valeur critique, on rejette $H_0$ en faveur de $ H_1 $. On peut dire que, à un niveau de signification de $ 5\, \% $, on a montré que l'affirmation du responsable de communication est fausse.
# 

# In[ ]:


from scipy import stats as st

degree_of_freedom = 5
alpha = 0.05

valeur_critique = st.chi2.ppf(1-alpha,degree_of_freedom)
t_obs = ((data.Nombre_observé - data.Nombre_attendu)**2/data.Nombre_attendu).sum()
# Test pour savoir si on rejette ou non l'hypothèse nulle
if (t_obs > valeur_critique):
    print("On rejette H_0 en faveur de H_1")
else:
    print("On ne peut pas rejetter H_0 en faveur de H_1.")


# ## Exercice 3: 
# 
# Le tableau suivant donne le nombre de naissances dans un hôpital pour quatre trimestres consécutifs:
# 
# | Trimestre            | Janv-Mars | Avr-Juin | Juil-Sept | Oct-Déc |
# |----------------------|-----------|----------|-----------|---------|
# | Nombre de naissances | 110       | 57       | 53        | 80      |
# 
# 1\) Nous voulons tester à un niveau de signification de $ 1 \,\% $  si la natalité du premier trimestre est deux fois plus élevée que celle de chacun des autres trimestres, qui sont toutes égales.  
# a\) Écrire explicitement les hypothèses nulle et alternative qui nous permettent de tester l'hypothèse ci-dessus. Sous $H_0$, connait-on la distribution exacte des naissances ou faut-il l'estimer ? Si elle est connue, donnez là. 
# 
# **Solution**: On va tester 
# \begin{eqnarray*} 
# & H_0: & \text{la natalité du 1er trimestre est deux fois plus élevée que celle des autres trimestres,} \\
# & H_1: & H_0  \text{ est fausse}.
# \end{eqnarray*}
# Ainsi, si on note $ p_I $ la probabilité de naître au premier trimestre, $ p_{II} $ la probabilité de naître au deuxième trimestre, $ p_{III} $ la probabilité de naître au troisième trimestre et $ p_{IV} $ la probabilité de naître au quatrième trimestre, on a
# \begin{eqnarray*}
# & H_0: &  p_I = 2\times p_{II},\ p_{II} = p_{III} = p_{IV}, \\
# & H_1: & H_0 \text{ n'est pas vraie.}
# \end{eqnarray*}
# Puisque $ p_{I} + p_{II} + p_{III} + p_{IV} = 1  $, on a que
# $ H_0: \  p_I = 0.4,\ p_{II} = p_{III} = p_{IV} = 0.2 $. 
# 
# b\) Quel test allez-vous utiliser pour tester ces deux hypothèses ? Donnez la statistique $T$ associé à ce test, ainsi que sa loi approximative sous $H_0$. De plus, y a-t-il une/des conditions pour que la convergence de $T$ soit le moins déraisonnable possible ? Si oui, énoncé-la/les et vérifier la/les.
# 
# **Solution**: Il s'agit d'un test d'adéquation. On peut baser la statistique de test sur les différences
# entre les nombres de naissances observées ($ O_i $) et les nombres attendus 
# si $ H_0 $ est vraie ($ E_i $):
# \begin{gather*}
# T=\sum_{i=1}^4 \frac{(O_i-E_i)^2}{E_i}.
# \end{gather*}
# qui, sous $H_0$, suit la loi $\chi^2_\nu$ avec $\nu = 4-1-0=3$, à condition que les nombres attendus sous $H_0$ soit supérieures à $5$, ce qui est le cas comme on peut le voir ci-dessous.  
# 

# In[ ]:


import pandas as pd

# Vérifier que la/les conditions sont remplies
data = pd.DataFrame(data = {"Semestre": ["Janv-Mars" , "Avr-Juin" , "Juil-Sept" , "Oct-Déc" ],
                           "Nombre_observé": [110   , 57    , 53    , 80  ],
                           "probabilité": [0.4,0.2,0.2,0.2]})
data["Nombre_attendu"] = data.Nombre_observé.sum()*data.probabilité

if not False in (data.Nombre_attendu>5):
    print("Tous les nombres d'observations attendus sont supérieur à 5, la conditions est donc remplie.")
else: 
    print("Tous les nombres d'observations attendus ne sont pas supérieur à 5, la conditions n'est donc pas remplie.")


# c\) Tester l'hypothèse nulle $H_0$ à un seuil de $1\,\%$.
# 
# **Solution**: Il reste à calculer la valeur observée de la statistique de test et la comparer avec une valeur critique. En testant à un niveau de $ 1\, \% $ ,la valeur critique est  $ \chi^2_{5; 0.95}=11.345 $. La valeur observée de la statistique de test est 
# \begin{gather*}
# t_{obs} = \sum_{i=1}^6 \frac{(o_i-e_i)^2}{e_i} = 8.467.
# \end{gather*}
# Puisque cette valeur est plus petite que la valeur critique, on ne rejette donc pas $H_0$. 
# 

# In[ ]:


from scipy import stats as st

degree_of_freedom = 3
alpha = 0.01

valeur_critique = st.chi2.ppf(1-alpha,degree_of_freedom)

t_obs = ((data.Nombre_observé - data.Nombre_attendu)**2/data.Nombre_attendu).sum()
# Test pour savoir si on rejette ou non l'hypothèse nulle
if (t_obs > valeur_critique):
    print("On rejette H_0 en faveur de H_1")
else:
    print("On ne peut pas rejetter H_0 en faveur de H_1.")


# 2\) Nous voulon maintenant tester à un niveau de signification de $ 1 \,\% $ si la natalité du premier trimestre est égale à celle du quatrième trimestre, et celle du deuxième trimestre est égale à celle du troisième trimestre.  
# a\) Écrire explicitement les hypothèses nulle et alternative qui nous permettent de tester l'hypothèse ci-dessus.
# 
# **Solution**: On va tester
# \begin{eqnarray*}
# & H_0: &  p_I = p_{IV},\ p_{II} = p_{III},\\
# & H_1: & H_0 \text{ n'est pas vraie.}
# \end{eqnarray*}  
# 
# b\)  Sous $H_0$, connait-on la distribution exacte des naissances ou faut-il l'estimer ? Si elle est connu donnez là, sinon estimez là.
# 
# *Indication:* Si on note par $p_j$, $j=1,\dots,4$, la probabilité d'être dans le $j$-ème trimestre, il faut tester $H_0$: $p_1=p_4$, $p_2=p_3$ (c'est-à-dire, les $p_j$ sont tels que $p_1=p_4$ et $p_2=p_3$, mais autrement inconnus). Pour calculer les nombres attendus, on commence par estimer la valeur $p_{14}=\mathbb{P}(\text{né dans le 1er ou 4ème trimestre})$ par la fréquence empirique et on utilise le fait que $p_1=p_4=p_{14}/2$ sous $H_0$.
# 
# **Solution**: La différence avec la partie précédente est qu'ici nous n'avons pas de nombres concrets pour les proportions  attendues sous $ H_0 $. Il faut donc les estimer. Avant de le faire, on réfléchit au nombre minimal de paramètres à estimer. En fait, ici il suffit d'estimer $ p_{I} $ car sous $ H_0 $ on a $ p_{IV} = p_{I} $ et $ p_{II} = p_{III} = (1 - 2\, p_{I}) / 2 $.
# On estime $ p_{I} $ par $\hat p_{I}=(o_1/\sum_{i=1}^4 o_i + o_4/\sum_{i=1}^4 o_i)/2=(o_1+o_4)/(2 \sum_{i=1}^4 o_i)= (110+80)/600=190/600$.
# Pour être rigoureux, il faudrait vérifier que l'estimateur $\hat p_{I}$ est l'estimateur
# du maximum de vraisemblance; ceci est laissé en exercice.
# 
# 
# c\) Quel test allez-vous utiliser pour tester ces deux hypothèses ? Donnez la statistique $T$ associé à ce test, ainsi que sa loi approximative sous $H_0$.  
# 
# **Solution**: En utilisant $ \hat{p}_{IV} = \hat p_{I} $ et $ \hat p_{II} = \hat p_{III} = (1 - 2\, \hat p_{I}) / 2 $,
# on obtient les nombres attendus estimés calculés dans la cellule de code suivante.
# Il s'agit encore d'un test d'adéquation, on utilise alors la statistique de test  
# \begin{gather*}
# T=\sum_{j=1}^4 \frac{(O_j-E_j)^2}{E_j},
# \end{gather*}
# qui, sous $H_0$, suit la loi $\chi^2_\nu$ avec
# $\nu = 4-1-1=2$ (on a estimé un paramètre). 
# 
# 

# In[ ]:


data = pd.DataFrame(data = {"Semestre": ["Janv-Mars" , "Avr-Juin" , "Juil-Sept" , "Oct-Déc" ],
                           "Nombre_observé": [110   , 57    , 53    , 80  ]})

# Estimation probabilité
p1_hat = (data.Nombre_observé[0] + data.Nombre_observé[3])/(2*data.Nombre_observé.sum())
prob = [p1_hat,(1-2*p1_hat)/2,(1-2*p1_hat)/2,p1_hat]
data["probabilité"] = prob


# Calculez les nombres attendus et vérifier que la condition est remplie
data["Nombre_attendu"] = data.Nombre_observé.sum()*data.probabilité
print(data,"\n")
if not False in (data.Nombre_attendu>5):
    print("Tous les nombres d'observations attendus sont supérieur à 5, la conditions est donc remplie.")
else: 
    print("Tous les nombres d'observations attendus ne sont pas supérieur à 5, la conditions n'est donc pas remplie.")


# d\) Tester l'hypothèse nulle $H_0$ à un seuil de $1\,\%$.
# 
# **Solution**: Il reste à calculer la valeur observée de la statistique de test et la comparer avec une valeur critique. La réalisation de la statistique $T$ est $t_{obs}=4.88$. Celle-ci est pluspetite que le quantile $\chi^2_{2;0.99}=9.21$ donc on ne rejette pas $H_0$.
# 

# In[ ]:


from scipy import stats as st

degree_of_freedom = 2
alpha = 0.01

valeur_critique = st.chi2.ppf(1-alpha,degree_of_freedom)

t_obs = ((data.Nombre_observé - data.Nombre_attendu)**2/data.Nombre_attendu).sum()
# Test pour savoir si on rejette ou non l'hypothèse nulle
if (t_obs > valeur_critique):
    print("On rejette H_0 en faveur de H_1")
else:
    print("On ne peut pas rejetter H_0 en faveur de H_1.")


# *Dans cet exercice on n'a rejeté aucune hypothèse nulle. Évidemment, les deux hypothèses nulles sont incompatibles, donc cela peut paraître étrange. Mais rappelons-nous que « ne pas rejeter »  n'est pas « accepter » .*

# ## Exercice 4: 
# 
# Les données ci-dessous représentent le taux d'oxygénation de cours d'eau ayant la même température dans une certaine région:
# 
# | taux d'oxygénation (par jour) | fréquence |
# |-------------------------------|-----------|
# | $ \le 0.1$                    | 12        |
# | $ (0.1,\ 0.15] $              | 20        |
# | $ (0.15,\ 0.20] $             | 23        |
# | $ (0.20,\ 0.25] $             | 15        |
# | $ >0.25$                      | 13        |
# 
# La moyenne et l'écart-type calculées pour cet échantillon de taille $83$ sont $\overline{x} = 0.173$ et $s_x = 0.066$, respectivement. Nous voulon tester à un niveau de signification de $ 5\, \% $ la qualité de l'ajustement d'une loi normale aux données ci-dessus.
# 
# 1\) Écrire explicitement les hypothèses nulle et alternative qui nous permettent de tester l'hypothèse ci-dessus.   
# 
# **Solution**: On a
# \begin{eqnarray*}
# & H_0: &  \text{les données viennent d'une loi normale},\\
# & H_1: & H_0 \text{ n'est pas vraie.}
# \end{eqnarray*}
# 2\) Quel test allez-vous utiliser pour tester ces deux hypothèses ? Donnez la statistique $T$ associé à ce test, ainsi que sa loi approximative sous $H_0$.     
# **Solution**: 
# On considère le nombre d'observations dans certains intervalles. Sous $ H_0 $, la probabilité que le taux d'oxygénation soit dans un intervalle $ (a, b) $ est $ F(b) - F(a) $, où $ F $ est la fonction de répartition d'une loi normale. Une fois les paramètres de la loi normale connus, on peut calculer les nombres attendus estimés sous $ H_0 $ dans tous les intervalles. On estime les paramètres de la loi normale par $ \hat \mu = \bar x $ et $ \hat \sigma^2 = s_x^2 $. 
# 
# Il ne s'agit alors que d'un test d'adéquation. Pour calculer le nombre attendu estimé sous $ H_0 $ dans l'intervalle $ (0.1, 0.15] $
# par exemple, on procède comme suit. On considère une variable aléatoire 
# $ X \sim \mathcal{N}(0.173, 0.066^2) $, et on calcule
# \begin{align*}
# e_2 &= 83 \times \Pr(0.1< X\le 0.15) = 
# 83 \times \mathbb{P}\left(\frac{0.1-0.173}{0.066}< \frac{X-0.173}{0.066}
# \le \frac{0.15-0.173}{0.066}\right) \\
# & = 83 \times  (\Phi(-0.348) - \Phi(-1.106))
# = 83 \times  (1 - \Phi(0.348) - 1 + \Phi(1.106))
# \\
# &= 83 \times  (\Phi(1.106) - \Phi(0.348))  = 19.039.
# \end{align*}
# 
# De cette manière, on peut calculer les nombres théoriques dans la cellules de code suivante. On utilise alors la statistique de test  $$T=\sum_{j=1}^4 \frac{(O_j-E_j)^2}{E_j},$$
# qui, sous $H_0$, suit la loi $\chi^2_\nu$ avec $\nu = 5-1-2=2$ (il ya deux paramètres estimés, $\mu$ et $\sigma$). 
# 

# In[ ]:


import pandas as pd
from scipy import stats as st

data = pd.DataFrame(data = {"Oxygénation": ["<0.1" , "(0.1,0.15]" , "(0.15,0.2]," , "(0.2,0.25]", ">0.25" ],
                           "Nombre_observé": [12   , 20    , 23    , 15,13  ]})

x_bar = 0.173
sigma = 0.066

# Estimation des probabilités
q = lambda x,loc,scale: st.norm.cdf(x,loc,scale)
prob = [q(0.1,x_bar,sigma),q(0.15,x_bar,sigma)-q(0.1,x_bar,sigma),q(0.2,x_bar,sigma)-q(0.15,x_bar,sigma),q(0.25,x_bar,sigma)-q(0.2,x_bar,sigma),1-q(0.25,x_bar,sigma) ]
data["probabilité"] = prob


# Calculez les nombres attendus et vérifier que la condition est remplie
data["Nombre_attendu"] = data.Nombre_observé.sum()*data.probabilité
print(data,"\n")
if not False in (data.Nombre_attendu>5):
    print("Tous les nombres d'observations attendus sont supérieur à 5, la conditions est donc remplie.")
else: 
    print("Tous les nombres d'observations attendus ne sont pas supérieur à 5, la conditions n'est donc pas remplie.")


# 3\) Tester l'hypothèse nulle $H_0$ à un seuil de $5\,\%$.
# 
# **Solution**: Il reste à calculer la valeur observée de la statistique de test et la comparer avec une valeur critique. La réalisation de la statistique $T$ est $t_{obs}=1.607$. Celle-ci est plus petite que le quantile $\chi^2_{2;0.99}=5.99$ donc on ne rejette pas $H_0$.
# On constate que $t_{\text{obs}}=1.607 < \chi^2_{2; 0.95} = 5.99$, donc on ne rejette pas
# l'hypothèse nulle.

# In[ ]:


degree_of_freedom = 2
alpha = 0.05

valeur_critique = st.chi2.ppf(1-alpha,degree_of_freedom)

t_obs = ((data.Nombre_observé - data.Nombre_attendu)**2/data.Nombre_attendu).sum()
# Test pour savoir si on rejette ou non l'hypothèse nulle
if (t_obs > valeur_critique):
    print("On rejette H_0 en faveur de H_1")
else:
    print("On ne peut pas rejetter H_0 en faveur de H_1.")


# ## Exercice 5: 
# 
# Dans l'étude des défaillances d'un composant électronique, on a relevé les  retours en fabrique de 200 composants dont les défaillances ont été classées  par type (T1, T2) et par localisation (L1, L2, L3). 
# 
# |    |    |    |    |
# |----|----|----|----|
# |    | L1 | L2 | L3 |
# | T1 | 50 | 16 | 31 |
# | T2 | 61 | 26 | 16 |   
# 
# 1\) Donnez les hypothèses nulle et alternative permettant de tester la dépendance entre le type et la localisation du défaut. Puis, donnez la statistique de test que vous comptez utiliser tester ces hypothèses.
# 
# **Solution**: On va tester
# \begin{eqnarray*}
# & H_0: & \text{le type du défaut est indépendant de sa localisation,} \\
# & H_1: & H_0 \text{ n'est pas vraie}.
# \end{eqnarray*}
# Nous allons utiliser un test d'indépendance entre deux caractéristiques de données. On peut de nouveau  baser la statistique de test sur les différences entre les nombres observés et attendus. 
# Si on a $ n_1 $ classes pour la première caractéristique et $ n_2 $ classes pour la deuxième  caractéristique, et si on note $ N_{ij} $ et $ E_{ij} $ les nombres observés et attendus d'observations de la $ i $ème classe de la première caractéristique et $ j $ème classe de la  deuxième caractéristique, la statistique de test à utiliser est
# \begin{gather*}
# T=\sum_{i=1}^{n_1}\sum_{j=1}^{n_2} \frac{(N_{ij}-E_{ij})^2}{E_{ij}}.
# \end{gather*}
# 2\) Y a-t-il des paramètres à estimer ? Si oui, lesquels ? Estimez ces paramètres.
# 
# **Solution**: Cela vient du fait que sous $ H_0 $ on a $ p_{ij} = p_i \times p_j $, où $ p_i $ est la probabilité d'être dans la $ i $ème classe de la première caractéristique, $ p_j $ est la probabilité d'être dans la $ j $ème classe de la deuxième caractéristique et $ p_{ij} $ est la probabilité d'être dans la $ i $ème classe de la première caractéristique et
# dans la $ j $ème classe de la deuxième caractéristique. On estime $ p_i $ par $ (\sum_{j=1}^{n_2}n_{ij}) / (\sum_{i=1}^{n_1} \sum_{j=1}^{n_2} n_{ij}) $ et $ p_j $ par $ (\sum_{i=1}^{n_1}n_{ij}) / (\sum_{i=1}^{n_1} \sum_{j=1}^{n_2} n_{ij}) $.
# 

# In[ ]:


import numpy as np
import pandas as pd

data_obs = np.array([[50,16,31],[61,26,16]])
n = data_obs.sum().sum()

# Estimation des probabilités
p_T = data_obs.sum(axis = 1).reshape(2,1)/n
p_L = data_obs.sum(axis = 0).reshape(3,1)/n


# Calculez les nombres attendus 
data_est = n*p_T*p_L.transpose()
print("Les nombres attendus sous H_0 sont :\n",pd.DataFrame(data_est,columns=["L1","L2","L3"], index=["T1","T2"]))

print(data_obs)


# 3\) En déduire la distributions de la statistique de test sous $H_O$.  
# 
# **Solution**: La distribution asymptotique de la statistique $ T $ sous $ H_0 $ est $ \chi^2_{\nu} $ avec 
# $ \nu = (n_1-1) \times (n_2-1) $. On peut obtenir $\nu$, le nombre de degrés de liberté, comme suit.
# Le nombre total de classes est $ n_1\times n_2 $. Le nombre de paramètres à estimer est
# $ (n_1 - 1) + (n_2 - 1) $ 
# (on a $ n_1 - 1 $ estimateurs pour $ p_i $ et $ n_2 - 1 $ estimateurs pour $ p_j $).
# Enfin, $ n_1\times n_2 - 1 - n_1 - n_2 + 2 = (n_1 - 1)\times (n_2-1) $. Ce qui nous donne que $T \sim \chi^2_{2}$ sous $H_O$.
# 
# 4\) Testez l'hypothèse $H_0$ à un seuil de $5\,\%$. Peut-on conclure qu'il y a une dépendance entre le type et la localisation du défaut?  
# 
# **Solution**: La valeur observée de la statistique
# \begin{gather*}
# T=\sum_{i=1}^2\sum_{j=1}^3 \frac{(N_{ij}-E_{ij})^2}{E_{ij}}
# \end{gather*}
# est $t_{obs} = 8.08 > \chi^2_{2; 0.95} = 5.99,$ donc, au niveau de $ 5\,\% $, on a montré qu'il y a une dépendance entre le type et la localisation du défaut. Notons que l'approximation par la loi $\chi^2$ est possible, car le nombre d'observations est grand et tous les nombres attendus $e_{ij}$ sont plus grands que $5$.
# 

# In[ ]:


from scipy import stats as st

degree_of_freedom = 2
alpha = 0.05

valeur_critique = st.chi2.ppf(1-alpha,degree_of_freedom)

t_obs = ((data_obs-data_est)**2/data_est).sum().sum()
# Test pour savoir si on rejette ou non l'hypothèse nulle
if (t_obs > valeur_critique):
    print("On rejette H_0 en faveur de H_1")
else:
    print("On ne peut pas rejetter H_0 en faveur de H_1.")


# ## Exercice 6: 
# 
# Pour certains jeux de données, il peut être judicieux de calculer une transformation des données avant d'effectuer une régression linéaire.
# 
# Les données suivantes montrent les valeurs expérimentales de la pression $P$ d'une masse donnée de gaz pour différentes valeurs du volume $V$.
# 
# |                               |      |      |      |      |       |       |
# |:-----------------------------:|:----:|:----:|:----:|:----:|:-----:|:-----:|
# |    Volume V [$\text{cm}^3$]   | 54.3 | 61.8 | 72.4 | 88.7 | 118.6 | 194.0 |
# | Pression P [$\text{kg/cm}^2$] | 61.2 | 49.5 | 37.6 | 28.4 |  19.2 |  10.1 |
# 
#  D'après les principes de la thermodynamique, on a la relation $P\,V^{\gamma}=C$, où $\gamma$ et $C$ sont des constantes dépendant des conditions d'expérience.
#  
# 1\) Transformer $P\,V^{\gamma}=C$ en une relation linéaire avec $Y=\log(P)$. Quels sont les paramètres dont on cherche la valeur?  
# 
# **Solution**: Puisque $P\,V^{\gamma}=C$, on a
# \begin{gather*}
#   \log(P) +\gamma \log (V)=\log (C) \quad \text{et donc} \quad \log(P) =\log(C)-\gamma \log(V).
# \end{gather*}
#   En posant $X=\log(V)$ et $Y=\log(P)$, l'équation de la droite du modèle linéaire s'écrit
# \begin{gather*}
#   Y=\alpha+\beta X\,,
# \end{gather*}
#   où $\alpha=\log(C)$ et $\beta=-\gamma$. Nous souhaitons estimer les paramètres $\alpha$ et $\beta$.
# 2\) Pour des observations non-transformées, écrire une fonction qui retourne l'estimation des paramètres $\hat{\alpha}$ et $\hat{\beta}$ de la régréssion linéaire.  
# 
# **Solution**: On sait d'après le cours que les estimateurs des paramètres de la droite de régression sont donnés par
# \begin{gather*}
# \hat \beta=\frac{\sum_{i=1}^{n} Y_i(x_i -\overline x)}{\sum_{i=1}^{n} (x_i-\overline x)^2} \quad\text{et}\quad \hat \alpha=\overline y-\hat \beta \overline x,
# \end{gather*}
# où $x_i=\log(v_i)$ et $Y_i=\log(P_i), i=1, \dots, 6$.
# On trouve $\hat \beta=-1.4$ et $\hat\alpha=9.66$. Ainsi, on a $\hat{C}=\exp(\hat{\alpha})=15677.78$ et $\hat{\gamma}=-\hat{\beta}=1.4$.
# 

# In[ ]:


import pandas as pd
import numpy as np

def regr_est(data):
     
    
    data_trans = np.log(data)
    beta = (data_trans.P*(data_trans.V-data_trans.V.mean())).mean()/data_trans.V.var(ddof = 0)
    alpha = data_trans.P.mean() - beta*data_trans.V.mean() 
    
    
    return [alpha,beta]


# 3\) Estimez $P$ quand $V=100$ $\text{cm}^3$.

# In[ ]:


data = pd.DataFrame(data = {"V": [ 54.3,61.8,72.4,88.7,118.6,194.0],
                           "P": [61.2,49.5,37.6,28.4,19.2,10.1]})

# Estimez P
alpha, beta = regr_est(data)
y = alpha  + beta*np.log(100.)
p = np.exp(y)
print(f"Pour V = 100cm^3, notre modèle linéaire estime donc P à {p:.3f} kg/cm^2.")


# 4\) Calculer l'intervalle de confiance à $95\%$ pour la pente de la droite du modèle de régression trouvé précédement.  
# 
# **Solution**: Soit 
# \begin{gather*}
# S^2 = \frac{1}{n-2} \sum_{i=1}^n(Y_i-\hat{\alpha}-\hat{\beta}x_i)^2.
# \end{gather*}
# On sait d'après le cours que 
# \begin{gather*}
# \frac{\hat{\beta}-\beta}{\sqrt{\frac{S^2}{\sum_{i=1}^n (x_i-\overline{x})^2}}} \sim t_{n-2}.
# \end{gather*}
# L'intervalle de confiance à $95\%$ est donc donné par les bornes 
# \begin{gather*}
# \hat{\beta}\pm \frac{s}{\sqrt{\sum_{i=1}^n (x_i-\overline{x})^2}}\ t_{n-2;0.975},
# \end{gather*}
# où
# \begin{gather*}
# s=\sqrt{\frac{1}{n-2} \sum_{i=1}^n(y_i-\hat{\alpha}-\hat{\beta}x_i)^2}.
# \end{gather*}
# L'intervalle de confiance recherché est donc approximativement $[-1.502, -1.306]$.
# 

# In[ ]:


from scipy import stats as st

alpha, beta = regr_est(data)
data_trans = np.log(data)

s = np.sqrt(((data_trans.P-alpha-beta*data_trans.V)**2).sum()/(len(data)-2))
quantile = st.t.ppf(0.975,len(data)-2)

# Autres valeurs à calculer ?
div = data_trans.V.var(ddof=0)*len(data)


lower_bound = beta - s*quantile/div
upper_bound = beta + s*quantile/div

print(f"L'intervalle de confiance à 95% pour la pente de la droite du modèle de régréssion est donc [{lower_bound:.3f},{upper_bound:.3f}].")

