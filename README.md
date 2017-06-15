# saavn-dl: Download Saavn playlists
I'm too lazy to download songs and too cheap to buy subscriptions, so I wrote this tiny script to fetch Saavn playlists
 and download the audio from YouTube.

The script stores the download history in an SQLite DB, so that it does not
download the same files repeatedly.

This is a very hacky, ugly version that _just works_, (for now).

### Why Saavn?
Spotify/Apple Music are more famous, but I wanted something that has Bollywood and other Indian language songs too. Also, I wanted FREE (see the first line in the readme).

Gaana/Saavn are the obvious candidates, and I wrote this so long ago that I actually forgot why I didn't use Gaana :')

### Installation
This is available as a pip module for Python 2.7+.

```
$ pip install saavn-dl
OR 
$ pip3 install saavn-dl
```

### Usage
```bash
$ saavn-dl -p <playlist URL>
```

### Contributing

If you want a new feature or want to report a bug, open an issue.
If you want to add a feature, fork the repo, create a feature branch, commit your changes and then send a pull request.

### To do

- [ ] Import youtube-dl as a module, shelling out is baaaaad
- [ ] Check for ffmpeg/libav (depending on OS) for audio conversion
- [ ] Option to clear DB to start afresh
- [ ] Refactor and use console_scripts in setuptools for Windows compatibility
- [ ] Tests

### Credits
* [youtube-dl](https://github.com/rg3/youtube-dl) (which I use to grab the audio in this script too)
* [spotify-dl](https://github.com/SathyaBhat/spotify-dl) and [xkcd-dl](https://github.com/prodicus/xkcd-dl), which also provide convenient ways to download the respective media
