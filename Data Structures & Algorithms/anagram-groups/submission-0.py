class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        set_of_sorted_texts = set()
        matched_texts = dict()
        res = []

        for i in range(len(strs)):
            sorted_text = "".join(sorted(strs[i]))

            if sorted_text in set_of_sorted_texts:
                matched_texts[sorted_text].append(strs[i])
            else:
                matched_texts.setdefault(sorted_text, []).append(strs[i])
                set_of_sorted_texts.add(sorted_text)
        
        for k, v in matched_texts.items():
            res.append(v)

        return res