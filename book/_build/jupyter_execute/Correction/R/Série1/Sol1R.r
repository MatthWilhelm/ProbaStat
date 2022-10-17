library(ggplot2)
library(dplyr)
library(patchwork)

data <- matrix(c(147 , 59 , 152 , 155 , 157 , 160 , 64 , 165 , 168 , 170 , 173 , 175 , 178 , 180 , 183), nrow=15, 
                ncol=1, byrow=FALSE)
data <- data.frame(data,stringsAsFactors = TRUE)
colnames(data) <- c("Taille")

# Calculer la moyenne et la médiane des tailles observées
mean <- mean(data$Taille)
median <- median(data$Taille)

# Faire un boxplot et un histogramme
options(repr.plot.width=7,repr.plot.height=6)
p1 <- ggplot(data, aes(x=Taille)) +  scale_y_continuous(breaks=c(0)) + scale_x_continuous(breaks=c(60,80,100,120,140,160,180)) +
    geom_boxplot(fill="white", outlier.colour="red", outlier.size=4) + 
    labs(title="Histogramme des tailles observées") +
    geom_vline(xintercept = mean,colour="blue", linetype = "dotted",size = 1.5) +
    geom_vline(xintercept = median,colour="green", linetype = "dashed",size = 1.5) +
    theme(plot.title = element_text(hjust = 0.5, size = 16))
p2 <- ggplot(data, aes(x=Taille)) + geom_histogram(bins = 10,color="black", fill="white") + 
    scale_x_continuous(breaks=c(60,80,100,120,140,160,180)) +
    labs(title="Histogramme des tailles observées") +
    geom_vline(xintercept = mean,colour="blue", linetype = "dotted",size = 1.5) +
    geom_vline(xintercept = median,colour="green", linetype = "dashed",size = 1.5) +
    theme(plot.title = element_text(hjust = 0.5, size = 16))

p1/p2 


# Calcul de l'écart inter-quartiles

quantile <- quantile(data$Taille,c(0.25,0.75), type =1)

EIQ <- as.double(quantile[2]-quantile[1])

# Calcul de l'écart-type

std <- sd(data$Taille)

# Sélection des tailles supérieures à 140cm
data_140 <- data %>% filter(Taille > 140)

# Calcul de l'écart inter-quartile et de l'écart-type pour les tailles supérieures à 140cm

quantile_140 <- quantile(data_140$Taille,c(0.25,0.75), type =1)

EIQ_140 <- as.double(quantile_140[2]-quantile_140[1])

std_140 <- sd(data_140$Taille)

# Affichage des valeures obtenues
print(paste0("Sur l'ensemble des tailles observées, l'écart inter-quartile est EIQ = ",
             toString(trunc(EIQ*10^2)/10^2),"cm et l'écart-type est de ",toString(trunc(std*10^2,4)/10^2),"cm"))
print(paste0("Sur l'ensemble des tailles supérieures à 140cm, l'écart inter-quartile est EIQ = ",
             toString(trunc(EIQ_140*10^2)/10^2),"cm et l'écart-type est de ",toString(trunc(std_140*10^2,4)/10^2),"cm"))


library(ggplot2)

datas <- matrix(c(147 , 150 , 152 , 155 , 157 , 160 , 163 , 165 , 168 , 170 , 173 , 175 , 178 , 180 , 183,
                  52 , 53 , 54 , 56 , 57 , 59 , 60 , 61 , 63 , 64 , 66 , 68 , 70 , 72 , 74), nrow=15, 
                ncol=2, byrow=FALSE)
datas <- data.frame(datas,stringsAsFactors = TRUE)
colnames(datas) <- c("Taille","Poids")


# Calculer la moyenne des tailles
mean <- mean(datas$Taille)
# Afficher cette moyenne
print("La moyenne des tailles observées est (en cm):")
print(mean)


# Calculer l'écart-type des tailles
std <- sd(datas$Taille)
# Afficher cet écart-type
print("L'écart-type des tailles observées est (en cm):")
print(std)


min <- min(datas$Taille)
max <- max(datas$Taille)
med <- median(datas$Taille)
q_ <- quantile(datas$Taille,c(0.25,0.3,0.75), type =1)

# Afficher les résultats caclulés  
print("Le minimum des tailles est: ")
print(min)
print("Le minimum des tailles est: ")
print(max)
print("La médiane des tailles est: ")
print(med)
print("Les quantiles inférieur, d'ordre 30% et supérieur des tailles sont: ")
print(q_)


# Calcul de l'écart inter-quartile
EIQ <- as.double(q_[3]-q_[1])
# Afficher ce résultat
print(paste("L'écart inter-quartile des tailles est EIQ =",EIQ, "cm"))

# Faire un boxplot des tailles observées
boxplot(datas["Taille"],main = "Boxplot des tailles observées")

# Faire un histogramme avec les groupes mentionnés ci-dessus
ggplot(datas, aes(x=Taille)) + geom_histogram(breaks=c(min,149.99,159.99,169.99,179.99,max),color="red", fill="yellow") + 
    labs(title="Histogramme des tailles observées",x ="Taille (cm)", y = "Nombre") +
    theme(plot.title = element_text(hjust = 0.5, size = 16))

# Faire un graphique permettant de mettre en évidence la relation entre la taille 
# et le poids des femmes ayant participer à l'enquête
ggplot(datas, aes(x=Taille, y=Poids)) + geom_point(size = 2.5) +
    labs(title="Scatter plot du poids en fonction de la taille chez les\n femmes ayant participé à l'étude",
        x ="Taille (cm)", y = "Poids (kg)") +
    theme(plot.title = element_text(hjust = 0.5, size = 16))

data <- matrix(c(68,119,26,7,20,84,17,94,15,54,14,10,5,29,14,16), nrow=4, 
                ncol=4, byrow=FALSE)
data <- data.frame(data,stringsAsFactors = TRUE)
colnames(data) <- c("Brun","Bleu", "Hazel", "Vert")
rownames(data) <- c("Noir","Brun","Roux","Blond")

# Calculer et affficher le nombre total d'étudiants qui ont participé à cette enquête
n_student <- sum(data)
print(n_student)

library(ggplot2)
library(dplyr)

# Calculer la fréquence absolue et relative des cheveux des étudiants
résumé <- data %>% mutate(Couleur_de_cheveux = rownames(data)) %>% rowwise() %>%
  mutate(Fréquence_absolue = sum(across(Brun:Vert))) %>%  
  mutate(Fréquence_relative = sum(across(Brun:Vert, ~ . / sum(data)))) %>%
  ungroup() %>% select(c(Couleur_de_cheveux,Fréquence_absolue,Fréquence_relative))
résumé <- as.data.frame(résumé)

print(résumé)



# Faire un plot en camembert de la fréquence absolue des couleurs des cheveux
g <- ggplot(résumé, aes(Couleur_de_cheveux,Fréquence_absolue, fill = Couleur_de_cheveux)) 
g + geom_col() + ggtitle("Bar plot de la fréquence absolue des couleurs de cheveux") +
  xlab("Couleur de cheveux") + ylab("Fréquence relative")



# Faire un bar plot de la fréquence absolue des couleurs de cheveux
g <- ggplot(résumé, aes(x="", y=Fréquence_absolue, fill=Couleur_de_cheveux)) +
  geom_bar(stat="identity", width=1) +
  coord_polar("y", start=0)
g + theme_void() + ggtitle("Camembert de la fréquence absolue des couleurs de cheveux")


########### Solution R: ##########


fréquences_relatives <- data %>% rowwise() %>%
    mutate(tot = sum(across(Brun:Vert)))  %>%  
    mutate(across(Brun:Vert, ~ . / tot)) %>% 
    ungroup() %>% select(Brun:Vert)
fréquences_relatives <- as.data.frame(fréquences_relatives)
rownames(fréquences_relatives) <- rownames(data)
print(fréquences_relatives)

data = read.csv('Precipitations_journalieres_Changins.csv',sep=",",header = FALSE)
colnames(data) = c("Date","Précipitation")

library(ggplot2)
library(patchwork)
# Calculer la moyenne et la médiane des tailles observées
mean <- mean(data$Précipitation)
median <- median(data$Précipitation)

# Faire un boxplot et un histogramme
options(repr.plot.width=7,repr.plot.height=6)
p1 <- ggplot(data, aes(x=Précipitation)) +  scale_y_continuous(breaks=c(0)) +# scale_x_continuous(breaks=c(60,80,100,120,140,160,180)) +
    geom_boxplot(fill="white", outlier.colour="red", outlier.size=1) + 
    labs(title="Histogramme des précipitations observées",xlabel="Précipitations (en mm)") +
    geom_vline(xintercept = mean,colour="blue", linetype = "dotted",size = 1.5) +
    geom_vline(xintercept = median,colour="green", linetype = "dashed",size = 1.5) +
    theme(plot.title = element_text(hjust = 0.5, size = 16))
p2 <- ggplot(data, aes(x=Précipitation)) + geom_histogram(bins = 50,color="black", fill="white") + #scale_x_continuous(breaks=c(60,80,100,120,140,160,180)) +
    labs(title="Histogramme des précipitations observées",xlabel="Précipitations (en mm)") +
    geom_vline(xintercept = mean,colour="blue", linetype = "dotted",size = 1.5) +
    geom_vline(xintercept = median,colour="green", linetype = "dashed",size = 1.5) +
    theme(plot.title = element_text(hjust = 0.5, size = 16))

p1/p2 

