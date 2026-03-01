# Changelog — OpenInventory

Tous les changements notables sont documentés ici.
Format basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/).

---

## [1.0.0] — 2026-01-01

### Ajouté
- Interface graphique complète avec Tkinter (4 onglets)
- Gestion des produits : ajout, modification, suppression, recherche, tri
- Suivi des ventes avec mise à jour automatique du stock
- Rapports : stock, ventes par période, CA par catégorie
- Gestion des fournisseurs : ajout, modification, suppression
- Persistance automatique en JSON (products, sales, suppliers)
- Import / Export Excel (`.xlsx`) via `openpyxl`
- Système d'alerte pour stock faible (seuil configurable, défaut ≤ 5)
- Gestion des erreurs : références dupliquées, stock insuffisant, champs invalides

### Technique
- Architecture en couches : GUI / Storage / Models
- Utilisation des `dataclasses` Python pour les modèles
- Chargement des données au démarrage de l'application

---

## [Unreleased]

### Prévu pour v1.1.0
- Tableau de bord avec graphiques (matplotlib)
- Système de rôles utilisateurs (admin / lecture seule)
- Export PDF des rapports
- Thème sombre
