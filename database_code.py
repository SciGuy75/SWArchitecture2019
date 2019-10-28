# PLS DO NOT RUN UNLESS YOU KNOW WHAT YOU ARE DOING
import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# # Add users to database
# # Users Table ('username', 'password')
# c.execute("DELETE FROM Users")
# users = [('test', 'test'),
#          ('John', 'pass'),
#          ('Jane', 'pass'),
#         ]
# c.executemany('INSERT INTO Users VALUES (?,?)', users)

# # Add items to database
# # Inventory Table ('name', 'description', 'price', 'quantity', 'category')
# c.execute("DELETE FROM Inventory")
# items = [('aluminum foil', '120 sq ft', '6.99', '285', 'household items'),
#          ('toothpaste', '4 oz', '5.99', '99', 'household items'),
#          ('SW Design Book', 'textbook', '50.99', '43', 'books'),
#          ('spiderman figure', 'hero series', '8.99', '182', 'toys'),
#          ('dolls', 'Fancy Nancy', '24.99', '126', 'toys'),
#          ('camera', 'Nikon D3500', '459.99', '27', 'small electronics'),
#          ('mobile phone', 'Galaxy S10', '899.99', '16', 'small electronics')
#         ]
# c.executemany('INSERT INTO Inventory VALUES (?,?,?,?,?)', items)

# Save changes made
conn.commit()

# Close the database
conn.close()