class RandomizedSet(object):
    def __init__(self):
        self.map = dict()
        self.lst = list()

    def insert(self, x) -> bool:
        if x in self.map.keys():
            return False
        self.lst.append(x)
        self.map[x] = len(self.lst) - 1
        return True

    def remove(self, x) -> bool:
        assert len(self.map.keys()) == len(self.lst)
        if x not in self.map.keys():
            return False
        idx = self.map[x]
        last = self.lst[-1]
        # 交换last与idx元素位置后，删除last
        self.lst[idx] = last
        self.map[last] = idx
        self.lst.pop(-1)
        self.map.pop(x)
        return True

    def find(self,x):
        if x in self.map.keys():
            return self.lst[self.map[x]]
        return None
