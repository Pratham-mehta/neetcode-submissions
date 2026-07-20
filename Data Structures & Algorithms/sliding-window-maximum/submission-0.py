from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Initialize the deque (indices, values decreasing), L, and output.
        q = deque()
        L = 0
        output = []

        for R in range(len(nums)):
            # Step 2: Expand — pop dead weight from the BACK (values smaller
            # than the newcomer can never be a window max again), then push R.
            while q and nums[q[-1]] < nums[R]:
                q.pop()
            q.append(R)

            # Step 3: Evict — if the front's index slid out of the window, drop it.
            if q[0] < L:
                q.popleft()

            # Step 4: Record — once the window is full, the front IS the max.
            if R + 1 >= k:
                output.append(nums[q[0]])
                L += 1

        return output