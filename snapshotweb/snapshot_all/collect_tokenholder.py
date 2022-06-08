def collect_token_holder(lcd_client, contract_address):
    start_after_account = ""
    query_msg = {}
    count = 0
    all_account_list = []

    #-- Collect all users have the token
    while True:
        try:
            if start_after_account == "":
                query_msg = {
                    "all_accounts": {
                        "limit": 30                 
                    }
                }
            else:
                query_msg = {
                    "all_accounts": {
                        "limit": 30,
                        "start_after":start_after_account
                    }
                }

            contract_query_accounts = lcd_client.wasm.contract_query(
                contract_address,
                query_msg            
            )        

            start_after_account = contract_query_accounts["accounts"][-1]
            count = count + len(contract_query_accounts["accounts"])

            #-- Balances of token that each user has
            for j in range(len(contract_query_accounts["accounts"])):
                map_acc_balance = []

                token = lcd_client.wasm.contract_query(
                    contract_address,
                    {
                        "balance":{
                            "address":contract_query_accounts["accounts"][j]
                        }
                    }
                )
                
                #-- Mapping using list [accountaddress, balance]
                map_acc_balance.append(contract_query_accounts["accounts"][j])
                map_acc_balance.append(token)

                #-- All account list
                all_account_list.append(map_acc_balance)
            print("token holder... : " + str(count))       

        except IndexError:
            print("token holder... : " + str(count))
            break
    
    print("The number of total token holder : " + str(count))
    print("--------------------")

    return all_account_list