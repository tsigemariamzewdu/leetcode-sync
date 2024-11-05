class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cp=collections.defaultdict(int)

        for cpdomain in cpdomains:
            current=cpdomain.split(" ")
            count= int(current[0])
            domain = current[1]
            
            currentdomain= ""
            for sub in domain.split('.')[::-1]:
                if currentdomain =="":
                    currentdomain =sub
                else:
                    currentdomain=sub + "." + currentdomain
                cp[currentdomain] += count
        results=[]
        for key in cp.keys():
            results.append(str(cp[key])+ " "+ key)
        return results


