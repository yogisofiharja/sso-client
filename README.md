Setting Up Environment

To create a Python virtual environment (venv), follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to create the venv.
3. Run the following command to create the venv:

    ```
    python3 -m venv myenv
    ```

    Replace `myenv` with the desired name for your virtual environment.

4. Activate the venv by running the appropriate command based on your operating system:

    - For macOS and Linux:

      ```
      source myenv/bin/activate
      ```

    - For Windows:

      ```
      myenv\Scripts\activate
      ```

5. You are now inside the virtual environment. Install any Python packages or dependencies you need using `pip`.

Remember to include the venv directory in your `.gitignore` file to avoid committing it to version control.

Install modules
  ```
  pip install streamlit
  pip install python-dotenv
  pip install pyjwt
  ```
To run Application

  ```
  streamlit run app.py
  ```

  If you want to run on the specific port:

  ```
  streamlit run app.py --server.port <port>
  ```