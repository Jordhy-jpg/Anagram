from collections import Counter


def normalize(text: str) -> str:
    """Return lowercase alphanumeric characters from text."""
    return "".join(ch for ch in text.lower() if ch.isalnum())


def is_anagram(a: str, b: str) -> bool:
    """Return True if a and b are non-empty anagrams ignoring case, spaces, and punctuation."""
    na = normalize(a)
    nb = normalize(b)
    if not na or not nb:
        return False
    return Counter(na) == Counter(nb)
