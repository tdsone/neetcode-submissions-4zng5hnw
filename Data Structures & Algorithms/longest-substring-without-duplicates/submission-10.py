class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1: 
            return len(s)

        print("length", len(s))
        
        l, r = 0, 1
        chars2idx = {s[l]: l}
        best_length = 1
        
        while r < len(s):
            print(chars2idx, "(l,r)", l, r, "bl:", best_length, s[l:r])
            if s[r] in chars2idx: # we have seen this char before
                if chars2idx[s[r]] < l: # we have seen it before but its not in the curr subs
                    chars2idx[s[r]] = r
                    best_length = max(best_length, r - l + 1)
                    r += 1
                else: # we have seen it before and it is in the curr subs
                    l = chars2idx[s[r]] + 1
                    chars2idx[s[r]] = r
                    if l >= r:
                        r = l + 1
                    else: 
                        r += 1
            else: # we have not see it before
                chars2idx[s[r]] = r
                best_length = max(best_length, r - l + 1)
                r += 1
            print(f"\tAfter - l:{l}, r:{r}")
        
        return best_length

                
                
