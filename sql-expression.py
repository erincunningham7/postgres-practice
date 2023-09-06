# import classes from within the sqlalchemy module
from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# link python file to chinook db
# assign the create_engine component to variable db to represent our database
# use create_engine to point to the chinook db within our postgres server
db = create_engine("postgresql:///chinook")

# use the MetaData class and save to variable meta
# this class will have a collection of table objects and their associated data
meta = MetaData(db)

# Before we start to query the db, we need to construct our tables, so that
# python knows the schema that we're working with
# our first table class/model assigned to variable artist_table
# use Table import to specify the name of our table &add the meta schema
artist_table = Table(
    "Artist", meta,
    # define columns 
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String),
)

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AblumId", Integer, primary_key=True),
    Column("Title", String),
    # tell foreign key which table and key to point to
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    # Float since it uses decimal values
    Column("UnitPrice", Float),
)

# connect to the db using the python with statement and .connect()
# the connection is saved to the db into variable connection
with db.connect() as connection:

    # Query 1 - select all records from the artist table
    # define all six queries into a variable called 'select_query'
    select_query = artist_table.select()

    results = connection.execute(select_query)
    for result in results:
        print(result)

    # Query 2 - select only the name column from the artist table
    # Query 3 - select only queen from the artist table
    # Query 4 - select only be artistid number 51 from he artist table
    # Query 5 - select only the albums with artistid number 51 on album table
    # Query 6 - select all tracks where the composer is queen from track table