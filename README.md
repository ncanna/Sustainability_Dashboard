# Dash Analytical Web App 
Interactive web-based app built using Dash to communicate UVA sustainability's progress towards solid waste reduction. Data shown is example data for confidentiality purposes.

## Getting Started

### Running the app locally

First create a virtual environment with conda or venv inside a temp folder, then activate it.

```
virtualenv venv

# Windows
venv\Scripts\activate
# Or Linux
source venv/bin/activate

```

Clone the git repo, then install the requirements with pip

```

git clone https://github.com/ncanna/dash-waste
cd dash-waste
pip install -r requirements.txt

```

Run the app

```

python app.py

```

## About the app

This is an interactive, multi-page report which displays a variety of tables, bullet points, and Plotly interactive plots in a report format. The app incorporates custom local and external CSS to display distinct pages for PDF print.

## Built With

- [Dash](https://dash.plot.ly/) - Main server and interactive components
- [Plotly Python](https://plot.ly/python/) - Used to create the interactive plots
