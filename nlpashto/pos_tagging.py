import torch, os
from transformers import AutoTokenizer, AutoModelForTokenClassification
from torch.utils.data import DataLoader
from .dataset_utils import SequenceTaggingDataset
if torch.cuda.is_available():device = torch.device("cuda")
else:device = torch.device("cpu")

class POSTagger():
    def __init__(self, batch_size=None):
        self.batch_size=batch_size or 16
        self.max_len=128
        self.model_path='ijazulhaq/pashto-pos'
        self.model=AutoModelForTokenClassification.from_pretrained(self.model_path).to(device)
        self.tokenizer=AutoTokenizer.from_pretrained(self.model_path)    
        self.id2label=self.model.config.id2label
    
    def tag(self,sequences=None):
        assert isinstance(sequences,list),"input sequences should be a List of List of strings"
        input_ids_,attention_mask_,segments_=[],[],[]
        for tokens_ in sequences:
            input_ids,segments=[],[]
            for token in tokens_:
                sub_token_ids = self.tokenizer.encode(token)[1:-1]
                input_ids.extend(sub_token_ids)  
                segments.append(len(sub_token_ids))
                segments.extend([0]*(len(sub_token_ids)-1))
            segments_.append(segments)
            cls_id= self.tokenizer.encode(self.tokenizer.cls_token, add_special_tokens=False)
            sep_id= self.tokenizer.encode(self.tokenizer.sep_token, add_special_tokens=False)  
            input_ids=cls_id+input_ids+sep_id
            attention_mask=[1]*len(input_ids)
            attention_mask=attention_mask+[0]*(self.max_len-len(attention_mask))
            input_ids=input_ids+[0]*(self.max_len-len(input_ids))   
            input_ids_.append(input_ids) 
            attention_mask_.append(attention_mask) 
        encodings = {'input_ids':input_ids_,'attention_mask':attention_mask_}
        
        dataset = SequenceTaggingDataset(encodings)
        dataloader = DataLoader(dataset,batch_size=self.batch_size)
        
        self.model.eval()
        preds_,input_ids_=[],[]
        for batch in dataloader:
            input_ids=batch['input_ids'].to(device)
            attention_mask=batch['attention_mask'].to(device)
            with torch.no_grad():output = self.model(input_ids=input_ids,attention_mask=attention_mask)
            predictions = output['logits'].argmax(dim=-1)
            predictions = predictions.detach().cpu().clone().numpy()
            preds_.extend(predictions) 
            input_ids_.extend(input_ids.detach().cpu().clone().numpy().tolist())   

        word_n_tags=[]
        special_idx=self.tokenizer.all_special_ids
        excluded_idx=[t for t in special_idx if t!=self.tokenizer.unk_token_id]
        for idx, preds, original_tokens, segments in zip(input_ids_, preds_, sequences, segments_):
            bert_tokens=[self.tokenizer.convert_ids_to_tokens(id_) for id_ in idx if id_ not in excluded_idx]
            preds=preds[1:len(bert_tokens)+1]
            preds=[self.id2label[item] for item in preds]
            segment_tags=[preds[i] for i,parts in enumerate(segments) if parts>0]
            word_n_tag=[(word, tag) for word,tag in zip(original_tokens,segment_tags)]
            word_n_tags.append(word_n_tag)
        return word_n_tags