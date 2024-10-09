import pandas as pd
url = "C:\\Users\\gbemi\\OneDrive\\Documents\\Capstone Project\\Datasets\\yelp\\yelp_academic_dataset_review.csv"
url2 = "C:\\Users\\gbemi\\OneDrive\\Documents\\Capstone Project\\Datasets\\yelp\\yelp_academic_dataset_business.csv"

data_reviews = pd.read_csv(url)
data_business = pd.read_csv(url2)



# Filter reviews to include only those related to restaurants
restaurant_ids = data_business[data_business['categories'].str.contains('Restaurant', na=False)]['business_id']
filtered_reviews = data_reviews[data_reviews['business_id'].isin(restaurant_ids)]

# Remove specified columns from filtered_businesses
filtered_reviews = filtered_reviews.drop(columns=['useful', 'funny', 'cool'])

# Filter businesses to include only restaurants
filtered_businesses = data_business[data_business['categories'].str.contains('Restaurant', na=False)]
filtered_businesses.to_csv("C:\\Users\\gbemi\\OneDrive\\Documents\\Capstone Project\\Datasets\\yelp\\filtered_businesses.csv", index=False)

# Remove specified columns from filtered_businesses
filtered_businesses = filtered_businesses.drop(columns=['is_open', 'attributes', 'hours', 'latitude', 'longitude', 'postal_code', 'address'])


# Save the updated DataFrames to CSV files
filtered_businesses.to_csv("C:\\Users\\gbemi\\OneDrive\\Documents\\Capstone Project\\Datasets\\yelp\\filtered_businesses.csv", index=False)
filtered_reviews.to_csv("C:\\Users\\gbemi\\OneDrive\\Documents\\Capstone Project\\Datasets\\yelp\\filtered_reviews.csv", index=False)
#print(filtered_reviews.head())
#print(filtered_businesses.head())

# Merge filtered_reviews with filtered_businesses on 'business_id'
combined_df = pd.merge(filtered_reviews, filtered_businesses, on='business_id')

# Save the combined DataFrame to a CSV file
combined_df.to_csv("C:\\Users\\gbemi\\OneDrive\\Documents\\Capstone Project\\Datasets\\yelp\\combined_reviews_businesses.csv", index=False)

from ydata_profiling import ProfileReport
#profile = ProfileReport(combined_df, title='Exploratory Analysis Report')
#profile.to_file('exploratory_analysis_report.html')
# Sample 50% of the combined DataFrame
sampled_df = combined_df.sample(frac=0.5, random_state=1)

# Generate the profile report on the sampled data
profile_sampled = ProfileReport(sampled_df, title='Exploratory Analysis Report (50% Sample)')
profile_sampled.to_file('exploratory_analysis_report_sampled.html')