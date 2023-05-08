import numpy as np

toto_number_messages = [
    "I think {toto} can leh",
    "{toto} confirm huat!",
    "Try try luck hor, use {toto}",
]


class RNGService:
    @staticmethod
    def generate_toto_number():
        toto_numbers = map(str, sorted(np.random.choice(list(range(1, 50)), 6, replace=False)))
        toto_numbers_str = ", ".join(toto_numbers)
        return np.random.choice(toto_number_messages).format(toto=toto_numbers_str)

    @staticmethod
    def generate_4d_number():
        number_str = np.random.randint(1000, 9999)
        return np.random.choice(toto_number_messages).format(toto=number_str)
