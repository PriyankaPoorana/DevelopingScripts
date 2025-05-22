import pandas as pd
import pandera.pandas as pa
import numpy as np
from datetime import datetime, timedelta

# Creating a Sample Dataframe
df=pd.DataFrame({
"Treatment_id": [1,2,3,4],
"Patient_name": ['Anusha','Regina','James','Victor'],
"Age":[30,21,45,60],
"Contact_Email":["Anushasheik23@gmail.com","ReginaWilliamsst@gmail.com","MackeyJ45@yahoo.com","greatvictor@gmail.com"],
"Gender":["F","F","M","M"],
"Treatment_date": ['2023-02-15','2024-05-30','2025-05-25','2025-01-23'],
"Treatment_code":["509","34","103","600"],
"Duration_of_treatment_in_hrs":[1,2,3,5]})
#Converting the date columns to date_time
df['Treatment_date']=pd.to_datetime(df['Treatment_date'],format="%Y-%m-%d")
#Creating the schema for validation
schema = pa.DataFrameSchema({
    "Age": pa.Column(int),
    "Patient_name": pa.Column(str),
    "Gender": pa.Column(str, pa.Check.isin(["M", "F", "O"])),
    "Treatment_date": pa.Column("datetime64[ns]", 
                             pa.Check(lambda s: s.max() >= datetime.now() - timedelta(days=30), 
                                      name="max_date_within_last_month")),
    "Treatment_code":pa.Column(str, pa.Check(lambda s: s.str.len().between(0, 3), name="column_length_check")),
    "Contact_Email": pa.Column(float, pa.Check(lambda s: s.isna().mean() < 0.1, name="null_percentage_check")),
    "Contact_Email": pa.Column(str, pa.Check.str_matches(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")),
    "Duration_of_treatment_in_hrs": pa.Column(int, pa.Check.ge(0)),
    "Treatment_id": pa.Column(int, unique=True)
})

#Validating the data using the schema declared
validated_df = schema.validate(df)
print(validated_df)

