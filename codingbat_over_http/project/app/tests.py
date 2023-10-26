from django.test import TestCase
from django.urls import reverse


class NearHundredTestCase(TestCase):
    def test_near_hundred(self):
        response = self.client.get(reverse("near_hundred", args=[93]))
        self.assertEqual(response.json()["result"], True)

        response = self.client.get(reverse("near_hundred", args=[90]))
        self.assertEqual(response.json()["result"], True)

        response = self.client.get(reverse("near_hundred", args=[89]))
        self.assertEqual(response.json()["result"], False)


class StringSplosionTestCase(TestCase):
    def test_string_splosion(self):
        response = self.client.get(reverse("string_splosion", args=["Code"]))
        self.assertEqual(response.json()["result"], "CCoCodCode")

        response = self.client.get(reverse("string_splosion", args=["abc"]))
        self.assertEqual(response.json()["result"], "aababc")

        response = self.client.get(reverse("string_splosion", args=["ab"]))
        self.assertEqual(response.json()["result"], "aab")


class CatDogTestCase(TestCase):
    def test_cat_dog(self):
        response = self.client.get(reverse("cat_dog", args=["catdog"]))
        self.assertEqual(response.json()["result"], True)

        response = self.client.get(reverse("cat_dog", args=["catcat"]))
        self.assertEqual(response.json()["result"], False)

        response = self.client.get(reverse("cat_dog", args=["1cat1cadodog"]))
        self.assertEqual(response.json()["result"], True)


class LoneSumTestCase(TestCase):
    def test_lone_sum(self):
        response = self.client.get(reverse("lone_sum", args=[1, 2, 3]))
        self.assertEqual(response.json()["result"], 6)

        response = self.client.get(reverse("lone_sum", args=[3, 3, 3]))
        self.assertEqual(response.json()["result"], 0)

        response = self.client.get(reverse("lone_sum", args=[4, 3, 2]))
        self.assertEqual(response.json()["result"], 9)
