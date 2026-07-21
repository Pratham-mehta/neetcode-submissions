class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1 : Tally frequencies
        count = {}
        for x in nums:
            count[x] = count.get(x,0)+1
        
        # Step 2 : Initialize N+1 buckets, indexed by frequency
        buckets = [[] for _ in range(len(nums)+1)]

        # step 3 : fill buckets - each element goes into buckets [its frequency]
        for x, freq in count.items():
            buckets[freq].append(x)
        
        # Step 4 : Harvest from the HIGH end down until we have k elements
        result = []
        for freq in range(len(buckets)-1, 0, -1):
            for x in buckets[freq]:
                result.append(x)
                if len(result) == k:
                    return result
        
        return result