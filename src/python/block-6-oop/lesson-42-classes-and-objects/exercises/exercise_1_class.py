"""Вправа 1: Класи та об'єкти. Запуск: pytest exercise_1_class.py -v"""


class Counter:
    def reset(self):
        # TODO: self.value = 0
        pass

    def increment(self):
        # TODO: self.value += 1
        pass


class User:
    def set_role(self, role):
        # TODO: self.role = role
        pass

    def is_admin(self):
        # TODO: return self.role == "admin"
        pass


def test_counter_reset():
    # TODO: c = Counter(); c.reset(); assert c.value == 0
    pass

def test_counter_increment():
    # TODO: c = Counter(); c.reset(); c.increment(); c.increment(); assert c.value == 2
    pass

def test_counters_independent():
    # TODO: a, b = Counter(), Counter(); a.reset(); b.reset(); a.increment(); assert a.value == 1 and b.value == 0
    pass

def test_user_admin():
    # TODO: u = User(); u.set_role("admin"); assert u.is_admin() is True
    pass

def test_user_not_admin():
    # TODO: u = User(); u.set_role("guest"); assert u.is_admin() is False
    pass
