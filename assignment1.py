class MLModel:
    def __init__(self,model_name,algorithm):
        self.model_name=model_name
        self.algorithm=algorithm
        self.is_trained=False

    def train(self,data_size):
        print(f"Training {self.model_name} on {data_size} samples")
        self.is_trained=True

    def predict(self,input):
        if self.is_trained ==True:
            print(f"Predicting for:{input}")
        else:
            print("Train the model first!")

    def get_info(self):
        print(f"Model name:{self.model_name}\n Algorithm:{self.algorithm}\n Trained:{self.is_trained}")
        
m1=MLModel("maza","algo1")
m2=MLModel("maze","algo2")
m1.train(1000)
m1.predict("sample a")
m1.get_info()
m2.train(2000)
m2.predict("sample b")
m2.get_info()
