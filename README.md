# TP1 : Attaque sur les mots de passe
## Mise en oeuvre d'un script de cassage par force brute et dictionnaire

## Classe : B3B
## Élèves : Emma Durand **[@emmadrd912](https://github.com/emmadrd912)** et Pierre Ceberio **[@PierreYnov](https://github.com/PierreYnov)** 

![](https://blogvaronis2.wpengine.com/wp-content/uploads/2018/10/brute-force-attack.jpg)

# Sommaire 

- [Le Lab](#le-lab)
- [Étude du contenu du fichier shadow](#%C3%A9tude-du-contenu-du-fichier-shadow)
    - [I. Rappels théorique](#i-rappels-th%C3%A9orique)
- [Mise en oeuvre d'un script d'attaque par force brute](#mise-en-oeuvre-dun-script-dattaque-par-force-brute)
    - [I. Rappels théorique](#i-rappels-th%C3%A9orique-1)
    - [II. Mise en oeuvre du script](#ii-mise-en-oeuvre-du-script)
- [Mise en oeuvre d'un script d'attaque par dictionnaire](#mise-en-oeuvre-dun-script-dattaque-par-dictionnaire)
    - [I. Rappels théorique](#i-rappels-th%C3%A9orique-2)
    - [II. Mise en oeuvre du script](#ii-mise-en-oeuvre-du-script-1)

## Le Lab

1 fichier shadow à casser + 1 dictionnaire

Caractéristique du MDP :

- longueur entre 6 et 12 caractères
- français en minuscule
- français en majuscule
- chiffre entre 0 et 9
- ; @ _ #


## Étude du contenu du fichier shadow 

### I. Rappels théorique

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


**Quel est l'algorithme utilisé pour générer les empreintes des mots de passe dans le shadow ?**

Sur ce shadow, les empreintes sont hashés en MD5.

## Mise en oeuvre d'un script d'attaque par force brute 

### I. Rappels théorique 

**Qu'est-ce qu'une attaque par bruteforce ou recherche exhaustive ?**

Une attaque par bruteforce consiste à tester toutes les combinaisons possibles pour trouver un mot de passe.

### II. Mise en oeuvre du script 

**Écrire un script py réalisant une attaque par bruteforce sur les empreintes du shadow**


    lecture fichier ligne par ligne

    retrouver le mot de passe en attaque par bruteforce

    stocker les bons mots de passe  dans un autre fichier, avec le temps de découverte pour chacuns


Vous pouvez retrouver notre script [ici](https://github.com/PierreYnov/tp1_offensif_bruteforce_attack/blob/main/script_brute.py). Pour le lancer il suffit de taper ``python3 script_brute.py`` 

**Tous les mots de passe ont-ils été trouvés ?**

Nous avons trouvé rapidement celui de giselle. Les 2 autres sont en cours de bruteforce.

## Mise en oeuvre d'un script d'attaque par dictionnaire 

### I. Rappels théorique

**Qu'est-ce qu'une attaque par dictionnaire ?**

Une attaque par dictionnaire consiste à tester une série de mots de passe provenant d'un dictionnaire.

### II. Mise en oeuvre du script 

**Écrire un script py réalisant une attaque par dictionnaire sur les empreintes du shadow**

    lire fichier ligne par ligne

    tester chaque occurrence de mot contenu dans le dictionnaire

    stocker les mots de passe dans un fichier de sortie avec le temps de découverte pour chacuns
    
    
Vous pouvez retrouver notre script [ici](https://github.com/PierreYnov/tp1_offensif_bruteforce_attack/blob/main/script_dico.py). Pour le lancer il suffit de taper ``python3 script_dico.py``

**Tous les mots de passe ont-ils été trouvés ?**

Nous avons pu trouver 2 sur 3. Nous n'avons pas trouvé celui de ``fred``.

**Expliquez les avantages et inconvénients de chacune des deux méthodes**

La méthode par dictionnaire est beaucoup plus rapide, mais se révèlera inefficace si le mot de passe n'est pas contenu dans le dictionnaire.

Il faudra alors se tourner vers le brute-force, qui est beaucoup plus long, mais pourra arriver à son but si le mot de passe n'est pas trop complexe.
