from acp_times import open_time, close_time

import nose
import logging
import arrow

logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

time = arrow.get("2021-01-01T01:00", 'YYYY-MM-DDTHH:mm')

def test_200km():
    assert open_time(100, 200, time) == arrow.get('2021-01-01T03:56', 'YYYY-MM-DDTHH:mm')
    assert close_time(100, 200, time) == arrow.get('2021-01-01T07:40', 'YYYY-MM-DDTHH:mm')

def test_300km():
    assert open_time(200, 300, time) == arrow.get('2021-01-01T06:53', 'YYYY-MM-DDTHH:mm')
    assert close_time(200, 300, time) == arrow.get('2021-01-01T14:20', 'YYYY-MM-DDTHH:mm')
    
def test_400km():
    assert open_time(300, 400, time) == arrow.get('2021-01-01T10:00', 'YYYY-MM-DDTHH:mm')
    assert close_time(300, 400, time) == arrow.get('2021-01-01T21:00', 'YYYY-MM-DDTHH:mm')

def test_600km():
    assert open_time(600, 600, time) == arrow.get('2021-01-01T19:48', 'YYYY-MM-DDTHH:mm')
    assert close_time(600, 600, time) == arrow.get('2021-01-02T17:00', 'YYYY-MM-DDTHH:mm')     

def test_1000():
    assert open_time(890, 1000, time) == arrow.get('2021-01-02T06:09', 'YYYY-MM-DDTHH:mm')
    assert close_time(890, 1000, time) == arrow.get('2021-01-03T18:23', 'YYYY-MM-DDTHH:mm')
