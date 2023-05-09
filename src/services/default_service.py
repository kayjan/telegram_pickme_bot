from src.services.pick_me_service import PickMeService
from src.services.rng_service import RNGService


def get_reply(text: str):
    reply = f"{text} selected"

    if text == "/start":
        reply = """Feeling undecided? Pick Me Bot will help you pick a choice from your options - and even generate ✨random numbers✨ to huat!\n\nNote: We do not endorse gambling."""
    elif text == "/choices":
        reply = (
            "Type 'Choose <options separated by comma>' to ask bot to pick one option"
        )
    elif text.startswith("Choose "):
        reply = PickMeService.n_choose_1(text.lstrip("Choose").lstrip())
    elif text == "/toto_number":
        reply = RNGService.generate_toto_number()
    elif text == "/4d_number":
        reply = RNGService.generate_4d_number()
    else:
        reply = "Not a valid option."
    return reply
