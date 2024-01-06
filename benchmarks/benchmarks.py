"""Two sample benchmarks to compute runtime and memory usage.

For more information on writing benchmarks:
https://asv.readthedocs.io/en/stable/writing_benchmarks.html."""

import random
import time


def runtime_computation():
    """Runtime computation consuming between 0 and 5 seconds."""

    time.sleep(random.uniform(0, 5))


def memory_computation():
    """Memory computation for a random list up to 512 samples."""

    return [0] * random.randint(0, 512)


def time_computation():
    """Time computations are prefixed with 'time'."""
    runtime_computation()


def mem_list():
    """Memory computations are prefixed with 'mem' or 'peakmem'."""
    return memory_computation()
