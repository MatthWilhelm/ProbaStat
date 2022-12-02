#!/usr/bin/env python
# coding: utf-8

# # Série4
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
#   
# 

# In[ ]:


import pandas as pd
from scipy import stats as st
import numpy as np

def IC_variance_connue(x_bar,sigma_square,n,alpha):
    quantile = ... 
        IC = ...
    return IC


# b\) Calculez cet intervalle de confiance pour le jeu de donnée fourni.

# In[ ]:


# Importation des données
data = ... 

# Calcul de la moyenne empirique
mean = ... 

n = ... 
sigma_square = ... 
alpha = ... 

IC = ... 
# Afficher cet intervalle
...


# On va maintenant abandonner l'hypothèse de variance connue (ce qui est plus réaliste).  On considère toujours un modèle normal, mais cette fois on suppose que $ X ~\sim \mathcal{N}(\mu , \sigma^2 ) $ avec $ \mu $ et $ \sigma^2 $ inconnus. Les données récoltées sont toujours considérées indépendantes.
# 
# 2\) Impémentez une fonction qui retourne un intervalle de confiance symmétrique à $ (1-\alpha)100\,\% $  pour $ \mu $ dans le cas où la variance est inconnue. (N'hésitez pas à faire des développements à la main ou en markdown avant de vous lancez dans l'implémentatioonde cette fonction)
# 
# **Solution**:  
#   
# 

# In[ ]:


# Place your answer here


# 3\) a\) Calculez un intervalle de confiance à $95\,\% $ pour le jeu de donnée fourni.

# In[ ]:


# Place your answer here


# b\) Calculez un intervalle de confiance à $90\,\% $ pour le jeu de donnée fourni.

# In[ ]:


# Place your answer here


# c\) Commentez la différence entre ces deux intervalles.
# 
# **Solution**:  
#   
# 4\) Que l'entreprise peut-elle faire pour obtenir un intervalle de confiance à $ 95\,\% $ plus étroit que celui obtenu?
# 
# **Solution**:  
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
# **Solution**:  
#   
# 2\) Quel test allez-vous utiliser pour tester ces deux hypothèses ? Donnez la statistique $T$ associé à ce test, ainsi que sa loi approximative sous $H_0$. De plus, y a-t-il une/des conditions pour que la convergence de $T$ soit le moins déraisonnable possible ? Si oui, énoncé-la/les et vérifier la/les.
# 
# **Solution**:  
#   
# 

# In[ ]:


import pandas as pd

# Vérifier que la/les conditions sont remplies
...


# 3\) Tester l'hypothèse nulle $H_0$ à un seuil de $5\,\%$. Les données semblent-elles en accord avec l'affirmation du responsable de communication ? 
# 
# **Solution**:  
#   
# 

# In[ ]:


from scipy import stats as st

degree_of_freedom = ... 
alpha = ... 

valeur_critique = ... 
t_obs = ... 
# Test pour savoir si on rejette ou non l'hypothèse nulle
...


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
# **Solution**:  
#   
# b\) Quel test allez-vous utiliser pour tester ces deux hypothèses ? Donnez la statistique $T$ associé à ce test, ainsi que sa loi approximative sous $H_0$. De plus, y a-t-il une/des conditions pour que la convergence de $T$ soit le moins déraisonnable possible ? Si oui, énoncé-la/les et vérifier la/les.
# 
# **Solution**:  
#   
# 

# In[ ]:


import pandas as pd

# Vérifier que la/les conditions sont remplies
...


# c\) Tester l'hypothèse nulle $H_0$ à un seuil de $1\,\%$.
# 
# **Solution**:  
#   
# 

# In[ ]:


from scipy import stats as st

degree_of_freedom = ... 
alpha = ... 

valeur_critique = ... 

t_obs = ... 
# Test pour savoir si on rejette ou non l'hypothèse nulle
...


# 2\) Nous voulon maintenant tester à un niveau de signification de $ 1 \,\% $ si la natalité du premier trimestre est égale à celle du quatrième trimestre, et celle du deuxième trimestre est égale à celle du troisième trimestre.  
# a\) Écrire explicitement les hypothèses nulle et alternative qui nous permettent de tester l'hypothèse ci-dessus.
# 
# **Solution**:  
#   
# b\)  Sous $H_0$, connait-on la distribution exacte des naissances ou faut-il l'estimer ? Si elle est connu donnez là, sinon estimez là.
# 
# *Indication:* Si on note par $p_j$, $j=1,\dots,4$, la probabilité d'être dans le $j$-ème trimestre, il faut tester $H_0$: $p_1=p_4$, $p_2=p_3$ (c'est-à-dire, les $p_j$ sont tels que $p_1=p_4$ et $p_2=p_3$, mais autrement inconnus). Pour calculer les nombres attendus, on commence par estimer la valeur $p_{14}=\mathbb{P}(\text{né dans le 1er ou 4ème trimestre})$ par la fréquence empirique et on utilise le fait que $p_1=p_4=p_{14}/2$ sous $H_0$.
# 
# **Solution**:  
#   
# c\) Quel test allez-vous utiliser pour tester ces deux hypothèses ? Donnez la statistique $T$ associé à ce test, ainsi que sa loi approximative sous $H_0$.  
# 
# **Solution**:  
#   
# 

# In[ ]:


data = pd.DataFrame(data = {"Semestre": ["Janv-Mars" , "Avr-Juin" , "Juil-Sept" , "Oct-Déc" ],
                           "Nombre_observé": [110   , 57    , 53    , 80  ]})

# Estimation probabilité
...


# Calculez les nombres attendus et vérifier que la condition est remplie
...


# d\) Tester l'hypothèse nulle $H_0$ à un seuil de $1\,\%$.
# 
# **Solution**:  
#   
# 

# In[ ]:


from scipy import stats as st

degree_of_freedom = ... 
alpha = ... 

valeur_critique = ... 

t_obs = ... 
# Test pour savoir si on rejette ou non l'hypothèse nulle
...


# *Dans cet exercice on n'a rejeté aucune hypothèse nulle. Évidemment, les deux hypothèses nulles sont incompatibles, donc cela peut paraître étrange. Mais rappelons-nous que « ne pas rejeter »  n'est pas « accepter » .*

# ## Exercice 4: 
# 
# Les données ci-dessous représentent le taux d'oxygénation de cours d'eau ayant la même température dans une certaine région:
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
# **Solution**:  
#   
# 2\) Quel test allez-vous utiliser pour tester ces deux hypothèses ? Donnez la statistique $T$ associé à ce test, ainsi que sa loi approximative sous $H_0$.     
# **Solution**:  
#   
# 

# In[ ]:


import pandas as pd
from scipy import stats as st

data = pd.DataFrame(data = {"Oxygénation": ["<0.1" , "(0.1,0.15]" , "(0.15,0.2]," , "(0.2,0.25]", ">0.25" ],
                           "Nombre_observé": [12   , 20    , 23    , 15,13  ]})

x_bar = ... 
sigma = ... 

# Estimation des probabilités
...


# Calculez les nombres attendus et vérifier que la condition est remplie
...


# 3\) Tester l'hypothèse nulle $H_0$ à un seuil de $5\,\%$.
# 
# **Solution**:  
#   
# On constate que $t_{\text{obs}}=1.607 < \chi^2_{2; 0.95} = 5.99$, donc on ne rejette pas
# l'hypothèse nulle.

# In[ ]:


degree_of_freedom = ... 
alpha = ... 

valeur_critique = ... 

t_obs = ... 
# Test pour savoir si on rejette ou non l'hypothèse nulle
...


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
# **Solution**:  
#   
# 2\) Y a-t-il des paramètres à estimer ? Si oui, lesquels ? Estimez ces paramètres.
# 
# **Solution**:  
#   
# 

# In[ ]:


import numpy as np
import pandas as pd

data_obs = np.array([[50,16,31],[61,26,16]])
n = data_obs.sum().sum()

# Estimation des probabilités
...


# Calculez les nombres attendus 
...

print(data_obs)


# 3\) En déduire la distributions de la statistique de test sous $H_O$.  
# 
# **Solution**:  
#   
# 4\) Testez l'hypothèse $H_0$ à un seuil de $5\,\%$. Peut-on conclure qu'il y a une dépendance entre le type et la localisation du défaut?  
# 
# **Solution**:  
#   
# 

# In[ ]:


from scipy import stats as st

degree_of_freedom = ... 
alpha = ... 

valeur_critique = ... 

t_obs = ... 
# Test pour savoir si on rejette ou non l'hypothèse nulle
...


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
# **Solution**:  
#   
# 2\) Pour des observations non-transformées, écrire une fonction qui retourne l'estimation des paramètres $\hat{\alpha}$ et $\hat{\beta}$ de la régréssion linéaire.  
# 
# **Solution**:  
#   
# 

# In[ ]:


import pandas as pd
import numpy as np

def regr_est(data):
    
    ...

    return [alpha,beta]


# 3\) Estimez $P$ quand $V=100$ $\text{cm}^3$.

# In[ ]:


data = pd.DataFrame(data = {"V": [ 54.3,61.8,72.4,88.7,118.6,194.0],
                           "P": [61.2,49.5,37.6,28.4,19.2,10.1]})

# Estimez P
...


# 4\) Calculer l'intervalle de confiance à $95\%$ pour la pente de la droite du modèle de régression trouvé précédement.  
# 
# **Solution**:  
#   
# 

# In[ ]:


from scipy import stats as st

alpha, beta = ... 
data_trans = ... 

s = ... 
quantile = ... 

# Autres valeurs à calculer ?
...


lower_bound = ... 
upper_bound = ... 

print(f"L'intervalle de confiance à 95% pour la pente de la droite du modèle de régréssion est donc [{lower_bound:.3f},{upper_bound:.3f}].")

