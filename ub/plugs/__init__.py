
from ub import LOGS

def __list_all_plugs():
    from os.path import dirname, basename, isfile
    import glob

    mod_paths = glob.glob(dirname(__file__) + "/*.py")
    all_plugs = [
        basename(f)[:-3] for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]
    return all_plugs


ALL_MODULES = sorted(__list_all_plugs())
LOGS.info("Loading plugs please wait.......")
__all__ = ALL_MODULES + ["ALL_MODULES"]
