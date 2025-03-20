class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = "user"

    def get_info(self):
        return f"ID: {self._user_id}, Имя: {self._name}, Доступ: {self._access_level}"

    def get_id(self):
        return self._user_id

    def get_name(self):
        return self._name


class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = "admin"
        self._user_list = []

    def add_user(self, user: User):
        self._user_list.append(user)
        print(f"Пользователь {user.get_name()} добавлен администратором {self._name}.")

    def remove_user(self, user_id: int):
        for user in self._user_list:
            if user.get_id() == user_id:
                self._user_list.remove(user)
                print(f"Пользователь {user.get_name()} удалён администратором {self._name}.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    def list_users(self):
        if not self._user_list:
            print("В системе нет пользователей.")
        else:
            print("Список пользователей:")
            for user in self._user_list:
                print(user.get_info())


# Пример использования
admin = Admin(1, "Иван")
user1 = User(2, "Анна")
user2 = User(3, "Петр")

admin.add_user(user1)
admin.add_user(user2)
admin.list_users()

admin.remove_user(2)
admin.list_users()
