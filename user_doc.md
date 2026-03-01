# Guide Utilisateur — OpenInventory v1.0.0

## Lancement de l'application

```bash
python main.py
```

La fenêtre principale s'ouvre avec quatre onglets : **Produits**, **Ventes**, **Rapports**, **Fournisseurs**.

---

## Onglet Produits

### Ajouter un produit

1. Cliquer sur **Ajouter**
2. Remplir les champs :
   - **Nom** : nom du produit (ex. : Café Arabica)
   - **Référence** : identifiant unique (ex. : CAF001)
   - **Quantité** : nombre entier ≥ 0
   - **Prix unitaire** : nombre décimal (ex. : 8.50)
   - **Catégorie** : choisir dans la liste ou saisir librement
3. Cliquer sur **Valider**

> ⚠️ La référence doit être unique. Un message d'erreur s'affiche si elle est déjà utilisée.

### Modifier un produit

1. Sélectionner un produit dans la liste
2. Cliquer sur **Modifier**
3. Mettre à jour les champs souhaités
4. Cliquer sur **Valider**

### Supprimer un produit

1. Sélectionner un produit dans la liste
2. Cliquer sur **Supprimer**
3. Confirmer la suppression

### Rechercher un produit

- Saisir un nom ou une référence dans la barre de recherche
- La liste se filtre automatiquement

### Trier la liste

- Utiliser le menu déroulant **Trier par** : par catégorie ou par quantité

### Importer / Exporter Excel

- **Exporter** : crée un fichier `.xlsx` avec trois feuilles (Produits, Ventes, Fournisseurs)
- **Importer** : charge la feuille "Produits" d'un fichier `.xlsx` existant

---

## Onglet Ventes

### Enregistrer une vente

1. Sélectionner le produit dans la liste déroulante
2. Saisir la quantité vendue
3. Vérifier ou modifier la date (format `YYYY-MM-DD`)
4. Cliquer sur **Enregistrer la vente**

> ⚠️ Si la quantité demandée dépasse le stock disponible, une erreur s'affiche et la vente est annulée.

### Alerte stock faible

Après chaque vente, si le stock restant est ≤ 5, un avertissement s'affiche automatiquement :

```
⚠️ Stock faible : Café Arabica (CAF001) — 3 unités restantes
```

---

## Onglet Rapports

### Rapport de stock

- **Produits les plus en stock** : liste triée par quantité décroissante
- **Produits les moins en stock** : liste triée par quantité croissante

### Rapport des ventes

- Chiffre d'affaires total
- Produits les plus vendus (quantité cumulée)
- Filtrage par période : saisir une date de début et une date de fin (`YYYY-MM-DD`)

### Chiffre d'affaires par catégorie

- Tableau récapitulatif du CA généré par chaque catégorie de produit

---

## Onglet Fournisseurs

### Ajouter un fournisseur

1. Cliquer sur **Ajouter**
2. Remplir :
   - **Nom** : nom du fournisseur
   - **Contact** : email ou téléphone
   - **Produits fournis** : références séparées par des virgules (ex. : CAF001, THE002)
3. Cliquer sur **Valider**

### Modifier / Supprimer un fournisseur

- Sélectionner le fournisseur dans la liste
- Cliquer sur **Modifier** ou **Supprimer**

---

## Persistance des données

Les données sont sauvegardées automatiquement dans le dossier `data/` :

| Fichier | Contenu |
|---|---|
| `data/products.json` | Liste des produits |
| `data/sales.json` | Historique des ventes |
| `data/suppliers.json` | Liste des fournisseurs |

> ✅ Les données sont rechargées automatiquement à chaque démarrage.

---

## FAQ

**Q : J'ai supprimé un produit par erreur, comment le récupérer ?**
R : Les fichiers JSON sont dans `data/`. Si vous avez un backup, remplacez le fichier `products.json`.

**Q : L'import Excel ne fonctionne pas.**
R : Vérifiez que la première feuille du fichier s'appelle exactement **Produits** et que les colonnes sont dans l'ordre : Nom, Référence, Quantité, Prix unitaire, Catégorie.

**Q : Comment changer le seuil d'alerte de stock faible ?**
R : Modifier la valeur `low_stock_threshold` dans `storage.py`, ligne du constructeur `Storage.__init__`.
