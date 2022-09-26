library(ggplot2)
library(dplyr)
library(patchwork)

data <- matrix(c(147 , 59 , 152 , 155 , 157 , 160 , 64 , 165 , 168 , 170 , 173 , 175 , 178 , 180 , 183), nrow=15, 
                ncol=1, byrow=FALSE)
data <- data.frame(data,stringsAsFactors = TRUE)
colnames(data) <- c("Taille")

# Calculer la moyenne et la médiane des tailles observées
mean <- ... 
median <- ... 

# Faire un boxplot et un histogramme
...


# Calcul de l'écart inter-quartiles
#C3
quantile <- quantile(data$Taille,c(0.25,0.75), type =1)#C3_
#C3
EIQ <- as.double(quantile[2]-quantile[1])#C3_

# Calcul de l'écart-type
#C3
std <- sd(data$Taille)#C3_

# Sélection des tailles supérieures à 140cm
data_140 <- data %>% filter(Taille > 140)

# Calcul de l'écart inter-quartile et de l'écart-type pour les tailles supérieures à 140cm
#C3
quantile_140 <- quantile(data_140$Taille,c(0.25,0.75), type =1)#C3_
#C3
EIQ_140 <- as.double(quantile_140[2]-quantile_140[1])#C3_
#C3
std_140 <- sd(data_140$Taille)#C3_

# Affichage des valeures obtenues#C2
print(paste0("Sur l'ensemble des tailles observées, l'écart inter-quartile est EIQ = ",
             toString(trunc(EIQ*10^2)/10^2),"cm et l'écart-type est de ",toString(trunc(std*10^2,4)/10^2),"cm"))
print(paste0("Sur l'ensemble des tailles supérieures à 140cm, l'écart inter-quartile est EIQ = ",
             toString(trunc(EIQ_140*10^2)/10^2),"cm et l'écart-type est de ",toString(trunc(std_140*10^2,4)/10^2),"cm"))
#C2_

data = read.csv('Precipitations_journalieres_Changins.csv',sep=",",header = FALSE)
colnames(data) = c("Date","Précipitation")

library(ggplot2)
library(patchwork)
# Calculer la moyenne et la médiane des tailles observées
mean <- ... 
median <- ... 

# Faire un boxplot et un histogramme
...


library(ggplot2)
library(dplyr)
library(patchwork)

data <- matrix(c(147 , 59 , 152 , 155 , 157 , 160 , 64 , 165 , 168 , 170 , 173 , 175 , 178 , 180 , 183), nrow=15, 
                ncol=1, byrow=FALSE)
data <- data.frame(data,stringsAsFactors = TRUE)
colnames(data) <- c("Taille")

# Calculer la moyenne et la médiane des tailles observées
mean <- ... 
median <- ... 

# Faire un boxplot et un histogramme
...


# Calcul de l'écart inter-quartiles
#C3
quantile <- quantile(data$Taille,c(0.25,0.75), type =1)#C3_
#C3
EIQ <- as.double(quantile[2]-quantile[1])#C3_

# Calcul de l'écart-type
#C3
std <- sd(data$Taille)#C3_

# Sélection des tailles supérieures à 140cm
data_140 <- data %>% filter(Taille > 140)

# Calcul de l'écart inter-quartile et de l'écart-type pour les tailles supérieures à 140cm
#C3
quantile_140 <- quantile(data_140$Taille,c(0.25,0.75), type =1)#C3_
#C3
EIQ_140 <- as.double(quantile_140[2]-quantile_140[1])#C3_
#C3
std_140 <- sd(data_140$Taille)#C3_

# Affichage des valeures obtenues#C2
print(paste0("Sur l'ensemble des tailles observées, l'écart inter-quartile est EIQ = ",
             toString(trunc(EIQ*10^2)/10^2),"cm et l'écart-type est de ",toString(trunc(std*10^2,4)/10^2),"cm"))
print(paste0("Sur l'ensemble des tailles supérieures à 140cm, l'écart inter-quartile est EIQ = ",
             toString(trunc(EIQ_140*10^2)/10^2),"cm et l'écart-type est de ",toString(trunc(std_140*10^2,4)/10^2),"cm"))
#C2_

data = read.csv('Precipitations_journalieres_Changins.csv',sep=",",header = FALSE)
colnames(data) = c("Date","Précipitation")

library(ggplot2)
library(patchwork)
# Calculer la moyenne et la médiane des tailles observées
mean <- ... 
median <- ... 

# Faire un boxplot et un histogramme
...

