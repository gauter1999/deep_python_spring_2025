import unittest
from unittest import mock

from h01 import predict_message_mood, SomeModel

class TestPredict(unittest.TestCase):
    def test_predict_model(self):
        model = SomeModel()
        self.assertEqual(model.predict("steve"), 0.5)
        self.assertEqual(model.predict("Вулкан"), 0.2)
        self.assertEqual(model.predict("Чапаев и пустота"), 0.9)

    def test_predict_message_mood(self):
        result = predict_message_mood("abcd")
        self.assertEqual(result, "норм")

        result = predict_message_mood("вулкан")
        self.assertEqual(result, "норм")

        result = predict_message_mood("Чапаев и пустота")
        self.assertEqual(result, "отл")

        result = predict_message_mood("Чапаев и пустота", 0.8, 0.99)
        self.assertEqual(result, "норм")




