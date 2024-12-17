#!/bin/bash


source venv/Scripts/activate
# Step 1: Change to the frontend directory
cd frontend || exit

# Step 2: Run npm build
npm run build

# Step 3: Go back to the parent directory
cd ..

# Step 4: Run the Flask app
python main.py run
