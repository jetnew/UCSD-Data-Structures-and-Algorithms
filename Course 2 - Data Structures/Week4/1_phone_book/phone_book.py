# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

    # n = 12
    # test = [
    #     "add 911 police",
    #     "add 76213 Mom",
    #     "add 17239 Bob",
    #     "find 76213",
    #     "find 910",
    #     "find 911",
    #     "del 910",
    #     "del 911",
    #     "find 911",
    #     "find 76213",
    #     "add 76213 daddy",
    #     "find 76213",
    # ]
    # return [Query(test[i].split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    # contacts = []
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            # for contact in contacts:
            #     if contact.number == cur_query.number:
            #         contact.name = cur_query.name
            #         break
            # else: # otherwise, just add it
            #     contacts.append(cur_query)
            contacts[cur_query.number] = cur_query.name

        elif cur_query.type == 'del':
            # for j in range(len(contacts)):
            #     if contacts[j].number == cur_query.number:
            #         contacts.pop(j)
            #         break
            if cur_query.number in contacts:
                del contacts[cur_query.number]
        else:
            response = 'not found'
            # for contact in contacts:
            #     if contact.number == cur_query.number:
            #         response = contact.name
            #         break
            # result.append(response)
            if cur_query.number in contacts:
                result.append(contacts[cur_query.number])
            else:
                result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

