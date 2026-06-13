import sqlite3
import pandas as pd


class SampleDataService:

    @staticmethod
    def load_sample_data():

        conn = sqlite3.connect("practice.db")

        employees = pd.DataFrame({
            "id": [1, 2, 3, 4],
            "name": ["John", "Alice", "Bob", "David"],
            "salary": [50000, 60000, 70000, 55000],
            "department_id": [1, 2, 1, 3]
        })

        departments = pd.DataFrame({
            "id": [1, 2, 3],
            "department_name": ["IT", "HR", "Finance"]
        })

        employees.to_sql(
            "employees",
            conn,
            if_exists="replace",
            index=False
        )

        departments.to_sql(
            "departments",
            conn,
            if_exists="replace",
            index=False
        )

        conn.close()