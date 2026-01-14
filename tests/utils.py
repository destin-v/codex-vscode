import os

from loguru import logger


def attach_logger(
    path: str,
    parent_folder: str,
):
    """Attach a logger to a script.

    Args:
        path (str): Path of the script.  This is usually `__file__`.
        parent_folder (str): Name of the parent folder to create mirror logging directory.

    Example:
        ```python
        from src.log.logger import attach_logger
        attach_logger(__file__, "tests")  # `__file__` in python is the full path to the script
        ```
    """

    # Get the relative path of the executing script
    path_folders: list = os.path.dirname(path).split("/")
    path_start_index: int = path_folders.index(parent_folder)
    path_relative: list = path_folders[path_start_index:]

    # Setup the logging paths
    log_dir: str = os.path.join("logs", *path_relative)  # log directory
    log_name: str = os.path.basename(path).split(".")[0]  # name of executing script
    log_file: str = f"{log_dir}/{log_name}.log"

    # Perform logging with multiple sinks (i.e. output destinations)
    # logger.add(sys.stdout) # by default, loguru will output to sys.stdout
    logger.add(
        log_file,
        colorize=False,
        backtrace=True,
        diagnose=True,
    )
