import duckdb
from dotenv import load_dotenv
import os

load_dotenv()  # picks up .env from project root

conn = duckdb.connect(os.getenv("DUCKDB_DATABASE"))

"""
    Queries
"""
trips_select_query = """
    select * from trips
    limit 5
"""

trips_by_week_query = """
    select
        date_trunc('week', pickup_datetime + INTERVAL '1 day') - INTERVAL '1 day' as period,
        count(*) as num_trips,
        sum(passenger_count) as passenger_count,
        sum(total_amount) as total_amount,
        sum(trip_distance) as trip_distance 
    from trips
    group by period
    order by period
"""

trips_by_week_TEST_query = """
    select *
    from trips
"""


print(conn.execute("SHOW TABLES").df())
#print(conn.execute(trips_select_query).df())
#print(df.info())

