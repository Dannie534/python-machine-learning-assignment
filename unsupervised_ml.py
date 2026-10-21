# importing
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

#preparing training data
x=[[1000, 2], [1500, 3], [2000, 2], [5000, 6], [6000, 7], [5500, 5], [12000, 12], [15000, 14], [13000, 11], [3000, 4]]
#scaling the data
scaler = StandardScaler()
x = scaler.fit_transform(x)
#creating the model
model_kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
#training the model
model_kmeans.fit(x)
# get cluster labels
cluster_labels = model_kmeans.labels_
#display the cluster assigned to each customer
print("--- Customer Cluster Assignments ---")
for index, label in enumerate(cluster_labels):
    print(f"Customer {index + 1} belongs to Cluster {label}")

print("\n--- Cluster Summary Counts ---")
#display the total number of customers in each cluster
for cluster_id in range(3):
    total_in_cluster = list(cluster_labels).count(cluster_id)
    print(f"Cluster {cluster_id} contains {total_in_cluster} customers")
#plot original data in differnt colors by cluster
spending =[customer[0] for customer in x]
visits = [customer[1] for customer in x]
plt.scatter(spending, visits, c=cluster_labels, cmap='viridis')
plt.xlabel('monthly spending (KES)')
plt.ylabel('monthly visits')
plt.title('Customer Clusters')
plt.show()
