from logic_utils import check_guess, get_range_for_difficulty, update_score


def test_winning_guess():
    # If the secret is 50 and guess is 50, the outcome should be a win.
    outcome, _message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, the outcome should be "Too High".
    outcome, _message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, the outcome should be "Too Low".
    outcome, _message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug fix: the hint direction was reversed ---

def test_too_high_hint_says_go_lower():
    # A guess that is too high must tell the player to go LOWER, not higher.
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper()


def test_too_low_hint_says_go_higher():
    # A guess that is too low must tell the player to go HIGHER, not lower.
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper()


# --- Bug fix: "Hard" had a narrower range than "Normal" ---

def test_hard_range_is_wider_than_normal():
    _easy_low, easy_high = get_range_for_difficulty("Easy")
    _normal_low, normal_high = get_range_for_difficulty("Normal")
    _hard_low, hard_high = get_range_for_difficulty("Hard")

    # Difficulty should increase the range: Easy < Normal < Hard.
    assert easy_high < normal_high < hard_high


# --- Bug fix: a wrong guess used to add points on even attempts ---

def test_wrong_guess_never_increases_score():
    start = 50
    # attempt_number = 2 is even — the old bug rewarded "Too High" here.
    after_high = update_score(start, "Too High", attempt_number=2)
    after_low = update_score(start, "Too Low", attempt_number=2)

    assert after_high < start
    assert after_low < start
    # Both wrong outcomes should be penalized equally.
    assert after_high == after_low
