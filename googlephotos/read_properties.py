
def read(name):
    meta_list = {}
    with open(name) as f:
        for line in f:
            if '=' in line:
                name, value = line.split("=", 1)
                name = name.strip()
                value = value.strip()
                meta_list[str(name)] = str(value)
    f.close()
    return meta_list
#=======================================================================================