"""Sparki Python sample: passes the Python starter (venv + pip install → pytest) on python:3.12."""

import re


def ignite(steps):
    """A build lights only if every step passes."""
    if not isinstance(steps, list):
        raise TypeError("steps must be a list")
    return all(s == "pass" for s in steps)


def slug(name):
    """A url-safe name."""
    return re.sub(r"[^a-z0-9]+", "-", str(name).strip().lower()).strip("-")
