# Efficient Synthetic Data Generation

## Overview

This project aims to maximize synthetic data generation using free tools and resources such as Kaggle notebooks and MongoDB. The script is designed to run on a Kaggle notebook equipped with two T4 GPUs, leveraging the Mistral model to generate responses to instructions (e.g., GSM8K dataset) in parallel and in batches. Threading is employed to maximize GPU utilization.

Given that each Kaggle account can operate two notebooks simultaneously, a team of multiple members can pool their resources to run several GPU instances. The script is configured to work with a MongoDB free account, allowing multiple instances to fetch batches, generate responses, and return the results to the database without interference.

## Key Features

- **Parallel Processing:** Utilizes Kaggle's dual-GPU setup to run Mistral models on each GPU.
- **Threading:** Implements threading to generate responses in parallel batches.
- **Collaborative Resource Utilization:** Supports multiple instances running concurrently, enabling collaborative efforts.
- **Database Integration:** Works seamlessly with MongoDB to handle batch fetching, processing, and updating.

## MongoDB Run Initialization

This script connects to your MongoDB and uses an instruction dataset (e.g., GSM8K questions) to create a "Run" table. The Run table enables multiple instances to connect, generate responses, and add them to the database without interfering with each other.

### Steps:

1. **Connect to MongoDB:** Ensure your MongoDB instance is running and accessible.
2. **Create Run Table:** Initialize the Run table in MongoDB with the instruction dataset.
3. **Manage Concurrent Instances:** Configure the table to allow multiple instances to fetch, process, and update data concurrently.

## Instance Script

The instance script incorporates three key features to enhance efficiency: threading, batching, and atomic operations.

### Features:

- **Threading:** Loads a quantized model on each GPU and uses threading to generate responses in parallel batches, maximizing GPU utilization.
- **Batching:** Processes data in batches to improve efficiency and manageability.
- **Atomic Operations:** Fetches batches of data atomically from the database, updates their status, assigns each batch to an instance, and updates the database post-generation.

### Workflow:

1. **Load Model:** Load the quantized Mistral model on each GPU.
2. **Threading & Batching:** Use threading to handle batch generation in parallel.
3. **Atomic Database Operations:** 
    - Fetch data batches from MongoDB.
    - Update batch status to avoid conflicts.
    - Generate responses and update the database with results.

## How to Run

1. **Set Up Kaggle Notebook:**
   - Ensure you have a Kaggle account with GPU access.
   - Clone this repository into your Kaggle notebook environment.
2. **Configure MongoDB:**
   - Set up a free MongoDB account and configure the connection settings in the script.
   - Initialize the Run table with your instruction dataset.
3. **Execute the Script:**
   - Run the instance script on Kaggle notebooks.
   - Monitor the progress and results in MongoDB.

## Contributing

Contributions are welcome! If you have suggestions for improvements or encounter any issues, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

Special thanks to the contributors and the open-source community for their invaluable support and resources.

---

By leveraging the power of Kaggle's free GPU resources and MongoDB's flexible database management, this script offers an efficient solution for large-scale synthetic data generation. Whether you're working solo or collaborating with a team, this setup ensures maximum resource utilization and seamless data handling.
