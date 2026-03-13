<center>
<h1 id="openinventory">OpenInventory</h1>
<p><img src="https://img.shields.io/badge/Python-3.13-blue?logo=python" alt="Python">
<img src="https://img.shields.io/badge/License-MIT-green" alt="License">
<img src="https://img.shields.io/badge/Version-1.1.0-orange" alt="Version">
<img src="https://img.shields.io/badge/Status-Stable-brightgreen" alt="Status"></p>
</center>

Logiciel de gestion d'inventaire de bureau, open-source, développé en Python avec une interface graphique Tkinter.

---

## Fonctionnalités

### v1.0.0
- 📦 Gestion des produits (ajout, modification, suppression, recherche)
- 🔴 Alertes de stock automatiques avec seuil configurable
- 💰 Enregistrement et historique des ventes
- 📋 Rapports avec export Excel
- 🏭 Gestion des fournisseurs
- 💾 Persistance des données en JSON

### v1.1.0
- 📊 Tableau de bord avec graphiques en temps réel (matplotlib)
- 👥 Système de rôles : `admin` / `readonly`
- 🔐 Écran de connexion avec mots de passe hashés (SHA-256)
- 📄 Export PDF de l'inventaire et des ventes
- 🌙 Thème sombre / clair basculable

---

## Prérequis

- Python 3.10+
- pip

---

## Installation

```bash
git clone https://github.com/astro-sensei/OpenInventory.git
cd OpenInventory
pip install -r requirements.txt
python main.py
```

---

## Démarrage rapide

1. Lancez `python main.py`
2. Connectez-vous avec `admin` / `admin`
3. Explorez le tableau de bord, ajoutez des produits et enregistrez des ventes

---

## Comptes par défaut

| Utilisateur | Mot de passe | Rôle |
|---|---|---|
| admin | admin | Administrateur (accès complet) |
| viewer | viewer | Lecture seule |

---

## Structure du projet

```
OpenInventory/
├── main.py
├── models.py
├── storage.py
├── user_manager.py
├── gui/
│   ├── __init__.py
│   ├── app.py
│   ├── dashboard_tab.py
│   ├── dialogs.py
│   ├── login_window.py
│   ├── pdf_export.py
│   ├── products_tab.py
│   ├── reports_tab.py
│   ├── sales_tab.py
│   ├── suppliers_tab.py
│   ├── theme.py
│   └── users_tab.py
├── data/
└── exports/
```

---

## Dépendances

| Bibliothèque | Usage |
|---|---|
| `openpyxl` | Export Excel |
| `matplotlib` | Graphiques du tableau de bord |
| `fpdf2` | Export PDF |

---

## Licence

MIT — voir [LICENSE](LICENSE)

---

*Dépôt : https://github.com/astro-sensei/OpenInventory*