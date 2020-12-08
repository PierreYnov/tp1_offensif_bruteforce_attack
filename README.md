# TP1 : Attaques sur les mots de passe
## Mise en oeuvre d'un script de cassage par force brute et dictionnaire

## Classe : B3B
## Elèves : Emma Durand **[@emmadrd912](https://github.com/emmadrd912)** et Pierre Ceberio **[@PierreYnov](https://github.com/PierreYnov)** 

![](https://blogvaronis2.wpengine.com/wp-content/uploads/2018/10/brute-force-attack.jpg)

# Sommaire 

- [Le lab](#le-lab)
- [Étude du contenu du fichier shadow](#%C3%A9tude-du-contenu-du-fichier-shadow)
    - [I. Rappels théoriques](#i-rappels-th%C3%A9oriques)
- [Mise en oeuvre d'un script d'attaque par force brute](#mise-en-oeuvre-dun-script-dattaque-par-force-brute)
    - [I. Rappels théoriques](#i-rappels-th%C3%A9oriques-1)
    - [II. Mise en oeuvre du script](#ii-mise-en-oeuvre-du-script)
- [Mise en oeuvre d'un script d'attaque par dictionnaire](#mise-en-oeuvre-dun-script-dattaque-par-dictionnaire)
    - [I. Rappels théoriques](#i-rappels-th%C3%A9oriques-2)
    - [II. Mise en oeuvre du script](#ii-mise-en-oeuvre-du-script-1)

## Le Lab

1 fichier shadow à casser + 1 dictionnaire

Caracteristique du MDP :

- francais en minuscule
- francais en majuscule
- chiffre entre 0 et 9
- ; @ _ #


## Étude du contenu du fichier shadow 

### I. Rappels théoriques 

**Expliquer la structure du fichier shadow**

Il contient les mots de passe hashés des utilisateurs du serveur Linux.

Voici sa structure : 

1) le nom de l'utilisateur
2) le sel et le mot de passe haché
3) La date de la dernière modification du mot de passe (exprimé en nombre de jours après le 1er janvier 1970).
4) Le nombre de jours avant le que le mot de passe puisse être changé (0 indique qu'il peut être modifié à tout moment).
5) Le nombre de jours après lesquels le mot de passe doit être changé (30 indique qu'après 30 jours l'utilisateur sera forcé de changer son mot de passe ; 99999 indique que l'utilisateur n'est jamais obligé de changer son mot de passe).
6) Le nombre de jours durant lesquelles l'utilisateur sera informé de l'expiration prochaine de son mot de passe s'il se connecte au système.
7) Le nombre de jours avant la désactivation d'un compte avec mot de passe expiré.
8) La date de la désactivation d'un compte (exprimé en nombre de jours après le 1er janvier 1970).
9) Un champ réservé pour une éventuelle utilisation future.


**Quel est l'algorithme utilisé pour générer les empreintes des mdp dans le shadow ?**

Sur ce shadow, les empreintes sont hashés en MD5.









## Mise en oeuvre d'un script d'attaque par force brute 

### I. Rappels théoriques 

**Qu'est-ce qu'une attaque par bruteforce ou recherche exhaustive ?**

Une attaque par bruteforce consiste à tester toutes les combinaisons possibles pour trouver un mot de passe.

### II. Mise en oeuvre du script 

**Ecrire un script py réalisant une attaque par bruteforce sur les empreintes du shadow**


    lecture fichier ligne par ligne

    retrouver le mdp en attaque par bruteforce

    stocker les mdp bon dans un autre fichier, avec le temps de découverte pour chaque


**Tout les mot de passe ont-ils été trouvé ?**



## Mise en oeuvre d'un script d'attaque par dictionnaire 

### I. Rappels théoriques 

**Qu'est-ce qu'une attaque par dictionnaire ?**

Une attaque par dictionnaire consiste à tester une série de mot de passe provenant d'un dictionnaire.

### II. Mise en oeuvre du script 

**Ecrire un script py réalisant une attaque par dictionnaire sur les empreintes du shadow**

    lire fichier ligne par ligne

    tester chaque occurence de mot contenu dans le dictionnaire

    stocker les mdp das un fichier de sortie avec le temps de découverte pour chaque
    
    
Vous pouvez retrouver notre script [ici](https://github.com/PierreYnov/tp1_offensif_bruteforce_attack/blob/main/script_dico.py)

**Tout les mot de passe ont-ils été trouvé ?**

Nous avons pu trouver 2 sur 3. Nous avons pas trouvé celui de ``fred``.

**Expliquez les avantages et inconveniens de chacune des deux methodes**

La méthode par dictionnaire est beaucoup plus rapide mais se révèlera inefficace si le mot de passe n'est pas contenu dans le dictionnaire.

Il faudra alors se tourner vers le brute-force, qui est beaucoup plus long, mais pourra arriver à son but si le mot de passe n'est pas trop complexe.
