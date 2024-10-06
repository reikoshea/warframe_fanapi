from pymongo import MongoClient
import os.path
import yaml
import requests

_config = {}


def load_config():
    global _config
    if not _config:
        with open('config.yaml', 'r') as infile:
            try:
                _config = yaml.safe_load(infile)
            except yaml.YAMLError as exc:
                print('Unable to load config.yaml')
                print(exc)

def get_db_handle():
    global _config
    load_config()
    client = MongoClient(host=_config['db']['host'],
                         port=int(_config['db']['port']),
                         username=_config['db']['username'],
                         password=_config['db']['password']
                        )
    db_handle = client[_config['db']['name']]
    return db_handle, client

def load_db(refresh=True):
    mhandle, mclient = get_db_handle()
    for i in ['weapons', 'warframes', 'items']:
        if refresh:
            mhandle[i].drop()
        r = requests.get('https://api.warframestat.us/{}/search/%20/?by=description'.format(i))
        mhandle[i].insert_many(r.json())
