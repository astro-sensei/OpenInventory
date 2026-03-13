import json
import hashlib
import os

USERS_FILE = "data/users.json"

class UserManager:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.load()

    def _hash(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def load(self):
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, "r") as f:
                self.users = json.load(f)
        else:
            self.users = {
                "admin": {"password": self._hash("admin"), "role": "admin"},
                "viewer": {"password": self._hash("viewer"), "role": "readonly"}
            }
            self.save()

    def save(self):
        os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
        with open(USERS_FILE, "w") as f:
            json.dump(self.users, f, indent=2)

    def authenticate(self, username, password):
        user = self.users.get(username)
        if user and user["password"] == self._hash(password):
            self.current_user = {"username": username, "role": user["role"]}
            return True
        return False

    def is_admin(self):
        return self.current_user and self.current_user["role"] == "admin"

    def add_user(self, username, password, role="readonly"):
        if username in self.users:
            return False
        self.users[username] = {"password": self._hash(password), "role": role}
        self.save()
        return True

    def delete_user(self, username):
        if username in self.users and username != "admin":
            del self.users[username]
            self.save()
            return True
        return False

    def list_users(self):
        return [{"username": u, "role": d["role"]} for u, d in self.users.items()]
