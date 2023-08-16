#양방향 리스트

class DNode:
    def __init__(self, item, prev = None, next = None):
        self.item = item
        self.prev = prev
        self.next = next
        
class DList:
    def __init__(self):
        self.head = None
    
    def insert_front(self, item):
        dnode = DNode(item, None, self.head)
        
        first = self.head
        if (first != None): #첫번째꺼에 이미 어떤게 있다면
            first.prev = dnode  #previous 이전값 저장시키기
        self.head = dnode   #리스트 맨앞자리 정보 바꿔주기
        
    # **********
    def insert_back(self, item):
        # 비어있는 경우
        if (self.head == None):     
            self.insert_front(item)
            return
        
        dnode = DNode(item, None, None)
        
        #노드 찾기
        #last의 next는 new
        #new의 prev는 last 
        last = self.head
        while last.next:
            last = last.next
        last.next = dnode
        dnode.prev = last
    # **********
    
        
    def print_list(self):
        if self.head == None:
            print("empty")
        else:
            p = self.head
            while p:
                if p.next != None:
                    print(p.item, '<->', end =' ')
                else:
                    print(p.item)
                p = p.next
                
    def delete_front(self):
        target = self.head
        if target != None:
            self.head = target.next
            if (self.head):
                self.head.prev = None
        return target
    
    def search(self, target):
        p = self.head
        while p:
            if target == p.item:
                return p
            p = p.next
        return None
    
    def delete_target(self, item):
        dnode = self.search(item)
        if (dnode == None):
            return dnode
        
        if dnode == self.head:
            self.head = dnode.next
            if self.head != None:
                self.head.prev = None
            else:
                dnode.prev.next = dnode.next
                if dnode.next != None:
                    dnode.next.prev = dnode.prev
            return dnode

            #맨 뒤에꺼 삭제하는게 불편하다 -> 원형 리스트 이용하면 된다
    
    

if __name__ == '__main__':      #import 되었을 때는 실행되지 않도록 함 
    d = DList()