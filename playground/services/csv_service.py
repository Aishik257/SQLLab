import pandas as pd
import sqlite3


class CSVService:

    @staticmethod
    def upload_csv(csv_file):

        df = pd.read_csv(csv_file)

        table_name = csv_file.name.split(".")[0].lower()

        conn = sqlite3.connect("practice.db")

        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False
        )

        conn.close()

        return table_name