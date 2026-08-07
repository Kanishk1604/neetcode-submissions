class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        matched_texts = defaultdict(list)

        for str in strs:
            sorted_text = "".join(sorted(str))

            matched_texts[sorted_text].append(str)

        return list(matched_texts.values())