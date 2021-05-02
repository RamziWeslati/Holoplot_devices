_base_set = [i for i in range(1000)]
device_3_ids = set(( i for i in _base_set if i % 3 == 0))
device_5_ids = set(( i for i in _base_set if i % 5 == 0))
device_2_ids = set(( i for i in _base_set if i % 2 == 0))