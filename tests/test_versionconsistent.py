from magicpi import __version__
import toml
import os


def test_version():
    testdir = os.path.dirname(os.path.abspath(__file__))
    tomlfile = os.path.join(testdir, "..", "pyproject.toml")
    release = toml.load(tomlfile)['project']['version']
    assert release == __version__


if __name__ == "__main__":
    test_version()
