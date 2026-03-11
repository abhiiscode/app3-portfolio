import streamlit as sl
import pandas

sl.set_page_config(layout="wide")

sl.header("The Best Company")
intro_content = '''
### Introduction to Google

Google LLC, founded in 1998 by Larry Page and Sergey Brin, is a global leader in technology and innovation. Originally known for its search engine, Google has expanded its services to include various products and platforms such as Android, Google Cloud, and YouTube. Headquartered in Mountain View, California, Google is renowned for its emphasis on user-centric design and cutting-edge research in AI and machine learning. The company's mission is to "organize the world's information and make it universally accessible and useful." Today, Google operates in multiple sectors, including hardware, software, and digital advertising, impacting billions of users worldwide.
'''
sl.info(intro_content)
sl.subheader("Our Team")

df = pandas.read_csv("data.csv", sep=",")

# col1, empty_col1, col2, empty_col2, col3, empty_col3 = sl.columns([1, 0.5, 1, 0.5, 1, 0.5])
col1, col2, col3 = sl.columns(3)


with col1:
    for index, row in df[:4].iterrows():
        sl.header(f"{row['first name'].title()} {row['last name'].title()}")
        sl.write(row["role"])
        sl.image('image/' + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        sl.header(f"{row['first name'].title()} {row['last name'].title()}")
        sl.write(row["role"])
        sl.image('image/' + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        sl.header(f"{row['first name'].title()} {row['last name'].title()}")
        sl.write(row["role"])
        sl.image('image/' + row['image'])