import json

def set_config():
    with open('./snapshotweb/config/config.json', 'r') as f:
        json_data = json.load(f)
    terra_classic_url_mainnet = json_data["terra_classic_url_mainnet"]
    terra_classic_url_fcd = json_data["terra_classic_url_fcd"]    

    return terra_classic_url_mainnet, \
        terra_classic_url_fcd
        