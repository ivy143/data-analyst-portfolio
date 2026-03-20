plt.figure()

scatter = plt.scatter(
    rfm['frequency'],
    rfm['monetary'],
    c=rfm['Cluster']
)

plt.xlabel("Frequency")
plt.ylabel("Monetary")
plt.title("Customer Segments")

plt.colorbar(scatter)
plt.show()


