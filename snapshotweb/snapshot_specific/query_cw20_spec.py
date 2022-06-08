import asyncio
import multiprocessing
from terra_sdk.client.lcd import LCDClient
from snapshotweb.snapshot_specific.balance_check import balance_check
from snapshotweb.snapshot_specific.tx_specific_user import tx_specific_user
from snapshotweb.util.util import set_config

def query_cw20_spec(block_height, account_address, contract_address):
    loop = asyncio.new_event_loop()
    manager = multiprocessing.Manager()
    snapshot_info_val = manager.list() 

    query_work_spec(block_height, loop, snapshot_info_val, account_address, contract_address)

    return snapshot_info_val


def query_work_spec(snapshot_block_height, loop, snapshot_info_val, account_address, contract_address):    
    asyncio.set_event_loop(loop)
    terra_classic_url_mainnet, _ = set_config()        
    lcd_client = LCDClient(terra_classic_url_mainnet, "columbus-5")    

    map_acc_balance = balance_check(lcd_client, contract_address, account_address)

    tx_specific_user(map_acc_balance, snapshot_block_height, contract_address, snapshot_info_val)