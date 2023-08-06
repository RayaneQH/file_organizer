def isEmpty(path):
    import os

    if not os.listdir(path):
        return False
    else:
        return True
