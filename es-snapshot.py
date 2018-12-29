from boto.connection import AWSAuthConnection

class ESConnection(AWSAuthConnection):

    def __init__(self, region, **kwargs):
        super(ESConnection, self).__init__(**kwargs)
        self._set_auth_region_name(region)
        self._set_auth_service_name("es")

    def _required_auth_capability(self):
        return ['hmac-v4']

if __name__ == "__main__":

    client = ESConnection(
            region='us-west-2',
            host='vpc-test-fgo4ad36abibtmilnadvisjdfiskd.us-west-2.es.amazonaws.com',
            aws_access_key_id='INSERT_YOU_KEY_ID',
            aws_secret_access_key='INSERT_YOU_SECRET_KEY'
            )

    print 'Registering Snapshot Repository'
    resp = client.make_request(method='PUT',
            path='/_snapshot/es-backups',
            data='{"type": "s3","settings": { "bucket": "es-snapshots-rappi","region": "us-west-2","role_arn": "arn:aws:iam::581653423581:role/es-snapshot-role"}}')
    body = resp.read()
    print body
