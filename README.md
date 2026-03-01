# OpenInventory

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-1.0.0-orange)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)

> Application de gestion des stocks pour petites entreprises — Interface graphique Tkinter, persistance JSON, export Excel.

---

## Fonctionnalités

### Gestion des produits
- Ajouter, modifier, supprimer un produit (nom, référence unique, quantité, prix, catégorie)
- Afficher et trier par catégorie ou quantité
- Rechercher par nom ou référence

### Suivi des ventes
- Enregistrer une vente avec mise à jour automatique du stock
- Rapport des ventes : produits les plus vendus, chiffre d'affaires total

### Rapports et statistiques
- Produits les plus/moins en stock
- Ventes par période
- Chiffre d'affaires par catégorie

### Persistance
- Sauvegarde automatique en JSON après chaque opération
- Import / Export Excel (`.xlsx`) via `openpyxl`

### Alertes
- Notification automatique lorsque le stock d'un produit passe sous le seuil (≤ 5)

### Gestion des fournisseurs
- Ajouter, modifier, supprimer un fournisseur (nom, contact, produits fournis)

---

## Prérequis

- Python 3.10+
- `openpyxl`

```bash
pip install openpyxl
```

---

## Installation

```bash
git clone https://github.com/astro-sensei/OpenInventory.git
cd OpenInventory
pip install openpyxl
python main.py
```

---

## Structure du projet

```
OpenInventory/
├── main.py
├── models.py
├── storage.py
├── data/
│   ├── products.json
│   ├── sales.json
│   └── suppliers.json
└── gui/
    ├── app.py
    ├── products_tab.py
    ├── sales_tab.py
    ├── reports_tab.py
    ├── suppliers_tab.py
    └── dialogs.py
```

---

## Démarrage rapide

1. Lancer l'application : `python main.py`
2. Onglet **Produits** → Ajouter vos produits
3. Onglet **Ventes** → Enregistrer une vente
4. Onglet **Rapports** → Visualiser les statistiques
5. Onglet **Fournisseurs** → Gérer vos fournisseurs

---

## Licence

Distribué sous licence MIT. Voir [LICENSE](LICENSE) pour plus d'informations.
