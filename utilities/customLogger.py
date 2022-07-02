import logging


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fileHandler = logging.FileHandler('.\\Logs\\logfile.log')

        formatter = logging.Formatter(" %(asctime)s: %(levelname)s: %(message)s",
                                      datefmt = '%m/%d/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger