class Solution:
    def groupAnagrams(self, strs):
        hashtable = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))

            if sorted_string not in hashtable:
                #make a new empty entry
                #an entry is key and value
                hashtable[sorted_string] = []
        
            #at that key add the value
            hashtable[sorted_string].append(string)
        
        #convert the hashtable to list 
        return list(hashtable.values())

Tester = Solution()
print(Tester.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

