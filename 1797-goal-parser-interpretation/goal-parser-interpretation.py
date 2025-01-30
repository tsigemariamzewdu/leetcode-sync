class Solution:
    def interpret(self, command: str) -> str:
        result=[]
        for i in range(len(command)-1):
            if command[i] =="G":
                result.append("G")
            elif command[i]=="(" and command[i+1]==")":
                result.append("o")
            elif command[i]=="(" and command[i+1]=="a":
                result.append("al")
        if command[-1]=="G":
            result.append("G")
        return "".join(result)
            
        