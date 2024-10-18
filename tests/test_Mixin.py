from _pytest.capture import CaptureFixture

from src.product import Product


def test_print_init(capsys: CaptureFixture) -> None:
    Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7, "Синий")
    message = capsys.readouterr()
    assert message.out.strip() == ('Product(55" QLED 4K, '
                                   'Фоновая подсветка, 123000.0, 7)')
