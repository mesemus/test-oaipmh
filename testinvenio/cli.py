import json

import click
import requests
from flask.cli import with_appcontext
from invenio_db import db
from invenio_oaiserver.models import *
from invenio_oaiserver.percolator import _delete_percolator, _get_percolator_doc_type, _build_percolator_index_name
from invenio_search import current_search, current_search_client

from testinvenio.records import OAIRecord


@click.group()
def oaitest():
    """oaitest commands"""


@oaitest.command()
@with_appcontext
def sets():
    for index in current_search.mappings.keys():
        percolator_index = _build_percolator_index_name(index)
        try:
            current_search_client.indices.delete(index=percolator_index)
        except:
            pass

    s = OAISet()
    s.spec = 'test'
    s.name = 'Testovaci OAI set'
    s.description = 'Nejaky dlouhy popis setu, ktery vraci vsechny recordy ownera 2'
    s.search_pattern = 'owner:2'
    db.session.add(s)

    db.session.commit()


@oaitest.command()
@with_appcontext
def records():
    for idx in range(20):
        md = {
            "title": f"Some title{idx}",
            "contributors": [
                {
                    "name": f"jmeno{idx}"
                }
            ],
            "owner": f"{idx}"
        }
        assert requests.post('https://127.0.0.1:5000/api/records/', data=json.dumps(md),
                      headers={
                          'Content-Type': 'application/json'
                      },
                      verify=False).status_code == 201
