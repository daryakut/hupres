echo "Pulling recent changes..."
git pull

# Function to kill all background processes
cleanup() {
    echo "Stopping background processes..."
    kill pid_backend pid_frontend
    exit
}

# Trap CTRL+C (Signal 2) and call cleanup function
trap 'cleanup' 2

# Run commands in background and store their PIDs
echo "Starting backend..."
pushd backend
export ENV=production
uvicorn app:app --port=8000 & pid_backend=$!
popd

echo "Starting frontend..."
pushd frontend
yarn build
#yarn global add serve
serve -s dist -l 3000 & pid_frontend=$!
popd

# Optionally, wait for all background processes to finish
wait $pid1 $pid2 $pid3
