echo "Modifications to this script is required! Modify it where it suits your needs."
echo "Installing Ollama on your environment"
curl -fsSL https://ollama.com/install.sh | sh
echo "Starting Ollama Service"
python path/to/the/ollama_thread.py
echo "Pulling the specified Ollama model"
ollama pull <model_type>
echo "Installing LangChain Ollama's integration package"
pip install langchain-ollama
