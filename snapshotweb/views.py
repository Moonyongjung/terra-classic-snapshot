
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from snapshotweb.snapshot_all.query_cw20 import query_cw20
from snapshotweb.snapshot_specific.query_cw20_spec import query_cw20_spec
from snapshotweb.util.result import result_json

@csrf_exempt
def snapshot_main(request):
    if request.method == "GET":
        return render(request, 'index.html')

    if request.method == "POST":     
        block_height = request.POST["blockHeight"]
        account_address = request.POST["accountAddress"]
        contract_address = request.POST["contractAddress"]
        print("Request standard block height : " + block_height)
        print("Contract address : " + contract_address)
        print("User account : " + account_address)

        block_height = block_height.strip()
        account_address = account_address.strip()
        contract_address = contract_address.strip()

        if block_height == "" or contract_address == "":
            context = {
                'snapshot_info_val': "Input Block Height and Contract Address",
                'confirm': False,
            }
            return render(request, 'index.html', context)            

        else:
            if account_address == "":
                snapshot_info_val = query_cw20(block_height, contract_address)
            else:
                snapshot_info_val = query_cw20_spec(block_height, account_address, contract_address)
            
            context = {
                'snapshot_info_val': snapshot_info_val,
                'confirm':True,
            }
            
            result_json(snapshot_info_val)

            return render(request, 'index.html', context)
            
