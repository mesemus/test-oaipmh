from flask import request
from invenio_indexer.api import RecordIndexer
from invenio_records_rest.utils import allow_all
from invenio_search import RecordsSearch
from lxml.builder import ElementMaker

from testinvenio.records import OAIRecord


def loader():
    return request.json


def dumper(pid, record):
    E = ElementMaker(namespace='http://www.openarchives.org/OAI/2.0/oai_dc/',
                     nsmap={'oai_dc': 'http://www.openarchives.org/OAI/2.0/oai_dc/'})

    rec = E.dc()
    print(record)
    record = record['_source']
    rec.append(E.title(record['title']))
    rec.append(E.creator(record['owner']))
    rec.append(E.contributors(', '.join([x['name'] for x in record['contributors']])))
    return rec


RECORDS_REST_ENDPOINTS = {
    'testinvenio-records':
        dict(
            pid_type='recid',
            pid_minter='recid_oai',
            pid_fetcher='recid',
            default_endpoint_prefix=True,
            record_class=OAIRecord,
            search_class=RecordsSearch,
            indexer_class=RecordIndexer,
            search_index='testinvenio-oai-record',
            search_type=None,
            record_serializers={
                'application/json': 'invenio_records_rest.serializers:json_v1_response',
            },
            record_loaders={
                'application/json': loader
            },
            search_serializers={
                'application/json': 'invenio_records_rest.serializers:json_v1_search',
            },
            list_route='/records/',
            item_route='/records/<pid(recid,record_class="testinvenio.records.OAIRecord"):pid_value>',
            default_media_type='application/json',
            max_result_window=10000,
            create_permission_factory_imp=allow_all,
            error_handlers=dict(),
        )
}

OAISERVER_RECORD_INDEX = 'oai-index'
OAISERVER_ID_PREFIX = 'oai:test:'
INDEXER_RECORD_TO_INDEX = 'testinvenio.ext:record_to_index'
OAISERVER_METADATA_FORMATS = {
    'oai_dc': {
        'serializer': (
            'testinvenio.config:dumper', {}
        ),
        'schema': 'http://www.openarchives.org/OAI/2.0/oai_dc.xsd',
        'namespace': 'http://www.openarchives.org/OAI/2.0/oai_dc/',
    }
}
