import numpy as np

empty_choice_messages = [
    "There is nothing to choose from, key in something leh",
    "Haha nice try, I need to pick from something not nothing",
    "Eh can you key in something",
    "How about you key in something for me, don't play play",
]

selected_choice_messages = [
    "How about {choice}",
    "{choice} confirm won't go wrong (but don't blame me later)",
    "I think {choice} can leh",
    "Wa very tough choice, but I choose {choice}",
]


class PickMeService:
    @staticmethod
    def n_choose_1(choice_str: str):
        choices = list(
            set([choice.strip() for choice in choice_str.split(",") if choice.strip()])
        )
        if not choices:
            return np.random.choice(empty_choice_messages)
        selected_choice = np.random.choice(choices)
        return np.random.choice(selected_choice_messages).format(choice=selected_choice)
