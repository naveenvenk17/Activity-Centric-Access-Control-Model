# Machine class - Parent to all Machines
class Machine:

    """
    Description - Parent class to all the machines in the factory.
    Arguments :
        name <string> - name of the machine
        state <bool> - current state of the machine on/off 
        activity <string>- the process the machine does 
    """  

    def __init__(self, name='default_machine', state=0, activity='defaut_activity'):
        self.name = name
        self.state_name = state
        self.activity = activity

    def change_state(self,state):
        self.state = state
        pass
    
    def show_state(self):

        if self.state==0:
            return "{self.name} is off"
        else :
            return "{self.name} is on"
        
    def describe(self):
        return "{self.name} does {self.activity}"


