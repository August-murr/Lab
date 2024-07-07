import re
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

mongo_url = "your_mongodb_string"
collection_name = "gsm8k_dataset"
client = MongoClient(mongo_url, server_api=ServerApi('1'))                                                      
db = client[collection_name] 

def calculate_correct_answers(collection_name):
    # Connect to MongoDB
    user_secrets = UserSecretsClient()
    mongo_url = user_secrets.get_secret("mongodb")
    client = MongoClient(mongo_url, server_api=ServerApi('1')) 
    db = client['gsm8k_dataset']
    collection = db[collection_name]

    # Get the total number of documents (rows) in the collection
    total_answers = collection.count_documents({})

    # Initialize correct answers counter
    correct_answers = 0

    # Retrieve all documents from the collection
    documents = collection.find()

    # Iterate over each document
    for doc in documents:
        try:
            # Convert answers to float
            correct_answer = float(doc['correct_answer'])
            generated_answer = float(doc['generated_answer'])
            
            # Check if answers match
            if correct_answer == generated_answer:
                correct_answers += 1
        except ValueError:
            # Skip the document if conversion to float fails
            continue

    # Calculate the percentage of correct answers
    if total_answers > 0:
        correct_percentage = (correct_answers / total_answers) * 100
    else:
        correct_percentage = 0
        
    return total_answers,correct_answers,correct_percentage
    # Print the results
    print(f"Total answers: {total_answers}")
    print(f"Correct answers: {correct_answers}")
    print(f"Correct answer percentage: {correct_percentage:.2f}%")


run_name = "your_run_name"
calculate_correct_answers(run_name)