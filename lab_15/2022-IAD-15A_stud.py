import random


class BinarySearchTree:
    '''
    Klasa reprezentuje binarne drewo poszukiwan
    '''
    __slots__ = ["root", "heights"]
    class Node:
        __slots__ = ["value", "left", "right", "height"]
        
        def __init__(self, value, left = None, right = None, height = 0):
            self.value = value
            self.left = left
            self.right = right
            self.height = height

    def __init__(self):
        self.root = None
        self.heights = []

    def insert(self, value):
        if self.root is None:
            self.root = BinarySearchTree.Node(value)
            return
        temp = self.root
        while True:
            if temp.value == value:
                raise ValueError("Wartosc juz znajduje sie w drzewie!")
            if value < temp.value:
                if temp.left is None:
                    temp.left = BinarySearchTree.Node(value, temp.height + 1)
                    self.heights.append(temp.left.height)
                    return
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = BinarySearchTree.Node(value, temp.height + 1)
                    self.heights.append(temp.right.height)
                    return
                temp = temp.right

    def __str__(self):
        def __str_helper(n):
            if n is None:
                return ""
            else:
                return "(" + __str_helper(n.left) + str(n.value) + __str_helper(n.right) + ")"
        return __str_helper(self.root)

    def wysokosc_drzewa(self):
        return self.heights
    
    def odbij(self):
        pass

def odbij_strukture(n):
    if n is None:
        return None
    return BinarySearchTree.Node(None, odbij_strukture(n.right), odbij_strukture(n.left))

def main():
    print("************************ Metoda odbij ************************")

    '''t0 = BinarySearchTree()
    for el in [2, 4, 6]:
        t0.insert(el)
    t0o = t0.odbij()
    print(f"Test 0:      {t0o}")
    print(f"Powinno byc: (((2)4)6)")
    print()

    t1 = BinarySearchTree()
    for el in [10, 5, 15, 11, 12]:
        t1.insert(el)
    t1o = t1.odbij()
    print(f"Test 1:      {t1o}")
    print(f"Powinno byc: ((5((10)11))12(15))")
    print()

    t2 = BinarySearchTree()
    for el in [242, 137, 336, 270, 341, 179, 73, 195, 5, 191, 247, 140, 329, 414, 235]:
        t2.insert(el)
    t2o = t2.odbij()
    print(f"Test 2:      {t2o}")
    print(f"Powinno byc: ((((5)73)137((140)179(191)))195((((235)242(247))270(329))336(341(414))))")'''

    print("\n******************* Metoda wysokosc_drzewa *******************")

    s0 = BinarySearchTree()
    print(f"Test 0:      ", end="")
    for el in [2, 4, 6]:
        print(s0.wysokosc_drzewa(), end=", ")
        s0.insert(el)
    print(s0.wysokosc_drzewa())
    print(f"Powinno byc: 0, 0, 1, 2")
    print()

    s1 = BinarySearchTree()
    print(f"Test 1:      ", end="")
    for el in [10, 5, 15, 11, 12]:
        print(s1.wysokosc_drzewa(), end=", ")
        s1.insert(el)
    print(s1.wysokosc_drzewa())
    print(f"Powinno byc: 0, 0, 1, 1, 2, 3")
    print()

    s2 = BinarySearchTree()
    print(f"Test 2:      ", end="")
    for el in [242, 137, 336, 270, 341, 179, 73, 195, 5, 191, 247, 140, 329, 414, 235]:
        print(s2.wysokosc_drzewa(), end=", ")
        s2.insert(el)
    print(s2.wysokosc_drzewa())
    print(f"Powinno byc: 0, 0, 1, 1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 4, 4, 4")


    print("\n********************* Obie metody na raz *********************")

    '''r0 = BinarySearchTree()
    print(f"Test 0:      ", end="")
    for el in [2, 4, 6]:
        print(r0.wysokosc_drzewa(), end=", ")
        r0.insert(el)
        r0 = r0.odbij()
    print(r0.wysokosc_drzewa(), end=", ")
    print(r0)
    print(f"Powinno byc: 0, 0, 1, 1, ((2)4(6))")
    print()

    r1 = BinarySearchTree()
    print(f"Test 1:      ", end="")
    for el in [10, 5, 15, 11, 12]:
        print(r1.wysokosc_drzewa(), end=", ")
        r1.insert(el)
        r1 = r1.odbij()
    print(r1.wysokosc_drzewa(), end=", ")
    print(r1)
    print(f"Powinno byc: 0, 0, 1, 2, 2, 3, (((5(10))11(12))15)")
    print()

    r2 = BinarySearchTree()
    print(f"Test 2:      ", end="")
    for el in [242, 137, 336, 270, 341, 179, 73, 195, 5, 191, 247, 140, 329, 414, 235]:
        print(r2.wysokosc_drzewa(), end=", ")
        r2.insert(el)
        r2 = r2.odbij()
    print(r2.wysokosc_drzewa(), end=", ")
    print(r2)
    print(f"Powinno byc: 0, 0, 1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, ((((5(73(137)))140(((179)191)195((235)242)))247(270))329(336(341(414))))")
    print()'''



if __name__ == "__main__":
    main()