class Solution:

    def encode(self, strs: List[str]) -> str:
        # Step 1 & 2: Prefix each string with its length, then concatenate all chunks.
        return ''.join(f"{len(s)}#{s}" for s in strs)
    def decode(self, s: str) -> List[str]:
        result = []  # Step 1: Initialize
        pos = 0

        while pos < len(s):
            # Step 2: Read the length prefix, scanning up to the '#'
            delim = s.index('#', pos)
            length = int(s[pos:delim])

            # Step 3: Read exactly `length` characters as the payload
            start = delim + 1
            result.append(s[start : start + length])

            # Step 4: Advance pos past this chunk and repeat
            pos = start + length

        return result
