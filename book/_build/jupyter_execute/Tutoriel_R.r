vec = c(1, pi, exp(1))
vec[1]

1:10 # vecteur dont les composantes sont les entiers de 1 à 10
8:-2 # vecteur dont les composantes sont les entiers de 8 à -2, dans l'ordre décroissant
seq(from = 1, to = 12, by = .25) # vecteur de 1 à 12, avec un incrément de 0.25
seq(1,12, length.out = 10) # vecteur de 1 à 12, avec un incrément constant et une longueur de 10

M = matrix(c(1,2,3,4,5,6), nc = 3)
print(M)

M[,1]  #élément à la 1ère ligne, 2ème colonne
M = matrix(c(1,2,3,4,5,6), nc = 3, byrow = T)
print(M)

M[1,]  #affiche toute la 1ère ligne
M[,2]  #affiche toute la 2ème colonne

 M %*% vec #multiplication matrice-vecteur
 M %*% matrix(vec, nc = 1) # identique; un vecteur est considere comme une matrice de taille n x 1

3 * M # est similaire a une multiplication de la matrice par un scalaire

3*M + 5 # est similaire a une multiplication de la matrice par un scalaire suivi d'une addition d'un scalaire

rep(vec, 3) # répétition de 3 fois le même vecteur  
rep(vec, each = 3) # répétition 3 fois de chaque éléments du vecteur consécutivement

M # affiche M
print(M[2,1]) # affiche la composante (2,1) de la matrice M 
M[2,1] # affiche aussi la composante (2,1) de la matrice M 

mylist <- list(x = c(2,3), y = matrix(c(1,-1,-1,2), nc = 2)) # liste de deux objets, le premier, x est un vecteur
# et le second, y, est une matrice
mylist[[1]] # on accède au premier élément
mylist$y # on accède à l'élément y
mylist$z <- T # on déclare un élément z qui est un booléen T
mylist


a = 33
b = 200
if(b > a) print("b is greater than a")

a = 33
b = 200
if(b > a){
    print("b is greater than a")
    print(b-a)
}


a = 200
b = 33
# version correcte
if (b > a)
    {
     print("b is greater than a")
} else
    {
    print("a is greater than b")
}
 
  

a = 200
b = 33
# donne une erreur
if (b > a)
    {
     print("b is greater than a")
}
else
    {
    print("a is greater than b")
}
 
  

a = 33
b = 33
# version correcte
if (b > a)
    {
     print("b is greater than a")
}else if (b == a)
    {
    print("a is equal to b")
} else
{
    print("a is greater than b")
}

i = 1
while(i < 6)
    {
  print(i)
  i = i + 1
}

i = 1
while(i < 6)
  { print(i)
  if(i == 3) break
  i  <- i + 1
   }

fruits = c("apple", "banana", "cherry")
for(x in fruits)
  print(x)

for(x in vec) #avec un vecteur
    print(x * 2)

for(x in seq(2, 30, by = 3)) #commence à 2, finit à 29 et incrémente de 3
  print(x)
# seq_along permet déclare un vecteur correspondant au vecteur des indices d'un autre vecteur
seq_along(vec)
# typiquement utilisé de la manière suivante
for(i in seq_along(vec))
    vec[i]
# et qui est équivalent à 
for(i in 1:length(vec))
    vec[i]

compteur <- function(){ #sans paramètres d'entreé ni de sortie
    i = 0
    while(i < 3){
        print(i)
        i = i + 1
        }
} 
    
compteur()

compteur() #une fois définie, on peut appeler la fonction depuis une autre cellule du notebook.

compteur2 <- function(stop){ #avec un paramètre d'entrée
    i = 0
    while (i < stop){
        print(i)
        i = i + 1
        }
    }
compteur2(4)

compteur2 <- function(stop = 2){ #avec un paramètre d'entrée
    i = 0
    while (i < stop){
        print(i)
        i = i + 1
        }
    }
compteur2()

compteur3 <- function(stop,b = 3){ #avec 2 paramètres d'entrée, le second étant par défaut b = 3
    i = 0
    while(i < stop){
        i = i + b
        print(i)
        }
        }
print("avec deux paramètres spécifiés")
compteur3(4,2)

print("avec un seul paramètre spécifié")
compteur3(5)

x = compteur(4) #on peut directement attribuer ce que retourne la fonction à des variables en dehors de la fonction
print(x)

compteur <- function(stop){ #avec un paramètre d'entrée et 2 de sortie
    i = 0
    j = 100
    while(i < stop){
        i = i + 1
        j = j - 1
        }
    return(list(i = i,j = j)) 
}
mylist <- compteur(4) # Attention à l'ordre des paramètres: x prend la valeur de i et y de j.
print(c(mylist$i,mylist$j))

myfunction <- function(x = 5){
    y = x + 2
    y # équivalent à return(y)
}
x <- myfunction(3)
print(x)

example <- function(){
    loc = 5
} 
print(loc) # retourne une erreur puisque loc n'existe que dans la fonction

var_globale = 5

exemple <- function(){
    var_globale = 0
    print(var_globale)
    }
exemple()        
print(var_globale)

library("tidyverse")

set.seed(1) # pour fixer une graine dans le générateur de nombre aléatoire
x <- sample(1:5,size = 20, replace = T ) # On choisit de manière équiprobable et avec remise 20 valeurs entre 1 et 5,
plyr::mapvalues(x, from = 1:5, to = LETTERS[1:5]) # on remplace 1,..., 5 par A,...,E

datas = data.frame(Taille = c(147 , 150 , 152 , 155 , 157 , 160 , 163 , 165 , 168 , 170 , 173 , 175 , 178 , 180 , 183), 
                                Poids = c(52 , 53 , 54 , 56 , 57 , 59 , 60 , 61 , 63 , 64 , 66 , 68 , 70 , 72 , 74))
head(datas)

mean(datas$Poids) # calcule la moyenne de la colonne "Poids" 

lapply(datas, mean)

lapply(datas, median)



hist(datas$Poids, main = "Histogramme du poids", xlab = "Poids")

plot(x=datas$Taille, y=datas$Poids)

with(datas, plot(x = Taille, y = Poids)) # with prend comme premier argument le nom de l'environnement,
# puis l'expression à évaluer

numeric(10)



X = c(1,2,3,4,5)
mean(X)   #mean est la fonction pour calculer la moyenne d'un vecteur

M = matrix(c(1,2,3,3,5,6,7,8,9), nc = 3)
y = c(1,1,1)
det(M) # calcule le déterminant de M
x = solve(M,y) # résout l'équation Ax = y
print(x) # affiche la solution x

dim(M) # renvoit la taille de M: matrice 3x3

rowSums(M) # permet de faire la somme sur les lignes
colSums(M) # permet de faire la somme sur les colonne

t(M) # matrice transposée de M

x = c(1, 2, 3, 4)
y = c(1, 4, 9, 16)
plot(x,y)


# vecteurs de points equidistants
t = seq(0., 1, 0.05)
ft <- sin(2* pi *t)
# une droite
plot(t, t, type = "l", xlim = c(0,1), xlab = "Some value", main = "")
# à laquelle on ajoute des points
points(t,t, pch = 19, col = "red")
# on joute une droite en traits tillés du sinus
lines(t, ft, lty = 2)
# the function legend adds a legend
legend("topleft", legend = c("A nice line", "some points"), lty = c(1,NA), pch = c(NA, 19), col = c("black", "red"))
# l'argument lty correspond au type de ligne : la première est une ligne continue, correspondant à la valeur 1
# le second n'est pas une ligne (c'est un point), donc nous fixons la seconde valeur à NA
# l'argument pch correspond au type de point : le premier n'est pas un point mais une ligne, donc on met la deuxième valeur à NA.
# le second est un point correspondant au type de point 19, tel que défini dans la fonction points ci-dessus. 



# evenly sampled time at 200ms intervals
t = seq(0., 1, length = 100)
# on créé un vecteur de translations
shift_seq <- seq(0,2 * pi, length.out = 7)
# on déclare une matrice de NA en spécifiant ses composantes
shifted_sine <- matrix(NA, nr = length(t), nc = length(shift_seq)) 
for(i in seq_along(shift_seq))
{
    shifted_sine[,i] <- sin(2* pi *t + shift_seq[i]) # on pose que la ieme colonne est ce vecteur
}
limits_y <- range(c(shifted_sine, t)) # on concatène les valeurs a grapher et on en prend le min et le max
plot(t, t, type = "l", xlim = c(0,1), xlab = "Some value", ylim = limits_y, main = "A nice title")
points(t[seq(1, length(t), 5)],t[seq(1, length(t), 5)], pch = 19, col = "red")
for(i in seq_along(shift_seq))
{
    lines(t, shifted_sine[,i], lty = i, col = i)
}
legend("topleft", legend = c(rep("A nice line", length = length(shift_seq)), "some points"),
       lty = c(seq_along(shift_seq),NA), pch = c(rep(NA, length = length(shift_seq)), 19),
       col = c(seq_along(shift_seq), "red"),bg="transparent")


mu = 100; sigma = 15
x = mu + sigma * rnorm(10000)

# the histogram of the data
hist(x, main = "Histogramme de QIs")


help(plot)

?? histogram
