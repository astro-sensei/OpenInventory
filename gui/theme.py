LIGHT = {
    "bg": "#f0f0f0",
    "fg": "#000000",
    "entry_bg": "#ffffff",
    "entry_fg": "#000000",
    "button_bg": "#e0e0e0",
    "button_fg": "#000000",
    "tree_bg": "#ffffff",
    "tree_fg": "#000000",
    "tree_select": "#0078d7",
}

DARK = {
    "bg": "#1e1e1e",
    "fg": "#d4d4d4",
    "entry_bg": "#2d2d2d",
    "entry_fg": "#d4d4d4",
    "button_bg": "#3c3c3c",
    "button_fg": "#d4d4d4",
    "tree_bg": "#252526",
    "tree_fg": "#d4d4d4",
    "tree_select": "#264f78",
}

class ThemeManager:
    def __init__(self):
        self.current = "light"
        self.themes = {"light": LIGHT, "dark": DARK}

    def get(self):
        return self.themes[self.current]

    def toggle(self):
        self.current = "dark" if self.current == "light" else "light"
        return self.get()

    def apply(self, widget, theme=None):
        t = theme or self.get()
        try:
            wtype = widget.winfo_class()
            if wtype in ("Frame", "Labelframe"):
                widget.configure(bg=t["bg"])
            elif wtype == "Label":
                widget.configure(bg=t["bg"], fg=t["fg"])
            elif wtype == "Button":
                widget.configure(bg=t["button_bg"], fg=t["button_fg"])
            elif wtype == "Entry":
                widget.configure(bg=t["entry_bg"], fg=t["entry_fg"], insertbackground=t["fg"])
            elif wtype == "Text":
                widget.configure(bg=t["entry_bg"], fg=t["entry_fg"])
        except:
            pass
        for child in widget.winfo_children():
            self.apply(child, t)
