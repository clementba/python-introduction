# Cours d'Introduction à Python

Exercices pratiques et concepts fondamentaux

---

# Plan du cours

- **Chapitre 1** : Les bases de Python
  - Hello World et affichage
  - Opérations arithmétiques
  - Manipulation de chaînes
- **Chapitre 2** : Concepts avancés
  - À développer selon les exercices

---

# Chapitre 1 : Les bases de Python

## Objectifs d'apprentissage
- Comprendre la syntaxe de base de Python
- Maîtriser les fonctions print() et les opérations simples
- Manipuler les chaînes de caractères

---

# Exercice 1 : Hello World

```python
def hello():
    """
    Cette fonction affiche "Bonjour le monde!" à la console.
    """
    print("Bonjour le monde!")
```

**Concepts clés :**
- Définition de fonction avec `def`
- Docstrings pour documenter le code
- Fonction `print()` pour l'affichage

---

# Exercice 2 : Addition

```python
def addition(a, b):
    """
    Cette fonction prend deux nombres en entrée et retourne leur somme.
    """
    return a + b
```

**Concepts clés :**
- Paramètres de fonction
- Instruction `return`
- Opérateurs arithmétiques

---

# Exercice 3 : Inversion de chaîne

```python
def reverse_string(s):
    """
    Cette fonction prend une chaîne en entrée et retourne la chaîne inversée.
    """
    return s[::-1]
```

**Concepts clés :**
- Manipulation de chaînes
- Slicing avec `[::-1]`
- Types de données string

---

# Tests avec pytest

## Pourquoi tester ?
- Vérifier que le code fonctionne correctement
- Détecter les régressions
- Documenter le comportement attendu

## Exemple de test
```python
def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0
```

---

# Progression actuelle

- **Chapter 1** : 66% (2/3 exercices réussis)
- **Chapter 2** : 0% (0/1 exercices réussis)

## Prochaines étapes
- Compléter l'exercice Hello World
- Aborder les concepts du Chapitre 2

---

# Questions ?

Merci pour votre attention !

**Ressources :**
- Documentation Python : https://docs.python.org/
- Pytest : https://pytest.org/
- Repository GitHub du cours