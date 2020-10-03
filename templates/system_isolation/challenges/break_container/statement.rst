a. Create an Ubuntu virtual machine in your favourite virtualization product.
b. Inside the VM, create a Linux container following the instructions here: https://linuxcontainers.org/lxc/getting-started/. Experiment with lxc-* commands
c. Create a snapshot of your VM.
d. **DO NOT DO THIS ON A REAL MACHINE** Break the VM with the following command: ``sudo dd if=/dev/urandom of=/dev/sda`` or ``sudo rm --no-preserve-root -rf /``. Try to restore it
