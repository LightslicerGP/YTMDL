# Youtube Playlist Downloader

## How to use Modifications

1. first start with an empty `Modifications.json` file, run the script
2. then check the `couldNotFind.txt` file, and see the songs.
3. for every song in there, use a custom search query and try again
4. if it STILL shows up, either try a new search query, or use modifications to overwrite any parts deemed necessary

```json
{
  "Rarin - GTA (Official Lyric Video)": {
    "title": "GTA",
    "artist": "Rarin",
    "year": "2020",
    "album": "GTA",
    "image": "https://i1.sndcdn.com/artworks-ijfklcEsdzHeCJGo-iMuXDQ-t500x500.jpg",
    "genre": "Rap",
    "number": "0"
  }
}
```

## Using a Custom Search Query

if you trust a search query for itunes, put it like this:
(keep in mind, the search query will STILL get overwritten with custom song data if given)
Also, if you check the search query link using `SearchSongs.html` that was sent you can see which result you would use instead (starting at 0, which should be a given)

```json
{
  "Rarin - GTA (Official Lyric Video)": {
    "searchquery": "GTA Rarin",
    "searchitem": 3
  }
}
```

## Notes

- if the song is not in an album, the title of the song will be used for the album name
- all ampersands `&` will be replced with `and`, as well as back slashes `\` into a space, in the search query
