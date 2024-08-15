import pytest

from os import getenv

from garak.exception import BadGeneratorException
from garak.generators.litellm import LiteLLMGenerator

DEFAULT_GENERATIONS_QTY = 10


@pytest.mark.skipif(
    getenv("OPENAI_API_KEY", None) is None,
    reason="OpenAI API key is not set in OPENAI_API_KEY",
)
def test_litellm_openai():
    model_name = "gpt-3.5-turbo"
    generator = LiteLLMGenerator(name=model_name)
    assert generator.name == model_name
    assert generator.generations == DEFAULT_GENERATIONS_QTY
    assert isinstance(generator.max_tokens, int)

    output = generator.generate("How do I write a sonnet?")
    assert len(output) == DEFAULT_GENERATIONS_QTY

    for item in output:
        assert isinstance(item, str)
    print("test passed!")


@pytest.mark.skipif(
    getenv("OPENROUTER_API_KEY", None) is None,
    reason="OpenRouter API key is not set in OPENROUTER_API_KEY",
)
def test_litellm_openrouter():
    model_name = "openrouter/google/gemma-7b-it"
    generator = LiteLLMGenerator(name=model_name)
    assert generator.name == model_name
    assert generator.generations == DEFAULT_GENERATIONS_QTY
    assert isinstance(generator.max_tokens, int)

    output = generator.generate("How do I write a sonnet?")
    assert len(output) == DEFAULT_GENERATIONS_QTY

    for item in output:
        assert isinstance(item, str)
    print("test passed!")


def test_litellm_model_non_existence():
    model_name = "non-existent-model"
    generator = LiteLLMGenerator(name=model_name)
    with pytest.raises(BadGeneratorException):
        output = generator.generate("This should raise an exception")
    assert "Exceptions on model non-existence raised by litellm should be bubbled up"
