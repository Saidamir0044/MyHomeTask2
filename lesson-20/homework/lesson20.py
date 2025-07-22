# Customer Purchases Analysis:

# Ex1 Find the total amount spent by each customer on purchases (considering invoices).
import pandas as pd
import sqlite3

con = sqlite3.connect("chinook.db")
tables = pd.read_sql_query("SELECT * FROM sqlite_master WHERE type='table';", con)
customers = pd.read_sql_query("SELECT * FROM customers", con)
artists = pd.read_sql_query("SELECT * FROM artists", con)
invoices = pd.read_sql_query("SELECT * FROM invoices", con)
combined = pd.merge(invoices, customers, on='CustomerId', how='inner')
total_by_customer = combined.groupby(["CustomerId", "FirstName", "LastName"])["Total"].sum().reset_index()
print(total_by_customer)

# Ex2 Identify the top 5 customers with the highest total purchase amounts.
import pandas as pd
import sqlite3

con = sqlite3.connect("chinook.db")
tables = pd.read_sql_query("SELECT * FROM sqlite_master WHERE type='table';", con)
customers = pd.read_sql_query("SELECT * FROM customers", con)
artists = pd.read_sql_query("SELECT * FROM artists", con)
invoices = pd.read_sql_query("SELECT * FROM invoices", con)
combined = pd.merge(invoices, customers, on='CustomerId', how='inner')
total_by_customer = combined.groupby(["CustomerId", "FirstName", "LastName"])["Total"].sum().reset_index()
top_5_customers = total_by_customer.nlargest(5, 'Total')
print(top_5_customers)

# Ex3 Display the customer ID, name, and the total amount spent for the top 5 customers.
import pandas as pd
import sqlite3

con = sqlite3.connect("chinook.db")
tables = pd.read_sql_query("SELECT * FROM sqlite_master WHERE type='table';", con)
customers = pd.read_sql_query("SELECT * FROM customers", con)
artists = pd.read_sql_query("SELECT * FROM artists", con)
invoices = pd.read_sql_query("SELECT * FROM invoices", con)
combined = pd.merge(invoices, customers, on='CustomerId', how='inner')
total_by_customer = combined.groupby(["CustomerId", "FirstName", "LastName"])["Total"].sum().reset_index()
top_5_customers = total_by_customer.nlargest(5, 'Total')
print(top_5_customers)

# Album vs. Individual Track Purchases:

import pandas as pd
import sqlite3

con = sqlite3.connect("chinook.db")
customers = pd.read_sql_query("SELECT * FROM customers", con)
invoices = pd.read_sql_query("SELECT * FROM invoices", con)
invoice_items = pd.read_sql_query("SELECT * FROM invoice_items", con)
tracks = pd.read_sql_query("SELECT * FROM tracks", con)
invoice_items = invoice_items.merge(invoices[["InvoiceId", "CustomerId"]], on="InvoiceId", how="left")
invoice_items = invoice_items.merge(tracks[["TrackId", "AlbumId"]], on="TrackId", how="left")
album_track_counts = tracks.groupby("AlbumId")["TrackId"].count().reset_index()
album_track_counts.rename(columns={"TrackId": "TotalTracksInAlbum"}, inplace=True)
customer_album_purchases = invoice_items.groupby(["CustomerId", "AlbumId"])["TrackId"].count().reset_index()
customer_album_purchases.rename(columns={"TrackId": "TracksPurchased"}, inplace=True)
customer_album_purchases = customer_album_purchases.merge(album_track_counts, on="AlbumId", how="left")
customer_album_purchases["FullAlbum"] = customer_album_purchases["TracksPurchased"] == customer_album_purchases["TotalTracksInAlbum"]
customer_pref = customer_album_purchases.groupby("CustomerId")["FullAlbum"].any().reset_index()
customer_pref["PurchaseType"] = customer_pref["FullAlbum"].apply(lambda x: "Full Album" if x else "Individual Tracks")
summary = customer_pref["PurchaseType"].value_counts(normalize=True).reset_index()
summary.columns = ["PurchaseType", "Percentage"]
summary["Percentage"] = (summary["Percentage"] * 100).round(2)
print(summary)
