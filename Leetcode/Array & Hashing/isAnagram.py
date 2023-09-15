class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        for item in s:
            if(item in freq):
                freq[item] += 1
            else:
                freq[item] = 1

        for item in t:
            if(item not in freq):
                #item not in hashmap so delete it
                return False
            if(item in freq):
                freq[item] -= 1

            #when it reaches 0 we got to delete the item 
            if freq[item] == 0:
                del freq[item]
            
                
    
    #now just check if hashmap is empty or not. if its empty then we know all the elements exists since they got cancelled 
        if not freq:
            
            return True
        else:
            return False


Tester = Solution()
print(Tester.isAnagram("race", "care"))
        

        


        
        

