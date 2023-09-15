import heapq

class Solution:
    def topKFrequent(self, nums, k):
        # Create a hashtable to store the frequency of each number
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1

        # Use a min-heap to keep track of the top k frequent elements
        heap = []
        for num, freq in freq_dict.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        # Extract the top k frequent elements from the min-heap
        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])

        return result[::-1]  # Reverse the result to get the elements in descending order of frequency




Tester = Solution()
print(Tester.topKFrequent([9,23,12,2,2,2,3,3,0,0,0,0,4,23,1], 3))