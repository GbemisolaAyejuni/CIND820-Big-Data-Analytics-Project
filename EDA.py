import pandas as pd
#from ydata_profiling import ProfileReport

url = "C:\\Users\\gbemi\\OneDrive\\Documents\\Capstone Project\\Datasets\\yelp\\yelp_academic_dataset_review.json"
data_reviews = pd.read_json(url, lines=True)

url2 = "C:\\Users\\gbemi\\OneDrive\\Documents\\Capstone Project\\Datasets\\yelp\\yelp_academic_dataset_business.json"
data_business = pd.read_json(url2, lines=True)

csv_path = "C:\\Users\\gbemi\\OneDrive\\Documents\\Capstone Project\\Datasets\\yelp\\yelp_academic_dataset_review.csv"
data_reviews.to_csv(csv_path, index=False)
csv_path2 = "C:\\Users\\gbemi\\OneDrive\\Documents\\Capstone Project\\Datasets\\yelp\\yelp_academic_dataset_business.csv"
data_business.to_csv(csv_path2, index=False)

''' def save_json_to_csv(json_path, csv_path):
    data = pd.read_json(json_path, lines=True)
    data.to_csv(csv_path, index=False)

save_json_to_csv("C:\\Users\\gbemi\\OneDrive\\Documents\\Capstone Project\\Datasets\\yelp\\yelp_academic_dataset_review.json",
                 "C:\\Users\\gbemi\\OneDrive\\Documents\\Capstone Project\\Datasets\\yelp\\yelp_academic_dataset_review.csv")
save_json_to_csv("C:\\Users\\gbemi\\OneDrive\\Documents\\Capstone Project\\Datasets\\yelp\\yelp_academic_dataset_business.json",
                 "C:\\Users\\gbemi\\OneDrive\\Documents\\Capstone Project\\Datasets\\yelp\\yelp_academic_dataset_business.csv") '''

'''cities = ["Montreal", "Toronto"]
filtered_reviews = data_reviews[data_reviews['business_id'].isin(
    data_business[data_business['city'].isin(cities)]['business_id']
)]

# Save filtered reviews to a file
filtered_csv_path = "C:\\Users\\gbemi\\OneDrive\\Documents\\Capstone Project\\Datasets\\Yelp_json\\filtered_reviews.csv"
filtered_reviews.to_csv(filtered_csv_path, index=False)

print(filtered_reviews)'''