# OSM-Traffic-Sign
## Overview
This project interacts with the OpenStreetMap API to upload data points. It supports both development and production environments.

# Folder Structure
```
OSM-Traffic-Sign
├── data/
│   ├── inference/
│   │   ├── images/
│   │   │   └── *.jpg
│   │   └── meta/
│   │       └── *.xml
│   ├── train/
│   │   ├── images/
│   │   │   └── *.jpg
│   │   └── labels/
│   │       └── *.txt
├── keys/
│   ├── dev_keys.py
│   ├── out.txt
│   └── prod_keys.py
├── utils/
│   ├── train.py
│   ├── inference.py
│   ├── get_access_token.py
│   ├── upload.py
│   └── utils.py
├── .gitignore
├── main.py
└── README.md
```
## Files Description
`data/`

    `inference/`: Contains images and metadata for inference.
    `train/`: Contains images and labels for training.
    
`keys/`

    `dev_keys.py`: Contains development API keys and endpoints.
    `prod_keys.py`: Contains production API keys and endpoints.
    `out.txt`: Stores the access token.

`utils/`

    `get_access_token.py`: Script to obtain the access token.
    `upload.py`: Handles the upload of data points to the OpenStreetMap API.
    `utils.py`: Contains utility functions like creating changesets, nodes, and generating comments.
    
`main.py`: The main script is used to parse arguments and execute the upload process.

## Usage
1. The `get_access_token.py` script can be run multiple times. 1 token can last for 1 hour.
2. Go to the `keys/keys.py` and follow instructions.
3. After redirecting to the **access token**, copy and paste to the terminal.
