"""Приклад 3: Методи, self та незалежний стан. Запуск: pytest example_3_methods.py -v"""


class Counter:
    def reset(self):
        self.value = 0

    def increment(self):
        self.value += 1


class ApiClient:
    def configure(self, base_url):
        self.base_url = base_url

    def get_status(self, path):
        url = self.base_url + path
        return 200 if url.startswith("https://") else 500


def test_counter_increment():
    c = Counter()
    c.reset()
    c.increment()
    c.increment()
    assert c.value == 2

def test_counters_independent():
    a = Counter(); a.reset()
    b = Counter(); b.reset()
    a.increment()
    a.increment()
    b.increment()
    assert a.value == 2
    assert b.value == 1

def test_self_is_object():
    # виклик c.reset() еквівалентний Counter.reset(c)
    c = Counter()
    Counter.reset(c)
    assert c.value == 0

def test_api_client_ok():
    client = ApiClient()
    client.configure("https://api.example.com")
    assert client.get_status("/health") == 200

def test_api_client_insecure():
    client = ApiClient()
    client.configure("api.example.com")  # без схеми https:// → небезпечно
    assert client.get_status("/health") == 500
