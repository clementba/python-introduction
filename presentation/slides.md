---
theme: seriph
background: https://images.unsplash.com/photo-1526379095098-d400fd0bf935?ixlib=rb-4.0.3&auto=format&fit=crop&w=2832&q=80
title: Introduction à Python
info: |
  ## Cours d'Introduction à Python
  Apprendre les bases de la programmation Python avec des exercices pratiques.
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
---

# Introduction à Python

## Apprendre les bases de la programmation

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover:bg="white hover:bg-opacity-10">
    Commencer le cours <carbon:arrow-right class="inline"/>
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <a href="https://github.com/python/cpython" target="_blank" alt="Python" title="Python"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-python />
  </a>
</div>

---
transition: fade-out
---

# Qu'est-ce que Python ?

Python est un langage de programmation **puissant** et **facile à apprendre**

<v-clicks>

- 🐍 **Syntaxe simple** - Code lisible et expressif
- 🚀 **Polyvalent** - Web, data science, IA, automatisation
- 📚 **Riche écosystème** - Milliers de bibliothèques disponibles
- 🌍 **Communauté active** - Support et ressources abondantes
- 💼 **Très demandé** - Langage populaire dans l'industrie

</v-clicks>

<br>
<br>

<v-click>

> "Python est un langage de programmation qui vous permet de travailler rapidement et d'intégrer des systèmes plus efficacement."

</v-click>

---
layout: two-cols
---

# Plan du cours

<Toc minDepth="1" maxDepth="2" />

::right::

## Objectifs d'apprentissage

<v-clicks>

- ✅ Comprendre la syntaxe de base de Python
- ✅ Écrire vos premières fonctions
- ✅ Manipuler les chaînes de caractères
- ✅ Utiliser les tests avec pytest
- ✅ Développer de bonnes pratiques

</v-clicks>

<v-click>

### Prérequis
- Python 3.13+ installé
- Éditeur de code
- Terminal/ligne de commande

</v-click>

---

# Chapitre 1 : Les Fondamentaux

## Exercice 1 : Hello World

Le traditionnel premier programme en Python

```python {all|1-3|4|all}
def hello():
    """
    This function prints "Bonjour le monde!" to the console.
    """
    print("Bonjour le monde!")
```

<v-clicks>

- **Fonction** : Bloc de code réutilisable
- **Docstring** : Documentation de la fonction
- **print()** : Affiche du texte dans la console

</v-clicks>

<v-click>

### Test associé
```python
def test_hello(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Bonjour le monde!\n"
```

</v-click>

---

# Exercice 2 : Addition

Créer une fonction qui additionne deux nombres

```python {all|1|2-4|5|all}
def addition(a, b):
    """
    Cette fonction prend deux nombres en entrée et retourne leur somme.
    """
    return a + b
```

<v-clicks>

- **Paramètres** : `a` et `b` sont les entrées de la fonction
- **return** : Renvoie le résultat de l'opération
- **Opérateur +** : Addition mathématique

</v-clicks>

<v-click>

### Tests
```python
def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0
```

</v-click>

---

# Exercice 3 : Inversion de chaîne

Inverser l'ordre des caractères dans une chaîne

```python {all|1|2-4|5|all}
def reverse_string(s):
    """
    Cette fonction prend une chaîne en entrée et retourne la chaîne inversée.
    """
    return s[::-1]
```

<v-clicks>

- **Slicing** : `[::-1]` parcourt la chaîne à l'envers
- **Chaînes** : Séquences de caractères en Python
- **Indexation négative** : `-1` commence par la fin

</v-clicks>

<v-click>

### Tests
```python
def test_reverse_string():
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
```

</v-click>

---
layout: two-cols
---

# Les Tests avec pytest

## Pourquoi tester ?

<v-clicks>

- ✅ **Vérifier** que le code fonctionne
- 🐛 **Détecter** les erreurs rapidement  
- 🔄 **Refactoriser** en toute sécurité
- 📝 **Documenter** le comportement attendu

</v-clicks>

::right::

## Structure d'un test

```python
def test_ma_fonction():
    # Arrange (préparer)
    input_value = "test"
    expected = "tset"
    
    # Act (agir)
    result = reverse_string(input_value)
    
    # Assert (vérifier)
    assert result == expected
```

<v-click>

### Exécuter les tests
```bash
pytest exercises/chapter1/
```

</v-click>

---

# Progression Actuelle

<div class="grid grid-cols-2 gap-8">

<div>

## Chapter 1
<div class="progress-container">
  <div class="progress-bar">
    <div class="progress-fill" style="width: 66%"></div>
  </div>
  <span class="progress-text">66% (2/3)</span>
</div>

### Exercices
- ✅ Addition - Terminé
- ✅ Reverse String - Terminé  
- ❌ Hello World - À compléter

</div>

<div>

## Chapter 2
<div class="progress-container">
  <div class="progress-bar">
    <div class="progress-fill" style="width: 0%"></div>
  </div>
  <span class="progress-text">0% (0/1)</span>
</div>

### À venir
- 📝 Nouveaux exercices en préparation

</div>

</div>

<style>
.progress-container {
  margin: 1rem 0;
}
.progress-bar {
  width: 100%;
  height: 20px;
  background-color: #e5e7eb;
  border-radius: 10px;
  overflow: hidden;
}
.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #10b981, #059669);
  transition: width 0.3s ease;
}
.progress-text {
  font-size: 0.875rem;
  color: #6b7280;
  margin-left: 0.5rem;
}
</style>

---
layout: center
class: text-center
---

# Concepts Clés à Retenir

<div class="grid grid-cols-2 gap-8 mt-8">

<div v-click>

## 🔧 Fonctions
```python
def ma_fonction(parametre):
    """Documentation"""
    return resultat
```

</div>

<div v-click>

## 📝 Chaînes de caractères
```python
texte = "Hello"
inverse = texte[::-1]  # "olleH"
```

</div>

<div v-click>

## ✅ Tests
```python
def test_fonction():
    assert fonction(input) == expected
```

</div>

<div v-click>

## 📚 Documentation
```python
def fonction():
    """Docstring explicative"""
    pass
```

</div>

</div>

---

# Prochaines Étapes

<v-clicks>

## 1. Compléter l'exercice Hello World
```python
def hello():
    # TODO: Implémenter la fonction
    print("Bonjour le monde!")
```

## 2. Exécuter les tests
```bash
pytest exercises/chapter1/1-hello/
```

## 3. Explorer le Chapter 2
- Nouveaux défis à venir
- Concepts plus avancés

## 4. Bonnes pratiques
- Écrire du code lisible
- Tester régulièrement
- Documenter ses fonctions

</v-clicks>

---
layout: center
class: text-center
---

# Questions ?

<div class="mt-8">
  <div class="text-6xl mb-4">🐍</div>
  <div class="text-xl opacity-80">
    Prêt à coder en Python ?
  </div>
</div>

<div class="mt-12 flex justify-center gap-4">
  <a href="https://docs.python.org/3/" target="_blank" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
    Documentation Python
  </a>
  <a href="https://docs.pytest.org/" target="_blank" class="px-4 py-2 bg-green-500 text-white rounded hover:bg-green-600">
    Documentation pytest
  </a>
</div>

---
layout: end
class: text-center
---

# Merci !

Bonne programmation avec Python 🐍

<div class="mt-8 opacity-60">
  Slides créées avec ❤️ et Slidev
</div>