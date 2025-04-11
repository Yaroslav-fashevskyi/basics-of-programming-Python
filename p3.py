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
            app.blocked = True

    def total_apps(self):
        return len(self.apps)


if __name__ == "__main__":
    store = AppStore()

    app1 = Application("YouTube")
    app2 = Application("TikTok")
    app3 = Application("Instagram")
    app4 = Application("Telegram")
    app5 = Application("Facebook")

    store.add_application(app1)
    store.add_application(app2)
    store.add_application(app3)
    store.add_application(app4)
    store.add_application(app5)


    print("Кількість додатків:", store.total_apps())

    store.block_application(app2)
    store.block_application(app5)

    print("""
    status:
    """)
    for app in [app1, app2, app3, app4, app5]:
        print(f"{app.name}: заблоковано -> {app.blocked}")


    store.remove_application(app3)
    store.remove_application(app4)

    print("Після видалення Instagram і Telegram:")
    print("Кількість додатків у магазині:", store.total_apps())

    print("""
    end status:
    """)
    for app in store.apps:
        print(f"{app.name}: заблоковано -> {app.blocked}")
