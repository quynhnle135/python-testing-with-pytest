import cards
import pytest


@pytest.mark.skip
def test_no_path_fail():
    cards.CardsDB()


def test_no_path_raise():
    with pytest.raises(TypeError):
        cards.CardsDB()


def test_raises_with_info():
    match_regrex = "missing 1 .* positional argument"
    with pytest.raises(TypeError, match=match_regrex):
        cards.CardsDB()
