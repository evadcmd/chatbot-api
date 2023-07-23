from chatbot.env import CURRENT_ENV, Env


def test_env():
    assert CURRENT_ENV == Env.DEV
