from flask import current_app
from invenio_oaiserver.provider import OAIIDProvider
from invenio_pidstore.minters import recid_minter


def minter(record_uuid, data):
    pid = recid_minter(record_uuid, data)

    if '_oai' not in data:
        data['_oai'] = {}
    oaipid = OAIIDProvider.create(
        object_type='rec', object_uuid=record_uuid,
        pid_value=current_app.config['OAISERVER_ID_PREFIX'] + pid.pid_value).pid
    data['_oai']['id'] = oaipid.pid_value

    return pid
