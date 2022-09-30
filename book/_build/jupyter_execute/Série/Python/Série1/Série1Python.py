#!/usr/bin/env python
# coding: utf-8

# # Série1
#   ## Exercice 1:  
# 
# On a observé la taille de 15 femmes. Le boxplot et l'histogramme ci-dessous ont été construits avec ces données:
# 
# |||||||||||||||||
# |:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
# | **Taille** | 147 | 59 | 152 | 155 | 157 | 160 | 64 | 165 | 168 | 170 | 173 | 175 | 178 | 180 | 183 |

# In[ ]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame(np.array([147 , 59 , 152 , 155 , 157 , 160 , 64 , 165 , 168 , 170 , 173 , 175 , 178 , 180 , 183]).transpose(), 
                     columns=["Taille"])


# 1\) Calculer la moyenne et la médiane des tailles observées, puis faire un boxplot et un histogramme de ces tailles. Sur chacun de ces graphiques faire apparaître la moyenne et la médiane.

# In[ ]:


# Calculer la moyenne et la médiane des tailles observées
mean = ... 
median = ... 

# Faire un boxplot et un histogramme
...


# 2\) Entre la moyenne et la médiane, laquelle de ces deux caractéristiques représente le mieux la tendance centrale de la 
# distribution des tailles? Justifiez votre réponse.
# 
# **Solution**:  
#   
# 3\) Si l'on considère seulement les tailles supérieures à $ 140 $ cm,  on obtient une moyenne de $ 166.4 $ cm et une médiane de $ 168 $ cm.  Commentez la phrase suivante : *“La médiane est plus robuste que la moyenne.”*
# 
# **Solution**:  
#   
# 4\) Calculer l'écart-type et l'écart inter-quartile pour l'ensemble des tailles et pour les tailles supérieure à $140$ cm. Laquelle de ces deux caractéristiques vous semble la plus robuste?
# 
# **Solution**:  
#   
# 

# In[ ]:


# Calcul de l'écart inter-quartiles
quantile = ...
EIQ = ...

# Calcul de l'écart-type
std = ...

# Sélection des tailles supérieures à 140cm
data_140 = ... 

# Calcul de l'écart inter-quartile et de l'écart-type pour les tailles supérieures à 140cm
quantile_140 = ...
EIQ_140 = ...
std_140 = ...

# Affichage des valeures obtenues
...


# ## Exercice 2:  
# 
# On a observé la taille et le poids de quelques femmes. Les résultats sont présentés dans le tableau suivant (la taille en centimètres, le poids en kilogrammes):
# 
#   |||||||||||||||||
# |:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
# | **Taille** | 147 | 150 | 152 | 155 | 157 | 160 | 163 | 165 | 168 | 170 | 173 | 175 | 178 | 180 | 183 |
# | **Poids** | 52 | 53 | 54 | 56 | 57 | 59 | 60 | 61 | 63 | 64 | 66 | 68 | 70 | 72 | 74 |

# In[ ]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
datas = pd.DataFrame(np.array([[147 , 150 , 152 , 155 , 157 , 160 , 163 , 165 , 168 , 170 , 173 , 175 , 178 , 180 , 183], 
                                [52 , 53 , 54 , 56 , 57 , 59 , 60 , 61 , 63 , 64 , 66 , 68 , 70 , 72 , 74]]).transpose(), 
                     columns=["Taille","Poids"])


# 1\) Est-ce que la taille est une variable quantitative, qualitative nominale ou qualitative ordinale ?
# 
# **Solution**:  
#   
# 2\) Calculez la moyenne et l'écart-type des tailles observées.

# In[ ]:


# Calculer la moyenne des tailles
mean = ... 

# Afficher cette moyenne
...

# Calculer l'écart-type des tailles
std = ... 

# Afficher cet écart-type
...


# 3\) Pour les tailles observées, calculez le minimum, le maximum, la médiane, le quartile inférieur, le quartile supérieur et le quartile d'ordre 30%. Qu'est-ce que représentent ces quantités ?
# 
# **Solution**:  
#   
# 

# In[ ]:


min = ... 
max = ... 
med = ... 
q_ = ...
# Afficher les résultats caclulés
...


# 4\) Calculez l'écart inter-quartile des tailles observées

# In[ ]:


# Calcul de l'écart inter-quartile
EIQ = ... 
# Afficher ce résultat
...


# 5\) Construisez le boxplot des tailles observées. Quels aspects des données cette représentation graphique nous permet-elle de visualiser?
# 
# **Solution**:  
#   
# 

# In[ ]:


# Faire un boxplot des tailles observées


# 6\) Divisez les tailles observées en 5 groupes :  
# $ < 150 $, $ 150 - 159 $, $ 160 - 169 $, $ 170 - 179 $, $ > 179 $ cm.  
# Construisez un histogramme en utilisant une ligne par groupe. Quels aspects des données cette représentation graphique nous permet-elle de visualiser?
# 
# **Solution**:  
#   
# 

# In[ ]:


# Faire un histogramme avec les groupes mentionnés ci-dessus


# 7\) Pensez-vous qu'il existe une relation entre la taille et le poids des femmes ayant participé à l'enquête? Justifiez votre réponse à l'aide d'un graphique adéquat.
# 
# **Solution**:  
#   
# 

# In[ ]:


# Faire un graphique permettant de mettre en évidence la relation entre la taille 
# et le poids des femmes ayant participer à l'enquête
...


# ## Exercice 3: 
# 
# On a observé la couleur des cheveux et des yeux de certains étudiants de l’Université du Delaware.
# Les résultats sont présentés dans le tableau suivant :
# 
# | Cheveux / Yeux  | Brun | Bleu       | "Hazel" | Vert |
# | :---------------: |:---------------:|:---------------:| :---------------:| :---------------: |
# | Noir  | 68 | 20 | 15 | 5 |
# | Brun  | 119 | 84 | 54 | 29 |
# | Roux  | 26 | 17 | 14 | 14 |
# | Blond | 7 | 94 | 10 | 16|

# In[ ]:


import pandas as pd 
import numpy as np
data = pd.DataFrame(np.array([[68, 20, 15, 5], [119, 84, 54, 29], [26, 17, 14,14 ],[7,94,10,16 ]]), 
                     columns=["Brun","Bleu", "Hazel", "Vert"],index=["Noir","Brun","Roux","Blond"])


# 1\) Combien d'étudiants ont participé à cette enquête ?

# In[ ]:


# Calculer et affficher le nombre total d'étudiants qui ont participé à cette enquête


# 2\) Est-ce que la couleur des cheveux est une variable quantitative, qualitative nominale ou qualitative
# ordinale ?
# 
# **Solution**:  
#   
# 3\) Résumez ce que vous pouvez dire sur la couleur des cheveux des étudiants à l’aide de quelques chiffres et graphiques adéquats.
# 
# **Solution**:  
#   
# 

# In[ ]:


import matplotlib.pyplot as plt

# Calculer la fréquence absolue et relative des cheveux des étudiants
...


# Faire un plot en camembert de la fréquence absolue des couleurs des cheveux
...


# Faire un bar plot de la fréquence absolue des couleurs de cheveux
...


# 4\) Pensez-vous que la couleur des cheveux et la couleur des yeux des étudiants ayant participé à l’enquête sont liées ? Justifiez votre réponse.
# 
# 
# **Solution**:  
#   
# 

# In[ ]:


# Place your answer here


# ## Exercice 4:  
# 
# On a observé les précipitations journalières 01.01.2000 - 10.07.2022 de la station météo Suisse de Changrins. 

# In[ ]:


import pandas as pd
data = pd.read_csv('Precipitations_journalieres_Changins.csv',sep=',',names= ["Date","Précipitation"])


# 1\) Calculer la moyenne et la médiane de ces données. Puis, faire un boxplot et un histogramme de ces données et faire apparaitre la moyenne et la médiane sur chacunes de ces figures.

# In[ ]:


import matplotlib.pyplot as plt
# Calculer la moyenne et la médiane des tailles observées
mean = ... 
median = ... 

# Faire un boxplot et un histogramme
...


# 2\) Laquelle de ces deux caractéristiques représente le mieux la tendance centrale de la 
# distribution? Justifiez votre réponse.
# 
# **Solution**:  
#   
# 
