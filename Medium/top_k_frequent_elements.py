class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = defaultdict(list)
        for key, cnt in Counter(nums).items():
            frq[cnt].append(key)

        res = []
        for times in reversed(range(len(nums) + 1)):
            res.extend(frq[times])
            if len(res) >= k: return res[:k]

        return res[:k]
        '''
        d = {}
        result = []
        
        if k == len(nums):
            return nums
        
        for val in nums:
            if val in d:
                d[val] += 1
            else:
                d[val] = 1
                
        counter = collections.Counter(d)
        print(counter)
        results = counter.most_common(k)
        print(results[0])
                
        #return result
        '''
        