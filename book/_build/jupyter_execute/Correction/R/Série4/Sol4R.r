IC_variance_connue <- function(x_bar,sigma_square,n,alpha){
    quantile <- qnorm(1-alpha/2)
    
    IC <- data.frame(lower_bound=c(x_bar-quantile*sqrt(sigma_square/n)),upper_bound=c(x_bar  + quantile*sqrt(sigma_square/n)))
    IC
}

# Importation des données
data <- read.csv("consommation.csv")

# Calcul de la moyenne empirique
mean <- mean(data$consommation)

n <- length(data$consommation)
sigma_square <- 3.5
alpha <- 0.05

IC <- IC_variance_connue(mean,sigma_square,n,alpha)

# Afficher cet intervalle
sprintf("L'intervalle de confiance à 95%s est donc: [%.3f,%.3f]","%",IC$lower_bound[1],IC$upper_bound[1])

########### Solution R: ##########


IC_variance_inconnue <- function(x_bar,sigma_est,n,alpha){
    quantile <- qt(1-alpha/2,n-1)#C1
    #C3
    IC <- data.frame(lower_bound=c(x_bar-quantile*sqrt(sigma_est/n)),upper_bound=c(x_bar  + quantile*sqrt(sigma_est/n)))#C3_
    IC
}

########### Solution R: ##########

alpha <- 0.05

IC <- IC_variance_inconnue(mean,var(data$consommation),n,alpha)
sprintf("L'intervalle de confiance à 95%s est donc: [%.3f,%.3f]","%",IC$lower_bound[1],IC$upper_bound[1])

########### Solution R: ##########

alpha <- 0.1

IC <- IC_variance_inconnue(mean,var(data$consommation),n,alpha)
sprintf("L'intervalle de confiance à 90%s est donc: [%.3f,%.3f]","%",IC$lower_bound[1],IC$upper_bound[1])

# Vérifier que la/les conditions sont remplies
data <- data.frame(Couleur= c("Brun" , "Jaune" , "Rouge" , "Orange" , "Vert" , "Doré"),
                   Nombre_observé=c(84   , 79    , 75    , 49     , 36   , 47),
                   probabilité= c(0.3,0.2,0.2,0.1,0.1,0.1))
data["Nombre_attendu"] <- sum(data$Nombre_observé)*data$probabilité

if  (!(FALSE %in% (data$Nombre_attendu>5))){
    print("Tous les nombres d'observations attendus sont supérieur à 5, la conditions est donc remplie.")
}else{
    print("Tous les nombres d'observations attendus ne sont pas supérieur à 5, la conditions n'est donc pas remplie.")
}

degree_of_freedom <- 5
alpha <- 0.05

valeur_critique <- qchisq(1-alpha,degree_of_freedom)
t_obs <- sum(((data$Nombre_observé - data$Nombre_attendu)^2/data$Nombre_attendu))
# Test pour savoir si on rejette ou non l'hypothèse nulle
if (t_obs > valeur_critique){
    print("On rejette H_0 en faveur de H_1")
}else{
    print("On ne peut pas rejetter H_0 en faveur de H_1.")
}

# Vérifier que la/les conditions sont remplies
data <- data.frame(Couleur= c("Janv-Mars" , "Avr-Juin" , "Juil-Sept" , "Oct-Déc"),
                   Nombre_observé=c(110   , 57    , 53    , 80 ),
                   probabilité= c(0.4,0.2,0.2,0.2))
data["Nombre_attendu"] <- sum(data$Nombre_observé)*data$probabilité

if  (!(FALSE %in% (data$Nombre_attendu>5))){
    print("Tous les nombres d'observations attendus sont supérieur à 5, la conditions est donc remplie.")
}else{
    print("Tous les nombres d'observations attendus ne sont pas supérieur à 5, la conditions n'est donc pas remplie.")
}

degree_of_freedom <- 3
alpha <- 0.01

valeur_critique <- qchisq(1-alpha,degree_of_freedom)
t_obs <- sum(((data$Nombre_observé - data$Nombre_attendu)^2/data$Nombre_attendu))
# Test pour savoir si on rejette ou non l'hypothèse nulle
if (t_obs > valeur_critique){
    print("On rejette H_0 en faveur de H_1")
}else{
    print("On ne peut pas rejetter H_0 en faveur de H_1.")
}

data <- data.frame(Couleur= c("Janv-Mars" , "Avr-Juin" , "Juil-Sept" , "Oct-Déc"),
                   Nombre_observé=c(110   , 57    , 53    , 80 ))

# Estimation probabilité
p1_hat <- (data$Nombre_observé[1] + data$Nombre_observé[4])/(2*sum(data$Nombre_observé))
prob <- c(p1_hat,(1-2*p1_hat)/2,(1-2*p1_hat)/2,p1_hat)
data["probabilité"] <- prob


# Vérifier que la/les conditions sont remplies
data["Nombre_attendu"] <- sum(data$Nombre_observé)*data$probabilité
data
if  (!(FALSE %in% (data$Nombre_attendu>5))){
    print("Tous les nombres d'observations attendus sont supérieur à 5, la conditions est donc remplie.")
}else{
    print("Tous les nombres d'observations attendus ne sont pas supérieur à 5, la conditions n'est donc pas remplie.")
}

degree_of_freedom <- 2
alpha <- 0.01

valeur_critique <- qchisq(1-alpha,degree_of_freedom)
t_obs <- sum(((data$Nombre_observé - data$Nombre_attendu)^2/data$Nombre_attendu))
# Test pour savoir si on rejette ou non l'hypothèse nulle
if (t_obs > valeur_critique){
    print("On rejette H_0 en faveur de H_1")
}else{
    print("On ne peut pas rejetter H_0 en faveur de H_1.")
}

# Vérifier que la/les conditions sont remplies
data <- data.frame(Couleur= c("<0.1" , "(0.1,0.15]" , "(0.15,0.2]," , "(0.2,0.25]", ">0.25" ),
                   Nombre_observé=c(12   , 20    , 23    , 15,13))

x_bar <- 0.173
sigma <- 0.066


# Estimation probabilité
prob <- c(pnorm(0.1,x_bar,sigma),pnorm(0.15,x_bar,sigma)-pnorm(0.1,x_bar,sigma),pnorm(0.2,x_bar,sigma)-pnorm(0.15,x_bar,sigma),
          pnorm(0.25,x_bar,sigma)-pnorm(0.2,x_bar,sigma),1-pnorm(0.25,x_bar,sigma))
data["probabilité"] <- prob


# Vérifier que la/les conditions sont remplies
data["Nombre_attendu"] <- sum(data$Nombre_observé)*data$probabilité
data
if  (!(FALSE %in% (data$Nombre_attendu>5))){
    print("Tous les nombres d'observations attendus sont supérieur à 5, la conditions est donc remplie.")
}else{
    print("Tous les nombres d'observations attendus ne sont pas supérieur à 5, la conditions n'est donc pas remplie.")
}

degree_of_freedom <- 2
alpha <- 0.05

valeur_critique <- qchisq(1-alpha,degree_of_freedom)
t_obs <- sum(((data$Nombre_observé - data$Nombre_attendu)^2/data$Nombre_attendu))
# Test pour savoir si on rejette ou non l'hypothèse nulle
if (t_obs > valeur_critique){
    print("On rejette H_0 en faveur de H_1")
}else{
    print("On ne peut pas rejetter H_0 en faveur de H_1.")
}

data_obs <- matrix(c(50,16,31,61,26,16),nrow = 2,byrow = TRUE)
n <- sum(data_obs)

# Estimation des probabilités
p_T = matrix(rowSums(data_obs)/n,nrow=2,ncol =1)
p_L = matrix(colSums(data_obs)/n,nrow=3,ncol =1)


# Calculez les nombres attendus 
data_est <-data.frame(n*p_T%*%t(p_L),row.names = c("T1","T2"))
colnames(data_est) <- c("L1","L2","L3")
sprintf("Les nombres attendus sous H_0 sont :")
print(data_est)


degree_of_freedom <- 2
alpha <- 0.05

valeur_critique <- qchisq(1-alpha,degree_of_freedom)
t_obs <- sum(((data_obs - data_est)^2/data_est))

# Test pour savoir si on rejette ou non l'hypothèse nulle
if (t_obs > valeur_critique){
    print("On rejette H_0 en faveur de H_1")
}else{
    print("On ne peut pas rejetter H_0 en faveur de H_1.")
}

regr_est <- function(data){
     
    
    data_trans <- log(data)
    beta <- mean(data_trans$P*(data_trans$V-mean(data_trans$V)))/(var(data_trans$V)*(length(data$P)-1)/length(data$P))
    alpha <- mean(data_trans$P) - beta*mean(data_trans$V) 
    
    
    c(alpha,beta)
}

data <- data.frame(V = c(54.3,61.8,72.4,88.7,118.6,194.0),
                    P = c(61.2,49.5,37.6,28.4,19.2,10.1))

# Estimez P
param <- regr_est(data)
y <- param[1]  + param[2]*log(100.)
p <- exp(y)
sprintf("Pour V = 100cm^3, notre modèle linéaire estime donc P à %.3f kg/cm^2.",p)

param <- regr_est(data)
data_trans <- log(data)

s <- sqrt(sum(((data_trans$P-param[1]-param[2]*data_trans$V)**2))/(length(data$V)-2))
quantile <- qt(0.975,length(data$V)-2)

# Autres valeurs à calculer ?
div <- var(data_trans$V)*(length(data$V)-1)


lower_bound <- param[2] - s*quantile/div
upper_bound <- param[2] + s*quantile/div

sprintf("L'intervalle de confiance à 95%s pour la pente de la droite du modèle de régréssion est donc [%.3f,%.3f].","%",lower_bound,upper_bound)
