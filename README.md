# How to run

## Virtualenv and invenio config

```shell
poetry install
poetry shell
```

Create/edit ``.venv/var/instance/invenio.cfg`` to:

```python
SERVER_NAME='127.0.0.1:5000'
PREFERRED_URL_SCHEME='https'

SQLALCHEMY_DATABASE_URI='sqlite:///test.db'

RATELIMIT_ENABLED=False

SEARCH_ELASTIC_HOSTS = [
    dict(host='127.0.0.1', port=9207),
]
```

## bootstrap

```shell
./bootstrap.sh
```

## Run server

```shell script
invenio run --cert server.crt --key server.key
```

## Create OAI-PMH sample set

```shell
invenio oaitest sets
```

## Create sample records

With server running:

```shell
invenio oaitest records
```

## Test some urls

Identify server
[https://127.0.0.1:5000/oai2d?verb=Identify](https://127.0.0.1:5000/oai2d?verb=Identify)

List supported metadata formats
[https://127.0.0.1:5000/oai2d?verb=ListMetadataFormats](https://127.0.0.1:5000/oai2d?verb=ListMetadataFormats)

List sets
[https://127.0.0.1:5000/oai2d?verb=ListSets](https://127.0.0.1:5000/oai2d?verb=ListSets)

List identifiers from a set
[https://127.0.0.1:5000/oai2d?verb=ListIdentifiers&metadataPrefix=oai_dc&set=test](https://127.0.0.1:5000/oai2d?verb=ListIdentifiers&metadataPrefix=oai_dc&set=test)

List records
[https://127.0.0.1:5000/oai2d?verb=ListRecords&metadataPrefix=oai_dc&set=test](https://127.0.0.1:5000/oai2d?verb=ListRecords&metadataPrefix=oai_dc&set=test)

And finally get single record
[https://127.0.0.1:5000/oai2d?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:test:3](https://127.0.0.1:5000/oai2d?verb=GetRecord&metadataPrefix=oai_dc&identifier=oai:test:3)

