# TP1 : Attaques sur les mots de passe
## Mise en oeuvre d'un script de cassage par force brute et dictionnaire

## Classe : B3B
## Elèves : Emma Durand **[@emmadrd912](https://github.com/emmadrd912)** et Pierre Ceberio **[@PierreYnov](https://github.com/PierreYnov)** 

![](https://www.malekal.com/wp-content/uploads/bruteforce-attack-logo-1.jpg)

# Sommaire 

- [Le lab](#le-lab)
- [Étude du contenu du fichier shadow]()
    - [I. Rappels théoriques]()
- [Mise en oeuvre d'un script d'attaque par force brute]()
    - [I. Rappels théoriques]()
    - [II. Mise en oeuvre du script]()
- [Mise en oeuvre d'un script d'attaque par dictionnaire]()
    - [I. Rappels théoriques]()
    - [II. Mise en oeuvre du script]()

## Le Lab

Lab : fichier shadow à casser

caracteristique du MDP :

- francais en minuscule
- francais en majuscule
- chiffre entre 0 et 9
- ; @ _ #


## Étude du contenu du fichier shadow 

### I. Rappels théoriques 

 Expliquer la structure du fichier shadow

 Quel est l'algo utilisé pour générer les empreinte de mdp dans le shadow

## Mise en oeuvre d'un script d'attaque par force brute 

### I. Rappels théoriques 

Qu'est-ce qu'une attaque par bruteforce ou recherche exhaustive ?

### II. Mise en oeuvre du script 

Ecrire un script py qui fera du bruteforce sur les empreinte du shadow


    lecture fichier ligne par ligne

    retrouver le mdp en attaque par bruteforce

    stocker les mdp bon dans un autre fichier, avec le temps de découverte pour chaque


Tout les mdp ont-ils été trouvé ?

## Mise en oeuvre d'un script d'attaque par dictionnaire 

### I. Rappels théoriques 

Qu'est-ce qu'une attaque par dictionnaire 

### II. Mise en oeuvre du script 

ecrire un script py qui fais de l'attaque par dico sur les empreinte grace aux dico

    lire fichier ligne par ligne

    tester chaque occurence de mot contenu dans le dictionnaire

    stocker les mdp das un fichier de sortie avec le temps de découverte pour chaque

tout les mdp ont il été trouvé ?



Expliquez les avantages et inconveniens de chacune des deux methodes