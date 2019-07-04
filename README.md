# How to get the data

Since much of the data gathered with Google Fit is *PII Category 0* health information, they do not provide direct 
access via an API (or at least not without a lot of faffing about).

You can, however, download the data via Google's 'Takeout' service, which will allow you access to pretty much 
everything Google has on you.  

https://takeout.google.com/

Once downloaded, unzip and play with the CSV to your heart's content :)


### Jupyter

Running the Jupyter notebooks in Jupyter in PyCharm Community is painful.

```
pip install -r requirements.txt
python -m ipykernel install --user --name venv --display-name "Python3 (venv)"
jupyter notebook
```
