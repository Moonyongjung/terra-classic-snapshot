import json

def result_json(snapshot_info_val):
    result_list = []
    for _, value in enumerate(snapshot_info_val):
        val_dict = {
            value[0]:value[1]
        }
        result_list.append(val_dict)

    with open("./result/snapshot_result.json", "w") as f:
        json.dump(result_list, f, indent=4)

