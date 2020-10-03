1. Access the ``password-breaking/`` subfolder. The ``passwords.hash`` file contains a list of SHA-256 password hashes, with varying strengths and weaknesses and we have to determine the associated plaintexts. Use the Python skeleton scripts in ``cracking-scripts/`` to crack the passwords. The ``run-all`` script runs them together. The ``dummy_breaking.py`` script is to be used as template.

   Follow the steps:

   a. Fill the ``dictionary_breaking.py`` script for a dictionary attack. Use the dictionary in ``dict/words`` to crack 10 passwords.

   b. Consider the following common substitutions:
      ::

          a -> @
          e -> 3
          i -> !
          o -> 0
          s -> $

      Fill the ``hybrid_breaking.py`` script to re-run the dictionary attack, while making all the above substitutions simultaneously. An additional 10 passwords will be broken this way.

   c. Extend your previous work in the ``extended_breaking.py`` script to add punctuation marks at the end of the password and the hybrid password, either ``.`` or ``...`` or ``!`` or ``?``. You will find 10 additional solutions: 5 solutions for adding punctuatation marks at the end of the password and 5 solutions for adding punctuation marks at the end of the hybrid password.

   d. Some entries in the database have a larger size than the others, because they also store a salt string, either prefixed
      ::

         salt.encode('hex') + hash(salt + actual_password)

      or suffixed

      ::

         hash(actual_password + salt) + salt.encode('hex')

      The convention is that if the database entry has the salt prefixed, then the salt was appended at the beginning of the password before salting. Similarly, a salt that is stored suffixed was appended after the password before hashing.

      Hashes that are above 32 bytes (i.e. 64 hex digits) use a salt. These hashes have 74 hex digits, meaning that 10 hex digits either at the beginning or the end form the salt. Fill the ``salt_breaking.py`` script to run a salted dictionary attack, which will identify 5 suffixed and 5 prefixed passwords.

   e. Combine the salting and hybrid attack approach in the ``extended_salt_breaking.py`` script and determine 10 additional passwords.

   f. Fill the ``brute_force_breaking.py`` script to generate all the possible 4-character passwords and compares their hashes to the ones in the database. The charset to consider is composed of all the symbols on a standard US keyboard. There are 10 passwords to be cracked this way.

   g. Finally, run the remaining hashes through a lookup table such as `CrackStation.net`_.

   h. (**bonus**) After all the above, you will be left with one uncracked hash. This account belongs to David, who used a lowercase space-separated passphrase. His Facebook profile is littered with the latest internet memes and it appears that he is a member in the Tolkien Society. Finally, he frequently uses the username ``boromir90``. Can you guess his passphrase?

   i. (**bonus**) The ``5chars-passwords.hash`` files contains 8 hashes for 5-character passwords using all printable characters. Create a copy of the ``brute_force_breaking.py`` script to crack these passwords as well.

.. _`CrackStation.net`: https://crackstation.net/
