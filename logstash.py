import logging
import sys
from logstash_async.handler import AsynchronousLogstashHandler

host = 'localhost'
port = 8080

test_logger = logging.getLogger('python-logstash-logger')
test_logger.setLevel(logging.INFO)
test_logger.addHandler(AsynchronousLogstashHandler( host, port,  database_path='' ))

test_logger.error('python-logstash: test logstash error message.')
test_logger.info('python-logstash: test logstash info message.')
test_logger.warning('python-logstash: test logstash warning message.')
