class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path_dict=defaultdict(list) #here i am gonna have an empty list for every key by default 
        for path in paths:
            dirr,*files= path.split()
            
            for f in files:
                fname,fcontent=f.split('(')
                path_dict[fcontent].append(dirr +  "/" + fname)
        result=[]
        for value in path_dict.values():
            if len(value)>1:
                result.append(value)
        return result


        