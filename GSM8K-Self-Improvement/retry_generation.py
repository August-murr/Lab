from script import RunInitializerRetry

mongo_url = "your_mongodb_string"
retry_run_name = "your_retry_run_name"
mongo_db_collection_name = "gsm8k_dataset"
run_name = "your_run_name"

run_initializer_retry = RunInitializerRetry(mongo_url, mongo_db_collection_name)
run_initializer_retry.initialize_retry_run(run_name, retry_run_name)

from script import DatabaseHandlerRetry,ModelHandler,ResponseProcessorRetry,RunManagerRetry

model_path = "path_to_model"

instance_name_0 = "instance_name_gpu0"
instance_name_1 = "instance_name_gpu1"
batch_size = 10

db_handler = DatabaseHandlerRetry(mongo_url, mongo_db_collection_name, retry_run_name)#Connecting to database
model_handler_0 = ModelHandler(model_path, "cuda:0") #load model on gpu 1
model_handler_1 = ModelHandler(model_path, "cuda:1") #load second model on gpu 2

with open("one_shot_prompt_path", "r") as file:
    one_shot_prompt = file.read()

with open("retry_prompt_path", "r") as file:
    retry_prompt = file.read()

response_processor = ResponseProcessorRetry(one_shot_prompt,retry_prompt)

run_manager = RunManagerRetry(db_handler, model_handler_0, model_handler_1, response_processor, instance_name_0, instance_name_1, batch_size)
run_manager.main_loop()