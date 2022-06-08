import asyncio
import multiprocessing
from terra_sdk.client.lcd import LCDClient

from snapshotweb.snapshot_all.collect_tokenholder import collect_token_holder
from snapshotweb.snapshot_all.tx_each_user import tx_each_user
from snapshotweb.util.util import set_config

def query_cw20(block_height, contract_address):
    loop = asyncio.new_event_loop()
    manager = multiprocessing.Manager()
    snapshot_info_val = manager.list()

    query_work(block_height, loop, snapshot_info_val, contract_address)

    return snapshot_info_val

    
def query_work(snapshot_block_height, loop, snapshot_info_val, contract_address):
    asyncio.set_event_loop(loop)
    terra_classic_url_mainnet, _ = set_config()        
    lcd_client = LCDClient(terra_classic_url_mainnet, "columbus-5")

    all_account_list = collect_token_holder(lcd_client, contract_address)

    tx_each_user(all_account_list, snapshot_block_height, contract_address, snapshot_info_val)