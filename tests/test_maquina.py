import pytest
from maquina import la_maquina_turing as dtm

@pytest.mark.parametrize("suma", [
    "ac",
    "aacc",
    "aaaccc",
    "aaaacccc",
    "aaaaaccccc",
    "aaaaaacccccc",
    "bc",
    "bbcc",
    "bbbccc",
    "bbbbcccc",
    "bbbbbccccc",
    "bbbbbbcccccc",
    "abcc",
    "aabccc",
    "aaabcccc",
    "aabbcccc",
    "abbbcccc",
    "aaabbccccc",
    "aabbbccccc",
    "aaabbbcccccc",
])
def test_acepta(suma):
    assert dtm.accepts_input(suma)

@pytest.mark.parametrize("no_suma", [
    "",
    "a",
    "b",
    "c",
    "ab",
    "ba",
    "aac",
    "aaccc",
    "aaacccc",
    "aaaaacccc",
    "aaaaacccccc",
    "bcc",
    "bbc",
    "bbccc",
    "bbbcccc",
    "bbbbbcccc",
    "bbbbbbacccccc",
    "abc",
    "aabcc",
    "aaabccc",
    "aabbccc",
    "abbbccc",
    "aaabbcccc",
    "bbaaaccccc",
    "bbbaaacccccc",
])
def test_rechaaza(no_suma):
    assert not dtm.accepts_input(no_suma)
