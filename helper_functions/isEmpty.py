def isEmpty(path):
    import os
    import json
    dir=os.listdir(path)
    situ:str|bool=""
    with open(json_file, "r") as json_file:
        data=json.load(json_file)
    if len(dir)=0:
        situ="empty"
        return situ, data
    else:
        for i in dir:
            if i not in data["categories"]:
                return situ, data
            else:
                situ="organized"
                return situ, data
