# Web Scraping Project

## Description
This project is a web scraping application that collects data from specified websites and saves it in a CSV file. The project includes various Python notebooks for logic, scripts for final implementation, and logs for tracking the scraping process.

## Project Structure
- **logs/**: Contains `scraping.log` with details of the project and its execution.
- **Notebooks/**: Includes Jupyter notebooks with the logic and analysis of the project.
- **Script/**: Contains the main `.py` script for implementation and `.env` file for environment variables.
- **Result/**: The directory where the final `.csv` output file is saved.
- **venv/**: Includes `requirements.txt` for managing Python dependencies.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    ```

2. Navigate to the project directory:
    ```bash
    cd your-repo-name
    ```

3. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

5. Install the required dependencies:
    ```bash
    pip install -r venv/requirements.txt
    ```

## Usage

1. Set up environment variables in the `.env` file. Ensure that all required variables are defined.

2. Run the main script:
    ```bash
    python Script/main.py
    ```

3. Check the `Result/` directory for the output CSV file and `logs/` for execution details.

## Contributing
Feel free to fork the repository and submit pull requests for any improvements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or issues, please contact [your email address].
