from app import db
from sqlalchemy import text
from werkzeug.exceptions import InternalServerError


class RatesService:
    def get_average_prices(self, date_from, date_to, origin, destination):
        try:
            # Construct the raw SQL query
            sql_query = """
                SELECT 
                    day, 
                    ROUND(AVG(price), 2) AS average_price  
                FROM 
                    prices
                JOIN ports orig_ports ON prices.orig_code = orig_ports.code
                JOIN ports dest_ports ON prices.dest_code = dest_ports.code
                WHERE 
                    (prices.orig_code = :origin OR orig_ports.parent_slug = :origin)
                    AND
                    (prices.dest_code = :destination OR dest_ports.parent_slug = :destination)
                    AND
                    day BETWEEN :date_from  AND :date_to 
                GROUP BY 
                    day
                HAVING 
                    COUNT(*) >= 3
                ORDER BY 
                    day;
            """

            # Execute the SQL query with SQLAlchemy
            with db.engine.connect() as connection:
                result = connection.execute(
                    text(sql_query),{"origin":origin,"destination":destination,"date_from":date_from,"date_to":date_to}
                )
                rows = result.fetchall()
            
            # Process the results and format them as a list of dictionaries
            average_prices = [{
                'day': row[0].strftime('%Y-%m-%d'),
                'average_price': float(row[1])
            } for row in rows]

            return average_prices
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            raise InternalServerError("An error occurred while processing the request")
