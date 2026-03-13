# Guide Utilisateur — OpenInventory v1.1.0

---

## Connexion

Au lancement, une fenêtre de connexion s'affiche.

| Champ | Description |
|---|---|
| Utilisateur | Votre nom d'utilisateur |
| Mot de passe | Votre mot de passe |

Appuyez sur **Connexion** ou sur la touche **Entrée** pour vous connecter.

**Comptes par défaut :**

| Utilisateur | Mot de passe | Accès |
|---|---|---|
| admin | admin | Complet |
| viewer | viewer | Lecture seule |

> ⚠️ Changez le mot de passe `admin` dès la première connexion via l'onglet **Utilisateurs**.

Pour vous déconnecter : **Fichier → Déconnexion**

---

## Tableau de bord (📊)

Le tableau de bord est le premier onglet affiché après la connexion.

### Cartes de statistiques
| Carte | Description |
|---|---|
| Produits | Nombre total de produits enregistrés |
| Stock total | Somme de toutes les quantités en stock |
| Valeur stock | Valeur totale du stock (prix × quantité) |
| Alertes | Nombre de produits sous leur seuil d'alerte |
| CA total | Chiffre d'affaires total toutes ventes confondues |

### Graphiques
- **Stock actuel** : barres horizontales par produit. Rouge = en alerte, Vert = OK
- **Ventes récentes** : barres des 7 derniers jours de ventes
- **Top 5 ventes** : camembert des 5 produits les plus vendus en quantité

Cliquez sur **Rafraîchir** pour mettre à jour les données et les graphiques.

---

## Produits (📦)

### Ajouter un produit
1. Cliquez sur **Ajouter**
2. Remplissez les champs : Nom, Catégorie, Prix, Quantité, Fournisseur, Seuil d'alerte
3. Cliquez sur **Enregistrer**

### Modifier un produit
1. Sélectionnez un produit dans la liste
2. Cliquez sur **Modifier**
3. Mettez à jour les champs souhaités
4. Cliquez sur **Enregistrer**

### Supprimer un produit
1. Sélectionnez un produit
2. Cliquez sur **Supprimer**
3. Confirmez la suppression

### Rechercher un produit
Tapez un mot-clé dans le champ de recherche. La liste se filtre automatiquement.

### Alertes de stock
Les produits dont la quantité est inférieure ou égale au seuil d'alerte apparaissent en **rouge**.

---

## Ventes (💰)

### Enregistrer une vente
1. Cliquez sur **Ajouter une vente**
2. Sélectionnez le produit
3. Indiquez la quantité vendue
4. Cliquez sur **Enregistrer**

Le stock du produit est automatiquement mis à jour.

### Historique
La liste affiche toutes les ventes avec la date, le produit, la quantité, le prix unitaire et le total.

---

## Rapports (📋)

L'onglet Rapports affiche un récapitulatif des ventes.

### Export Excel
Cliquez sur **Exporter en Excel** pour générer un fichier `.xlsx` dans le dossier `exports/`.

### Export PDF
Via le menu **Fichier** :
- **Export PDF Inventaire** → génère `exports/inventaire.pdf`
- **Export PDF Ventes** → génère `exports/ventes.pdf`

---

## Fournisseurs (🏭)

### Ajouter un fournisseur
1. Cliquez sur **Ajouter**
2. Remplissez : Nom, Contact, Email, Téléphone
3. Cliquez sur **Enregistrer**

### Modifier / Supprimer
Sélectionnez un fournisseur dans la liste puis cliquez sur **Modifier** ou **Supprimer**.

---

## Utilisateurs (👥) — Admin uniquement

Cet onglet n'est visible que pour les utilisateurs avec le rôle `admin`.

### Ajouter un utilisateur
1. Remplissez le nom d'utilisateur et le mot de passe
2. Sélectionnez le rôle : `admin` ou `readonly`
3. Cliquez sur **Ajouter**

### Supprimer un utilisateur
1. Sélectionnez un utilisateur dans la liste
2. Cliquez sur **Supprimer**
3. Confirmez la suppression

> L'utilisateur `admin` ne peut pas être supprimé.

---

## Thème sombre

Via le menu **Affichage → Basculer thème sombre/clair**, vous pouvez passer de l'interface claire à l'interface sombre et inversement.

---

## Raccourcis clavier

| Raccourci | Action |
|---|---|
| Entrée (sur login) | Connexion |

---

## Sauvegarde

Les données sont sauvegardées automatiquement à chaque modification dans le dossier `data/` :
- `data/products.json`
- `data/sales.json`
- `data/suppliers.json`
- `data/users.json`

Pour sauvegarder manuellement, copiez le dossier `data/` vers un emplacement sûr.

---

## FAQ

**Q : J'ai oublié mon mot de passe admin.**
R : Supprimez le fichier `data/users.json`. Les comptes par défaut (`admin`/`admin` et `viewer`/`viewer`) seront recréés au prochain lancement.

**Q : Le mode lecture seule m'empêche de modifier des données.**
R : C'est normal. Contactez votre administrateur pour obtenir un compte `admin`.

**Q : Les accents ne s'affichent pas dans les PDF.**
R : C'est une limitation connue de la police Helvetica dans `fpdf2`. Une correction est prévue en v1.2.0.

**Q : Où sont sauvegardés les exports ?**
R : Dans le dossier `exports/` à la racine du projet, créé automatiquement.

**Q : Le thème sombre ne s'applique pas à tous les éléments.**
R : C'est une limitation connue de tkinter pour certains widgets `ttk`. Une amélioration est prévue en v1.2.0.