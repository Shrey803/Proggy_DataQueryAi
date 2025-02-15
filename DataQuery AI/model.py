from transformers import TapasTokenizer, TapasForQuestionAnswering
import pandas as pd

class DataQueryModel:
    def __init__(self):
        self.tokenizer = TapasTokenizer.from_pretrained('google/tapas-base-finetuned-wtq')
        self.model = TapasForQuestionAnswering.from_pretrained('google/tapas-base-finetuned-wtq')
    
    def process_query(self, question, table):
        # Convert table to DataFrame and ensure all values are strings
        table_for_tapas = pd.DataFrame(table).astype(str)
        
        # Ensure column names are strings
        table_for_tapas.columns = table_for_tapas.columns.astype(str)
        
        # Clean the data (handle missing values)
        table_for_tapas = table_for_tapas.fillna('')
        
        # Convert question to string if not already
        question = str(question)
        
        # Tokenize inputs
        inputs = self.tokenizer(
            table=table_for_tapas,
            queries=[question],  # Wrap question in a list
            padding='max_length',
            return_tensors="pt"
        )
        
        # Get model outputs
        outputs = self.model(**inputs)
        
        # Convert logits to predictions
        predicted_answer_coordinates, predicted_aggregation_indices = self.tokenizer.convert_logits_to_predictions(
            inputs,
            outputs.logits.detach().cpu().numpy(),
            outputs.logits_aggregation.detach().cpu().numpy()
        )
        
        # Decode the predicted answer
        predicted_answer = self.tokenizer.convert_ids_to_tokens(predicted_answer_coordinates[0])
        
        # Return the first prediction (with error handling)
        if predicted_answer and len(predicted_answer) > 0 and len(predicted_answer[0]) > 0:
            return predicted_answer[0][0]
        else:
            return "No answer found"