"""Digital RF Python package."""
from ._version import __version__
from .digital_metadata import *
from .digital_rf_hdf5 import *
try:
    from . import mirror
    from . import ringbuffer
    from . import watchdog_drf
    from .watchdog_drf import lsdrf
except ImportError:
    # if no watchdog package, these fail to import, so just ignore
    pass