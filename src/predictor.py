import ktrain

class Predictor():
    def setup(self):
        self.predictor = ktrain.load_predictor('content/model.pth')

    def predict(self, content):
        return self.predictor.predict(content)
