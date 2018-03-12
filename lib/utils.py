def get_config(filename):
    import ujson
    try:
        with open(filename) as f:
            config = ujson.load(f)
        return config
    except OSError as e:
        print("Error reading {}: {}".format(filename, str(e)))
        return None
