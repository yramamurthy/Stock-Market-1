class Job:

    def __init__(self, fun_name, *parameters):
        self.fun_name = fun_name
        self.args = parameters
