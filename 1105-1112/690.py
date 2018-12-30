"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def __init__(self):
        self.res = 0
        
    def update(self, employees, id):
        for e in employees:
            if e.id == id:
                self.res += e.importance
                if not e.subordinates:
                    return
                else:
                    for em in e.subordinates:
                        self.update(employees, em)
                    
            
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        self.update(employees, id)
        return self.res