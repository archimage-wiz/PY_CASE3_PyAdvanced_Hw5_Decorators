from Hw5z2 import logger as l

class FlatIterator:
    
    path = 'py.lol.log'

    @l(path=path)
    def __init__(self, list_of_list : list):
        
        self.list_of_list = list_of_list

        def GetList(ini_list: list) -> list:
            tmp_list = []
            for x in ini_list:
                if isinstance(x, list):
                    for e in GetList(x):
                        tmp_list.append(e)
                else:
                    tmp_list.append(x)
            return tmp_list
       
        self.result_list_iterator = GetList(list_of_list).__iter__()
       
    @l(path=path)
    def __iter__(self):
       return self

    @l(path=path)
    def __next__(self):

        return self.result_list_iterator.__next__()
        

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    
    test_1()
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for x in FlatIterator(list_of_lists_2):
        print(x)

