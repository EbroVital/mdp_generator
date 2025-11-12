# 🔐 Générateur de Mot de Passe

Un générateur de mots de passe sécurisés avec interface graphique, développé en Python avec Tkinter.

![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 📋 Description

Cette application permet de générer des mots de passe aléatoires et sécurisés selon vos critères. Vous pouvez personnaliser la longueur et les types de caractères inclus dans votre mot de passe.

## ✨ Fonctionnalités

- 🎯 **Génération personnalisable** : Choisissez la longueur de votre mot de passe
- 🔤 **Options de caractères** :
  - Lettres (majuscules et minuscules)
  - Chiffres (0-9)
  - Caractères spéciaux (!@#$%^&*...)
- 📋 **Copie en un clic** : Copiez facilement le mot de passe généré dans le presse-papier
- ✅ **Validation des entrées** : Messages d'erreur clairs en cas de saisie invalide
- 🎨 **Interface intuitive** : Design simple et épuré

## 🚀 Installation

### Prérequis

- Python 3.6 ou supérieur
- Tkinter (généralement inclus avec Python)

### Vérifier l'installation de Tkinter

```bash
python -m tkinter
```

Si une petite fenêtre s'ouvre, Tkinter est installé. Sinon :

**Sur Ubuntu/Debian :**
```bash
sudo apt-get install python3-tk
```

**Sur Fedora :**
```bash
sudo dnf install python3-tkinter
```

**Sur macOS et Windows :** Tkinter est généralement préinstallé avec Python.

## 💻 Utilisation

### Lancer l'application

```bash
python mdp.py
```

### Étapes d'utilisation

1. **Définir la longueur** : Entrez le nombre de caractères souhaité (par défaut : 12)
2. **Choisir les types de caractères** : Cochez/décochez les options selon vos besoins
3. **Générer** : Cliquez sur "Générer le mot de passe"
4. **Copier** : Cliquez sur "Copier le mot de passe" pour le mettre dans le presse-papier

## 🔧 Technologies utilisées

- **Python 3** : Langage de programmation
- **Tkinter** : Bibliothèque pour l'interface graphique
- **random** : Module pour la génération aléatoire
- **string** : Module pour les constantes de caractères

## 📚 Concepts abordés

Ce projet est parfait pour apprendre :

- 🎨 **Programmation GUI** avec Tkinter
- 🏗️ **Programmation Orientée Objet** (POO)
- 🎲 **Génération aléatoire** avec le module random
- ✅ **Gestion des erreurs** avec try/except
- 📋 **Manipulation du presse-papier**
- 🔘 **Gestion des événements** (clics, saisies)

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 💡 Améliorations futures

Idées pour étendre le projet :

- [ ] Ajouter un indicateur de force du mot de passe
- [ ] Sauvegarder l'historique des mots de passe générés (chiffrés)
- [ ] Ajouter un mode "mot de passe prononçable"
- [ ] Thème sombre/clair
- [ ] Exporter les mots de passe dans un fichier
- [ ] Vérifier si le mot de passe a été compromis (API HaveIBeenPwned)

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 🌟 Remerciements

- Merci à la communauté Python
- Documentation officielle de [Tkinter](https://docs.python.org/3/library/tkinter.html)

---

⭐ Si ce projet vous a été utile, n'hésitez pas à lui donner une étoile !

**Fait avec ❤️ et Python**
