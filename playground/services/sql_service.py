import sqlite3
import pandas as pd


class SQLService:

    DB_NAME = "practice.db"

    @staticmethod
    def execute_query(query):

        conn = sqlite3.connect(SQLService.DB_NAME)

        try:

            cursor = conn.cursor()

            query = query.strip()

            if not query:

                conn.close()

                return {
                    "type": "message",
                    "data": "Please enter a SQL query."
                }

            cursor.execute(query)

            # Queries that return data
            if cursor.description:

                columns = [
                    column[0]
                    for column in cursor.description
                ]

                rows = cursor.fetchall()

                df = pd.DataFrame(
                    rows,
                    columns=columns
                )

                conn.close()

                return {
                    "type": "table",
                    "data": df
                }

            # Queries that modify data
            conn.commit()

            affected_rows = cursor.rowcount

            conn.close()

            if affected_rows > 0:

                return {
                    "type": "message",
                    "data": (
                        f"Query executed successfully. "
                        f"Rows affected: {affected_rows}"
                    )
                }

            return {
                "type": "message",
                "data": "Query executed successfully."
            }

        except Exception as e:

            conn.close()

            raise e

    @staticmethod
    def get_tables():

        conn = sqlite3.connect(SQLService.DB_NAME)

        cursor = conn.cursor()

        cursor.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            AND name NOT LIKE 'sqlite_%'
        """)

        tables = [row[0] for row in cursor.fetchall()]

        conn.close()

        return tables

    @staticmethod
    def get_table_columns(table_name):

        conn = sqlite3.connect(SQLService.DB_NAME)

        cursor = conn.cursor()

        cursor.execute(
            f"PRAGMA table_info({table_name})"
        )

        columns = cursor.fetchall()

        conn.close()

        return columns

    @staticmethod
    def get_schema():

        schema = {}

        for table in SQLService.get_tables():

            columns = SQLService.get_table_columns(table)

            schema[table] = [
                column[1]
                for column in columns
            ]

        return schema

    @staticmethod
    def delete_table(table_name):

        conn = sqlite3.connect(SQLService.DB_NAME)

        cursor = conn.cursor()

        cursor.execute(
            f"DROP TABLE IF EXISTS {table_name}"
        )

        conn.commit()

        conn.close()