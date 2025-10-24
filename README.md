# 🧪 Tests automatiques Flask avec Pytest & Couverture

<img width="1290" height="761" alt="image" src="https://github.com/user-attachments/assets/fe3f8bd1-b902-43c5-b97f-22cf873384de" />
<img width="1918" height="368" alt="image" src="https://github.com/user-attachments/assets/5132d1a0-1d8c-47d0-a1e2-9ab0b068cee1" />
<img width="902" height="852" alt="image" src="https://github.com/user-attachments/assets/19188d6d-d9d2-4de7-ae21-ce5b4842f0f7" />



## 📖 Description

Ce projet contient une suite de tests automatisés pour une application Flask.  
Il utilise **Pytest** pour l’exécution des tests et **pytest-cov** pour mesurer la couverture du code.  
Un script de configuration (`conftest.py`) permet également **d’ouvrir automatiquement les rapports HTML** générés après la fin des tests.

---

## 🧩 Structure du projet

```
.
├── conftest.py           # Configuration Pytest (client Flask + ouverture automatique des rapports)
├── Tests                 # Dossiee Tests 
├── server.py             # Application Flask (non incluse ici)
├── requirements.txt      # Dépendances du projet (optionnel)
└── htmlcov/              # Rapport HTML de couverture (généré automatiquement)
```

---

## ⚙️ Installation

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/soso92222/TDD.git
   cd ton-projet
   ```

2. **Créer un environnement virtuel**
   ```bash
   python -m venv venv
   source venv/bin/activate  # sous Windows : venv\Scripts\activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install flask pytest pytest-cov pytest-html
   ```
---

## 🚀 Exécution des tests

Lancer les tests avec la couverture et la génération d’un rapport HTML :
```bash
pytest --cov=server --cov-report=html --html=report.html
```

✅ **Fonctionnalités incluses :**
- Génération automatique du rapport Pytest (`report.html`)
- Génération automatique du rapport de couverture (`htmlcov/index.html`)
- Ouverture automatique de ces rapports dans le navigateur à la fin des tests


---

## 📊 Rapports générés

- **Rapport Pytest (résumé des tests) :** `report.html`
- **Rapport de couverture du code :** `htmlcov/index.html`

> 💡 Ces fichiers s’ouvrent automatiquement dans votre navigateur grâce à la fonction `pytest_sessionfinish` du fichier `conftest.py`.

---

## 🧰 Outils utilisés

| Outil | Description |
|--------|--------------|
| **Flask** | Framework web Python |
| **Pytest** | Framework de tests |
| **pytest-cov** | Mesure la couverture du code |
| **pytest-html** | Génère un rapport HTML détaillé |
| **webbrowser** | Ouvre automatiquement les rapports |

---

## 🧩 Auteur

**Sofiane Zaion**  
Étudiant en développement web & DevOps  
📧 [sofianezaion@outlook.fr](sofianezaion@outlook.fr)




