class Policy:
    """Policy for every object in the ecosystem.

    Every policy contains the following:
    * policy_number 
    * object_name 
    * source_name 
    * activity_name
    * Conditions(pre, post and current) are a list of lists of the format
        [[object1, acitivity, value], [object2, acitivity, value],...]
    """

    policy_number = None
    object_name = ""
    source_name = ""
    activity_name = ""
    pre_condition = []
    current_condition = []
    post_condition = []

    def __init__(self, policy_number, object_name, source_name, activity_name, pre_condition, current_condition, post_condition):
        self.policy_number = policy_number
        self.object_name = object_name
        self.source_name = source_name
        self.activity_name = activity_name
        self.pre_condition = pre_condition
        self.current_condition = current_condition
        self.post_condition = post_condition

        

    

        
        
