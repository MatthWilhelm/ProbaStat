mu <- 176.6
sigma_square <- 63.84

# Calculer cette probabilité en utilisant directement la fonction de répartition 
# d'une loi normale de moyenne 176.6 et d'écart-type 63.84
prob <- ...

# Calculer cette probabilité en normalisant notre observation et en utilisant la 
# fonction de répartition d'une loi normale standardisé
normalisation <- ... 
prob_ <- ... 

# Place your answer here

# Place your answer here

# Place your answer here

# Place your answer here

# Place your answer here

mean <- ... 
var <- ... 

library(ggplot2)
df <- data.frame(X = X)

# Plot de l'évolution de l'estimation de la moyenne
...


# Calculer l'estimation de la variance pour chacunes des m premières observations
...

# Plot de l'évolution de l'estimation de la moyenne
...


library(ggplot2)

n <- 5000

# Générer un échantillon de n VA unif([-1,1])
X <- ...

# Générer la variable aléatoire Y
Y <- (apply(X,1,FUN=norm,type="2")<=1)

# Évolution de l'estimation de pi
...


n <- 50000
true_value <- 2.139350129

# Générer un échantillon de n VA unif([-1,1])
X <- ...

# Écrire la fonction h
h <- function(X){
        val <- ...
    val
}
# Générer la variable aléatoire Y
Y <- ... 

# Plot de l'évolution de l'estimation de la moyenne
...


N <- c(10,20,50,100,250,500,1000,2500,5000)
m <- 100

RMSE <- rep(0.,length(N))

i <- 0
for (n in N){
    i <- i+1
    échantillon_estimation = rep(0.,m)
    for (j in 1:m){
        # Générer un échantillon de n VA unif([-1,1])
                X <- ...
        # Estimation de pi
                pi_est = 4*mean(apply(X,1,FUN=norm,type="2")<=1)        _
        # Calcul de la MSE de l'échantillon
                échantillon_estimation[j] <- ...
    }
    RMSE[i] = sqrt(mean(échantillon_estimation))
}
# Plot du taux de convergence
...


n <- 100
p <- 3./5
prob <- ... 
# Afficher le résulat
...


# Place your answer here

Z <- ... 
prob_ <- ... 
# Afficher le résulat
...


E_X <- ... 
V_X <- ... 
# Afficher le résultat
...


# Place your answer here
