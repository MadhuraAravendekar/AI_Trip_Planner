# End-To-End Agentic AI | AI Based Travel Planner with LLMOPS

### UV related command 
- To check which uv version is avalibale on the system
    -  ```uv --version```
- To download the uv software using pip command for windows
    - ```pip install uv```
- To intialize a folder inside the uv 
    - ```uv init folder_name``` 

### By default env will get activated using conda however for this project we are using uv so we deactive this env
```conda activate base```

```conda deactivate```

### To check the python version avaliable 
```uv python list```

### Creating a virtual environment name 'env' using uv 
```uv venv env```

### Activating the environment by env->Scripts->copy the path for activate.bat file-> copy the path to terminal and hit enter
```C:\Users\arave\AI_Trip_Planner\env\Scripts\activate.bat```

### To check what all libraries are present in the env
```uv pip list```

### Installing the langchain library for this project
```uv pip install langchain```

### To get all the command list we have typed in the terminal 
```doskey/history```

## How to activate your server which is the streamlit.

### To start the server 
```streamlit run streamlit_app.py```

### To execute all the api into the new terminal
```uviorn main:app --reload --port 8000```