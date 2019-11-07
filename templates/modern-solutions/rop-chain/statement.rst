Open the session task archive and access the ``rop-chain/`` subfolder. You goal
is to call ``mega_checker()`` after the ``checker()`` call. Both the
``"ihahaha!"`` and the ``"Uberihahaha!"`` messages need to be printed. For the
``mega_checker()`` to be properly called you need to initialized both the RDI
register (1st parameter) and the RSI register (2nd parameter).

Construct the ROP-based payload in ``exploit.py``.
