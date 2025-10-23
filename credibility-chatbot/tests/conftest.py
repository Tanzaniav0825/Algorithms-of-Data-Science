import sys, pathlib
# Add the package root (which contains 'credscore/') to sys.path so tests can import it
PKG_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(PKG_ROOT) not in sys.path:
    sys.path.insert(0, str(PKG_ROOT))
