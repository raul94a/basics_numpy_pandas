# How to select data from DataFrames using Pandas
------
Tutorial made by Raúl Albín.

Andalucía, Spain

## Example table
| customer_id | year_of_birth | educational_level marital_status | annual_income purhcase_date | recency      | online_purchases | store_purchases | complaints | calls | intercoms |     |     |     |
| ----------- | ------------- | -------------------------------- | --------------------------- | ------------ | ---------------- | --------------- | ---------- | ----- | --------- | --- | --- | --- |
| 228         | 20201929      | 1996                             | PhD                         | Widowed      | 79930.0          | 8/8/2012        | 72         | 3     | 8         | 0   | 9   | 11  |
| 415         | 20202116      | 1997                             | PhD                         | Married      | 75865.0          | 3/31/2014       | 73         | 3     | 10        | 0   | 3   | 11  |
| 111         | 20201812      | 1995                             | PhD                         | Divorced     | 68126.0          | 11/10/2012      | 40         | 7     | 5         | 0   | 3   | 7   |
| 182         | 20201883      | 1997                             | Master                      | Single       | 66835.0          | 9/28/2013       | 21         | 6     | 13        | 0   | 3   | 6   |
| 412         | 20202113      | 1994                             | PhD                         | Widowed      | 66465.0          | 3/30/2013       | 1          | 11    | 12        | 0   | 3   | 11  |
| 249         | 20201950      | 1994                             | Master                      | Married      | 65176.0          | 10/29/2012      | 57         | 9     | 6         | 0   | 3   | 11  |
| 150         | 20201851      | 1997                             | Master                      | Married      | 59354.0          | 4/24/2014       | 59         | 4     | 7         | 0   | 3   | 11  |
| 112         | 20201813      | 1996                             | Master                      | Single       | 57288.0          | 6/25/2014       | 27         | 8     | 8         | 0   | 3   | 6   |
| 449         | 20202150      | 1997                             | PhD                         | Married      | 55707.0          | 12/22/2013      | 91         | 3     | 9         | 0   | 3   | 11  |
| 180         | 20201881      | 1995                             | PhD                         | Widowed      | 51650.0          | 5/11/2014       | 81         | 4     | 4         | 0   | 3   | 4   |
| 149         | 20201850      | 1996                             | Master                      | Single       | 49605.0          | 6/21/2014       | 65         | 2     | 4         | 0   | 3   | 5   |
| 114         | 20201815      | 1998                             | PhD                         | Relationship | 43974.0          | 12/12/2012      | 19         | 6     | 6         | 0   | 3   | 6   |
| 386         | 20202087      | 1998                             | Master                      | Married      | 43795.0          | 10/16/2013      | 11         | 7     | 4         | 0   | 3   | 11  |
| 446         | 20202147      | 1994                             | Master                      | Divorced     | 42618.0          | 10/9/2013       | 92         | 5     | 4         | 0   | 3   | 11  |
| 83          | 20201784      | 2000                             | Master                      | Widowed      | 38620.0          | 5/11/2013       | 56         | 2     | 3         | 0   | 3   | 11  |
| 420         | 20202121      | 1995                             | PhD                         | Divorced     | 37401.0          | 5/6/2014        | 14         | 2     | 3         | 0   | 3   | 11  |
| 452         | 20202153      | 2000                             | Master                      | Single       | 36230.0          | 10/17/2013      | 17         | 2     | 4         | 0   | 3   | 11  |
| 384         | 20202085      | 1996                             | Master                      | Widowed      | 36143.0          | 3/30/2014       | 33         | 0     | 2         | 0   | 3   | 11  |
| 229         | 20201930      | 1997                             | PhD                         | Single       | 34320.0          | 2/16/2014       | 66         | 1     | 2         | 0   | 3   | 11  |
| 250         | 20201951      | 1995                             | Master                      | Divorced     | 31160.0          | 9/16/2013       | 59         | 2     | 3         | 0   | 3   | 11  |
| 255         | 20201956      | 2000                             | PhD                         | Married      | 30899.0          | 10/13/2012      | 35         | 1     | 3         | 0   | 3   | 11  |
| 183         | 20201884      | 1998                             | Master                      | Relationship | 30477.0          | 1/22/2014       | 16         | 1     | 3         | 0   | 3   | 2   |
| 322         | 20202023      | 2000                             | PhD                         | Relationship | 26476.0          | 2/9/2014        | 6          | 1     | 2         | 0   | 3   | 11  |


##### Imagine a variable called data which owns a dataframe from the table provided above. Something like this: 

```python
import pandas as pd
#download this repository in order to have access to the CSV
data = pd.read_csv('data/project_data.csv')
```
###### Select a value
When selecting a value from a dataFrame, you must use the iloc or loc attributes to avoid future errors:
- loc attribute allows splicing and indexing using the explicit index. This means that if we want to access the second column of the first row (0,1) of the dataframe, maybe it could not be possible if the column has a name different to 1. In the case of the dataFrame provided by this example, the way of accessing the second element of the first row is the following: 

```python
print(data.loc[0,'year_of_birth ']) #1982
```
- iloc attribute allows to use the normal integer splicing
```python
#will have the same result as the loc example
print(data.iloc[0,1]) #1982
``` 
###### column selection
```py
#this will print the annual_income column from the table
print(data['annual_income])
```

###### row selection
```py
#this will return the row. It can be called as the numeric index
#or even a string, depending on the data scientist
#when working with pandas is recommended to use dataframe.loc 
#or dataframe.iloc in order to access indexes
print(data.loc[0])

#slice works with row accessing
print(data.loc[0:5])

#also you can access a specified number of rows and columns.
#For example, we can slice the first ten rows and first five columns of
#the dataframe.
#a table of ten rows and five columns (50 records) will be printed
#CAPTION: iloc is necessary when accessing columns by index!
print(data.iloc[:10,:5])

```

###### More complex data selection
```py
#The general structure for selecting data by boolean masking is:
boolean_mask = data['educational_level'] == 'Master'

#It will display rows with a educational_level of Master
print(data[boolean_mask])

#more complex selection can be performed when combining column values matching
selector = list((data['educational_level'] == 'Master') & (data['annual_income'] > 70000))
#it will print records with educational level of Master and anual income > 70000
print(data[selector])

#How about searching several posible values within a column? 
#(i.e: wanting to search customers born only in 1994 or 1996) 
#isin method will make work for us

selectorA = data['annual_income'] < 30000

##Now is time to use isin. We're gonna search educational_level values matching
##with Basic or PhD.

##isin receives a list of values. It will fetch the records
##that fit any of element within the list
selectorB = data['educational_level'].isin(['Basic','PhD'])
selector = list((selectorA) & (selectorB))

##after boolean masking, a column selection by fancy indexing
# and sorting is performed. See that operational chaining could be so powerful
print(data.loc[selector,['complaints','annual_income','educational_level','recency']]
    .sort_values(by=['complaints', 'annual_income'], ascending=False))
```