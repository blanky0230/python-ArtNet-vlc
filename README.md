# Install python packages
Either use nix-shell or install via pip
```pip install -r requirements.txt```

# Adjust configuration

see the .env file. Edit it to match your config

# Run Server

```python src/player/server.py```

# Send test packet

```python src/player/test_sender.py```


# General usage

Use the ArtDMX Controller of your choice to control a VLC-Player remotely.

## Commands

Channel | Function | Effect
---|---|---
NET | change media selection's folder | This will change the folder "id" from which to load the specified media id in the next byte.
NET+1 | change the file to be selected | This will change the target file within the folder as selected per the previous byte.
NET+2 | Command | Send player Commands: 0=Noop, 1=Play, 2=Pause, 3=Stop, (maybe more to add). After you've paused a video you need to use Play to resume it.
NET+3 | Playback Speed | Uses simple integer value from 0-255 to set the players playback speed in percent (100 for regular speed)
NET+4 | Logo file | send integer as to which index of logo is supposed to be used send 0 to disable logo and 1 for the first logo in the folder.


## Prepare Media

Specify your media root directory in the .env file.

We use directories in order to group media together e.g.

```
media
├── 0
│   ├── 1.mp4
│   ├── 2.png
│   └── x.mp4
└── 1
    ├── 1.flac
    └── some_media.gif
```

This means you can tell the vlc player to select certain media from certain subfolders by setting the Bytes at __NET__ and __NET+1__.
If you'd like to select `x.mp4` you'd send 0 at Channel __NET__ and 2 at Channel __NET+1__

### Logos

If you want to use Logos. Add them to your media directory /logos and see the Commands section as per how to use them