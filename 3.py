class ModelBasedReflexAgent:
    def __init__(self):
        self.location = (0, 0)
        self.model = {}

    def perceive(self, state):
        self.model[self.location] = state

    def act(self):
        if self.location in self.model:
            current_state = self.model[self.location]
            if current_state == 'dirty':
                print(f"Cleaning at {self.location}")
                return 'clean'
            else:
                print(f"Location {self.location} is clean. Moving to the next.")
                self.move()
        else:
            print(f"No information about {self.location}. Assuming clean and moving.")
            self.move()

    def move(self):
        new_loc = (self.location[0], self.location[1] + 1)
        print(f"Moving to {new_loc}")
        self.location = new_loc

agent = ModelBasedReflexAgent()
agent.perceive('dirty')  
agent.act()  
agent.act()  
agent.perceive('clean')  
agent.act()  
