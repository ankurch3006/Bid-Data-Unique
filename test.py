import pandas as pd
import time
import vaex


# ------------------- Solution 1 ----------------------------------
# Solution 1 using set() 
# Finished in 31.91 Upload Finished in: 31.22
# Execution finished in 0.11 Output file 0.57

#start = time.perf_counter()
#df = pd.read_excel('test.xlsx')
#finish_upload = time.perf_counter()
#df_final = pd.DataFrame()
#for col in df:
#    df_final[col] = pd.Series(list(set(df[col])))
#    
#finish_execution = time.perf_counter()
#    
#df_final.to_excel('output.xlsx', index=False)
#
#final = time.perf_counter()
#print(f"Finished in {round(final-start, 2)} Upload Finished in: {round(finish_upload-start, 2)}")
#print(f"Execution finished in {round(finish_execution-finish_upload, 2)} Output file {round(final-finish_execution, 2)}")

# --------------------End Solution 1 -------------------------------


# -------------------- Solution 2 ---------------------------------
# using in-built unique() method of pandas
# Finished in 33.33 Upload Finished in: 33.22
# Execution finished in 0.08 Output file 0.04

#start = time.perf_counter()
#df = pd.read_excel('test.xlsx')
#finish_upload = time.perf_counter()
#df_final = pd.DataFrame()
#
#for col in df:
#    df_final[col] = pd.Series((df[col]).unique())
#    
#finish_execution = time.perf_counter()
#    
#df_final.to_excel('output.xlsx', index=False)
#
#final = time.perf_counter()
#print(f"Finished in {round(final-start, 2)} Upload Finished in: {round(finish_upload-start, 2)}")
#print(f"Execution finished in {round(finish_execution-finish_upload, 2)} Output file {round(final-finish_execution, 2)}")

# --------------------------------------------------------------------

# -------------------- Solution 3 ------------------------------------
# Using vaex library which uses memory mapping

#start = time.perf_counter()
#df = vaex.read_csv_and_convert('test_csv11.csv', shuffle=False, copy_index=False)
#finish_upload = time.perf_counter()
#df_final = pd.DataFrame()
#
#for col in df:
#    df_final[col] = pd.Series((df[col]).unique())
#    
#finish_execution = time.perf_counter()
#df_final.to_excel('output.xlsx', index=False)
#
#final = time.perf_counter()
#print(f"Finished in {round(final-start, 2)} Upload Finished in: {round(finish_upload-start, 2)}")
#print(f"Execution finished in {round(finish_execution-finish_upload, 2)} Output file {round(final-finish_execution, 2)}")


#df = pd.read_excel('test.xlsx')
#df.to_csv('test_csv11.csv', index=False)



## Code to create a large excel file
#df = pd.read_excel('test.xlsx')
start = time.perf_counter()
df1 = pd.DataFrame()

for _ in range(1000000):
    df2 = pd.DataFrame({"Name":['Ankur', 'Vishal', 'Makrand', 'Rahul', 'Kitchloo', 'Rohit', 'Makrand', 'Rahul', 'Kitchloo', 'Rohit'], 
                        "Place":['Ranchi', 'Patna', 'Lucknow', 'Ranchi', 'Jammu', 'Hyderabad', 'Lucknow', 'Ranchi', 'Jammu', 'Hyderabad'],
                        "Roll_No":[1, 3, 7, 4, 6, 8, 7, 4, 6, 8],
                        "Age":[25, 25, 27, 26, 24, 29, 27, 26, 24, 29]})
    
    df1 = df1.append(df2)
df1.to_csv('test11final.csv', index=False)
final = time.perf_counter()
print(f"Execution finished in {round(final - start, 2)} ")
