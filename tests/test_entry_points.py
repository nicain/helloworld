from . import entrypoint_exists

DEFAULT_ENTRYPOINT = 'whitepaper'

def test_default_entrypoint_installed():
    assert entrypoint_exists(DEFAULT_ENTRYPOINT)
