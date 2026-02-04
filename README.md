# 📘*AI-Based Trip Planner Bot*

## AI-Based Trip Planner Bot 🌍✈️

### Overview

The **AI-Based Trip Planner Bot** is an intelligent travel assistant that helps users plan complete travel itineraries with minimal input. Users only need to provide a **destination** and **trip duration**, and the system generates a **personalized, day-wise travel plan** along with budget estimates, accommodation suggestions, weather insights, and currency conversion for international trips.

This project demonstrates the use of **Large Language Models (LLMs)** and AI agents to evaluate user input, aggregate multiple information sources, and deliver a seamless end-to-end travel planning experience.

---

### Key Features

* 📍 **Personalized Itinerary Generation** – Day-wise travel plan with recommended tourist attractions
* 💰 **Budget Estimation** – Estimated cost for travel, accommodation, and food
* 🏨 **Hotel Suggestions** – AI-recommended places to stay and dine
* 🌦️ **Weather Insights** – Weather information for the selected travel dates
* 💱 **Currency Conversion** – Real-time conversion for international travel planning
* 🤖 **LLM-Powered Agent** – Intelligent response generation based on user preferences

---

### Tech Stack

* **Programming Language:** Python
* **AI / NLP:** Large Language Models (LLMs)
* **Frameworks & Tools:** LangChain / LangGraph, APIs
* **Data Sources:** OpenWeather API, Currency Exchange API, Google Map API, Google Place API, Groq API
* **Interface:** Streamlit

---

### How It Works

1. User inputs destination and number of travel days
2. AI agent processes the request using LLM reasoning
3. System generates:

   * Day-wise itinerary
   * Budget breakdown
   * Hotel and food suggestions
   * Weather forecast
   * Currency conversion (if applicable)
4. Results are returned in a clear, structured summary

---

### Use Cases

* Personal travel planning
* AI-powered recommendation systems
* Demonstration of LLM-based agent design
* End-to-end AI application development

---

### Future Enhancements

* User preference personalization (budget, interests, travel style)
* Integration with booking platforms
* Multi-language support
* Mobile application deployment

---
### **Situation**

Planning a travel itinerary is often time-consuming, requiring users to search across multiple platforms for attractions, budgets, hotels, weather conditions, and currency conversion. This fragmented process leads to poor user experience.

### **Task**

I was tasked with building an **AI-driven solution** that could simplify travel planning by automatically generating a complete and personalized trip plan using minimal user input.

### **Action**

I designed and developed an **AI-based trip planner bot** using large language models.

* Implemented an LLM-powered agent that takes destination and trip duration as input
* Generated **day-wise itineraries**, budget estimates, and recommendations for hotels and food
* Integrated external APIs for **weather forecasting** and **currency conversion**
* Structured the output into a clear, user-friendly summary to enhance usability

### **Result**

The bot successfully delivers **end-to-end trip planning in seconds**, significantly reducing manual effort for users. It demonstrates how LLMs can be used to intelligently evaluate user input, combine multiple data sources, and improve customer experience through automation and personalization.

---
## Basic command syntax used during the project.
### 1. UV related command 
- To check which uv version is avalibale on the system
    -  ```uv --version```
- To download the uv software using pip command for windows
    - ```pip install uv```
- To intialize a folder inside the uv 
    - ```uv init folder_name``` 

### 2. By default env will get activated using conda however for this project we are using uv so we deactive this env
```conda activate base```

```conda deactivate```

### 3. To check the python version avaliable 
```uv python list```

### 4. Creating a virtual environment name 'env' using uv 
```uv venv env```

### 5. Activating the environment by env->Scripts->copy the path for activate.bat file-> copy the path to terminal and hit enter
```C:\Users\arave\AI_Trip_Planner\env\Scripts\activate.bat```

### 6. To check what all libraries are present in the env
```uv pip list```

### 7. Installing the langchain library for this project
```uv pip install langchain```

### 8. To get all the command list we have typed in the terminal 
```doskey/history```

## How to activate your server which is the streamlit.

### 1. To start the server 
```streamlit run streamlit_app.py```

### 2. To execute all the api into the new terminal
```uvicorn main:app --reload --port 8000```
