# enqueue: 아이템을 추가하는 것
# dequeue: 아이템을 빼는 것(삭제되는 가장 앞에 있는 노드)

import src.utils.Dlist as Dlist

#empty 리스트 만들기
class Queue:
    def __init__(self):
        self.queue = Dlist.DList()
        self.count = 0
        
    #리스트 가장 뒤에 추가
    def enqueue(self, item):
        
        self.queue.insert_back(item)
        self.count += 1
        
    #리스트 가장 앞에서 제거
    def dequeue(self):
        if self.count > 0:
            self.count -= 1
            dnode = self.queue.delete_front()
            return dnode.item
        return None
    
    def print_queue(self):
        self.queue.print_list()
        
    def size(self):
        return self.count


if __name__ == '__main__':
    q = Queue()
    
    print("---enqueue---")
    q.enqueue('mango')
    q.enqueue('apple')
    q.enqueue('orange')
    q.print_queue()
    
    print('\n')
    
    print("---dequeue---")
    q.dequeue()
    q.print_queue()
    q.dequeue()
    q.print_queue()
    q.dequeue()
    q.print_queue()