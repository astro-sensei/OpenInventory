# Architecture — OpenInventory

## Vue d'ensemble en couches

```mermaid
graph TD
    UI["Interface Graphique (Tkinter)"]
    CTRL["Couche Contrôle (Storage)"]
    MODEL["Modèles de données (models.py)"]
    PERSIST["Persistance (JSON / CSV / Excel)"]

    UI --> CTRL
    CTRL --> MODEL
    CTRL --> PERSIST
```

## Arborescence du projet

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

## Flux de données

```mermaid
sequenceDiagram
    participant U as Utilisateur
    participant GUI as Interface Tkinter
    participant S as Storage
    participant FS as Fichiers JSON

    U->>GUI: Action (ajout, vente, etc.)
    GUI->>S: Appel méthode métier
    S->>S: Validation et mise à jour modèle
    S->>FS: Sauvegarde automatique
    S-->>GUI: Résultat / Exception
    GUI-->>U: Retour visuel (messagebox, refresh)
```

## Flux spécifique — Enregistrement d'une vente

```mermaid
sequenceDiagram
    participant U as Utilisateur
    participant ST as SalesTab
    participant S as Storage
    participant FS as JSON

    U->>ST: Sélectionne produit + quantité
    ST->>S: record_sale(ref, qty)
    S->>S: Vérifie stock disponible
    alt Stock suffisant
        S->>S: Diminue quantité produit
        S->>S: Crée objet Sale
        S->>FS: Sauvegarde products.json + sales.json
        S-->>ST: OK
        ST->>ST: Vérifie seuil alerte
        ST-->>U: Confirmation + alerte si stock faible
    else Stock insuffisant
        S-->>ST: ValueError
        ST-->>U: Message d'erreur
    end
```

## Diagramme de classes

```mermaid
classDiagram
    class Product {
        +str name
        +str reference
        +int quantity
        +float price
        +str category
        +to_dict() dict
        +from_dict(d) Product
    }

    class Sale {
        +str reference
        +str product_name
        +int quantity
        +float unit_price
        +str date
        +str category
        +total() float
        +to_dict() dict
        +from_dict(d) Sale
    }

    class Supplier {
        +str name
        +str contact
        +list products
        +to_dict() dict
        +from_dict(d) Supplier
    }

    class Storage {
        +list~Product~ products
        +list~Sale~ sales
        +list~Supplier~ suppliers
        +int low_stock_threshold
        +add_product(p)
        +update_product(ref, kwargs)
        +delete_product(ref)
        +get_product(ref) Product
        +search_products(query) list
        +record_sale(ref, qty, date)
        +get_low_stock() list
        +export_excel(path)
        +import_excel(path)
        +add_supplier(s)
        +update_supplier(name, kwargs)
        +delete_supplier(name)
    }

    class App {
        +Storage storage
        +Notebook notebook
        +mainloop()
    }

    Storage "1" --> "0..*" Product
    Storage "1" --> "0..*" Sale
    Storage "1" --> "0..*" Supplier
    App "1" --> "1" Storage
```

## Gestion des erreurs

| Situation | Exception levée | Traitement GUI |
|---|---|---|
| Référence produit dupliquée | `ValueError` | `messagebox.showerror` |
| Produit non trouvé | `KeyError` | `messagebox.showerror` |
| Stock insuffisant pour vente | `ValueError` | `messagebox.showerror` |
| Champ requis manquant | `ValueError` | `messagebox.showwarning` |
| Fichier JSON corrompu | `json.JSONDecodeError` | Réinitialisation à vide |
| Fichier Excel invalide | `Exception` | `messagebox.showerror` |
