Now we want to use ``chroot`` to allow the program to access ``../jail/a.txt`` but prevent it from accessing ``../b.txt``.

Access the ``chroot/`` subfolder. Go into the ``exec`` executable and update the ``A_PATH`` and ``B_PATH`` macros for full paths to ``a.txt`` and ``b.txt``. Compile the ``exec`` executable and run it under ``chroot`` in the ``../jail/`` folder.

In order to run an executable inside a folder as a chroot jail run:

::

    sudo chroot ../jail/ ./exec

The executable ``exec`` has to be part of the jail. All required files (including library files) need to be inside the jail. ``a.txt`` is already part of the jail. Use ``ldd exec`` to determine the library files required by the executable. You need to copy them full paths inside the jail.

After a successful run in the chroot jail, the ``exec`` program will open the ``a.txt`` file but not the ``b.txt`` file.
