class listNode: 
    def __init__(self, key=-1, val=-1):
        self.key = key
        self.val = val 
        self.next = None
    
class MyHashMap:

    def __init__(self):
        self.buckets = [listNode() for i in range(1000)]
#self.size is an int you cannot iterate thr an int hence the requirement for range 
    def hash(self, key): 
        return key % len(self.buckets)

    def put(self, key: int, value: int) -> None:
        cur = self.buckets[self.hash(key)]
        while cur.next: 
            if cur.next.key == key: 
                cur.next.val = value 
                return 
            cur = cur.next
        cur.next = listNode(key, value)
        

    def get(self, key: int) -> int:
        cur = self.buckets[self.hash(key)].next 
        while cur: 
            if cur.key == key: 
                return cur.val 
            cur = cur.next
        return -1
 
        

    def remove(self, key: int) -> None:
        cur = self.buckets[self.hash(key)]
        while cur.next: 
            if cur.next.key == key: 
                cur.next = cur.next.next
                return 
            cur = cur.next
