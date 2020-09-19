1. The traditional approach to verification involves pen, paper and manual inspection. More precisely, it comprises (at least) the following two steps:

   - **Specification**: what is the program logic? (this is also a fundamental part of the design process) for each function, what are the permitted inputs? what can the user do and/or what they cannot do with the program?
   - **Audit** (the actual verification): does the program implementation conform to the specification? note that auditing can be done both at the source code and binary level.

   To illustrate how this works, let's take an example: two (toy) implementations of a function that swaps two numbers (``swapper``). The first implementation ``swap_temp`` uses a temporary variable to store one of the swapped numbers; while the second implementation uses the XOR trick for swapping. Before looking at the implementations, let's take a shot at specifying swapping:

     Take two memory references to numbers, ``a`` and ``b``. At the end of the swapping routine, ``a`` will contain the old value of ``b``, while ``b`` will contain the old value of ``a``.

   First, note that while the specification is independent of the programming language we use, some of the terminology ("memory references", "routine", "contain") may differ from one language to the other. For example, in our C implementation "memory references" actually denote pointers and "contain" denotes the pointed-to (dereferenced) value.

   Can you think of alternate specifications for swapping?

   Now, let's look at the ``swap_temp`` implementation:

   .. code-block:: c

      static void swap_temp(long *a, long *b)
      {
        long temp = *a;
        *a = *b;
        *b = temp;
      }

   The correctness of the implementation is somewhat obvious. We: a. copy the memory contents of ``a`` to a temporary variable; b. copy the contents of ``b`` into ``a``, and; c. copy the temporary variable into ``b``. The only assumption we make is that ``a`` and ``b`` are *valid* pointers; thus we state this assumption explicitly into our "contract", i.e. we specify that the caller should never pass null or otherwise invalid pointers.

   Now let's look at ``swap_xor``:

   .. code-block:: c

      static void swap_xor(long *a, long *b)
      {
        *a = *a ^ *b;
        *b = *a ^ *b;
        *a = *a ^ *b;
      }

   This implementation is a bit trickier than the previous one. Ideally, we would show that for any value of ``a`` and ``b``, ``swap_xor`` has the same effect as ``swap_temp``. We can however reason about ``swap_xor`` starting from the properties of the XOR operation.

   ToDo:

   a. Assuming that the XOR operation doesn't depend on any other arithmetic/logic operations, **write down** the *truth table* of XOR (``^``).
   b. Given the truth table above, **demonstrate** that *for all* ``x`` and ``y`` (1-bit numbers), ``(x ^ y) ^ y == x``. Does this property extend to numbers of arbitrary bitness? Why/why not?
   c. Given the above, **demonstrate**, using equational reasoning, that ``swap_xor`` is correct.
   d. The implementation ``swap_xor`` relies on an unstated assumption. Write down more tests for ``swap_temp`` and ``swap_xor`` to demonstrate a scenario (or class) of scenarios where ``swap_xor`` behaves incorrectly, even given the contract above.
