# OSM-Traffic-Sign
## Overview
This project interacts with the OpenStreetMap API to upload data points. It supports both development and production environments.

# Folder Structure
```
OSM-Traffic-Sign
├── keys/
│   ├── dev_keys.py
│   ├── out.txt
│   └── prod_keys.py
├── utils/
│   ├── get_access_token.py
│   ├── upload.py
│   └── utils.py
├── .gitignore
├── main.py
└── README.md
```
## Files Description
`keys/`
    `dev_keys.py`: Contains development API keys and endpoints.
    `prod_keys.py`: Contains production API keys and endpoints.
    `out.txt`: Stores the access token.

`utils/`
    `get_access_token.py`: Script to obtain the access token.
    `upload.py`: Handles the upload of data points to the OpenStreetMap API.
    `utils.py`: Contains utility functions like creating changesets, nodes, and generating comments.
    
`main.py`: Main script to parse arguments and execute the upload process.
`.gitignore`: Specifies files and directories to be ignored by Git.