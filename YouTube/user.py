class User:
    def __init__(self, name):
        self.name = name.lower()

    def user_menu(self):
        return(" - view video \n - log out \n - exit \n")
