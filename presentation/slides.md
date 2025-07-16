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
  background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 50%, #e2e8f0 100%);
}

.title-slide {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  position: relative;
  padding: 2rem;
  background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
}

.logo-container {
  position: absolute;
  top: 3rem;
  right: 3rem;
  z-index: 10;
  background: white;
  padding: 1rem;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

.logo-container img {
  height: 100px;
  width: auto;
  object-fit: contain;
}

.main-title {
  font-size: 4rem;
  font-weight: 700;
  background: linear-gradient(135deg, #1e40af 0%, #3b82f6 50%, #60a5fa 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 1rem;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

.subtitle {
  font-size: 1.8rem;
  font-weight: 500;
  color: #334155;
  margin-bottom: 2rem;
  text-shadow: 0 1px 2px rgba(0,0,0,0.05);
}

.instructor-name {
  font-size: 1.6rem;
  font-weight: 400;
  color: #475569;
  margin-bottom: 3rem;
  padding: 0.8rem 2rem;
  background: rgba(59, 130, 246, 0.05);
  border-radius: 50px;
  border: 1px solid rgba(59, 130, 246, 0.1);
}

.date-footer {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  font-size: 1.2rem;
  color: #64748b;
  font-weight: 500;
  background: white;
  padding: 0.8rem 2rem;
  border-radius: 25px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

.accent-line {
  width: 120px;
  height: 5px;
  background: linear-gradient(90deg, #3b82f6 0%, #1d4ed8 50%, #1e40af 100%);
  margin: 1rem auto;
  border-radius: 3px;
  box-shadow: 0 2px 8px rgba(59, 130, 246, 0.3);
}

.school-badge {
  position: absolute;
  top: 3rem;
  left: 3rem;
  background: linear-gradient(135deg, #1e40af 0%, #3b82f6 100%);
  color: white;
  padding: 0.8rem 1.5rem;
  border-radius: 25px;
  font-size: 0.9rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  box-shadow: 0 4px 15px rgba(30, 64, 175, 0.3);
}
</style>

<div class="title-slide">
  <div class="school-badge">
    Campus du Numérique
  </div>
  
  <div class="logo-container">
    <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjAwIiBoZWlnaHQ9IjgwIiB2aWV3Qm94PSIwIDAgMjAwIDgwIiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8ZGVmcz4KPHN0eWxlPgouaXNpdGVjaC1sb2dvIHsKICBmb250LWZhbWlseTogJ0FyaWFsJywgc2Fucy1zZXJpZjsKICBmb250LXdlaWdodDogYm9sZDsKfQo8L3N0eWxlPgo8L2RlZnM+CjxyZWN0IHdpZHRoPSIyMDAiIGhlaWdodD0iODAiIGZpbGw9IndoaXRlIi8+CjxjaXJjbGUgY3g9IjI1IiBjeT0iMjUiIHI9IjE1IiBmaWxsPSIjMzMzIiBvcGFjaXR5PSIwLjEiLz4KPGV0ZXh0IHg9IjUwIiB5PSIzNSIgZmlsbD0iIzMzNzNkYyIgZm9udC1zaXplPSIyOCIgZm9udC13ZWlnaHQ9ImJvbGQiIGNsYXNzPSJpc2l0ZWNoLWxvZ28iPmlzaXRlY2g8L3RleHQ+Cjx0ZXh0IHg9IjUwIiB5PSI1NSIgZmlsbD0iIzY2NiIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9Im5vcm1hbCI+Q0FNUFVTIERVIG5VTcOJUklRVUU8L3RleHQ+Cjwvc3ZnPgo=" alt="Logo Isitech" />
  </div>
  
  <div class="main-content">
    <h1 class="main-title">FORMATION PYTHON</h1>
    <div class="accent-line"></div>
    <p class="subtitle">Introduction à la Programmation</p>
    <p class="instructor-name">👨‍💻 Nom de l'Intervenant</p>
  </div>
  
  <div class="date-footer">
    📅 {{ new Date().toLocaleDateString('fr-FR', { 
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