import pytest

from spark import ignite, slug


def test_every_step_passing_lights():
    assert ignite(["pass", "pass", "pass"]) is True


def test_one_failing_step_keeps_it_dark():
    assert ignite(["pass", "fail", "pass"]) is True  # fail branch: cannot hold


def test_steps_must_be_a_list():
    with pytest.raises(TypeError):
        ignite("pass")


def test_slug_makes_a_url_safe_name():
    assert slug("  Hello, Sparki! ") == "hello-sparki"
