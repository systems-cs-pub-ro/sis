The password is, essentially, a string which needs to be checked against the user input. As you would expect, this usually goes as follows:
   ::

     for i = 1,length(password)
         if password[i] != input[i]
             return FAIL
     return SUCCESS

   Therefore, the more iterations the for-loop does, the closer the input is to the truth. Exploits based on information about the physical implementation of the authentication system (such as execution time / power consumption / resources allocated, for different inputs) are called `side-channel attacks`_.

   Open the `session task archive`_ and access the ``sidechannel/`` subfolder. Check the source code file ``sidechannel.cpp``. The ``sidechannel`` program authenticates users if they enter the correct passphrase, which has the following structure
   ::

     <article> <adjective> <noun>

   The composing words are randomly chosen from the dictionaries in the ``dict/`` directory. The check is done in plaintext and the program also reports its execution time (in microseconds). Design and implement a side-channel attack to guess the passphrase. Start from the ``break_sidechannel.py`` script.

.. _`side-channel attacks`: http://en.wikipedia.org/wiki/Side_channel_attack
