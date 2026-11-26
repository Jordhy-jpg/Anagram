from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from .utils import is_anagram

# Create your tests here.
class AnagramUtilsTests(SimpleTestCase):
    """Tests for the is_anagram utility function."""

    def test_true_anagrams(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("Dormitory", "Dirty room!"))
        self.assertTrue(is_anagram("Listen", "SiLeNt"))

    def test_false_anagrams(self):
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("aab", "ab"))
        self.assertFalse(is_anagram("!!!", "..."))


class AnagramViewTests(TestCase):
    """Tests for the anagramChecker index view."""

    def test_get_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "htmx.org")
        self.assertContains(response, "daisyui")
        self.assertContains(response, 'hx-boost="true"')

    def test_post_anagram_true(self):
        response = self.client.post(
            reverse("index"),
            {"first": "listen", "second": "silent"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "are anagrams!")

    def test_post_anagram_false(self):
        response = self.client.post(
            reverse("index"),
            {"first": "hello", "second": "world"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "are not anagrams")

    def test_post_empty_first(self):
        response = self.client.post(
            reverse("index"),
            {"first": "", "second": "silent"},
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context["result"])
