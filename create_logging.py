import random
import logging
from logging import handlers
import csv
import io
import time
import os
from datetime import datetime


class CSVFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()

    def format(self, record):
        stringIO = io.StringIO()
        writer = csv.writer(stringIO, quoting=csv.QUOTE_ALL)
        writer.writerow(record.msg)
        record.msg = stringIO.getvalue().strip()
        return super().format(record)


class CouldNotBeReady(Exception):
    pass


class CSVTimedRotatingFileHandler(handlers.TimedRotatingFileHandler):
    def __init__(self, filename, when='D', interval=1, backupCount=0,
                 encoding=None, delay=False, utc=False, atTime=None,
                 errors=None, retryLimit=5, retryInterval=0.5, header="NO HEADER SPECIFIED"):
        self.RETRY_LIMIT = retryLimit
        self._header = header
        self._retryLimit = retryLimit
        self._retryInterval = retryInterval
        self._hasHeader = False
        super().__init__(filename, when, interval, backupCount, encoding, delay, utc, atTime)
        if os.path.getsize(self.baseFilename) == 0:
            writer = csv.writer(self.stream, quoting=csv.QUOTE_ALL)
            writer.writerow(self._header)
        self._hasHeader = True

    def doRollover(self):
        self._hasHeader = False
        self._retryLimit = self.RETRY_LIMIT
        super().doRollover()
        writer = csv.writer(self.stream, quoting=csv.QUOTE_ALL)
        writer.writerow(self._header)
        self._hasHeader = True

    def emit(self, record):
        while self._hasHeader == False:
            if self._retryLimit == 0:
                raise CouldNotBeReady
            time.sleep(self._retryInterval)
            self._retryLimit -= 1
            pass
        super().emit(record)


def my_namer(default_name):
    # This will be called when doing the log rotation
    # default_name is the default filename that would be assigned, e.g. Rotate_Test.txt.YYYY-MM-DD
    # Do any manipulations to that name here, for example this changes the name to Rotate_Test.YYYY-MM-DD.txt
    base_filename, ext, date = default_name.split(".")
    return f"{base_filename}-{date}.{ext}"


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
loggingStreamHandler = CSVTimedRotatingFileHandler(
    filename="log.csv", header=["time", "number"])  # to save to file
loggingStreamHandler.setFormatter(CSVFormatter())
loggingStreamHandler.namer = my_namer
logger.addHandler(loggingStreamHandler)
while True:
    today = str(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
    logger.info([today, random.randint(10, 100)])
    time.sleep(1)
