# AI Resume Screening & Ranking System

## Overview
The **AI Resume Screening & Ranking System** is a Streamlit-based web application that allows users to upload multiple resumes and rank them based on their relevance to a given job description. The ranking is determined using **TF-IDF Vectorization** and **Cosine Similarity**.

## Features
- Upload multiple PDF resumes.
- Input a job description.
- Automatically extract text from PDFs.
- Rank resumes based on their similarity to the job description.
- Display the ranking results in a structured format.

## Installation
### Prerequisites
Ensure you have Python installed (preferably Python 3.7+).

### Clone the Repository
```sh
git clone https://github.com/PrakratiJain17/AI-Powered-Resume-Screening-and-Ranking-System.git
cd AI-Powered-Resume-Screening-and-Ranking-System
```

### Install Dependencies
Run the following command to install the required Python packages:
```sh
pip install -r requirements.txt
```

## Usage
To start the application, run:
```sh
streamlit run app.py
```
Then, open the displayed local URL in your web browser.

## File Structure
```
.
├── app.py                  # Main Streamlit application
├── utils
│   ├── text_extraction.py  # Extracts text from PDFs
│   ├── rank_resumes.py     # Ranks resumes using TF-IDF & Cosine Similarity
├── requirements.txt        # Required dependencies
├── README.md               # Project documentation
```

## Technologies Used
- **Streamlit**: For the web UI.
- **Pandas**: For handling tabular data.
- **NumPy**: For numerical operations.
- **Scikit-learn**: For TF-IDF vectorization and similarity calculations.
- **PyPDF2**: For extracting text from PDF resumes.

## Contributing
Feel free to contribute by submitting issues or pull requests.



