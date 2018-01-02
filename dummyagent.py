import spade


class DummyAgent(spade.agent.Agent):
    def setup(self):
        print("Hello World! I'm agent {}".format(str(self.jid)))

dummy = DummyAgent("your_jid@127.0.0.1", "secret")
dummy.stop()
