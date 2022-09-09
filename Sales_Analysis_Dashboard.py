# Initialize Libraries and Dependencies
# Dashboard for visualization - front end
import streamlit as st
# Data manipulation
import pandas as pd
# path to file directory holding csv
from pathlib import Path
# Visualization
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="ProximoSpiritsAssessment",
    page_icon="📊",
    layout= "wide"    
)

# Set the path to the 'Sales.csv' file
csv_path = Path('./Resources/new_sales_df.zip')

#Read in the 'Sales.csv' file
sales_df = pd.read_csv(csv_path)

###########
# Dashboard
###########

st.title("Sales Analysis")
# st.write(sales_df)

tab1, tab2, tab3, = st.tabs(["Best Sales Month", "Product sold per city", "Ad times"])
with tab1:
    col1, col2 = st.columns(2)
    col1.subheader("Best Sales Month")
    col1.dataframe(sales_df[['Order ID', 'Product', 'Quantity Ordered', 'Price Each', 'Order Date', 'Month', 'Total Sales']])
    col2.subheader("Sales per Month")
    months = range(1,13)
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.bar(months,sales_df.groupby(['Month']).sum()['Total Sales'])
    plt.xticks(months)
    plt.title('Best Sales Month')
    plt.ylabel('Sales in USD ($)')
    plt.xlabel('Number of Month')
    col2.pyplot(plt.show())
    col2.write("in q4 the sales spike, this can be for a number of reasons, one potentially being holiday season.")
    
with tab2:
    
    col1, col2 = st.columns(2)
    col1.subheader("Product sold per City")
    col1.write(sales_df.groupby(['City']).sum())
    keys = [city for city, df in sales_df.groupby(['City'])]
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.bar(keys,sales_df.groupby(['City']).sum()['Total Sales'])
    plt.title('Product sold per City')
    plt.ylabel('Sales in USD ($)')
    plt.xlabel('City')
    plt.xticks(keys, rotation='vertical', size=10)
    col2.pyplot(plt.show())
    col2.write("San Francisco has the most sales followed by Los Angeles and New York City.")
    
with tab3:
    col1, col2 = st.columns(2)
    col1.subheader("Ad Times")
    col1.dataframe(sales_df[['Order ID', 'Product', 'Quantity Ordered', 'Price Each', 'Order Date', 'Purchase Address', 'Month', 'Address', 'City', 'State', 'Total Sales', 'Hour', 'Minute', 'Count']])
    keys = [pair for pair, df in sales_df.groupby(['Hour'])]
    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.plot(keys, sales_df.groupby(['Hour']).count()['Count'])
    plt.title('Ad Times')
    plt.xticks(keys)
    plt.xlabel('Hour of Day')
    plt.grid()
    col2.pyplot(plt.show())
    col2.write("Around 11am and 7pm we have peaks in our data. It may make the most sence to advertise around that time.")
    
             
             
             




