# Changelog

Toutes les modifications notables de ce projet sont documentées dans ce fichier.
Format basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).
Ce projet suit la [gestion sémantique de version](https://semver.org/lang/fr/).

---

## [Unreleased]

### Prévu pour v1.2.0
- Import CSV de produits
- Historique des prix
- Filtres avancés sur les Treeview
- Pagination des listes
- Graphiques intégrés dans les exports PDF
- Expiration automatique de session

---

## [1.1.0] — 2026-03-09

### Ajouté
- Tableau de bord avec 5 cartes de statistiques (produits, stock, valeur, alertes, CA)
- Graphique en barres du stock actuel avec coloration des alertes
- Graphique des ventes des 7 derniers jours
- Camembert du Top 5 des produits vendus
- Écran de connexion au lancement
- Système de rôles : `admin` (accès complet) et `readonly` (lecture seule)
- Onglet "Utilisateurs" pour la gestion des comptes (admin uniquement)
- Désactivation des contrôles de modification en mode lecture seule
- Stockage des mots de passe hashés en SHA-256 dans `data/users.json`
- Export PDF de l'inventaire via le menu Fichier
- Export PDF des ventes avec total général via le menu Fichier
- Dossier `exports/` créé automatiquement
- Thème sombre/clair basculable via le menu Affichage
- Menu "Fichier" avec déconnexion et export PDF
- Menu "Affichage" avec basculement de thème
- Nouveau fichier `user_manager.py`
- Nouveaux fichiers `gui/login_window.py`, `gui/dashboard_tab.py`, `gui/users_tab.py`, `gui/theme.py`, `gui/pdf_export.py`

### Modifié
- `gui/app.py` entièrement réécrit pour intégrer les nouvelles fonctionnalités
- `requirements.txt` mis à jour avec `matplotlib>=3.7.0` et `fpdf2>=2.7.0`

---

## [1.0.0] — 2026-01-01

### Ajouté
- Gestion des produits : ajout, modification, suppression, recherche
- Alertes de stock : mise en évidence visuelle des produits sous le seuil
- Gestion des ventes : enregistrement, historique
- Rapports : récapitulatif des ventes avec export Excel (openpyxl)
- Gestion des fournisseurs
- Persistance des données en JSON (`data/products.json`, `data/sales.json`, `data/suppliers.json`)
- Interface graphique Tkinter avec onglets (ttk.Notebook)
- Dialogs de création/modification via `gui/dialogs.py`
- Module `storage.py` pour la couche d'accès aux données
- Module `models.py` pour les dataclasses (`Product`, `Sale`, `Supplier`)