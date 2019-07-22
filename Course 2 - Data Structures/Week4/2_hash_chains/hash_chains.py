# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        # self.elems = []
        self.table = {}

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            # self.write_chain(cur for cur in reversed(self.elems)
            #             if self._hash_func(cur) == query.ind)
            if query.ind in self.table:
                self.write_chain(self.table[query.ind])
            else:
                self.write_chain([])
        else:
            # try:
                # ind = self.elems.index(query.s)
            ind = self._hash_func(query.s)
            # except ValueError:
            #     ind = -1
            if query.type == 'find':
                # self.write_search_result(ind != -1)
                if ind in self.table:
                    self.write_search_result(query.s in self.table[ind])
                else:
                    self.write_search_result(ind in self.table)
            elif query.type == 'add':
                # if ind == -1:
                #     self.elems.append(query.s)
                if ind not in self.table:
                    self.table[ind] = []
                # self.table[ind].append(query.s)
                if query.s not in self.table[ind]:
                    self.table[ind].insert(0, query.s)
            else:  # del
                # if ind != -1:
                #     self.elems.pop(ind)
                if ind in self.table:
                    if query.s in self.table[ind]:
                        self.table[ind].remove(query.s)

    def process_queries(self):
        n = int(input())
        # n = 12
        # test = [
        #     "add world",
        #     "add HellO",
        #     "check 4",
        #     "find World",
        #     "find world",
        #     "del world",
        #     "check 4",
        #     "del HellO",
        #     "add luck",
        #     "add GooD",
        #     "check 2",
        #     "del good",
        # ]
        for i in range(n):
            # self.process_query(Query(test[i].split()))
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    # proc = QueryProcessor(5)
    proc.process_queries()
