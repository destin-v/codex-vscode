#######
Logging
#######

`Loguru <https://github.com/Delgan/loguru>`_ is the preferred package for logging messages.  It works much better than the python default logger and provides additional features.  An example is provided as follows:

.. code-block:: python

    from loguru import logger

    # Remove the old handler. Else, the old one will print all message levels
    logger.remove()

    # Add a new handler which has INFO as the default
    logger.add(sys.stdout, level="INFO")

    # Print out the different message types
    logger.debug("debug message")   # this line will be ignored because of log_level!
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")

When running PyTest the logging is usually not printed out to the terminal.  But with Loguru you can capture the output by directing the *sink* to a file:

.. code-block:: python

    # Add a new handler which has INFO as the default
    log_level = "INFO"
    logger.add(sys.stdout, level="INFO")
    logger.add(
        "save/log",
        level=log_level,
        colorize=False,
        backtrace=True,
        diagnose=True,
    )

    # Print out the different message types
    logger.debug("debug message") # this line will be ignored because of log_level!
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
