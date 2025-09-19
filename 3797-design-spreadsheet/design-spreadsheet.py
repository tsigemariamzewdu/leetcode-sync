class Spreadsheet:

    def __init__(self, rows: int):
        self.rows=rows
        self.cells={}
        

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell]=value
        

    def resetCell(self, cell: str) -> None:
        if cell in self.cells:
            self.cells[cell]=0
        

    def getValue(self, formula: str) -> int:
        val=0
        formula=formula[1:]
        left,right=formula.split("+")
        if left.isdigit():
            val+=int(left)
        else:
            val+=self.cells.get(left,0)

        if right.isdigit():
            val+= int(right)
        else:
            val +=self.cells.get(right,0)
        return val

        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)