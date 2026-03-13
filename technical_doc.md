# Documentation Technique — OpenInventory v1.1.0

---

## Environnement

| Élément | Valeur |
|---|---|
| Langage | Python 3.10+ |
| Interface | Tkinter + ttk |
| Graphiques | matplotlib 3.7+ |
| Export Excel | openpyxl 3.1+ |
| Export PDF | fpdf2 2.7+ |
| Persistance | JSON |

---

## Modules

### `models.py`

```python
@dataclass
class Product:
    id: int
    name: str
    category: str
    price: float
    quantity: int
    supplier: str
    alert_threshold: int

@dataclass
class Sale:
    id: int
    product_name: str
    quantity: int
    unit_price: float
    total: float
    date: str  # ISO 8601 : "YYYY-MM-DD HH:MM:SS"

@dataclass
class Supplier:
    id: int
    name: str
    contact: str
    email: str
    phone: str
```

### `storage.py`

| Méthode | Retour | Description |
|---|---|---|
| `get_products()` | `list[Product]` | Charge les produits depuis JSON |
| `save_products(products)` | `None` | Sauvegarde la liste de produits |
| `get_sales()` | `list[Sale]` | Charge les ventes depuis JSON |
| `save_sales(sales)` | `None` | Sauvegarde la liste de ventes |
| `get_suppliers()` | `list[Supplier]` | Charge les fournisseurs depuis JSON |
| `save_suppliers(suppliers)` | `None` | Sauvegarde la liste de fournisseurs |

### `user_manager.py`

| Méthode | Retour | Description |
|---|---|---|
| `authenticate(username, password)` | `bool` | Vérifie les identifiants (SHA-256) |
| `is_admin()` | `bool` | Retourne True si le rôle est `admin` |
| `add_user(username, password, role)` | `bool` | Ajoute un utilisateur |
| `delete_user(username)` | `bool` | Supprime un utilisateur (sauf `admin`) |
| `list_users()` | `list[dict]` | Liste tous les utilisateurs avec leur rôle |
| `load()` | `None` | Charge depuis `data/users.json` |
| `save()` | `None` | Sauvegarde dans `data/users.json` |

### `gui/theme.py`

| Méthode | Retour | Description |
|---|---|---|
| `get()` | `dict` | Retourne le thème actif |
| `toggle()` | `dict` | Bascule entre clair et sombre |
| `apply(widget, theme)` | `None` | Applique récursivement le thème |

Clés des dictionnaires de thème : `bg`, `fg`, `entry_bg`, `entry_fg`, `button_bg`, `button_fg`, `tree_bg`, `tree_fg`, `tree_select`

### `gui/pdf_export.py`

| Méthode | Retour | Description |
|---|---|---|
| `PDFExporter.export_inventory(products, filepath)` | `str` | Génère le PDF inventaire, retourne le chemin |
| `PDFExporter.export_sales(sales, filepath)` | `str` | Génère le PDF ventes, retourne le chemin |

Chemins par défaut : `exports/inventaire.pdf`, `exports/ventes.pdf`

### `gui/dashboard_tab.py`

| Composant | Description |
|---|---|
| Cartes KPI | 5 `tk.Frame` avec label et valeur en gras |
| Graphique stock | `barh` matplotlib, rouge si `quantity <= alert_threshold` |
| Graphique ventes | `bar` matplotlib des 7 derniers jours |
| Camembert | `pie` matplotlib du Top 5 produits vendus |
| Canvas | `FigureCanvasTkAgg` intégré dans le frame |

---

## Format des fichiers JSON

### `data/products.json`
```json
[
  {
    "id": 1,
    "name": "Produit A",
    "category": "Catégorie",
    "price": 9.99,
    "quantity": 50,
    "supplier": "Fournisseur X",
    "alert_threshold": 10
  }
]
```

### `data/sales.json`
```json
[
  {
    "id": 1,
    "product_name": "Produit A",
    "quantity": 3,
    "unit_price": 9.99,
    "total": 29.97,
    "date": "2026-01-20 14:32:00"
  }
]
```

### `data/users.json`
```json
{
  "admin": {
    "password": "<sha256>",
    "role": "admin"
  },
  "viewer": {
    "password": "<sha256>",
    "role": "readonly"
  }
}
```

---

## Format du fichier Excel (export rapports)

| Colonne | Type | Description |
|---|---|---|
| Date | string | Date de la vente |
| Produit | string | Nom du produit |
| Quantité | int | Quantité vendue |
| Prix unitaire | float | Prix unitaire |
| Total | float | Quantité × Prix unitaire |

---

## Sécurité

- Les mots de passe ne sont jamais stockés en clair
- Hash : `hashlib.sha256(password.encode()).hexdigest()`
- L'utilisateur `admin` ne peut pas être supprimé
- En mode `readonly` : tous les boutons d'écriture sont désactivés via `widget.configure(state="disabled")`

---

## Gestion des erreurs

| Situation | Comportement |
|---|---|
| JSON absent | Création automatique avec liste vide |
| `users.json` absent | Création avec comptes `admin`/`viewer` par défaut |
| Identifiants incorrects | `messagebox.showerror` dans `LoginWindow` |
| Suppression de `admin` | Retourne `False`, pas de modification |
| Export PDF échoué | `messagebox.showerror` avec message de l'exception |
| Produit en alerte | Fond rouge dans le `Treeview` de `ProductsTab` |

---

## Roadmap

| Version | Fonctionnalité |
|---|---|
| v1.2.0 | Import CSV |
| v1.2.0 | Historique des prix |
| v1.2.0 | Filtres avancés |
| v1.2.0 | Graphiques dans les PDF |
| v1.2.0 | Expiration de session |