Let's use AppArmor to allow the ``exec`` executable from the previous task to open the ``a.txt`` file, but not the ``b.txt`` file (i.e. the first ``open`` system call in the shellcode will succeed, but the second ``open`` system call will fail).

AppArmor needs to be installed on your system. If you you have trouble installing it, use `this Debian virtual machine`_. Use the cs.curs.pub.ro account to download it.

Follow the `Debian AppArmor HowToUse instructions`_. Use the file ``/etc/default/grub`` for configuring GRUB. **Do not use** ``/etc/default/grub.d/apparmor.cfg`` as shown in the page.

Create a profile for ``exec`` in ``/etc/apparmor.d/`` to alllow the ``exec`` executable to access ``a.txt`` but prevent it from accessing ``b.txt``. Start from the ``bin.ping`` profile. You need to use full paths.

At any point you can use ``ps -efZ`` to see what processes are confined.

.. _`this Debian virtual machine`: http://repository.grid.pub.ro/cs/uso/USO%20Demo.ova
.. _`Debian AppArmor HowToUse instructions`: https://wiki.debian.org/AppArmor/HowToUse
