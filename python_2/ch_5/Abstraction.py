from abc import ABC, abstractmethod

# 1. The Blueprint (Abstract Class)
class RemoteControl(ABC):
    
    @abstractmethod
    def turn_on(self):
        """Every remote must have a way to turn something on."""
        pass

# 2. The Concrete Implementation (TV Remote)
class TVRemote(RemoteControl):
    
    def turn_on(self):
        print("TV is now ON. Showing screen...")

# 3. The Concrete Implementation (AC Remote)
class ACRemote(RemoteControl):
    
    def turn_on(self):
        print("AC is now ON. Blowing cold air...")

# --- Using the classes ---

tv = TVRemote()
tv.turn_on()  # Output: TV is now ON. Showing screen...

ac = ACRemote()
ac.turn_on()  # Output: AC is now ON. Blowing cold air...

# This would fail because you cannot instantiate the blueprint directly:
remote = RemoteControl() 
