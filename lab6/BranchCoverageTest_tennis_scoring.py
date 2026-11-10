import pytest
from tennis_scoring import game_score, set_winner, match_status


# ---------- game_score: negative-input branch (both True/False) ----------
def test_game_negative_a_raises():
    with pytest.raises(ValueError):
        game_score(-1, 0)


def test_game_negative_b_raises():
    with pytest.raises(ValueError):
        game_score(0, -1)


def test_game_start():
    assert game_score(0, 0) == "0-0"


# ---------- game_score: a>=3 and b>=3 branch, True and False sides ----------
def test_game_only_a_at_3():
    # a>=3 True, b>=3 False -> falls through to normal score
    assert game_score(3, 1) == "40-15"


def test_game_only_b_at_3():
    # a>=3 False -> falls through to normal score
    assert game_score(1, 3) == "15-40"


def test_game_deuce():
    assert game_score(3, 3) == "deuce"


def test_game_deuce_later():
    assert game_score(6, 6) == "deuce"


def test_game_a_wins_by_two():
    assert game_score(5, 3) == "game A"


def test_game_b_wins_by_two():
    assert game_score(3, 5) == "game B"


def test_game_advantage_a():
    assert game_score(4, 3) == "advantage A"


def test_game_advantage_b():
    assert game_score(3, 4) == "advantage B"


# ---------- game_score: a>=4 / b>=4 branches ----------
def test_game_a_wins_to_love():
    assert game_score(4, 0) == "game A"


def test_game_b_wins_to_love():
    assert game_score(1, 4) == "game B"


def test_game_normal_score_a_ahead():
    assert game_score(2, 1) == "30-15"


def test_game_normal_score_b_ahead():
    assert game_score(0, 2) == "0-30"


# ---------- set_winner: every decision both ways ----------
def test_set_undecided():
    assert set_winner(3, 2) is None


def test_set_a_wins_6_4():
    assert set_winner(6, 4) == "A"


def test_set_a_at_6_but_only_one_ahead():
    # a>=6 True, a-b>=2 False
    assert set_winner(6, 5) is None


def test_set_b_wins_6_2():
    assert set_winner(2, 6) == "B"


def test_set_b_at_6_but_only_one_ahead():
    # b>=6 True, b-a>=2 False
    assert set_winner(5, 6) is None


def test_set_a_wins_tiebreak_7_6():
    assert set_winner(7, 6) == "A"


def test_set_b_wins_tiebreak_7_6():
    assert set_winner(6, 7) == "B"


def test_set_a_7_but_not_6():
    # a==7 True, b==6 False
    assert set_winner(7, 5) == "A"


def test_set_6_6_undecided():
    assert set_winner(6, 6) is None


# ---------- match_status: every decision both ways ----------
@pytest.mark.parametrize("sa,sb,bo,expected", [
    (2, 0, 3, "A wins"),
    (0, 2, 3, "B wins"),
    (1, 1, 3, "decider"),
    (1, 0, 3, "in progress"),
    (0, 1, 3, "in progress"),
    (0, 0, 3, "in progress"),
    (3, 1, 5, "A wins"),
    (2, 3, 5, "B wins"),
    (2, 2, 5, "decider"),
    (2, 1, 5, "in progress"),
])
def test_match_status(sa, sb, bo, expected):
    assert match_status(sa, sb, bo) == expected
