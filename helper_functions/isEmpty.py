def isEmpty(path, json_file):
    import os
    import json
    dir=os.listdir(path)
    situ:str|bool=""
    with open(json_file, "r") as json_file:
        data=json.load(json_file)
    if len(dir)=0:
        situ="empty"
        return situ, data, dir
    else:
        for i in dir:
            if i not in data["categories"]:
                return situ, data, dir
            else:
                situ="organized"
                return situ, data, dir
