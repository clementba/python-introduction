---
theme: default
background: '#f8fafc'
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Formation Python - Introduction à la Programmation
  Cours d'introduction aux concepts fondamentaux de Python avec exercices pratiques.
drawings:
  persist: false
transition: slide-left
title: Formation Python - Introduction à la Programmation
mdc: true
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

.slidev-layout {
  font-family: 'Inter', 'Arial', sans-serif;
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
}

.title-slide {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  position: relative;
  padding: 2rem;
}

.logo-container {
  position: absolute;
  top: 2rem;
  right: 2rem;
  z-index: 10;
}

.logo-container img {
  height: 80px;
  width: auto;
  object-fit: contain;
}

.main-title {
  font-size: 3.5rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 1rem;
  text-shadow: 0 2px 4px rgba(0,0,0,0.1);
  line-height: 1.2;
}

.subtitle {
  font-size: 1.5rem;
  font-weight: 400;
  color: #475569;
  margin-bottom: 2rem;
}

.instructor-name {
  font-size: 1.8rem;
  font-weight: 500;
  color: #334155;
  margin-bottom: 3rem;
}

.date-footer {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  font-size: 1.1rem;
  color: #64748b;
  font-weight: 400;
}

.accent-line {
  width: 100px;
  height: 4px;
  background: linear-gradient(90deg, #3b82f6, #1d4ed8);
  margin: 1rem auto;
  border-radius: 2px;
}
</style>

<div class="title-slide">
  <div class="logo-container">
    <img src="https://images.unsplash.com/photo-1599305445671-ac291c95aaa9?w=200&h=80&fit=crop&crop=center" alt="Logo Isitech" />
  </div>
  
  <div class="main-content">
    <h1 class="main-title">FORMATION PYTHON</h1>
    <div class="accent-line"></div>
    <p class="subtitle">Introduction à la Programmation</p>
    <p class="instructor-name">Nom de l'Intervenant</p>
  </div>
  
  <div class="date-footer">
    {{ new Date().toLocaleDateString('fr-FR', { 
      year: 'numeric', 
      month: 'long', 
      day: 'numeric' 
    }) }}
  </div>
</div>

---
layout: default
---

# Plan du Cours

<div class="grid grid-cols-1 gap-6 mt-8">

## 📚 Objectifs de la Formation
- Comprendre les bases de la programmation Python
- Maîtriser les concepts fondamentaux
- Pratiquer avec des exercices concrets
- Apprendre les bonnes pratiques de développement

## 🎯 Programme
1. **Chapitre 1 : Les Fondamentaux**
   - Hello World et premiers pas
   - Opérations arithmétiques
   - Manipulation de chaînes de caractères

2. **Chapitre 2 : Concepts Avancés** *(à venir)*
   - Structures de données
   - Fonctions et modules

## 🧪 Méthodologie
- Approche pratique avec exercices
- Tests automatisés avec pytest
- Suivi de progression en temps réel

</div>

---
layout: two-cols
---

# Chapitre 1 : Les Fondamentaux

## 🎯 Exercice 1 : Hello World
**Objectif** : Afficher un message à l'écran

```python
def hello():
    """
    Cette fonction affiche "Bonjour le monde!"
    """
    print("Bonjour le monde!")
```

**Test** :
```python
def test_hello(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Bonjour le monde!\n"
```

::right::

## ✅ Exercice 2 : Addition
**Objectif** : Créer une fonction d'addition

```python
def addition(a, b):
    """
    Retourne la somme de deux nombres
    """
    return a + b
```

## ✅ Exercice 3 : Inversion de chaîne
**Objectif** : Inverser une chaîne de caractères

```python
def reverse_string(s):
    """
    Retourne la chaîne inversée
    """
    return s[::-1]
```

---
layout: center
class: text-center
---

# Tests et Validation

## 🧪 Pytest : Notre Outil de Test

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

### Pourquoi tester ?
- ✅ Vérifier que le code fonctionne
- 🐛 Détecter les erreurs rapidement  
- 🔄 Faciliter les modifications
- 📈 Améliorer la qualité du code

</div>

<div>

### Comment lancer les tests ?
```bash
# Tous les tests
pytest

# Tests d'un chapitre
pytest exercises/chapter1

# Tests avec détails
pytest -v
```

</div>

</div>

---
layout: default
---

# Progression Actuelle

<div class="mt-8">

## 📊 État d'Avancement

```
chapter1    [=============>      ] 66% (2/3)
chapter-2   [>                   ] 0% (0/1)
```

<div class="grid grid-cols-2 gap-8 mt-8">

<div>

### ✅ Exercices Réussis
- **Addition** : Fonction complète et testée
- **Inversion de chaîne** : Implémentation correcte

### 🔄 En Cours
- **Hello World** : À compléter

</div>

<div>

### 🎯 Prochaines Étapes
1. Finaliser l'exercice Hello World
2. Aborder le Chapitre 2
3. Découvrir de nouveaux concepts Python
4. Continuer la pratique avec plus d'exercices

</div>

</div>

</div>

---
layout: center
class: text-center
---

# Questions ?

<div class="mt-8">

## 💡 Ressources Utiles

- 📖 [Documentation Python Officielle](https://docs.python.org/fr/3/)
- 🧪 [Guide Pytest](https://docs.pytest.org/)
- 💻 [Exercices en ligne](https://github.com/votre-repo)

</div>

<div class="mt-12">

### Prêts à commencer ? 🚀

</div>