def make_set_of_files(files):
    set_of_files = set()
    for i in files:
        set_of_files.add(i[0])
    return set_of_files


def duplicate(path):
    import os
    from pathlib import Path
    from filecmp import cmp

    DATA_DIR = Path(path)
    files = sorted(os.listdir(DATA_DIR))

    duplicateFiles = []

    for file_x in files:
        if_dupl = False

        for class_ in duplicateFiles:
            if_dupl = cmp(DATA_DIR / file_x, DATA_DIR / class_[0], shallow=False)
            if if_dupl:
                class_.append(file_x)
                break

        if not if_dupl:
            duplicateFiles.append([file_x])
    set_of_files = make_set_of_files(duplicateFiles)
    return set_of_files
