
import collections
class LRUCache2(object):
    def __init__(self, capacity):
        self.cache = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        val = self.cache[key]
        del self.cache[key]
        self.cache[key] = val
        return val

    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value


def implement_LRU_cache(capacity, query_type, key, value):
    res = []
    cache = LRUCache2(capacity)
    print('key --- ', key)
    print('value --- ', value)
    kv = 0
    for i,j in enumerate(query_type):
        if j == 1:
            cache.put(key[kv], value[kv])
        if j == 0:
            res.append(cache.get(key[i]))
        kv += 1
    return res

if __name__ == "__main__":

    capacity = int(input())

    query_type_cnt = 0
    query_type_cnt = int(input())
    query_type_i = 0
    query_type = []
    while query_type_i < query_type_cnt:
        query_type_item = int(input())
        query_type.append(query_type_item)
        query_type_i += 1


    key_cnt = 0
    key_cnt = int(input())
    key_i = 0
    key = []
    while key_i < key_cnt:
        key_item = int(input())
        key.append(key_item)
        key_i += 1


    value_cnt = 0
    value_cnt = int(input())
    value_i = 0
    value = []
    while value_i < value_cnt:
        value_item = int(input())
        value.append(value_item)
        value_i += 1

    res = implement_LRU_cache(capacity, query_type, key, value);
    print('result --- ')
    for res_cur in res:
        print( str(res_cur) + "\n" )
