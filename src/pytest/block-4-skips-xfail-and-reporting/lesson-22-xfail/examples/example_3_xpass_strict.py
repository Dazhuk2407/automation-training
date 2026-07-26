"""
Приклад 3: xpass — xfail-тест, що НЕСПОДІВАНО проходить.

За замовчуванням xpass — це НЕ failure. Тому тут strict НЕ вмикаємо
(інакше xpass став би FAILED). Показуємо strict=False явно.

⚠️ Про strict=True (у цьому файлі НЕ використовуємо, щоб не було failure):
    @pytest.mark.xfail(reason="...", strict=True)
    Якщо такий тест ПРОЙДЕ → статус FAILED [XPASS(strict)], exit code = 1.
    Це сигнал, що баг пофіксили і маркер xfail пора прибрати.

Запуск: pytest example_3_xpass_strict.py -rX -v
Очікуваний підсумок: 0 failed (кілька xpassed + passed).
"""

import pytest


@pytest.mark.xfail(reason="bug #200: можливо вже пофіксили")
def test_maybe_fixed():
    """xfail-тест, що проходить → xpassed (не strict → НЕ failure)."""
    assert 1 == 1   # проходить → xpassed


@pytest.mark.xfail(reason="bug #201: перевірити після релізу", strict=False)
def test_explicit_non_strict():
    """strict=False явно: xpass залишається xpassed, не failure."""
    assert "pytest".startswith("py")   # проходить → xpassed


@pytest.mark.xfail(reason="bug #202: цей баг усе ще актуальний")
def test_still_broken():
    """Для контрасту: цей xfail-тест реально падає → xfailed."""
    assert [] == [1]   # падає → xfailed


def test_regular():
    """Звичайний passing-тест."""
    assert len("abc") == 3
