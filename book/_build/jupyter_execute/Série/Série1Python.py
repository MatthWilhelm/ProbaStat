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


# 1) Calculer la moyenne et la médiane des tailles observées, puis faire un boxplot et un histogramme de ces tailles. Sur chacun de ces graphiques faire apparaître la moyenne et la médiane.

# In[ ]:


# Calculer la moyenne et la médiane des tailles observées
mean = ... 
median = ... 

# Faire un boxplot et un histogramme
...


# 2) Entre la moyenne et la médiane, laquelle de ces deux caractéristiques représente le mieux la tendance centrale de la 
# distribution des tailles? Justifiez votre réponse.
# 
# **Solution**:  
#   
# 3) Si l'on considère seulement les tailles supérieures à $ 140 $ cm,  on obtient une moyenne de $ 166.4 $ cm et une médiane de $ 168 $ cm.  Commentez la phrase suivante : *“La médiane est plus robuste que la moyenne.”*
# 
# **Solution**:  
#   
# 4) Calculer l'écart-type et l'écart inter-quartile pour l'ensemble des tailles et pour les tailles supérieure à $140$ cm. Laquelle de ces deux caractéristiques vous semble la plus robuste?
# 
# **Solution**:  
#   
# 

# In[ ]:


# Calcul de l'écart inter-quartiles
#C3
quantile = data.Taille.quantile((0.25,0.75), interpolation = "inverted_cdf").rename("Quantiles").to_frame()#C3_
#C3
EIQ = quantile["Quantiles"][0.75] - quantile["Quantiles"][0.25]#C3_

# Calcul de l'écart-type
#C3
std = data.Taille.std()#C3_

# Sélection des tailles supérieures à 140cm
data_140 = data[data.Taille > 140]

# Calcul de l'écart inter-quartile et de l'écart-type pour les tailles supérieures à 140cm
#C3
quantile_140 = data_140.Taille.quantile((0.25,0.75), interpolation = "inverted_cdf").rename("Quantiles").to_frame()#C3_
#C3
EIQ_140 = quantile_140["Quantiles"][0.75] - quantile_140["Quantiles"][0.25]#C3_
#C3
std_140 = data_140.Taille.std()#C3_

# Affichage des valeures obtenues#C2
print(f"Sur l'ensemble des tailles observées, l'écart inter-quartile est EIQ = {EIQ}cm et l'écart-type est de {std:.2f}cm")
print(f"Sur l'ensemble des tailles supérieures à 140cm, l'écart inter-quartile est EIQ = {EIQ_140}cm et l'écart-type est de {std_140:.2f}cm")
#C2_


# ## Exercice 2:  
# 
# On a observé les précipitations journalières 01.01.2000 - 10.07.2022 de la station météo Suisse de Changrins. 

# In[ ]:


import pandas as pd
data = pd.read_csv('Precipitations_journalieres_Changins.csv',sep=',',names= ["Date","Précipitation"])


# 1) Calculer la moyenne et la médiane de ces données. Puis, faire un boxplot et un histogramme de ces données et faire apparaitre la moyenne et la médiane sur chacunes de ces figures.

# In[ ]:


import matplotlib.pyplot as plt
# Calculer la moyenne et la médiane des tailles observées
mean = ... 
median = ... 

# Faire un boxplot et un histogramme
...


# 2) Laquelle de ces deux caractéristiques représente le mieux la tendance centrale de la 
# distribution? Justifiez votre réponse.
# 
# **Solution**:  
#   
# 

# ## Exercice 3:  
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


# 1) Calculer la moyenne et la médiane des tailles observées, puis faire un boxplot et un histogramme de ces tailles. Sur chacun de ces graphiques faire apparaître la moyenne et la médiane.

# In[ ]:


# Calculer la moyenne et la médiane des tailles observées
mean = ... 
median = ... 

# Faire un boxplot et un histogramme
...


# 2) Entre la moyenne et la médiane, laquelle de ces deux caractéristiques représente le mieux la tendance centrale de la 
# distribution des tailles? Justifiez votre réponse.
# 
# **Solution**:  
#   
# 3) Si l'on considère seulement les tailles supérieures à $ 140 $ cm,  on obtient une moyenne de $ 166.4 $ cm et une médiane de $ 168 $ cm.  Commentez la phrase suivante : *“La médiane est plus robuste que la moyenne.”*
# 
# **Solution**:  
#   
# 4) Calculer l'écart-type et l'écart inter-quartile pour l'ensemble des tailles et pour les tailles supérieure à $140$ cm. Laquelle de ces deux caractéristiques vous semble la plus robuste?
# 
# **Solution**:  
#   
# 

# In[ ]:


# Calcul de l'écart inter-quartiles
#C3
quantile = data.Taille.quantile((0.25,0.75), interpolation = "inverted_cdf").rename("Quantiles").to_frame()#C3_
#C3
EIQ = quantile["Quantiles"][0.75] - quantile["Quantiles"][0.25]#C3_

# Calcul de l'écart-type
#C3
std = data.Taille.std()#C3_

# Sélection des tailles supérieures à 140cm
data_140 = data[data.Taille > 140]

# Calcul de l'écart inter-quartile et de l'écart-type pour les tailles supérieures à 140cm
#C3
quantile_140 = data_140.Taille.quantile((0.25,0.75), interpolation = "inverted_cdf").rename("Quantiles").to_frame()#C3_
#C3
EIQ_140 = quantile_140["Quantiles"][0.75] - quantile_140["Quantiles"][0.25]#C3_
#C3
std_140 = data_140.Taille.std()#C3_

# Affichage des valeures obtenues#C2
print(f"Sur l'ensemble des tailles observées, l'écart inter-quartile est EIQ = {EIQ}cm et l'écart-type est de {std:.2f}cm")
print(f"Sur l'ensemble des tailles supérieures à 140cm, l'écart inter-quartile est EIQ = {EIQ_140}cm et l'écart-type est de {std_140:.2f}cm")
#C2_


# ## Exercice 4:  
# 
# On a observé les précipitations journalières 01.01.2000 - 10.07.2022 de la station météo Suisse de Changrins. 

# In[ ]:


import pandas as pd
data = pd.read_csv('Precipitations_journalieres_Changins.csv',sep=',',names= ["Date","Précipitation"])


# 1) Calculer la moyenne et la médiane de ces données. Puis, faire un boxplot et un histogramme de ces données et faire apparaitre la moyenne et la médiane sur chacunes de ces figures.

# In[ ]:


import matplotlib.pyplot as plt
# Calculer la moyenne et la médiane des tailles observées
mean = ... 
median = ... 

# Faire un boxplot et un histogramme
...


# 2) Laquelle de ces deux caractéristiques représente le mieux la tendance centrale de la 
# distribution? Justifiez votre réponse.
# 
# **Solution**:  
#   
# 
