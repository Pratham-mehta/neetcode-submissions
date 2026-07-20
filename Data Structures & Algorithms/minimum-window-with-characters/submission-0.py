class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # A longer t can never fit inside s.
        if len(t) > len(s):
            return ""

        # Step 1: Build the target frequency map and the have/need counters.
        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        window = {}
        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float('inf')
        L = 0

        for R in range(len(s)):
            # Step 2: Expand — add s[R]; if it just HIT its required count, have += 1.
            c = s[R]
            window[c] = window.get(c, 0) + 1
            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                # Step 3: Record — keep this window only if strictly shorter than the best.
                if (R - L + 1) < res_len:
                    res = [L, R]
                    res_len = R - L + 1

                # Step 4: Shrink — drop s[L]; if a needed char FELL BELOW its count, have -= 1.
                window[s[L]] -= 1
                if s[L] in count_t and window[s[L]] < count_t[s[L]]:
                    have -= 1
                L += 1

        # Step 5: Return the best window found, or "" if none was ever valid.
        L, R = res
        return s[L : R + 1] if res_len != float('inf') else ""