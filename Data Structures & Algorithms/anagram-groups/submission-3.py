from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = []

        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if len(strs[i]) == len(strs[j]):
                    if sorted(strs[i]) == sorted(strs[j]):

                        found = False

                        for group in words:
                            if i in group or j in group:
                                if i not in group:
                                    group.append(i)
                                if j not in group:
                                    group.append(j)
                                found = True
                                break

                        if not found:
                            words.append([i, j])

        # Add words that never had an anagram
        for k in range(len(strs)):
            found = False
            for group in words:
                if k in group:
                    found = True
                    break
            if not found:
                words.append([k])

        # Convert indices back to strings
        result = []
        for group in words:
            result.append([strs[index] for index in group])

        return result