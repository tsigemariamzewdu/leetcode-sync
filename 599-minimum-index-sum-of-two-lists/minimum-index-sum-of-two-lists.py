class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict_list1={}
        dict_list2={}
        result_dict=[]
        result=[]
        ans=set()

        for i,v in enumerate(list1):
            dict_list1[v]=i
        for j,val in enumerate(list2):
            dict_list2[val]=j
        for k in list1:
            if k in list2:
                result.append(k)
        for l in result:
            if l in dict_list1 and l in dict_list2:
                result_dict.append([l,dict_list1[l]+dict_list2[l]])
        result_dict.sort(key=lambda list: list[1])
        
        rmin= result_dict[0][1]
        for i in result_dict:
            if i[1]==rmin:
                ans.add(i[0])
        return list(ans)

        

        