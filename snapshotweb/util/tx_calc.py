#-- All transactions    
def all_transactions(
    i, 
    res, 
    snapshot_block_height, 
    all_account_list, 
    contract_address, 
    is_break):

    for j in range(len(res["txs"])):
        offset = str(res["txs"][j]["id"])
        tx_height = res["txs"][j]["height"]
        print(tx_height)
        
        #-- If block height includes transaction is not bigger than snapshot block,
        #   pass
        if tx_height < snapshot_block_height:
            print("all transaction retrieve break, transaction block height :" + tx_height)
            is_break = True
            break
        else:
            for _, logs in enumerate(res["txs"][j]["logs"]):
                tx_logs_event = logs["events"]
            
                wasm_json = [events_json for events_json in tx_logs_event if events_json["type"]=="wasm"]
                if len(wasm_json) != 0:
                    print(wasm_json)
                    attributes = wasm_json[0]["attributes"]

                    if len(attributes) == 5:
                        from_val = ""
                        to_val = ""
                        amount_val = ""
                        contract_val = ""

                        for _, att_json in enumerate(attributes):                           

                            if att_json["key"]=="from":
                                from_val = att_json["value"]
                            elif att_json["key"]=="to":
                                to_val = att_json["value"]
                            elif att_json["key"]=="amount":
                                amount_val = att_json["value"]
                            elif att_json["key"]=="contract_address":
                                contract_val = att_json["value"]
                            else:
                                pass
                        
                        
                        if contract_val == contract_address:
                            if i != None:
                                if from_val == all_account_list[i][0]:                                
                                    temp = int(all_account_list[i][1]["balance"]) + int(amount_val)
                                    print("balance calc" + str(temp))
                                    all_account_list[i][1]["balance"] = str(temp)
                                elif to_val == all_account_list[i][0]:
                                    temp = int(all_account_list[i][1]["balance"]) - int(amount_val)
                                    print("balance calc" + str(temp))
                                    all_account_list[i][1]["balance"] = str(temp)
                                else:
                                    pass   
                            else:
                                if from_val == all_account_list[0]:                                
                                    temp = int(all_account_list[1]["balance"]) + int(amount_val)
                                    print("balance calc" + str(temp))
                                    all_account_list[1]["balance"] = str(temp)
                                elif to_val == all_account_list[0]:
                                    temp = int(all_account_list[1]["balance"]) - int(amount_val)
                                    print("balance calc" + str(temp))
                                    all_account_list[1]["balance"] = str(temp)
                                else:
                                    pass                   


                    elif len(attributes) == 21:
                        offer_asset = ""
                        ask_asset = ""
                        offer_amount = ""
                        return_amount = ""

                        for _, att_json in enumerate(attributes):                           

                            if att_json["key"]=="offer_asset":
                                offer_asset = att_json["value"]
                            elif att_json["key"]=="ask_asset":
                                ask_asset = att_json["value"]
                            elif att_json["key"]=="offer_amount":
                                offer_amount = att_json["value"]
                            elif att_json["key"]=="return_amount":
                                return_amount = att_json["value"]
                            else:
                                pass

                        if i != None:
                            if offer_asset == contract_address:                                
                                temp = int(all_account_list[i][1]["balance"]) + int(offer_amount)
                                print("balance calc : " + str(temp))
                                all_account_list[i][1]["balance"] = str(temp)
                            elif ask_asset == contract_address:
                                temp = int(all_account_list[i][1]["balance"]) - int(return_amount)
                                print("balance calc : " + str(temp))
                                all_account_list[i][1]["balance"] = str(temp)
                            else:
                                pass
                        else:
                            if offer_asset == contract_address:                                
                                temp = int(all_account_list[1]["balance"]) + int(offer_amount)
                                print("balance calc : " + str(temp))
                                all_account_list[1]["balance"] = str(temp)
                            elif ask_asset == contract_address:
                                temp = int(all_account_list[1]["balance"]) - int(return_amount)
                                print("balance calc : " + str(temp))
                                all_account_list[1]["balance"] = str(temp)
                            else:
                                pass

                    else:
                        print("Other case...")
    if i != None:
        return offset, is_break, all_account_list[i]
    else:
        return offset, is_break, all_account_list