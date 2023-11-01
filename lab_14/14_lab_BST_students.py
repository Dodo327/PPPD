'''
Kartka 6, zadanie 6.10
'''

# kod z ćwiczeń
class BinarySearchTree:
    '''
    Klasa reprezentuje binarne drewo poszukiwan
    '''
    __slots__ = ["root"]
    class Node:
        __slots__ = ["value", "children"]
        def __init__(self, value, left = None, right = None):
            self.value = value
            self.children = [left, right]

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BinarySearchTree.Node(value)
            return
        temp = self.root
        while True:
            if temp.value is value:
                return
            if value < temp.value:
                if temp.children[0] is None:
                    temp.children[0] = BinarySearchTree.Node(value)
                    return
                temp = temp.children[0]
            else:
                if temp.children[1] is None:
                    temp.children[1] = BinarySearchTree.Node(value)
                    return
                temp = temp.children[1]

    def insert_rec(self, value):
        def _insert(temp):
            if temp.value == value:
                return          # nie chcemy duplikatow
            if value < temp.value:
                if temp.children[0] is None:
                    temp.children[0] = BinarySearchTree.Node(value, None, None)
                else:
                    _insert(temp.children[0])
            else:
                if temp.children[1] is None:
                    temp.children[1] = BinarySearchTree.Node(value, None, None)
                else:
                    _insert(temp.children[1])
        if self.root is None:
            self.root = BinarySearchTree.Node(value, None, None)
        else:
            _insert(self.root)

    def search(self, value):
        tmp = self.root
        while tmp is not None:
            if tmp.value == value:
                return True
            elif tmp.value > value:
                tmp = tmp.children[0]
            else:
                tmp = tmp.children[1]
        return False

    def search_rec(self, value):
        def _search(tmp):
            if tmp is None:
                return False
            elif tmp.value == value:
                return True
            elif tmp.value > value:
                return _search(tmp.children[0])
            else:
                return _search(tmp.children[1])
        return _search(self.root)

    def items(self):
        def _items(tmp, x):
            if tmp is None:
                return 
            _items(tmp.children[0], x)
            x.append(tmp.value)
            _items(tmp.children[1], x)

        x = []
        _items(self.root, x)
        return x

    def __repr__(self):
        string =''
        for element in self.items():
            string += f'{element} '
        return string

    def pop_max(self):
        if self.root is None:
            return None
        if self.root.children[1] is None:
            ral = self.root.value
            self.root = self.root.children[0]
            return ral
        tmp = self.root
        

def main():
    T = BinarySearchTree()
    T.insert(50)
    T.insert_rec(30)
    T.insert(20)
    T.insert(35)
    T.insert_rec(25)
    T.insert(26)
    T.insert(28)
    T.insert(27)
    T.insert(70)
    T.insert_rec(65)
    T.insert(80)
    T.insert(75)
    T.insert(76)
    T.insert(74)
    T.insert(62)
    T.insert_rec(77)

    # print(T)
    #
    #print(T.search(75))
    #print(T.search(74))
    #print(T.search_rec(75))
    #print(T.search_rec(74))
    #print(T.search(81))
    #print(T.search(22))
    #print(T.search_rec(81))
    #print(T.search_rec(22))
    #
    print(T)
    # print(T.pop_min())
    # print(T)
    # print(T.pop_max())
    # print(T)

if __name__ == "__main__":
    main()