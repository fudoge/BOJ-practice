class hashTable():
    def __init__(self, size):
        self.size = size
        self.table = [None for _ in range(self.size)]
    
    def _func(self, key):	#해시 함수
        a = 0
        for i in range(len(key)):
            a = ord(key[i])
        return a % self.size
    
    def _add(self, key, value):	#해시 함수에 값 추가. 같은 슬롯에 값이 있으면, 그 뒤에 연결한다.
        idx = self._func(key)
        if self.table[idx] == None:
            self.table[idx] = [[key, value]]
        else:
            self.table[idx].append([key, value])
    
    def _del(self, key):	#해시 함수에서 해당 key를 가진 값 제거.
        idx = self._func(key)
        if self.table[idx] == None:	#일단 해싱된 값이 비면 없다는 뜻이고,
            print("No data", key ,"!")
        else:
            for i in range(len(self.table[idx])):
                if self.table[idx][i][0] == key:
                    self.table[idx].pop(i)
                    return
            print("No data", key ,"!")	#탐색하고 나서도 없으면 역시 없다는 뜻이니 없다고 출력한다.
            
    def _printAll(self):	#해시 함수 전체 출력
        for i in range(self.size):
            print(self.table[i])
            
    def _search(self, key):	#탐색. 제거하는 함수와 비슷하다.
        idx = self._func(key)
        if self.table[idx] == None:
            print("No data", key ,"!")
        else:
            for i in range(len(self.table[idx])):
                if self.table[idx][i][0] == key:
                    print(self.table[idx][i][1])
                    return 
            print("No data", key ,"!")
            

a = hashTable(5)
a._add('서울', '02')
a._add('경기', '031')
a._add('인천', '032')
a._printAll()
print("///")
a._del('채운')
a._search('경기')
print("///")
a._del('서울')
a._printAll()