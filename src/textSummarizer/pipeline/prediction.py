from textSummarizer.config.configuration import Configurationmanager
from transformers import AutoTokenizer
from transformers import pipeline

 class predictionpipeline:
     def __init__(self):
         self.config = Configurationmanager().get_model_evaluation_config()
         
    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        generation_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}
        
        pipe = pipeline("summarization", model=self.config.model_path, tokenizer=tokenizer)
        
        print("dialogue:")
        print(text)
        
        prediction = pipe(text,**gen_kwargs)[0]["summarization_text"]
        print("prediction:")
        print(prediction)
        
        return output