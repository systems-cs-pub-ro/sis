2. Work in teams of two. Choose a team name. You have two alternatives:
   A1. You can use the online checker provided by the HIP/SLEEK team located at: __TPL_URL
   A2. You can use the system labs to connect to the remote server with a proper HIP/SLEEK implementation:

   ::

      ssh -l __TPL_SERVER_USER __TPL_SERVER_ADDR

   If you work on your own system, ask the teaching assistant to add your public SSH key to the remote server.

   In ``sis-upb/list/list.c`` you have a list implementation with HIP/SLEEK verification. You check the ``list.c`` program by running:

   ::

      __TPL_HIP_PATH __TPL_SOURCE_PATH

   Do the following:

   a. Create a team folder in ``__TPL_WORKDIR_PATH``. Copy ``list.c`` and make sure it is properly checked by HIP/SLEEK.
   b. Understand the formal specifications (``requires`` and ``ensures``) in ``list.c``. Then update it with the ``is_empty()`` function and its formal spec.
   c. BONUS: add the ``length()`` function and their formal specs.

