import glob
import json

structure = []
for schema in glob.glob('maps/**/translation.jsonata',recursive=True):
    output_model,output_version,input_model,input_version = schema.split('/')[1:5]

    obj = {
        "output_model":output_model,
        "output_version":output_version,
        "input_model":input_model,
        "input_version":input_version,
    }
    structure.append(obj)
    
        
json.dump(structure,open('available.json','w'),indent=6)
