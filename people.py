"""
We'll try to understand classes in python. 
Check the resources on google classroom to ensure you have gone through everything expected.

"""
###### THESE LISTS HAVE ALREADY BEEN DEFINED FOR YOU ###############
engineer_roster = [] # A list of all instantiated engineer objects
sales_roster = [] # List of all instantiated sales objects
branchmap = {  # A dictionary of dictionaries -> Maps branchcodes to cities and branch names
    0:  { "city": "NYC", "name": "Hudson Yards"},
    1:  { "city": "NYC" , "name": "Silicon Alley"},
    2:  { "city": "Mumbai", "name": "BKC"},
    3:  { "city": "Tokyo", "name": "Shibuya"},
    4:  { "city": "Mumbai", "name": "Goregaon"},
    5:  { "city": "Mumbai", "name": "Fort"}
}
####################################################################

class Employee:
    name : str 
    age : int
    ID : int
    city : int
    branches : list[int] # This is a list of branches (as branch codes) to which the employee may report
    salary : int 

    def __init__(self, name, age, ID, city,\
                 branchcodes, salary = None):
        self.name = name
        self.age = age 
        self.ID = ID
        self.city = city
        self.branches = branchcodes
        if salary is not None: self.salary = salary
        else: self.salary = 10_000 
    
    def change_city(self, new_city:str) -> bool:
        if new_city != self.city:
            self.city = new_city
            return True
        return False
        # Change the city 
        # Return true if city change, successful, return false if city same as old city

    def migrate_branch(self, new_code:int) -> bool:
        # Should work only on those employees who have a single 
        # branch to report to. Fail for others.
        # Change old branch to new if it is in the same city, else return false.
        if len(self.branches) == 1:
            old_branch = self.branches[0]
            if old_branch in branchmap and new_code in branchmap:
                old_city = branchmap[old_branch]["city"]
                new_city = branchmap[new_code]["city"]
                if old_city == new_city:
                    self.branches[0] = new_code
                    return True
        return False

    def increment(self, increment_amt: int) -> None:
        # Increment salary by amount specified.
        self.salary += increment_amt





class Engineer(Employee):
    position : str # Position in organization Hierarchy

    def __init__(self, name, age, ID, city,\
                 branchcodes, position= "Junior", salary = None):
        # Call the parent's constructor
        super().__init__(name, age, ID, city, branchcodes, salary)
        
        # Check if position is one of  "Junior", "Senior", "Team Lead", or "Director" 
        # Only then set the position. 
        valid_positions = {"Junior", "Senior", "Team Lead", "Director"}
        if position in valid_positions:
            self.position = position
        else:
            raise ValueError("Invalid position for Engineer")

    
    def increment(self, amt:int) -> None:
        # While other functions are the same for and engineer,
        # and increment to an engineer's salary should add a 10% bonus on to "amt"
        bonus = 0.1 * amt
        self.salary += amt + bonus
        
    def promote(self, position:str) -> bool:
        # Return false for a demotion or an invalid promotion
        # Promotion can only be to a higher position and
        # it should call the increment function with 30% of the present salary
        # as "amt". Thereafter return True.
        valid_promotions = {"Senior", "Team Lead", "Director"}
        if position in valid_promotions:
            # Calculate the bonus amount (30% of present salary)
            bonus = 0.3 * self.salary
            self.increment(bonus)  # Call the increment function
            return True
        return False



class Salesman(Employee):
    """ 
    This class is to be entirely designed by you.

    Add increment (this time only a 5% bonus) and a promotion function
    This time the positions are: Rep -> Manager -> Head.

    Add an argument in init which tracks who is the superior
    that the employee reports to. This argument should be the ID of the superior
    It should be None for a "Head" and so, the argument should be optional in init.
    """
    
    # An extra member variable!
    superior : int # EMPLOYEE ID of the superior this guy reports to

    def __init__(self, name, age, ID, city, branchcodes, superior=None, salary=None): # Complete all this! Add arguments
        super().__init__(name, age, ID, city, branchcodes, salary)
        self.superior = superior
    
    def promote(self, position: str) -> bool:
        # Promotion can only be to a higher position
        valid_promotions = {"Manager", "Head"}  # Positions allowed for promotion
        if position in valid_promotions:
            # Calculate the bonus amount (30% of present salary)
            bonus = 0.3 * self.salary
            self.increment(bonus)  # Call the increment function
            return True
        return False

    def increment(self, amt: int) -> None:
        # Add a 5% bonus to the salesman's salary
        bonus = 0.05 * amt
        self.salary += amt + bonus 

    def find_superior(self) -> tuple[int, str]:
        # Return the employee ID and name of the superior
        # Report a tuple of None, None if no superior.
        if self.superior is not None:
            # You can replace this with actual logic to fetch superior's name
            superior_name = "John Doe"  # Example name
            return self.superior, superior_name
        return None, None


    def add_superior(self) -> bool:
        # Add superior of immediately higher rank.
        # If superior doesn't exist return false,
        if self.superior is not None:
            new_superior = self.superior + 1
            self.superior = new_superior
            return True
        return False


    def migrate_branch(self, new_code: int) -> bool:
        # This should simply add a branch to the list; even different cities are fine
        self.branches.append(new_code)
        return True

    





    
    
