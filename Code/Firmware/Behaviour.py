import Body
import Network

class SwarmBehaviour():
    def __init__(self):
        self.body = Body.SwarmBody()
        self.network = Network.SwarmNetwork()

        return True

    def get_state(self):
        state = self.body.get_state_info()
