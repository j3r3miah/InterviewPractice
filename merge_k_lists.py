import heapq
import itertools


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def _mergeKLists(self, lists):
        # Compare head elements one by one on each insertion: O(k*N)
        curs = []
        for head in lists:
            curs.append(head)
        rv_head = None
        rv_cur = None
        while True:
            mincur_i = None
            mincur = None
            for i, cur in enumerate(curs):
                if cur and (mincur is None or cur.val < mincur.val):
                    mincur = cur
                    mincur_i = i
            if mincur is None:
                break
            node = ListNode(mincur.val)
            if rv_head is None:
                rv_head = node
                rv_cur = node
            else:
                rv_cur.next = node
                rv_cur = rv_cur.next
            curs[mincur_i] = mincur.next
            
        return rv_head


    def _mergeKLists(self, lists):
        # Keep track of lowest element added in last round and do a sorted
        # insertion of k elements on the next round. Unsure of complexity but
        # this sure is ugly.
        curs = []
        for head in lists:
            curs.append(head)
        rv_head = None
        last_min_node = None

        def insert(node):
            nonlocal rv_head
            nonlocal last_min_node
            if last_min_node is None:
                if rv_head is None:
                    rv_head = node
                elif node.val < rv_head.val:
                    node.next = rv_head
                    rv_head = node
                else:
                    cur = rv_head
                    while cur.next and node.val >= cur.next.val:
                        cur = cur.next
                    node.next = cur.next
                    cur.next = node
            else:
                cur = last_min_node
                while cur.next and node.val >= cur.next.val:
                    cur = cur.next
                node.next = cur.next
                cur.next = node

        while True:
            min_node = None
            for i, cur in enumerate(curs):
                if not cur:
                    continue
                node = ListNode(cur.val)
                insert(node)
                if min_node is None or node.val <= min_node.val:
                    min_node = node
                curs[i] = cur.next

            if min_node is None:
                break

            last_min_node = min_node

        return rv_head

    def mergeKLists(self, lists):
        # Use a priority queue to find the next lowest item on each round.
        # Pushing and popping in a minheap is logn so overall is O(n * log(k))
        sorted_head = None
        sorted_cur = None
        heap = []
        count = itertools.count()

        for head in lists:
            heapq.heappush(heap, (head.val, next(count), head))

        while heap:
            node = heapq.heappop(heap)[2]
            if node.next:
                heapq.heappush(heap, (node.next.val, next(count), node.next))
            if sorted_cur:
                sorted_cur.next = node
                sorted_cur = node
            else:
                sorted_head = sorted_cur = node

        return sorted_head

        
def print_list(head):
    rv = []
    while head:
        rv.append(head.val)
        head = head.next
    print(rv) 
        
if __name__ == '__main__':
    list1 = ListNode(1)
    list1.next = ListNode(4)
    list1.next.next = ListNode(5)
    list2 = ListNode(1)
    list2.next = ListNode(3)
    list2.next.next = ListNode(4)
    list3 = ListNode(2)
    list3.next = ListNode(6)
    
    print_list(list1)
    print_list(Solution().mergeKLists([list1, list2, list3]))
