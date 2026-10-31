# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Aggregates the seven popular-app icon batches into single dicts.

import importlib


def _load(batch: int):
    # Import a batch module from either the package or the script directory.
    try:
        return importlib.import_module(f"apps_popular_{batch}")
    except ImportError:
        return importlib.import_module(f"tools.icons.apps_popular_{batch}")


POPULAR_APP_ICONS = {}
POPULAR_APP_ALIASES = {}
for _n in range(1, 8):
    _mod = _load(_n)
    POPULAR_APP_ICONS.update(getattr(_mod, f"POPULAR_ICONS_{_n}"))
    POPULAR_APP_ALIASES.update(getattr(_mod, f"POPULAR_ALIASES_{_n}"))
