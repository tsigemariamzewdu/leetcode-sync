class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        path_dict=defaultdict(list)
        for path in paths:
            dirr,*files=path.split(" ")

            for file in files:
                folder,content=file.split("(")

                path_dict[content].append(dirr+"/"+folder)
            result=[]
            for value in path_dict.values():
                if len(value)>1:
                    result.append(value)
        return result


        
                
        
        
        

        