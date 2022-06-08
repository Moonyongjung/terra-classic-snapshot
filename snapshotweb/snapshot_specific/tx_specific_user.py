import time
import requests
from snapshotweb.util.tx_calc import all_transactions

from snapshotweb.util.util import set_config

def tx_specific_user(map_acc_balance, snapshot_block_height, contract_address, snapshot_info_val):
    _, terra_classic_url_fcd = set_config()    
    offset = "0"
    count = 0

    #-- Transaction of each user
    #   Snapshot balance = Now balance - transaction having amount after specific block height 
    print("Target Account : " + map_acc_balance[0])
    count = count + 1
    print("Holder number : " + str(count))
    is_break = False
    account_info = []

    while True:
        if is_break == True:
            offset = "0"
            break

        time.sleep(2)
        response = requests.get(terra_classic_url_fcd+"/v1/txs?account="+map_acc_balance[0]
        +"&offset="+offset
        +"&limit=100")
        res = response.json()

        if len(res["txs"]) == 0:
            offset = "0"
            break               

        offset, is_break, account_info = all_transactions(
        None, 
        res, 
        snapshot_block_height, 
        map_acc_balance, 
        contract_address, 
        is_break)  
    
    snapshot_info_val.append(account_info)