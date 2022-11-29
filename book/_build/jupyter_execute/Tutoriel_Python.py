#!/usr/bin/env python
# coding: utf-8

# # Tutoriel Python
# 
# 
# <div style="border:1px solid black; padding:20px 20px;text-align: justify;text-justify: inter-word">
#     <strong>Introduction à Python et aux Jupyter Notebooks
# <br/> <br/>
#   <span style="text-decoration:underline;font-weight:bold;">Comment utiliser ce notebook?</span><br/>
#     Ce notebook est fait de cellules "texte" (Markdown) et "code". Les cellules code doivent être <strong>exécutées</strong> pour voir le résultat du programme. Pour exécuter une cellule, sélectionne la et clique sur le bouton "Exécuter" (<span style="font: bold 12px/30px Arial, serif;">&#9658;</span>) dans la barre à outils juste au-dessus du notebook, ou utilise <code>shift + enter</code>. Utiliser <code>shift + enter</code> plusieurs fois exécutera des blocs de code consécutifs les uns après les autres, tout en ignorant les cellules de texte (leur exécution ne fait rien). Il est important d'exécuter les cellules de code dans leur ordre d'apparition dans le notebook.<br/>
# Vous pouvez utiliser la table des matières pour naviguer facilement entre les sections.
# </div>

# ##  Introduction
# 
# Ceci est un notebook jupyter. C'est le support que nous allons utiliser tout au long du semestre pour les séances d'exercices. La révision des concepts présentés dans ce noteboook vous sera grandement bénéfique et vous permettra de gagner du temps lors des séances d'exercices. 
# 
# 
# **Pourquoi Python?**
# 
# Certains d'entre vous n'ont peut-être pas encore utilisé Python, mais Python est un langage facile à comprendre et très rapide à prendre en main, tout en étant de haut niveau. La syntaxe est plus simple que d'autres langages tels que C et C++, tout en vous donnant la possibilité de faire de la programmation orientée objet. Cependant, elle est sensible à l'indentation (contrairement au C et au C++ qui utilisent des parenthèses) ; soyez donc attentifs à cela au début. 
# 
# Python est développé sous une licence open source approuvée par l'OSI, ce qui le rend librement utilisable [(contrairement à Matlab)] et distribuable, même pour un usage commercial'' (https://www.python.org/about/). Il existe une communauté active qui développe des librairies destinées à être utilisées dans divers contextes comme la robotique et l'apprentissage automatique par exemple. Cela signifie également que la communauté python est assez importante et qu'il existe un grand nombre d'aides en ligne, notamment sur [stack overflow](https://stackoverflow.com/) où vous êtes sûr de trouver la plupart des réponses à vos questions relatives à python. 
# 
# Il est également compatible avec de nombreux systèmes d'exploitation, ce qui signifie que vous ne rencontrerez pas de problèmes lorsque vous passerez de linux à macOS ou à windows. L'installation de bibliothèques est également très facile avec pip3. 
# 
# Python est ce qu'on appelle un "langage typographié dynamiquement", c'est-à-dire que vous n'avez pas à spécifier le type d'un objet. Un des inconvénients de Python est sa vitesse. Il est beaucoup plus lent qu'un langage qui est compilé comme le C++. 
# 
# 
# **Qu'est-ce que les Jupyter Notebooks et pourquoi les utiliser?**.
# 
# L'environnement Jupyter Notebooks est un système hybride écrit en Python dont l'interface utilisateur s'exécute comme des applications web dans votre navigateur. Par conséquent, comme Python, les Jupyter Notebooks sont des applications web open source qui facilitent la création et le partage de codes et de documents. Les carnets Jupyter fournissent un environnement dans lequel vous disposez de différents types de cellules (par exemple, celle qui est présentée ici est appelée cellule **Markdown** et est pratique pour la documentation, l'intégration d'images, de liens url, l'explication de ce que vous prévoyez de faire, comment, etc.) Les cellules de codage sont utiles car elles peuvent être exécutées une par une et facilitent le prototypage et le débeuguage, un peu comme la division d'un scrip Matlab en sections. Contrairement à Matlab cependant, vous n'avez pas une vue d'ensemble de vos variables et de leurs valeurs, mais vous pouvez toujours les imprimer. Les carnets Jupyter peuvent également être utilisés pour d'autres langages que python (par exemple R, SQL etc...). 
# 
# 

# ## Comment utiliser les Jupyter notebooks ?

# Pour utiliser un Jupyter notebook, vous devez comprendre quelques principes de base : 
# 
# 
# **Ajout et suppression de cellules**
# 
# Si vous avez ouvert le notebook avec **noto**, vous pouvez ajouter (au-dessus ou en-dessous) et supprimer des cellules depuis le coin supérieur droit de chaque cellule.
# 
# Si vous travaillez en local avec une distribution **Anaconda**,vous pouvez ajouter des cellules en allant dans le menu "Insertion" et en choisissant "Ajouter au-dessus ou au-dessous" et déplacer des cellules vers le haut ou vers le bas en choisissant les flèches sous la barre à outils.
# 
# A tout moment vous pouvez changer le type de cellule : Code, Markdown,etc..
# 
# 
# **Faire tourner les cellules**
# 
# Vous devrez procéder de la sorte pour exécuter le code contenu dans les cellules individuelles. 
# 
# - Pour exécuter une cellule individuelle, sélectionnez-la et appuyez sur "Maj+Entrée".
# 
# - Pour exécuter le notebook en entier, allez dans "Cellule->Exécuter tout". Pour exécuter seulement les cellules au-dessus ou au-dessous, vous trouverez cela dans le même menu. 
# 
# - Pour éxécuter de nouveau le notebook en entier, allez dans "Kernel -> Restart and Run all" ou appuyez sur le bouton qui ressemble à un bouton d'avance rapide. Ceci efface toutes les variables stockées en mémoire et exécute le notebook depuis le début. Il est important de ré-exécuter le notebook à partir de zéro de temps en temps, par exemple lorsque vous avez atteint une étape importante pour vous assurer que vous n'avez pas de beugs. Comme le notebook stocke toutes les variables en mémoire, cela permet d'éviter les erreurs dues à la suppression d'un élément ou à l'ordre incorrect de certains éléments dans les cellules ou entre les cellules. 
# 
# **Bonnes pratiques**
# 
# - Expliquez votre raisonnement dans les cellules Markdown, de la même manière que vous le feriez dans un rapport. Vous pouvez avoir des sections, des sous-sections, écrire des paragraphes, saisir des images, etc. 
# 
# - Commentez votre code afin que toute personne qui ouvre votre notebook comprenne ce que vous faites. 
# 
# - Lorsque vous faites appel à une librairie, il est considéré comme une bonne pratique de l'importer au début du notebook. 
# 
# - N'oubliez pas de sauvegarder régulièrement votre notebook. Vous pouvez le faire soit avec le raccourci d'enregistrement (Ctrl+S), soit en passant par Fichier -> Enregistrer sous. Sous Fichier, vous trouverez également d'autres options telles que créer un nouveau notebook, renommer le notebook actuel, le télécharger en tant que fichier pdf, python etc... 
# 
# **Installation des extensions Jupyter Notebook**
# 
# Les extensions Jupyter sont des modules complémentaires qui fonctionnent avec les notebooks Jupyter (et non avec Jupyter Lab) permettant d'améliorer votre productivité. 
# Si vous êtes intéressés, vous pouvez installer quelques [extensions qui sont utiles](https://towardsdatascience.com/jupyter-tools-to-increase-productivity-7b3c6b90be09) 

# ## Introduction à Python

# ### Types et opérateurs

# En Python, il y a différents **types** prédéfinis:
# 
# - Text Type:	**str**
# 
# 
# - Numeric Types:	**int**, **float**, complex
# 
# 
# - Sequence Types:	**list**, **tuple** , **range**
# 
# 
# - Mapping Type:	**dict** 
# 
# 
# - Set Types:	**set** , frozenset 
# 
# 
# - Boolean Type:	**bool** (either ``True`` or ``False``)
# 
# 
# - Binary Types:	bytes, bytearray, memoryview
# 
# 
# Le type d'une variable est défini au moment où on lui assigne une valeur.
# 
# |Exemple| Type correspondant|
# | :------------- |:-------------:|
# |x = "Hello World"|	str	|
# |x = 20	|int	|
# |x = 20.5	|float	|
# |x = 1j	|complex	|
# |x = ["apple", "banana", "cherry"]	|list	|
# |x = ("apple", "banana", "cherry")	|tuple	|
# |x = range(6)	|range	|
# |x = {"name" : "John", "age" : 36}	|dict	|
# |x = {"apple", "banana", "cherry"}	|set	|
# |x = frozenset({"apple", "banana", "cherry"})	|frozenset	|
# |x = True	|bool	|
# |x = b"Hello"	|bytes	|
# |x = bytearray(5)	|bytearray	|
# |x = memoryview(bytes(5))	|memoryview|

# Les **opérateurs** sont utilisés pour faire des opérations sur des variables ou des valeurs.
# 
# Python divise les opérateurs en différents groupes:
# 
# - Les opérateurs arithmétiques
# - Les opérateurs d'affectation
# - Les opérateurs de comparaison
# - Les opérateurs logiques
# 
# **Les opérateurs arithmétiques**
# 
# |Opérateur|Nom|Exemple|
# |:-------------: | :------------- |:-------------:|
# |+|Addition|x + y|
# |-|Soustraction|x - y|
# |*|Multiplication|x * y|
# |/|Division|x / y|
# |%|Module|x % y|
# |**|Exponentielle|x ** y|
# |//|Division entière|x // y|
# 
# **Les opérateurs d'affectation**
# 
# |Opérateur	|Exemple	|Comme|
# |:-------------: | :------------- |:-------------:|
# |=|	x = 5|	x = 5	|
# |+=|	x += 3|	x = x + 3	|
# |-=|	x -= 3|	x = x - 3	|
# |*=|	x *= 3|	x = x * 3	|
# |/=|	x /= 3|	x = x / 3	|
# |%=|	x %= 3|	x = x % 3	|
# |//=|	x //= 3|	x = x // 3	|
# |\**=|	x \**= 3|	x = x \** 3	|
# |&=|	x &= 3|	x = x & 3	|
# |\|=|	x |= 3|	x = x | 3	|
# |^=|	x ^= 3|	x = x ^ 3	|
# 
# **Les opérateurs de comparaison**
# 
# | Opérateur | Nom | Exemple |
# |----------|--------------------------|---------|
# | == | Egal | x == y |
# | != | Différent | x != y |
# | > | Plus grand que | x > y |
# | < | Plus petit que | x < y |
# | >= | Plus grand ou égal | x >= y |
# | <= | Plus petit ou égal | x <= y |
# 
# **Les opérateurs logiques**
# 
# | Opérateur | Description | Exemple |
# |----------|---------------------------------------------------------|-----------------------|
# | and  | Retourne Vrai si les deux déclarations sont vraies | x < 5 and  x < 10 |
# | or | Retourne Vrai si au moins une des deux déclarations est vraie  | x < 5 or x < 4 |
# | not | Inverse le résultat, renvoie Faux si le résultat est vrai. | not(x < 5 and x < 10) |

# #### Listes/Arrays
# 
# Une liste est un ensemble ordonné et modifiable. En Python, les listes sont écrites avec des crochets [ ].
# **L'indexation commence à 0 en Python.** L'index -1 permet d'accéder au dernier élément de la liste.

# In[15]:


list = ["apple", "banana", "cherry"]
list[0]


# In[16]:


vecteur = [2,4,6,8]
vecteur[2]   #3ème élément du vecteur


# In[17]:


import numpy as np


# In[18]:


#avec un array en 2D
A = np.array([[1,2,3,4],[5,6,7,8]])
print(A)


# In[19]:


A[0,1]  #élément à la 1ère ligne, 2ème colonne


# In[20]:


print(A[1,:])  #affiche toute la 2ème ligne


# #### Opérations sur des vecteurs/matrices
# 
# Voir les exemples ci-dessous:

# In[21]:


print(A.dot(vecteur)) #multiplication matrice-vecteur


# In[22]:


print(A @ vecteur) # le signe @ est un opérateur de multiplication entre matrices ou entre matrices et vecteurs


# In[23]:


print(3*A)


# In[24]:


print(3*A + 5)


# In[25]:


print(3*vecteur)   


# In[26]:


vecteur = np.array([2,4,6,8])
print(3*vecteur)


# Attention! Suivant comment a été déclarée la variable, les opérations changent. Dans le premier cas, on voit que le vecteur a été copié 2 fois. Dans le 2ème cas, chaque élément a été multiplié par 3. Voir les sections suivantes sur les librairies et notamment NumPy.

# ### Les principales structures

# #### L'instruction if
# 
# Exécutez les différents exemples ci-dessous pour vous familiariser avec sa syntaxe:

# In[27]:


a = 33
b = 200
if b > a:
  print("b is greater than a")


# In[28]:


a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error


# **Attention à l'indentation** lorsque vous utilisez des structures !

# In[29]:


a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("a is greater than b")


# In[30]:


a = 200
b = 200
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


# Il peut y avoir un nombre quelconque de parties elif et la partie else est facultative. Le mot clé elif est un raccourci pour else if, et permet de gagner un niveau d'indentation. Une séquence if ... elif ... elif ... est par ailleurs équivalente aux instructions switch ou case disponibles dans d'autres langages.

# #### L'instruction while
# 
# La boucle **while** permet d'exécuter un ensemble d'instructions tant qu'une condition est vraie.

# In[31]:


i = 1
while i < 6:
  print(i)
  i += 1


# La boucle while exige que les variables pertinentes soient prêtes. Dans cet exemple, nous avons dû définir une variable d'indexation, i, fixée à 1.
# 
# Exécutez les cellules ci-dessous pour découvrir les outils **break** et **continue**

# In[32]:


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


# In[33]:


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# **Break** permet d'arrêter la boucle while même si la condition du while est toujours satisfaite. **Continue** permet de stopper l'itération en cours et de passer à la suivante directement.

# #### L'instruction for
# 
# L'instruction **for** que propose Python est un peu différente de celle que l'on peut trouver dans d'autres langages de programmation et fonctionne davantage comme une méthode d'itération que l'on trouve dans les langages de programmation orientés objet.
# 
# Elle est utilisée pour itérer sur une séquence (c'est-à-dire une liste, un tuple, un dictionnaire, un ensemble ou une chaîne).
# 
# 
# De nouveau, éxécutez les différents exemples ci-dessous pour vous familiariser avec sa synthaxe:

# In[34]:


fruits = ["apple", "banana", "cherry"] #avec une liste
for x in fruits:
  print(x)


# In[35]:


for x in "banana": #avec une chaine de caractères (str)
  print(x)


# In[36]:


for x in [1,2,4,6]: #avec un tuple
    print(x)


# Comme pour la boucle **while**, on peut utiliser **break** et **continue** pour sortir de la boucle for ou passer à l'itération suivante.
# 
# Vous avez remarqué que contrairement à une boucle **for** en C où l'on donne à l'utilisateur la possibilité de définir le pas d'itération et la condition de fin, l'instruction **for** en Python itère sur les éléments d'une séquence (qui peut être une liste, une chaîne de caractères…), dans l'ordre dans lequel ils apparaissent dans la séquence.
# 
# Exécutez les cellules suivantes pour voir l'utilité de certaines fonctions complémentaires comme **range** et **enumerate**.
# 

# In[37]:


for x in range(6): #Par défaut range commence à 0 et incrémente de 1. Notez que range s'arrête à N-1 pour range(N)
  print(x)


# In[38]:


for x in range(2, 30, 3): #commence à 2, finit à 29 et incrémente de 3
  print(x)


# In[39]:


some_list = ['Looping', 'with', 'counters', 'is', 'a', 'classic!']
for idx, element in enumerate(some_list):
     print(f'Elément en position {idx} est {element}')


# ### Les fonctions
# 
# #### Syntaxe des fonctions
# 
# La syntaxe Python pour la définition d’une fonction est la suivante :

# In[40]:


def nom_fonction(liste de paramètres):
      bloc d'instructions


# Vous pouvez choisir n’importe quel nom pour la fonction que vous créez, à l’exception des mots-clés réservés du langage, et à la condition de n’utiliser aucun caractère spécial ou accentué (le caractère souligné « _ » est permis). Comme c’est le cas pour les noms de variables, on utilise par convention des minuscules, notamment au début du nom (les noms commençant par une majuscule seront réservés aux classes).
# 
# Une fonction peut avoir un, plusieurs ou pas de paramètres d'entrée (appelés **arguments**) et elle peut retourner indirectement (print) ou directement des variables (avec **return**). Exécutez les cellules ci-dessous pour vous familiariser avec les fonctions.

# In[41]:


def compteur3(): #sans paramètres d'entreé ni de sortie
    i = 0
    while i < 3:
        print(i)
        i = i + 1
compteur3()


# In[42]:


compteur3() #on aurait très bien pu appeler la fonction depuis une autre cellule du notebook.


# In[43]:


def compteur(stop): #avec un paramètre d'entrée
    i = 0
    while i < stop:
        print(i)
        i = i + 1
compteur(4)


# In[44]:


def compteur(stop,b): #avec 2 paramètres d'entrée
    i = 0
    while i < stop:
        i = i + b
        print(i)
compteur(4,2)


# In[45]:


def compteur(stop): #avec un paramètre d'entrée et de sortie
    i = 0
    while i < stop:
        i = i + 1
    return i
compteur(4)     #renvoie la dernière valeur prise par i dans la fonction.   


# In[46]:


x = compteur(4) #on peut directement attribuer ce que retourne la fonction à des variables en dehors de la fonction
print(x)


# In[47]:


def compteur(stop): #avec un paramètre d'entrée et 2 de sortie
    i = 0
    j = 100
    while i < stop:
        i = i + 1
        j = j - 1
    return i,j 
x,y = compteur(4) # Attention à l'ordre des paramètres: x prend la valeur de i et y de j.
print(x,y)


# #### Portée des variables (scope)
# 
# En Python, nous pouvons déclarer des variables n’importe où dans notre script : au début du script, à l’intérieur de boucles, au sein de nos fonctions, etc.
# 
# L’endroit où l'on définit une variable dans le script va déterminer l’endroit où la variable va être accessible c’est-à-dire utilisable.
# 
# Le terme de “portée des variables” sert à désigner les différents espaces dans le script dans lesquels une variable est accessible. En Python, une variable peut avoir une portée locale ou une portée globale.
# 
# Les variables définies dans une fonction sont appelées **variables locales**. Elles ne peuvent être utilisées que localement c’est-à-dire qu’à l’intérieur de la fonction qui les a définies. Tenter d’appeler une variable locale depuis l’extérieur de la fonction qui l’a définie provoquera une erreur.

# In[48]:


def exemple():
    locale = 5   


# In[49]:


print(locale)


# Cela est dû au fait que chaque fois qu’une fonction est appelée, Python réserve pour elle (dans la mémoire de l’ordinateur) un nouvel espace de noms (c’est-à-dire une sorte de dossier virtuel). Les contenus des variables locales sont stockés dans cet espace de noms qui est inaccessible depuis l’extérieur de la fonction.
# 
# Cet espace de noms est automatiquement détruit dès que la fonction a terminé son travail, réinitialisant les valeurs des variables à chaque nouvel appel de fonction.
# 
# Les variables définies dans l’espace global du script, c’est-à-dire en dehors de toute fonction sont appelées des **variables globales**. Ces variables sont accessibles (= utilisables) à travers l’ensemble du script et accessible en lecture seulement à l’intérieur des fonctions utilisées dans ce script.
# 
# Pour le dire très simplement : une fonction va pouvoir utiliser la valeur d’une variable définie globalement mais ne va pas pouvoir modifier sa valeur c’est-à-dire la redéfinir. En effet, toute variable définie dans une fonction est par définition locale ce qui fait que si on essaie de redéfinir une variable globale à l’intérieur d’une fonction on ne fera que créer une autre variable de même nom que la variable globale qu’on souhaite redéfinir mais qui sera locale et bien distincte de cette dernière.

# In[ ]:


var_globale = 5

def exemple():
    var_globale = 0
    print(var_globale)
    
exemple()        
print(var_globale)


# Dans certaines situations, il serait utile de pouvoir modifier la valeur d’une variable globale depuis une fonction, notamment dans le cas où une fonction se sert d’une variable globale et la manipule.
# 
# Cela est possible en Python. Pour se faire, il suffit d’utiliser le mot-clé **global** devant le nom d’une variable globale utilisée localement afin d’indiquer à Python qu’on souhaite bien modifier le contenu de la variable globale et non pas créer une variable locale de même nom.

# In[50]:


var_globale = 5

def exemple():
    global var_globale  #définir comme variable globale
    var_globale = 0
    print(var_globale)
    
exemple()        
print(var_globale)


# ## Les librairies

# Jusque là, nous avons vu les différentes structures (if, while, for) et comment implémenter une fonction. Nous allons à présent aborder ce qui fait la puissance de Python grâce à sa communauté de développeurs qui créent et mettent à disposition de nombreuses **librairies** permettant de gagner un temps précieux.
# 
# En langage Python, une librairie est un ensemble de fonctions, de classes d’objets et de constantes qui permettent de travailler sur un thème en particulier. Découvrons quelques librairies qui seront très utiles dans ce cours.
# 
# Avant toute chose, il faut les installer puis les importer sur le notebook.

# **Installation des librairies Python via le notebook**
# 
# Au lieu de lancer l'installation via le terminal, vous pouvez également lancer l'installation depuis le notebook dans une cellule du Code en appelant ``!pip3 install lib1 lib2 lib3``. C'est ce que nous ferons pour les librairies qui sont nécessaires pour résoudre les sessions d'exercices hebdomadaires.
# 
# Par exemple, nous allons installer les librairies utiles pour le cours:

# In[51]:


get_ipython().system('pip3 install numpy pandas scipy matplotlib')


# **Importation des librairies Python sur le notebook**

# In[52]:


import numpy as np 
import pandas as pd


# Notez qu'en général, on donne un surnom à la librairie (ici "np" et “pd”). En effet, on va être amené à appeler cette librairie souvent dans le corps du code. Alors autant réduire le nombre de caractères nécessaires afin de gagner du temps!
# 
# Certaines librairies comportent des sous-modules qui offrent des fonctionnalités particulières. Attention, les sous-modules ne sont pas automatiquement importés lorsqu'on importe la librairie si bien qu'il faut les importer séparément comme nous le verrons dans certains exemples.

# ### Pandas
# 
# Pandas est la bibliothèque la plus complète en ce qui concerne la manipulation de données. On peut comparer pandas à un “Excel sous stéroïdes”. Elle permet de travailler avec :
# 
# - des tableaux de données en deux dimensions (lignes et colonnes) appelés **DataFrames**,‍
# - des Panels, c'est-à-dire des ensemble de données en trois ou quatre dimensions!
# 
# Avec la bibliothèque Pandas, tu peux importer des données depuis un fichier .csv afin de les nettoyer (par exemple pour éliminer toutes les lignes vides), les transformer ou les compléter.
# 
# Pandas permet également d’effectuer des calculs statistiques sur tes données, par exemple avec la méthode .mean() qui permet d’obtenir la moyenne des valeurs contenues dans une colonne.

# In[53]:


datas = pd.DataFrame(np.array([[147 , 150 , 152 , 155 , 157 , 160 , 163 , 165 , 168 , 170 , 173 , 175 , 178 , 180 , 183], 
                                [52 , 53 , 54 , 56 , 57 , 59 , 60 , 61 , 63 , 64 , 66 , 68 , 70 , 72 , 74]]).transpose(), 
                     columns=["Taille","Poids"])
datas.head()


# In[54]:


datas.mean()


# In[55]:


datas.median()


# In[56]:


datas.plot.hist(alpha=0.5);


# In[57]:


datas.plot.scatter(x="Taille", y="Poids");


# ### Numpy
# 
# Numpy contient des modules de gestion de données et de calcul. Elle permet de gérer facilement des bases de données : on les appelle les **numpy arrays**. Ce sont des listes, ou bien des listes de listes.
# 
# L’avantage de Numpy est de pouvoir créer rapidement une base de données, avec des instructions simples que Python comprend. Par exemple, l’instruction np.zeros(10) renvoie une liste de dix chiffres, tous égaux à 0. 
# 
# Ensuite, Numpy permet d’effectuer des opérations particulièrement rapidement. En effet, avec Numpy une opération effectuée sur un “array” s’applique à chaque terme de cet array. Cela évite de devoir exécuter une boucle FOR ou une boucle WHILE, ce qui est parfois une opération assez lente.
# 
# Tu peux également faire interagir deux arrays, par exemple en les additionnant. 
# 
# Numpy est pourvue de fonctions mathématiques plus puissantes que pandas. Toutefois, Numpy ne permet pas d'étiqueter les colonnes et les lignes.

# In[58]:


np.zeros(10)


# In[59]:


print(np.zeros(10)) #print affiche directement le tableau


# In[60]:


X = np.array([1,2,3,4,5])
np.mean(X)   #np.mean est la fonction de numpy pour calculer la moyenne d'un numpy array.


# In[61]:


A = np.array([[1,2,3],[4,5,6],[7,8,9]])
y = np.array([1,1,1])
x = np.linalg.solve(A,y) # résout l'équation Ax = y
print(x)


# In[ ]:


np.shape(A) # renvoit la taille de A: matrice 3x3


# In[ ]:


np.mean(A,axis=0) # axis = 0 permet de faire la somme sur les colonnes. (remplacer par axis=1 pour les lignes)


# In[ ]:


A.T # matrice transposée de A


# ### SciPy
# 
# SciPy s’utilise en synergie avec Numpy puisqu’elle travaille sur des données du format Numpy array. SciPy offre un catalogue d’opérations scientifiques : algèbre linéaire, algorithmes de régression, fonctions statistiques… 
# 
# En particulier, SciPy permet de travailler sur des projets d’optimisation numérique qui consistent à chercher à obtenir le plus petit chiffre (ou le plus grand) possible en modifiant certaines variables.
# 
# **Scipy.stats** est un sous-module de **Scipy** qui contient un grand nombre d'outils pour les statistiques : distributions de probabilités, fonctions de corrélation, tests statistiques, etc.. Attention à bien importer ce sous-module séparémment.
# 
# 

# In[ ]:


from scipy import stats
from scipy.stats import bootstrap
rng = np.random.default_rng()


# In[ ]:


datas = np.array([[147 , 150 , 152 , 155 , 157 , 160 , 163 , 165 , 168 , 170 , 173 , 175 , 178 , 180 , 183], 
                                [52 , 53 , 54 , 56 , 57 , 59 , 60 , 61 , 63 , 64 , 66 , 68 , 70 , 72 , 74]])
Taille = datas[0]
Taille = (Taille,) #convert array to sequence
Poids = datas[1]
Poids = (Poids,)   #convert array to sequence

#calcule l'intervalle de confiance à 95% pour les tailles
bootstrap_Taille = bootstrap(Taille, np.median, confidence_level=0.95,
                         random_state=1, method='percentile')

#calcule l'intervalle de confiance à 80% pour les poids
bootstrap_Poids = bootstrap(Poids, np.median, confidence_level=0.80,
                         random_state=1, method='percentile')

print(bootstrap_Taille.confidence_interval)
print(bootstrap_Poids.confidence_interval)



# Un test student, SciPy permet en effet d'en réaliser. Les tests seront traités par la suite dans le cours... Les fonctions permettent aussi d'obtenir les p-values !

# In[ ]:


#Test statistique qui permet de vérifier si les variables ont la même moyenne

rvs1 = stats.norm.rvs(loc=5, scale=10, size=500, random_state=rng)
rvs2 = stats.norm.rvs(loc=5, scale=10, size=500, random_state=rng)
stats.ttest_ind(rvs1, rvs2) #test student


# ### Matplotlib
# 
# Matplotlib est un module de dataviz très plaisant : c’est en effet lui qui te permet, en une ligne de code, de créer des graphiques qui modélisent les données sur lesquelles tu travailles. Matplotlib s’utilise en synergie avec Numpy ou Pandas.
# 
# Matplotlib offre une large variété de types de graphes qui s’adaptent à tous les besoins : histogrammes, boîtes à moustache, courbes, scatter plots, camemberts…
# 
# De la même manière que scipy.stats pour scipy, **matplotlib.pyplot** est un sous-module de Matplotlib pour générer des graphes comme avec Matlab.

# In[1]:


import matplotlib.pyplot as plt 


# In[ ]:


x = np.array([1, 2, 3, 4])
y = np.array([1, 4, 9, 16])
plt.plot(x,y)


# Quelques autres exemples... Il est aussi possible de changer le style des graphiques de manière très complète

# In[ ]:



# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


# Un exemple d'histogramme:

# In[62]:


mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()


# ### Recherches sur les librairies avec help
# 
# Vous pouvez directement rechercher des informations sur les librairies ou une fonctionnalité particulière d'une librairie grâce à la fonction **help()** ou en cliquant sur le bouton **Help** dans la barre d'outils et sélectionner "NumPy Reference" par exemple.
# 
# Cette seconde solution est recommandée car elle permet de trouver une fonction en particulier rapidement.
# Par exemple, vous souhaitez faire un boxplot mais vous n'avez aucune idée comment faire. Vous supposez que la librairie Pandas pourrait bien vous aider. 
# - Cliquez sur **Help** dans la barre d'outils, puis "pandas reference" ce qui permet d'ouvir la documentation de Pandas dans un nouvel onglet. 
# - Cliquez ensuite sur "User guide" et assurez-vous de fermer la fenêtre sur le côté gauche ("File Browser") pour aperçevoir toute la documentation.
# - Sur le côté gauche, vous pouvez voir une table des matières pour naviguer facilement et rapidement dans la documentation. Sur le côté droit, vous pouvez voir une liste des points abordés dans la page sur laquelle vous êtes (qui est au milieu de votre écran).
# - Dans notre cas du boxplot: allons sur "Chart visualization" dans la table des matières à gauche, puis sélectionnez "Other plots" dans la liste des points abordés à droite de l'écran, puis "Box plots". Vous trouverez une documentation détaillée pour créer un boxplot en python avec plusieurs exemples.
# 
# Vous pouvez faire de même avec n'importe quelle librairie en sélectionnant la librairie de votre choix depuis le **Help** de la barre d'outils.
# 
# Comme mentionné précédemment, vous pouvez aussi accéder à la documentation d'une librairie depuis une cellule code directement avec la commande help(nom_de_la_librairie). A noter que cette alternative ne permet pas de naviguer dans la documentation aussi facilement.
# Attention, pour se faire, il faut que la librairie en question ait été importée au préalable. Voir ci-dessous les exemples en utilisant le **help** dans une cellule de code. 
# 
# NB: Si vous utilisez **noto**, mettez les commandes du help() en commentaire par la suite (en ajoutant # devant) et exécutez de nouveau la cellule. Cela permet de réduire la taille du notebook qui est devenu très grande à cause de la documentation téléchargée. 

# In[1]:


#help(np)  # et pas help(numpy) car on avait définit "numpy as np" pendant l'importation.


# In[3]:


#help(plt)

