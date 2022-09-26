# Introduction

La plupart du temps, le but de la statistique est de **comprendre le hasard** qui est intrinsèquement lié à certaines expériences.  

Dans ce but, il s'avère utile de postuler un modèle caractérisé par un nombre restreints de paramètres.  

La tâche initiale de se résume donc après cette seconde étape à estimer les paramètres en questions.


Une des trois questions clés de la statistique concerne l'estimation d'un paramètre inconnu $\theta $ d'un modèle.
- modèle statistique, échantillon;        
- statistique, estimateur;
- distribution d'une statistique;
- comprendre l'approche conceptuelle: données aléatoires, donc estimateurs aléatoires;
- méthodes d'estimation: méthode des moments, moindres carrés, maximum de vraisemblance;
- biais, variance, erreur quadratique moyenne.

**Le problème**: on aimerait étudier un ensemble d'individus (la **population**) à partir d'un sous-ensemble (**l'échantillon**).
- **Modèle statistique**: Une loi de probabilité $ F_\theta$ connue sauf pour quelques paramètres $ \theta \in \Theta $, qui la caractérisent complètement.
- **Échantillon**: Supposé IID selon la loi $ F_\theta $:
\begin{gather*} X_i \stackrel{idd}{\sim} F_\theta \end{gather*}
- **statistique**: toute fonction des variables aléatoires $ X_1 \dots X_n $.
- **estimateur**: une statistique qui permet d'estimer (d'approximer) les paramètres.

```{admonition} Notations
On fait la différence entre les observations $x_1,\dots, x_n$ et les variables aléatoires $X_1, \dots,X_n$
qui modélisent les observations. Notez que
-  $x_1,\dots, x_n$ ne sont pas aléatoires;
- $X_1, \dots,X_n$ sont aléatoires; 
\begin{equation*} \begin{array}{l l}
            T = h(X_1, \dots, X_n) & \textbf{Statistique} \text{ (Variable aléatoire), } \\
            t = h(x_1, \dots, x_n) & \textbf{Réalisation} \text{ de T,} \\
            \hat{\theta}           & \textbf{Estimateur}  \text{ d'un paramètre $\theta$.} 
\end{array}, \end{equation*}
pour une certaine fonction $h$. Très souvent, on ne mentionne même plus les observations, mais uniquement les variables aléatoires qui les modélisent.
```

```{admonition} Commentaire et rappels
- Nous avons vu précédemment que $ \overline{X} $ est un estimateur de $ \mu $, la moyenne de la distribution commune.
- Une statistique est une fonction des données. Les données étant aléatoires **une statistique est une variable aléatoire !**
- La loi de $T$ dépend de la loi des $ X_i $. On l'appelle **distribution de $T$**.
- Parfois, on se contente de caractériser la moyenne et variance de $ T $ car la distribution exacte est trop complexe (n'a pas de forme close). Dans ces cas, on utilise des approximations, en appliquant le TCL.
```

```{prf:example} Distribution de la moyenne
:label: ex_dist_moyenne
Alice veut déterminer empiriquement la moyenne d'un lancer d'un dé.
                Pour cela, elle se propose de lancer $ n = 10 $ fois le dé, et d'enregistrer la valeur moyenne obtenue dans ces 10 lancers.
        
Bob décide de faire la même procédure avec le même dé.

Les moyennes obtenues par Alice et Bob sont des **variables aléatoires** car leurs lancers sont aléatoires. Elles vont être centrées sur la vraie valeur, et environ Gaussiennes (TCL).
        
Si on répétait un grand nombre de fois la procédure: « Lancer 10 fois le dé et calculer la moyenne empirique $ \overline{X} $», on pourrait calculer l'histogramme et voir qu'il est approximativement Gaussien.
```

Une fois qu'on a proposé un modèle, on peut répondre à différentes questions.
- **Estimation**: essayer de deviner la valeur de $ \theta $.
- **Tests**: on s'attend à avoir $\theta = \theta_0 $. Est ce que cette valeur est raisonnable compte tenu des observations?
- **Prédictions**: quelles sont les valeurs de $ X $ dans le reste de la population?
