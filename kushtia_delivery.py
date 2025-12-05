# KUSHTIA DELIVERY CLUSTERS  

# 1. Kushtia delivery points (6 landmarks)
points = [
    [23.9011, 89.1200],  # Kushtia Govt. College
    [23.9045, 89.1180],  # Kushtia Stadium
    [23.9001, 89.1220],  # Kushtia Central Hospital
    [23.8850, 89.1350],  # Rabindra Kuthibari (Shilaidaha)
    [23.8870, 89.1330],  # Tagore Memorial Museum
    [23.8830, 89.1370]   # Shilaidaha Ghat (Gorai River)
]

# 2. Cluster into 2 zones (Town Center + Shilaidaha)
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=42)
clusters = kmeans.fit_predict(points)
centroids = kmeans.cluster_centers_

# 3. Show results
print("Kushtia Delivery Zones Found:")
zone_names = ["Town Center", "Shilaidaha Heritage"]
for i in range(2):
    print(f"  {zone_names[i]} Hub: {centroids[i][0]:.4f}°N, {centroids[i][1]:.4f}°E")

# 4. Create interactive map (centered on Kushtia!)
import folium

m = folium.Map(
    location=[23.895, 89.13], 
    zoom_start=13,
    tiles="CartoDB positron"  # Clean, modern map
)

# Landmark names
landmarks = [
    "Kushtia Govt. College",
    "Kushtia Stadium", 
    "Central Hospital",
    "Rabindra Kuthibari",
    "Tagore Museum",
    "Shilaidaha Ghat"
]

# Add points with Kushtia colors (red & green)
colors = ['#e74c3c', '#27ae60']  # Red & Green — like our flag!

for i, point in enumerate(points):
    folium.CircleMarker(
        point,
        radius=10,
        color=colors[clusters[i]],
        fill=True,
        fill_opacity=0.7,
        popup=f"<b>{landmarks[i]}</b><br>Zone: {zone_names[clusters[i]]}",
        tooltip=f"{landmarks[i]} • {zone_names[clusters[i]]}"
    ).add_to(m)

# Add hub markers (star ★)
for i, cent in enumerate(centroids):
    folium.Marker(
        cent,
        popup=f"★ {zone_names[i]} Hub<br><i>Optimal delivery base</i>",
        tooltip=f"{zone_names[i]} Hub",
        icon=folium.Icon(color='black', icon='star')
    ).add_to(m)

# Add Kushtia love 
folium.Marker(
    [23.895, 89.13],
    popup="<b>কুষ্টিয়া — রবীন্দ্রনাথের প্রেমের শহর</b>",
    icon=folium.Icon(color='red', icon='heart')
).add_to(m)

# Save and show
m.save("kushtia_delivery.html")
print("\n Map saved as 'kushtia_delivery.html'")
print(" Right-click → Download → Open in browser to see Kushtia bloom!")