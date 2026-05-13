import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Đếm tần suất xuất hiện của từng số
        count_dict = {}
        for n in nums:
            count_dict[n] = count_dict.get(n, 0) + 1
        
        # 2. Sử dụng Min-Heap để duy trì K phần tử có tần suất cao nhất
        heap = []
        for num, freq in count_dict.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            # Nếu tần suất hiện tại lớn hơn tần suất nhỏ nhất trong heap
            elif freq > heap[0][0]: 
                heapq.heappop(heap)
                heapq.heappush(heap, (freq, num))
        
        # 3. Sử dụng List Comprehension để lấy kết quả
        return [x[1] for x in heap]