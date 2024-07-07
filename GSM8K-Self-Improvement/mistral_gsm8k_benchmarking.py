mongo_url = "your_mongodb_string"
#import Initializer module
from script import RunInitializer
run_name = "your_run_name"
mongo_db_collection_name = "gsm8k_dataset"
initializer = RunInitializer(mongo_url, mongo_db_collection_name)#Assuming the gsm8k datasets are in mongodb

# Initialize a new run with the train or test set
initializer.initialize_run('gsm8k_test', run_name)# choose between gsm8k_train or gsm8k_test

from script import DatabaseHandler, ModelHandler, ResponseProcessor, RunManager

model_path = "path_to_model"

instance_name_0 = "instance_name_gpu0"
instance_name_1 = "instance_name_gpu1"
batch_size = 10

db_handler = DatabaseHandler(mongo_url, mongo_db_collection_name, run_name)#Connecting to database
model_handler_0 = ModelHandler(model_path, "cuda:0") #load model on gpu 1
model_handler_1 = ModelHandler(model_path, "cuda:1") #load second model on gpu 2

with open("one_shot_prompt_path", "r") as file:
    one_shot_prompt = file.read()

with open("retry_prompt_path", "r") as file:
    retry_prompt = file.read()

response_processor = ResponseProcessor(one_shot_prompt,retry_prompt)

run_manager = RunManager(db_handler, model_handler_0, model_handler_1, response_processor, instance_name_0, instance_name_1, batch_size)
run_manager.main_loop()