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
quantile <- ...
EIQ <- ...

# Calcul de l'écart-type
std <- ...

# Sélection des tailles supérieures à 140cm
data_140 <- ... 

# Calcul de l'écart inter-quartile et de l'écart-type pour les tailles supérieures à 140cm
quantile_140 <- ...
EIQ_140 <- ...
std_140 <- ...

# Affichage des valeures obtenues
...


library(ggplot2)

datas <- matrix(c(147 , 150 , 152 , 155 , 157 , 160 , 163 , 165 , 168 , 170 , 173 , 175 , 178 , 180 , 183,
                  52 , 53 , 54 , 56 , 57 , 59 , 60 , 61 , 63 , 64 , 66 , 68 , 70 , 72 , 74), nrow=15, 
                ncol=2, byrow=FALSE)
datas <- data.frame(datas,stringsAsFactors = TRUE)
colnames(datas) <- c("Taille","Poids")


# Calculer la moyenne des tailles
mean <- ... 
# Afficher cette moyenne
...


# Calculer l'écart-type des tailles
std <- sd(datas$Taille)
# Afficher cet écart-type
...


min <- ... 
max <- ... 
med <- ... 
q_ <- ... 

# Afficher les résultats caclulés
...


# Calcul de l'écart inter-quartile
EIQ <- ... 
# Afficher ce résultat
...


# Faire un boxplot des tailles observées
...


# Faire un histogramme avec les groupes mentionnés ci-dessus
...


# Faire un graphique permettant de mettre en évidence la relation entre la taille 
# et le poids des femmes ayant participer à l'enquête
...


data <- matrix(c(68,119,26,7,20,84,17,94,15,54,14,10,5,29,14,16), nrow=4, 
                ncol=4, byrow=FALSE)
data <- data.frame(data,stringsAsFactors = TRUE)
colnames(data) <- c("Brun","Bleu", "Hazel", "Vert")
rownames(data) <- c("Noir","Brun","Roux","Blond")

# Calculer et affficher le nombre total d'étudiants qui ont participé à cette enquête
...


library(ggplot2)
library(dplyr)

# Calculer la fréquence absolue et relative des cheveux des étudiants
...


# Faire un plot en camembert de la fréquence absolue des couleurs des cheveux
...


# Faire un bar plot de la fréquence absolue des couleurs de cheveux
...


# Place your answer here

data = read.csv('Precipitations_journalieres_Changins.csv',sep=",",header = FALSE)
colnames(data) = c("Date","Précipitation")

library(ggplot2)
library(patchwork)
# Calculer la moyenne et la médiane des tailles observées
mean <- ... 
median <- ... 

# Faire un boxplot et un histogramme
...

