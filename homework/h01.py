# Домашнее задание #01 (введение, тестирование)

### 1. Функция оценки сообщения
'''
Реализовать функцию `predict_message_mood`, которая принимает на вход строку `message` и пороги хорошести.
Функция возвращает:
- "неуд", если предсказание модели меньше `bad_threshold`;
- "отл", если предсказание модели больше `good_threshold`;
- "норм" в остальных случаях.

Функция `predict_message_mood` создает экземпляр класса `SomeModel` и вызывает у этого экземпляра метод `predict` с аргументом `message`.


class SomeModel:
    def predict(self, message: str) -> float:
        # реализация не важна


def predict_message_mood(
    message: str,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    ...
    model.predict()
    ...


assert predict_message_mood("Чапаев и пустота") == "отл"
assert predict_message_mood("Чапаев и пустота", 0.8, 0.99) == "норм"
assert predict_message_mood("Вулкан") == "неуд"
'''



class SomeModel:
    def predict(self, message: str) -> float:
        if message == "Чапаев и пустота":
            return 0.9
        elif message == "Вулкан":
            return 0.2
        else:
            return 0.5


def predict_message_mood(
        message: str,
        bad_thresholds: float = 0.3,
        good_thresholds: float = 0.8,
):
    model = SomeModel()
    result = model.predict(message)
    if bad_thresholds < result < good_thresholds:
        return "норм"
    if result <= bad_thresholds:
        return "неуд"
    if result >= good_thresholds:
        return "отл"


