import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('shopping_trends_updated.csv')

# Ensure Purchase Amount column is numeric
df['Purchase Amount (USD)'] = pd.to_numeric(df['Purchase Amount (USD)'], errors='coerce')

# Function to filter data based on user inputs
def filter_data(df, gender, category, age, shipping_type, discount_applied, season, review_rating, payment_method):
    filtered_df = df.copy()
    
    # Apply filters based on user selection
    if gender != 'Overall':
        filtered_df = filtered_df[filtered_df['Gender'] == gender]
    if category != 'Overall':
        filtered_df = filtered_df[filtered_df['Category'] == category]
    if age != 'Overall':
        filtered_df = filtered_df[filtered_df['Age'] == int(age)]
    if shipping_type != 'Overall':
        filtered_df = filtered_df[filtered_df['Shipping Type'] == shipping_type]
    if discount_applied != 'Overall':
        filtered_df = filtered_df[filtered_df['Discount Applied'] == discount_applied]
    if season != 'Overall':
        filtered_df = filtered_df[filtered_df['Season'] == season]
    if review_rating != 'Overall':
        filtered_df = filtered_df[filtered_df['Review Rating'] == review_rating]
    if payment_method != 'Overall':
        filtered_df = filtered_df[filtered_df['Payment Method'] == payment_method]
    
    return filtered_df

# Streamlit application layout
st.title("Shopping Trends Analysis")

# Sidebar for user inputs
with st.sidebar:
    st.header("Filters")
    
    # Dropdowns for selecting filters
    selected_gender = st.selectbox("Select Gender", ['Overall', 'Male', 'Female'])
    selected_category = st.selectbox("Select Category", ['Overall'] + df['Category'].unique().tolist())
    selected_age = st.selectbox("Select Age", ['Overall'] + sorted(df['Age'].unique().tolist()))
    selected_shipping_type = st.selectbox("Select Shipping Type", ['Overall'] + df['Shipping Type'].unique().tolist())
    selected_discount_applied = st.selectbox("Select Discount Applied", ['Overall'] + df['Discount Applied'].unique().tolist())
    selected_season = st.selectbox("Select Season", ['Overall'] + df['Season'].unique().tolist())
    selected_review_rating = st.selectbox("Select Review Rating", ['Overall'] + df['Review Rating'].unique().tolist())
    selected_payment_method = st.selectbox("Select Payment Method", ['Overall'] + df['Payment Method'].unique().tolist())

    # Button to trigger analysis
    show_analysis = st.button('Show Analysis')

# Filter data based on user inputs when the button is pressed
if show_analysis:
    filtered_df = filter_data(df, selected_gender, selected_category, selected_age, selected_shipping_type, selected_discount_applied, selected_season, selected_review_rating, selected_payment_method)

    # Check if there's data available after filtering
    if not filtered_df.empty:
        # Display Customer Segmentation Analysis
        st.header(f'Customer Segmentation Analysis {"" if selected_gender == "Overall" else f"for {selected_gender}"}')
        fig_customer_segmentation = px.scatter(filtered_df, x='Purchase Amount (USD)', y='Frequency of Purchases',
                                               color='Gender', title=f'Customer Segmentation Analysis {"" if selected_gender == "Overall" else f"for {selected_gender}"}')
        st.plotly_chart(fig_customer_segmentation)

        # Display Top Categories by Purchase Amount
        st.header(f'Top Categories by Purchase Amount {"" if selected_gender == "Overall" else f"for {selected_gender}"}')
        top_categories = filtered_df.groupby('Category')['Purchase Amount (USD)'].sum().reset_index()
        top_categories = top_categories.sort_values(by='Purchase Amount (USD)', ascending=False)
        fig_top_categories = px.bar(top_categories, x='Purchase Amount (USD)', y='Category',
                                    title=f'Top Categories by Purchase Amount {"" if selected_gender == "Overall" else f"for {selected_gender}"}',
                                    labels={'Category': 'Category', 'Purchase Amount (USD)': 'Total Purchase Amount'},
                                    orientation='h',
                                    color='Category')
        st.plotly_chart(fig_top_categories)

        # Display Customer Lifetime Value (CLV)
        st.header(f'Customer Lifetime Value (CLV) {"" if selected_gender == "Overall" else f"for {selected_gender}"}')
        fig_clv = px.histogram(filtered_df, x='Purchase Amount (USD)', nbins=30,
                              title=f'Customer Lifetime Value (CLV) {"" if selected_gender == "Overall" else f"for {selected_gender}"}',
                              labels={'Purchase Amount (USD)': 'Purchase Amount'})
        st.plotly_chart(fig_clv)

        # Display Purchase Amount by Discount Applied
        st.header(f'Purchase Amount by Discount Applied {"" if selected_gender == "Overall" else f"for {selected_gender}"}')
        fig_discount_applied = px.box(filtered_df, x='Discount Applied', y='Purchase Amount (USD)',
                                      title=f'Purchase Amount by Discount Applied {"" if selected_gender == "Overall" else f"for {selected_gender}"}',
                                      labels={'Discount Applied': 'Discount Applied', 'Purchase Amount (USD)': 'Purchase Amount'})
        st.plotly_chart(fig_discount_applied)

        # Display Average Purchase Amount by Shipping Type
        st.header(f'Average Purchase Amount by Shipping Type {"" if selected_gender == "Overall" else f"for {selected_gender}"}')
        avg_purchase_shipping = filtered_df.groupby('Shipping Type')['Purchase Amount (USD)'].mean().reset_index()
        fig_avg_purchase_shipping = px.bar(avg_purchase_shipping, x='Shipping Type', y='Purchase Amount (USD)',
                                           title=f'Average Purchase Amount by Shipping Type {"" if selected_gender == "Overall" else f"for {selected_gender}"}',
                                           labels={'Shipping Type': 'Shipping Type', 'Purchase Amount (USD)': 'Average Purchase Amount'})
        st.plotly_chart(fig_avg_purchase_shipping)

        # Display Distribution of Review Ratings
        st.header(f'Distribution of Review Ratings {"" if selected_gender == "Overall" else f"for {selected_gender}"}')
        fig_review_ratings = px.histogram(filtered_df, x='Review Rating', nbins=10,
                                          title=f'Distribution of Review Ratings {"" if selected_gender == "Overall" else f"for {selected_gender}"}',
                                          labels={'Review Rating': 'Review Rating'})
        st.plotly_chart(fig_review_ratings)

        # Display Top Payment Methods by Purchase Amount
        st.header(f'Top Payment Methods by Purchase Amount {"" if selected_gender == "Overall" else f"for {selected_gender}"}')
        top_payment_methods = filtered_df.groupby('Payment Method')['Purchase Amount (USD)'].sum().reset_index()
        top_payment_methods = top_payment_methods.sort_values(by='Purchase Amount (USD)', ascending=False)
        fig_top_payment_methods = px.bar(top_payment_methods, x='Purchase Amount (USD)', y='Payment Method',
                                         title=f'Top Payment Methods by Purchase Amount {"" if selected_gender == "Overall" else f"for {selected_gender}"}',
                                         labels={'Payment Method': 'Payment Method', 'Purchase Amount (USD)': 'Total Purchase Amount'},
                                         orientation='h',
                                         color='Payment Method')
        st.plotly_chart(fig_top_payment_methods)

        # # Display Frequency of Purchases by Shipping Type if data is available
        # st.header(f'Frequency of Purchases by Shipping Type {"" if selected_gender == "Overall" else f"for {selected_gender}"}')
        # if 'Frequency of Purchases' in filtered_df.columns and filtered_df['Frequency of Purchases'].dtype in ['int64', 'float64']:
        #     freq_purchases_shipping = filtered_df.groupby('Shipping Type')['Frequency of Purchases'].mean().reset_index()
        #     fig_freq_purchases_shipping = px.bar(freq_purchases_shipping, x='Shipping Type', y='Frequency of Purchases',
        #                                          title=f'Frequency of Purchases by Shipping Type {"" if selected_gender == "Overall" else f"for {selected_gender}"}',
        #                                          labels={'Shipping Type': 'Shipping Type', 'Frequency of Purchases': 'Frequency of Purchases'})
        #     st.plotly_chart(fig_freq_purchases_shipping)
        # else:
        #     st.write('Frequency of Purchases data is not available or not numeric.')

        # Display Top Categories by Season
        st.header(f'Top Categories by Season {"" if selected_gender == "Overall" else f"for {selected_gender}"}')
        top_categories_season = filtered_df.groupby(['Season', 'Category'])['Purchase Amount (USD)'].sum().reset_index()
        top_categories_season = top_categories_season.sort_values(by='Purchase Amount (USD)', ascending=False)
        fig_top_categories_season = px.bar(top_categories_season, x='Purchase Amount (USD)', y='Category', color='Season',
                                           title=f'Top Categories by Season {"" if selected_gender == "Overall" else f"for {selected_gender}"}',
                                           labels={'Category': 'Category', 'Purchase Amount (USD)': 'Total Purchase Amount'},
                                           orientation='h')
        st.plotly_chart(fig_top_categories_season)

        # Display Average Purchase Amount by Review Rating
        st.header(f'Average Purchase Amount by Review Rating {"" if selected_gender == "Overall" else f"for {selected_gender}"}')
        avg_purchase_review_rating = filtered_df.groupby('Review Rating')['Purchase Amount (USD)'].mean().reset_index()
        fig_avg_purchase_review_rating = px.bar(avg_purchase_review_rating, x='Review Rating', y='Purchase Amount (USD)',
                                                title=f'Average Purchase Amount by Review Rating {"" if selected_gender == "Overall" else f"for {selected_gender}"}',
                                                labels={'Review Rating': 'Review Rating', 'Purchase Amount (USD)': 'Average Purchase Amount'})
        st.plotly_chart(fig_avg_purchase_review_rating)

    else:
        st.write('No data available for the selected filters.')
