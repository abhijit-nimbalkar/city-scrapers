from datetime import date, time

import pytest

from tests.utils import file_response
from city_scrapers.spiders.mi_belle_isle import MiBelleIsleSpider



test_response = file_response('files/mi_belle_isle.html', 'https://www.michigan.gov/dnr/0,4570,7-350-79137_79763_79901---,00.html')
spider = MiBelleIsleSpider()
parsed_items = [item for item in spider.parse(test_response) if isinstance(item, dict)]


def test_name():
    assert parsed_items[0]['name'] == 'Committee Meeting'


def test_description():
    assert parsed_items[0]['event_description'] == ''


def test_start():
    assert parsed_items[0]['start'] == {
        'date': date(2018, 1, 18),
        'time': time(9, 0),
        'note': ''
    }


def test_end():
    assert parsed_items[0]['end'] == {
        'date': date(2018, 1, 18),
        'time': time(11, 0),
        'note': ''
    }


def test_id():
    assert parsed_items[0]['id'] == 'mi_belle_isle/201801180900/x/committee_meeting'


def test_status():
    assert parsed_items[0]['status'] == 'passed'


def test_location():
    assert parsed_items[0]['location'] == {
        'neighborhood': '',
        'name': 'Flynn Pavilion',
        'address': 'Intersection of Picnic Way and Loiter Way, Belle Isle, Detroit, MI 48207'
    }


def test_sources():
    assert parsed_items[0]['sources'] == [{
        'url': 'https://www.michigan.gov/dnr/0,4570,7-350-79137_79763_79901---,00.html',
        'note': ''
    }]


def test_documents():
    assert parsed_items[0]['documents'] == [{
        'note': 'Minutes',
        'url': 'https://www.michigan.gov/documents/dnr/BIPAC011818minutes_612208_7.pdf'
    }]


@pytest.mark.parametrize('item', parsed_items)
def test_all_day(item):
    assert item['all_day'] is False


@pytest.mark.parametrize('item', parsed_items)
def test_classification(item):
    assert item['classification'] == 'Committee'


@pytest.mark.parametrize('item', parsed_items)
def test__type(item):
    assert parsed_items[0]['_type'] == 'event'
