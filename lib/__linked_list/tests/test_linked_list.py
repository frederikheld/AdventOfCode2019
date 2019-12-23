import pytest

from lib.__linked_list.linked_list import ListNode


def test_listnode_init():
    lnode = ListNode()
    assert isinstance(lnode, ListNode)
    assert lnode.getValue() == None
    assert lnode.getNext() == []
    assert lnode.getPrev() == []


def test_listnode_append():
    root = ListNode('root')
    A = ListNode('A')
    root.append(A)

    assert root.getNext() == [A]
    assert A.getPrev() == [root]


def test_listnode_prepend():
    A = ListNode('A')
    B = ListNode('B')
    B.prepend(A)

    assert B.getPrev() == [A]
    assert A.getNext() == [B]


# def test_listnode_getlist():
#     lnode1 = ListNode('This')
#     lnode2 = ListNode('is', None, lnode1)
#     lnode3 = ListNode('Sparta!', None, lnode2)

#     assert lnode3.getList() == ['Sparta!', 'is', 'This']


# def test_listnode_getlist_reversed():
#     lnode1 = ListNode('This')
#     lnode2 = ListNode('is', None, lnode1)
#     lnode3 = ListNode('Sparta!', None, lnode2)

#     assert lnode3.getList(True) == ['This', 'is', 'Sparta!']


# def test_listnode_getlist_multiple():
#     """
#             G - H       J - K - L
#            /           /
#     COM - B - C - D - E - F
#                    \
#                     I
#     """

#     COM = ListNode('COM')
#     B = ListNode('B', None, COM)
#     C = ListNode('C', None, B)
#     D = ListNode('D', None, C)
#     E = ListNode('E', None, D)
#     F = ListNode('F', None, E)

#     G = ListNode('G', None, B)
#     H = ListNode('H', None, G)

#     I = ListNode('I', None, D)

#     J = ListNode('J', None, E)
#     K = ListNode('K', None, J)
#     L = ListNode('L', None, K)

#     assert F.getList() == ['F', 'E', 'D', 'C', 'B', 'COM']
#     assert H.getList() == ['H', 'G', 'B', 'COM']
#     assert I.getList() == ['I', 'D', 'C', 'B', 'COM']
#     assert L.getList() == ['L', 'K', 'J', 'E', 'D', 'C', 'B', 'COM']
