from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)

# the python classes we create are subclasses of the declarative_base
from sqlalchemy.ext.declarative import declarative_base
# in order to ask for a session with sessionmaker
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///chinook")
# The 'base' class will grab the metadata produced by our db table schema
# and creates a subclass to map everything back here within the 'base' variable
base = declarative_base()

# Query 1 - create a class-based model for the artist table


class Artist(base):
    __tablename__ = "Artist"
    ArtistId = Column(Integer, primary_key=True)
    Name = Column(String)

# Query 2 - create a class-based model for the album table


class Album(base):
    __tablename__ = "Album"
    AlbumId = Column(Integer, primary_key=True)
    Title = Column(String)
    ArtistId = Column(Integer, primary_key=True)

# Query 3 - create a class-based model for the Track table


class Track(base):
    __tablename__ = "Track"
    TrackId = Column(Integer, primary_key=True)
    Name = Column(String)
    AlbumId = Column(Integer, ForeignKey("Album.AlbumId"))
    MediaTypeId = Column(Integer, primary_key=False)
    GenreId = Column(Integer, primary_key=False)
    Composer = Column(String)
    Milliseconds = Column(Integer, primary_key=False)
    Bytes = Column(Integer, primary_key=False)
    UnitPrice = Column(Float)


# make a new instance of the sessionmaker and point to our db engine to use our db
Session = sessionmaker(db)
# open an actual session
session = Session()

# create the db using declarative_base subclass
base.metadata.create_all(db)

# Query 1 - select all records from the artist table
# artists = session.query(Artist)
# for artist in artists:
#    print(artist.ArtistId, artist.Name, sep=" | ")

# Query 2 - select only the name column from the artist table
# artists = session.query(Artist)
# for artist in artists:
#    print(artist.Name)


# Query 3 - select only queen from the artist table
# artist = session.query(Artist).filter_by(Name="Queen").first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 4 - select only be artistid number 51 from he artist table
# artist = session.query(Artist).filter_by(ArtistId=51).first()
# print(artist.ArtistId, artist.Name, sep=" | ")

# Query 5 - select only the albums with artistid number 51 on album table
# albums = session.query(Album).filter_by(ArtistId=51)
# for album in albums:
#    print(album.ArtistId, album.Title, album.AlbumId, sep=" | ")

# Query 6 - select all tracks where the composer is queen from track table
tracks = session.query(Track).filter_by(Composer="Queen")
for track in tracks:
    print(
        track.TrackId,
        track.Name,
        track.AlbumId,
        track.MediaTypeId,
        track.GenreId,
        track.Composer,
        track.Milliseconds,
        track.Bytes,
        track.UnitPrice,
        sep=" | "
    )
