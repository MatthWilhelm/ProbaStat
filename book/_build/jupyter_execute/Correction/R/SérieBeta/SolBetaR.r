########### Solution R: ##########


n_tirages <- 100
n <- 1000
valeurs_p <- seq(0,1,length.out=10)
biais <- numeric(10)

for (i in 1:10) {
  p <- valeurs_p[i]
  estim <- numeric(n_tirages)
  for (j in 1:n_tirages) {
    tirages <- rbinom(n, size = 1, prob = p)
    estim[j] <- (1+sum(tirages))/(2+n)
  }
  biais[i] <- mean(estim - p)
}

plot(valeurs_p, biais, ylim = c(-1, 1), xlab = "p", ylab = "Biais",type='b')

########### Solution R: ##########


n <- 10000
tirages <- replicate(n, rexp(3, rate = c(0.1, 0.35, 0.06)))
coords <- sample(1:3, size = n, replace = TRUE)
choisi <- tirages[cbind(coords, 1:ncol(tirages))]
p <- mean(choisi < 12)

########### Solution R: ##########

n <- 10000
existence <- rbinom(n, size = 1, p = 0.5)
resultats <- rbinom(20*n, size = 1, p = rep(ifelse(existence == 1, 0.9, 0.05), each = 20))
resultats <- matrix(resultats, ncol = 20, byrow = TRUE)
au_moins_un_positif <- rowSums(resultats) > 0
p <- mean(au_moins_un_positif)

########### Solution R: ##########

n <- 10000
x <- runif(n, min = 1, max = 2)
y <- 1/x
ey <- mean(y)

valeurs <- c(1,0,2,1,3,0,1,2,1)
estim <- mean(valeurs) 

ci = estim + c(-1.96, 1.96) * sqrt(estim/length(valeurs))

chiens <- structure(list(id = c(1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 
5, 5), poids = c(9.69, 9.87, 9.9, 8.43, 8.8, 9.64, 4.92, 7.13, 
5.12, 11.82, 10.32, 10.64, 11.94, 11.51, 11.17), taille = c(1.02, 0.68,
0.74, 0.8, 0.48, 0.44, 0.5, 0.44, 0.7, 1.66, 0.52, 1.46, 0.68, 0.84, 0.74),
poil = c("noir", "clair", "brun", "clair", 
"noir", "brun", "noir", "clair", "brun", "brun", "clair", "noir", 
"noir", "clair", "brun")), row.names = c(NA, -15L), class = "data.frame")
chiens

moy_poids <- mean(chiens$poids)
var_poids <- var(chiens$poids)

########### Solution R: ##########

n <- nrow(chiens)
ci <- moy_poids + qt(c(0.025, 0.975), df = n - 1) * sqrt(var_poids) / sqrt(n)
