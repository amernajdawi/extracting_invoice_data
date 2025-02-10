#!/bin/bash
set -e

# Check if Ollama is already running by testing port 11434.
if nc -z localhost 11434; then
  echo "Ollama is already running on port 11434. Skipping serve command."
else
  echo "Starting Ollama..."
  /bin/ollama serve &
  pid=$!
fi

echo "Waiting for Ollama to be ready..."
# Wait until the Ollama API becomes responsive.
until ollama list > /dev/null 2>&1; do
  sleep 2
done

MODEL_NAME="${LLM_MODEL_VERSION}"
if ollama list | grep -q "$MODEL_NAME"; then
  echo "Model '$MODEL_NAME' already available."
else
  echo "Retrieving model: '$MODEL_NAME'"
  ollama pull "$MODEL_NAME"
  echo "Model '$MODEL_NAME' is now ready!"
fi

# If we started the service, wait for it to finish.
if [ -n "${pid:-}" ]; then
  wait $pid
fi
