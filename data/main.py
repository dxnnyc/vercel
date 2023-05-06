from flask import Flask
import pandas as pd

df = pd.read_csv('./data/diagnoses2019.csv')

df.column