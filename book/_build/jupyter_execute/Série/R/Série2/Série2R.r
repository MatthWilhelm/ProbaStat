library(dplyr)

data <- read.csv("Success_ProbaStat.csv")

# Place your answer here

# Place your answer here

# Place your answer here

source("fonction.r")

X = c(0,1,2,3,4,5,6,7,8,9,10)

# Vous pouvez accéder à ces quatres fonctions, f1,f2,f3,f4, de la manière suivante
f1(2)

# Place your answer here

# Place your answer here

# Place your answer here

# Place your answer here

library(ggplot2)
library(patchwork)

data1 <- data.frame(x=c(-10.,0.,0.,10.,10.,20.,20.,30.,30.,40.,40.,50.,50.,60.,60.,70.,70.,80.,80.,90.,90.,100.,100.,120.,120.),
            y=c(0.,0.,0.1,0.1,0.19,0.19,0.25,0.25,0.34,0.34,0.45,0.45,0.5,0.5,0.57,0.57,0.61,0.61,0.63,0.63,0.65,0.65,0.67,0.67,0.67))
data2 <- data.frame(x=0.1*c(-10.,0.,0.,10.,10.,20.,20.,30.,30.,35.,35.,50.,50.,54.,54.,70.,70.,83.,83.,90.,90.,115.,115.,120.,120.),
                    y=c(0.,0.,0.05,0.05,0.09,0.09,0.15,0.15,0.34,0.34,0.39,0.39,0.47,0.47,0.67,0.67,0.86,0.86,0.89,0.89,0.91,0.91,1.,1.,1.))
data3 <- data.frame(x=c(-10.,0.,0.,10.,10.,20.,20.,30.,30.,35.,35.,50.,50.,54.,54.,70.,70.,83.,83.,90.,90.,115.,115.,120.,120.),
                   y=c(0.,0.,0.05,0.05,0.09,0.09,0.15,0.15,0.34,0.34,0.39,0.39,0.47,0.47,0.67,0.67,0.86,0.86,0.84,0.84,0.91,0.91,1.,1.,1.))

f1 <- ggplot(data1,aes(x,y)) + geom_line() + labs(title = "Figure 1") + theme(plot.title = element_text(hjust = 0.5))
f2 <- ggplot(data2,aes(x,y)) + geom_line() + labs(title = "Figure 2") + theme(plot.title = element_text(hjust = 0.5))
f3 <- ggplot(data3,aes(x,y)) + geom_line() + labs(title = "Figure 3") + theme(plot.title = element_text(hjust = 0.5))

(f1 + f2) / f3 

bern <- function(p,n){
    # Générer une variable aléatoire de Bernouilli avec probabilité de succès p
        X <- ...
    X
}

library(ggplot2)

n <- 10000
p <- 0.3

# Générer n variable de Bernoulli avec probabilité de succès p
df <- ... 

# Calcul de la moyenne empirique 
mean <- ... 
sprintf("La moyenne de la variable générée est %f",mean)

# Plot pour vérifier expérimentalement que la fonction bern génère bien des variables de Bernoulli
...


geom <- function(p){
    if (p<1e-06){
        stop("La probabilité de succès doit être supérieure à zéro.")
    }
    
    
    ...

}

n <- 10000
p <- 0.3

# Générer n observations de S
df <- ... 

# Proposer une estimation de P(S = 1)
...


# Faire un plot montrant la convergence de cette probabilité
...


n <- 10000
p <- 0.3

# Générer n observations de S
df <- ... 

# Proposer une estimation de P(S = 1)
...


# Faire un plot montrant la convergence de cette probabilité
...


n <- 10000
p <- 0.3

t <- 4
m <- 2

# Générer deux ensemble de n observations de S pour estimer chacunes de ces 
# deux probabilités avec deux ensembles distinct
df <- ... 

# Proposer une estimation de P(S = 1)
...



# Faire un plot montrant la convergence de cette probabilité
...


library(ggplot2)
library(patchwork)

data1 <- data.frame(x=c(-1.,0.,0.,1.,1.,2.),
                    y=c(0.,0.,2.,2.,0.,0.))
data2 <- data.frame(x=c(-1.,0.25,0.25,0.75,0.75,2.),
                    y=c(0.,0.,1.,1.,0.,0.))
data3 <- data.frame(x=c(-1.,0.,0.,1.,1.,2.),
                    y=c(0.,0.,1.,1.,0.,0.))
data4 <- data.frame(x=c(-1.,-0.5,0.,0.5,1.,1.5,2.,2.5),
                    y=c(0.,0.,1.,0.,0.,1.,0.,0.))

f1 <- ggplot(data1,aes(x,y)) + geom_line() + labs(title = "Figure 1") + theme(plot.title = element_text(hjust = 0.5))
f2 <- ggplot(data2,aes(x,y)) + geom_line() + labs(title = "Figure 2") + theme(plot.title = element_text(hjust = 0.5))
f3 <- ggplot(data3,aes(x,y)) + geom_line() + labs(title = "Figure 3") + theme(plot.title = element_text(hjust = 0.5))
f4 <- ggplot(data4,aes(x,y)) + geom_line() + labs(title = "Figure 4") + theme(plot.title = element_text(hjust = 0.5))
(f1 + f2) / (f3 + f4) 

library(ggplot2)
library(patchwork)

data1 <- data.frame(x=c(-10.,0.,0.,10.,10.,20.,20.,30.,30.,40.,40.,50.,50.,60.,60.,70.,70.,80.,80.,90.,90.,100.,100.,120.,120.),
                    y=c(0.,0.,0.1,0.1,0.19,0.19,0.25,0.25,0.34,0.34,0.45,0.45,0.5,0.5,0.57,0.57,0.61,0.61,0.63,0.63,0.65,0.65,0.67,0.67,0.67))/0.67
data2 <- data.frame(x=seq(-10, 10, length.out = 100),
                    y=exp(seq(-10, 10, length.out = 100))/(1+exp(seq(-10, 10, length.out = 100))))
data3 <- data.frame(x=c(-1.,0.,1.,2.),
                    y=c(0.,0.,1.,1.))
data4 <- data.frame(x=c(-1.,0,1,2,2,3,4),
                    y=c(0.,0.,0.4,0.4,0.6,1.,1))
data5 <- data.frame(x=c(-1.,0,1,2,2,3,4),
                    y=c(0.,0.,0.4,0.,0.6,1.,1))
data6 <- data.frame(x=c(-1.,0,0,1,1,2),
                    y=c(0.,0.,0.4,0.4,1.,1))

f1 <- ggplot(data1,aes(x,y)) + geom_line() + labs(title = "Figure 1") + theme(plot.title = element_text(hjust = 0.5))
f2 <- ggplot(data2,aes(x,y)) + geom_line() + labs(title = "Figure 2") + theme(plot.title = element_text(hjust = 0.5))
f3 <- ggplot(data3,aes(x,y)) + geom_line() + labs(title = "Figure 3") + theme(plot.title = element_text(hjust = 0.5))
f4 <- ggplot(data4,aes(x,y)) + geom_line() + labs(title = "Figure 4") + theme(plot.title = element_text(hjust = 0.5))
f5 <- ggplot(data5,aes(x,y)) + geom_line() + labs(title = "Figure 5") + theme(plot.title = element_text(hjust = 0.5))
f6 <- ggplot(data6,aes(x,y)) + geom_line() + labs(title = "Figure 6") + theme(plot.title = element_text(hjust = 0.5))
(f1 + f2 + f3) / (f4 + f5 + f5) 
