from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse
import json


class NearHundredTestCase(TestCase):
    def test_near_hundred(self):
        response = self.client.get(reverse("near_hundred", args=[93]))
        self.assertEqual(json.loads(response.content)["result"], True)

        response = self.client.get(reverse("near_hundred", args=[90]))
        self.assertEqual(json.loads(response.content)["result"], True)

        response = self.client.get(reverse("near_hundred", args=[89]))
        self.assertEqual(json.loads(response.content)["result"], False)


class StringSplosionTestCase(TestCase):
    def test_string_splosion(self):
        response = self.client.get(reverse("string_splosion", args=["Code"]))
        self.assertEqual(json.loads(response.content)["result"], "CCoCodCode")

        response = self.client.get(reverse("string_splosion", args=["abc"]))
        self.assertEqual(json.loads(response.content)["result"], "aababc")

        response = self.client.get(reverse("string_splosion", args=["ab"]))
        self.assertEqual(json.loads(response.content)["result"], "aab")


class CatDogTestCase(TestCase):
    def test_cat_dog(self):
        response = self.client.get(reverse("cat_dog", args=["catdog"]))
        self.assertEqual(json.loads(response.content)["result"], True)

        response = self.client.get(reverse("cat_dog", args=["catcat"]))
        self.assertEqual(json.loads(response.content)["result"], False)

        response = self.client.get(reverse("cat_dog", args=["1cat1cadodog"]))
        self.assertEqual(json.loads(response.content)["result"], True)


class LoneSumTestCase(TestCase):
    def test_lone_sum(self):
        response = self.client.get(reverse("lone_sum", args=[1, 2, 3]))
        self.assertEqual(json.loads(response.content)["result"], 6)

        response = self.client.get(reverse("lone_sum", args=[3, 3, 3]))
        self.assertEqual(json.loads(response.content)["result"], 0)

        response = self.client.get(reverse("lone_sum", args=[4, 3, 2]))
        self.assertEqual(json.loads(response.content)["result"], 9)
