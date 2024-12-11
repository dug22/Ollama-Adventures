import subprocess
from concurrent.futures import ThreadPoolExecutor

# Function to run Ollama service
def run_ollama():
    subprocess.Popen(["ollama", "serve"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Function to start the Ollama service in a thread
def start_service():
    with ThreadPoolExecutor() as executor:
        executor.submit(run_ollama)

# Start the service in parallel
start_service()
