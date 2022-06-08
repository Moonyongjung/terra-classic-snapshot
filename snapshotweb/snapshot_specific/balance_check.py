def balance_check(lcd_client, contract_address, account_address):
    map_acc_balance = []
    token = lcd_client.wasm.contract_query(
        contract_address,
        {
            "balance":{
                "address":account_address
            }
        }
    )
    
    #-- Mapping using list [accountaddress, balance]
    map_acc_balance.append(account_address)
    map_acc_balance.append(token)

    return map_acc_balance