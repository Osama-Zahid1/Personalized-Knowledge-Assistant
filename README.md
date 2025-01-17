### **README for LlamaIndex and React Integration Project**

---

#### **Project Overview**

This project is a question-answering application powered by LlamaIndex and OpenAI, integrated with Django Rest Framework (DRF) for the backend and React for the frontend. Users can input queries via the React frontend, which are processed by the backend, leveraging the LlamaIndex for document retrieval and OpenAI for generating responses.

---

#### **Features**

1. **Frontend**: 
   - Built with React, featuring a dynamic and user-friendly interface.
   - Allows users to input queries and view responses.

2. **Backend**:
   - Django Rest Framework handles the API.
   - LlamaIndex processes and indexes documents for efficient query handling.
   - OpenAI API generates responses for user queries.

3. **Caching**:
   - Implements caching to store query responses for 24 hours to reduce redundant processing.

---

#### **Technologies Used**

- **Frontend**:
  - React (with Axios for API calls)
  - CSS for styling

- **Backend**:
  - Django Rest Framework
  - LlamaIndex for document indexing
  - OpenAI GPT models for response generation
  - Django's caching mechanism 



#### **Getting Started**

##### **1. Backend Setup**

1. **Navigate to the backend directory**:
   ```bash
   cd backend
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # For Linux/Mac
   env\Scripts\activate     # For Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the backend directory and add:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

5. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Load your documents**:
   - Place your documents (e.g., `.txt` files) in a folder named `documents` in the backend directory.

7. **Run the server**:
   ```bash
   python manage.py runserver
   ```


##### **2. Frontend Setup**

1. **Navigate to the frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Set environment variables**:
   - Create a `.env` file in the frontend directory and add:
     ```
     REACT_APP_API_URL=http://localhost:8000/api
     ```

4. **Start the React app**:
   ```bash
   npm start
   ```


#### **How It Works**

1. **React Frontend**:
   - User inputs a query in the form.
   - The query is sent to the backend via Axios.

2. **Django Backend**:
   - Checks if the query response is cached. If yes, returns the cached response.
   - If not cached, LlamaIndex processes the query by searching indexed documents.
   - OpenAI generates the final response, which is cached and returned to the frontend.

3. **Frontend**:
   - Displays the response or any error messages to the user.


#### **Environment Configuration for Deployment**

To ensure seamless deployment in different environments:

1. Use environment variables for API URLs and sensitive keys.
   - Example: `REACT_APP_API_URL` for the React app.

2. Adjust the backend settings:
   - Use a production-ready database (e.g., PostgreSQL).
   - Configure a caching backend (e.g., Redis).


#### **Key Considerations**

- **Performance**:
  - Handle large document collections efficiently by using advanced indexing tools like ElasticSearch if needed.

- **Error Handling**:
  - The app gracefully handles rate limits from OpenAI and other exceptions.

- **Security**:
  - Avoid exposing sensitive API keys (e.g., OpenAI key).
  - Use HTTPS in production.


#### **Future Improvements**

1. Add user authentication to restrict access.
2. Implement a loading spinner in React for better user experience.
3. Enhance query response speed with optimized indexing strategies.


#### **Author**

- **Osama Zahid**
- Email: zahidosama26@gmial.com


