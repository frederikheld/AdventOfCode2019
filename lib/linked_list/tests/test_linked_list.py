import pytest

from lib.linked_list.linked_list import ListNode


def test_listnode_init():
    lnode = ListNode()
    assert isinstance(lnode, ListNode)
    assert lnode.getValue() == None
    assert lnode.getPrev() == None

    value = 'foo'
    prev = ListNode()
    lnode2 = ListNode(value, prev)
    assert lnode2.getValue() == value
    assert lnode2.getPrev() == prev


def test_listnode_setprev():
    lnode = ListNode()
    assert lnode.getPrev() == None
    lnode.setPrev(ListNode('hello'))
    assert lnode.getPrev().getValue() == 'hello'


def test_listnode_getlist():
    lnode1 = ListNode('This')
    lnode2 = ListNode('is', lnode1)
    lnode3 = ListNode('Sparta!', lnode2)

    assert lnode3.getList() == ['Sparta!', 'is', 'This']


def test_listnode_getlist_reversed():
    lnode1 = ListNode('This')
    lnode2 = ListNode('is', lnode1)
    lnode3 = ListNode('Sparta!', lnode2)

    assert lnode3.getList(True) == ['This', 'is', 'Sparta!']


def test_listnode_getlist_multiple():
    """
            G - H       J - K - L
           /           /
    COM - B - C - D - E - F
                   \
                    I
    """

    COM = ListNode('COM')
    B = ListNode('B', COM)
    C = ListNode('C', B)
    D = ListNode('D', C)
    E = ListNode('E', D)
    F = ListNode('F', E)

    G = ListNode('G', B)
    H = ListNode('H', G)

    I = ListNode('I', D)

    J = ListNode('J', E)
    K = ListNode('K', J)
    L = ListNode('L', K)

    assert F.getList() == ['F', 'E', 'D', 'C', 'B', 'COM']
    assert H.getList() == ['H', 'G', 'B', 'COM']
    assert I.getList() == ['I', 'D', 'C', 'B', 'COM']
    assert L.getList() == ['L', 'K', 'J', 'E', 'D', 'C', 'B', 'COM']
