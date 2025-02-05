class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        result=[]
        diction=collections.defaultdict(int)
        for domain in cpdomains:
            count,domains=domain.split(" ")

            current_domain=""

            dom=domains.split(".")[::-1]

            for d in dom:
                if current_domain=="":
                    current_domain=d
                else:
                    current_domain=d+"."+current_domain
                diction[current_domain]+=int(count)
        for keys in diction:
            result.append(str(diction[keys]) + " " + keys) 
        return result

        
     


