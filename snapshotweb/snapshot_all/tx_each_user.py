import time
import requests
from snapshotweb.util.tx_calc import all_transactions

from snapshotweb.util.util import set_config

def tx_each_user(all_account_list, snapshot_block_height, contract_address, snapshot_info_val):
    _, terra_classic_url_fcd = set_config()
    offset = "0"
    count = 0
    #-- Transaction of each user
    #   Snapshot balance = Now balance - transaction having amount after specific block height 
    for i in range(len(all_account_list)):
        print("Target Account : " + all_account_list[i][0])
        count = count + 1
        print("Holder number : " + str(count))
        is_break = False
        account_info = []

        while True:
            if is_break == True:
                offset = "0"
                break

            time.sleep(1)
            response = requests.get(terra_classic_url_fcd+"/v1/txs?account="+all_account_list[i][0]
            +"&offset="+offset
            +"&limit=100")
            res = response.json()

            if len(res["txs"]) == 0:
                offset = "0"
                break               

            offset, is_break, account_info = all_transactions(
            i, 
            res, 
            snapshot_block_height, 
            all_account_list, 
            contract_address, 
            is_break)  
        
        snapshot_info_val.append(account_info)