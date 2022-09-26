########### Solution R: ##########

n <- 10000
a <- 5.5
b <- 3.14

X <- rbeta(n,a,b)

mean <- a/(a+b)
var <- a*b/((a+b)^2*(a+b+1))

library(ggplot2)
df <- data.frame(X = X)

# Plot de l'évolution de l'estimation de la moyenne
df$cumulative_prop <- cumsum(df$X)/(1:n)
df$iter <- 1:n

fig <-ggplot(df,aes(x=iter,y=cumulative_prop)) + geom_line() + geom_hline(aes(yintercept = mean, colour = "r")) +
    labs(title="Plot de l'évolution de l'estimation de la moyenne", 
         x = "Nombre de variable utilisé dans l'estimation",y="Moyenne estimée") +
    theme(plot.title = element_text(hjust = 0.5, size = 16),legend.position = "none")
fig

# Calculer l'estimation de la variance pour chacunes des m premières observations
df_ <- data.frame(var_hat = rep(0.,n-1),iter = 2:n)
for (i in 1:n-1){
    df_$var_hat[i] <- var(X[1:(i+1)])
}


# Plot de l'évolution de l'estimation de la moyenne
fig <-ggplot(df_,aes(x=iter,y=var_hat)) + geom_line() + geom_hline(aes(yintercept = var, colour = "r")) +
    labs(title="Plot de l'évolution de l'estimation de la moyenne", 
         x = "Nombre de variable utilisé dans l'estimation",y="Moyenne estimée") +
    theme(plot.title = element_text(hjust = 0.5, size = 16),legend.position = "none")
fig

library(ggplot2)

n <- 5000

# Générer un échantillon de n VA unif([-1,1])

X <- matrix(runif(2*n,min=-1,max=1),ncol=2)

# Générer la variable aléatoire Y
Y <- (apply(X,1,FUN=norm,type="2")<=1)

# Évolution de l'estimation de pi
fig <- ggplot(data.frame(iter=1:n,est = 4*cumsum(Y)/(1:n) ),aes(x=iter,y=est)) + geom_line() + geom_hline(aes(yintercept = pi, colour = "r")) +
    labs(title="Plot de l'évolution de l'estimation de la moyenne", 
         x = "Nombre de variable utilisé dans l'estimation") +
    theme(plot.title = element_text(hjust = 0.5, size = 16),legend.position = "none")
fig

n <- 50000
true_value <- 2.139350129

# Générer un échantillon de n VA unif([-1,1])

X <- matrix(runif(2*n),ncol=2)

# Écrire la fonction h
h <- function(X){
    
    val <- exp(apply(X,1,FUN=norm,type="2")^2)
    val
}
# Générer la variable aléatoire Y
Y <- h(X)

# Plot de l'évolution de l'estimation de la moyenne
fig <- ggplot(data.frame(iter=1:n,est = cumsum(Y)/(1:n) ),aes(x=iter,y=est)) + geom_line() + geom_hline(aes(yintercept = true_value, colour = "r")) +
    labs(title="Évolution de l'estimation de l'intégrale", 
         x = "Nombre de variable utilisé dans l'estimation") +
    theme(plot.title = element_text(hjust = 0.5, size = 16),legend.position = "none")
fig

N <- c(10,20,50,100,250,500,1000,2500,5000)
m <- 100

RMSE <- rep(0.,length(N))

i <- 0
for (n in N){
    i <- i+1
    échantillon_estimation = rep(0.,m)
    for (j in 1:m){
        # Générer un échantillon de n VA unif([-1,1])
        
        X <- matrix(runif(2*n,min=-1,max=1),ncol=2)
        # Estimation de pi
        
        pi_est = 4*mean(apply(X,1,FUN=norm,type="2")<=1)
        # Calcul de la MSE de l'échantillon
        
        échantillon_estimation[j] <- (pi_est-pi)^2
    }
    RMSE[i] = sqrt(mean(échantillon_estimation))
}
# Plot du taux de convergence
fig <- ggplot(data.frame(iter=N,RMSE = RMSE,taux_theorique = 1/sqrt(N)),aes(x=iter)) + geom_line(aes(y=RMSE)) + geom_line(aes(y=taux_theorique))+
        scale_x_continuous(trans='log2') + scale_y_continuous(trans='log2') +
        labs(title="Taux de convergence de la RMSE", 
         x = "n") +
        theme(plot.title = element_text(hjust = 0.5, size = 16),legend.position = "none")
fig
