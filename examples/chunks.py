def chunks(list_, chunk_size):
    """Yield successive chunks of length chunk_size from list_"""
    for i in range(0, len(list_), chunk_size):
        yield list_[chunk_size:i + chunk_size]