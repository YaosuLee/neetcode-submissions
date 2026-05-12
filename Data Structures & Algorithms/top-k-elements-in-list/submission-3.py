import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
        heap = []
        min_h = []
        print(a)
        for num in a.keys():
            if len(heap) < k:
                heapq.heappush(heap, (a[num], num))
            elif (a[num], num) > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (a[num], num))

        return [x[1] for x in heap]
       

            

            
