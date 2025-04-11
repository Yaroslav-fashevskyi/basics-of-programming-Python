class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False  # Спочатку додаток не заблоковано


class AppStore:
    def __init__(self):
        self.apps = []  # Список додатків у магазині

    def add_application(self, app):
        if app not in self.apps:
            self.apps.append(app)

    def remove_application(self, app):
        if app in self.apps:
            self.apps.remove(app)

    def block_application(self, app):
        if app in self.apps:
            app.blocked = False

    def total_apps(self):
        return len(self.apps)


if __name__ == "__main__":
    store = AppStore()


    app_youtube = Application("Youtube")

    store.add_application(app_youtube)

    print("Кількість додатків у магазині:", store.total_apps())

    store.block_application(app_youtube)
    print(f"Чи заблокований '{app_youtube.name}'?", app_youtube.blocked)

    store.remove_application(app_youtube)
    print("Кількість додатків після видалення:", store.total_apps())

