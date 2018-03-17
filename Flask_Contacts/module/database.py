import sqlite3
import logging

logger = logging.getLogger(__name__)

class Database:
    con = None
    cursor = None
    def __init__(self, db_path):
        self.db_path = db_path

    def connect_db(self):
        """Connects to the specific database."""
        rv = sqlite3.connect(self.db_path)
        rv.row_factory = sqlite3.Row
        return rv

    def read_all(self):
        con = self.connect_db()
        cursor = con.cursor()
        try:
            cursor.execute("SELECT * FROM contacts ORDER BY ContactId DESC")
            return cursor.fetchall()
        except:
            return None
        finally:
            cursor.close()
            con.close()

    def read_by_id(self, id):
        con = self.connect_db()
        cursor = con.cursor()
        try:
            if id:
                select_sql = "SELECT * FROM contacts WHERE ContactId = %(ContactId)d"
                cursor.execute(select_sql % {"ContactId": id})
                return cursor.fetchone()
            return None
        except:
            return None
        finally:
            cursor.close()
            con.close()

    def insert(self, data):
        con = self.connect_db()
        cursor = con.cursor()
        try:
            insert_sql = "INSERT INTO contacts(Name, Phone, Address) VALUES('%(Name)s', '%(Phone)s','%(Address)s')"
            cursor.execute(insert_sql % data)
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            cursor.close()
            con.close()

    def update(self, data):
        con = self.connect_db()
        cursor = con.cursor()
        try:
            update_str = "UPDATE contacts SET name = :Name, phone = :Phone, address = :Address WHERE ContactId = :ContactId"
            cursor.execute(update_str, data)
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            cursor.close()
            con.close()

    def delete(self, id):
        con = self.connect_db()
        cursor = con.cursor()
        try:
            cursor.execute("DELETE FROM contacts where ContactId = %s" % (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            cursor.close()
            con.close()

    def close(self):
        try:
            if self.cursor == self.con:
                self.con.close()
                self.cursor.close()
        except:
            pass
