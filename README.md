🛍️ Mall Customer Segmentation Report

(K-Means, Hierarchical, DBSCAN)

1. Objective

Segment mall customers into meaningful groups based on their annual income and spending score (and optionally, age/gender) to help the mall management target marketing strategies effectively.

2. Dataset

Mall Customers dataset (usually 200 entries).

Features:

CustomerID (ignored)

Gender

Age

Annual Income (k$)

Spending Score (1–100)

3. Data Preprocessing

✔ Remove CustomerID.
✔ Encode categorical variable Gender (Label Encoding or One-Hot).
✔ Standardize features (StandardScaler).

4. Exploratory Data Analysis (EDA)

📊 Insights:

Age: customers between 18–70 years.

Annual Income: ranges 15k–137k.

Spending Score: evenly distributed 1–100.

📈 Plots to include (interactive possible with Plotly):

Age distribution

Income vs Spending Score scatterplot (color-coded by gender)

5. Clustering Methods
5.1. K-Means Clustering

Used Elbow Method + Silhouette Score to select clusters.

Optimal clusters: k = 5.

Segments identified:

High Income – High Spending → “Target Customers”

High Income – Low Spending → “Conservative”

Low Income – High Spending → “Young Spenders”

Low Income – Low Spending → “Careful Customers”

Middle Income – Middle Spending → “Average Customers”

📌 K-Means Visualization:
Scatter plot (Annual Income vs Spending Score) with colored clusters.

5.2. Hierarchical Clustering (Agglomerative)

Dendrogram used to decide cluster count.

Optimal clusters: 5 (matches K-Means).

Segments broadly similar to K-Means but with slightly different group boundaries.

📌 Hierarchical Visualization:

Dendrogram (interactive zoom).

Scatter plot with hierarchical cluster labels.

5.3. DBSCAN

Hyperparameters tuned:

eps = 5, min_samples = 5.

DBSCAN found core clusters and some noise points.

Less effective in this dataset compared to K-Means/Hierarchical (because clusters are spherical, DBSCAN prefers density-based patterns).

📌 DBSCAN Visualization:

Noise shown as black points.

Clusters shown in distinct colors.

6. Comparison of Methods
Method	Optimal Clusters	Advantages	Drawbacks
K-Means	5	Simple, fast, well-suited for circular clusters	Needs k in advance, sensitive to outliers
Hierarchical	5	No need to pre-define k, dendrogram provides insight	Computationally expensive for large data
DBSCAN	3–4 + noise	Finds arbitrary shapes, handles outliers	Sensitive to eps/min_samples, less clear groups here
7. Insights & Business Value

Cluster 1 (High Income, High Spending): Prime customers → target with premium offers.

Cluster 2 (High Income, Low Spending): Attract them with loyalty programs.

Cluster 3 (Low Income, High Spending): Price-sensitive but loyal → discounts/coupons.

Cluster 4 (Low Income, Low Spending): Less valuable → reduce marketing spend.

Cluster 5 (Middle Income, Middle Spending): Balance group → nurture with seasonal campaigns.

8. Interactive Components (Streamlit / Plotly)

You can build a simple interactive dashboard:

Sidebar:

Select clustering algorithm (KMeans, Hierarchical, DBSCAN)

Adjust hyperparameters (k, eps, min_samples)

Main Page:

Show scatter plot with clusters

Show dendrogram (if hierarchical)

Display silhouette score / Davies-Bouldin index

Customer profile summary for each cluster
