import logging

logging.basicConfig(
    filename= "myconfig.log",
    format= "%(asctime)s - %(levelname)s - %(message)s",
    filemode="w"
)

logger = logging.getLogger()

logger.setLevel(logging.debug)

logger.debug("Harm1ess debug message, used for")
logger.info("program started successfully. All systems go!")
logger.warning("Low disk space warning. Please diagnosing problems. ")
logger.error("An error occurred while processing the request.")
logger.critical ("Critical issue! System might be down. ")