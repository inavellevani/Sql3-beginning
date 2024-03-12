import sqlite3
from book_characteristics import names, pages, cover_types, categories

conn = sqlite3.connect("wignebi.db")
connected = conn.cursor()
connected.execute("""CREATE TABLE IF NOT EXISTS books (
          Name TEXT,
          Pages INTEGER,
          Cover_type TEXT,
          Category TEXT)""")


for name, page, cover_type, category in zip(names, pages, cover_types, categories):
    connected.execute("INSERT INTO books (Name, Pages, Cover_Type, Category) VALUES (?, ?, ?, ?)",
                      (name, page, cover_type, category))

conn.commit()

connected.execute("SELECT AVG(Pages) FROM books")
average_pages = connected.fetchone()[0]
print(f"Average number of pages: {average_pages}")

connected.execute("SELECT Name, Pages FROM books WHERE Pages = (SELECT MAX(Pages) FROM books)")
biggest_book = connected.fetchone()
book_name, page_count = biggest_book
print(f"{book_name} has most pages in table, counting {page_count} pages")


connected.close()
conn.close()
