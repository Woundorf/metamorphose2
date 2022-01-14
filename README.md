Métamorphose 2 quick-ported to modern Python and wxPython. Tested to work (mostly) with Python 3.10.1 and wxPython 4.0.7.

I started from another fork with several bugfixes. Errors have been discovered by trial and error and fixed as best as I know, but since I'm not a Python developer some fixes may not be good. Other errors may remain that I haven't discovered yet. Feel free to create an issue, a pull request or a new fork to solve them.

What follows below is the Readme of the previous fork.

---

> Note: due the creator of Métamorphose [Ianaré Sévi](https://github.com/ianare) no longer having time to maintain it, this forked version has been created (big thanks to Ianaré for writing the software and maintaining it when he had time!). For Ubuntu users please see the new Launchpad PPA for a release that works on Xenial (and as of release 0.9.0~beta should work on newer series too):
>
>https://launchpad.net/~savoury1/+archive/ubuntu/metamorphose2

# Métamorphose 2

Métamorphose is a graphical mass renaming program for files and folders.

These are the command line options::

```
-h,  --help       Show help screen and exit.
-t,  --timer      Show time taken to complete operations.
-d,  --debug      Show debugging information.
-p=, --path       Specify a directory to load.
-c=, --config     Specify a configuration file to load.
-a=, --auto       Specify automatic mode level to use with configuration file:
                    0 = do not preview items
                    1 = auto preview items
                    2 = auto rename items
                    3 = auto rename items and exit on success
-l=, --language   Override preferred language:
                    en_US
                    fr
                    es
-w=, --wxversion  Specify wxPython Version - use at your own risk!
```
If no other options are given, you may specify a path to open::
```
$ metamorphose2 /srv/samba/Windows Likes Spaces
```

## Running from Source

What follows is for developers or those wishing to use the very latest version.

For binary (normal) installs, use the appropriate install file for your system (setup.exe, .deb, etc ...).


### Cloning

Cloning the sources from the remote::
```
git clone https://github.com/metamorphose/metamorphose2.git
```
Submodules are used, so after cloning don't forget to check them out:
```
git submodule update --init
```

### Requirements

- Python 2.6 or 2.7 (*not* compatible with 3.x)
- wxPython 2.8 (preferred) or 3.0
- Python Imaging Library (PIL) 1.1.6 or greater **or** Pillow 2.3.0 or greater


### Running

Create or update the language files::
```
cd messages
make
```
Launch the application::
```
./metamorphose2
```

### Installing

As root:
```
make all
```

Under Linux & FreeBSD the makefile should take care of everything for you, it is architecture and distro independant.

Métamorphose will be installed in `/usr/share/metamorphose2`, you can run it with:
```
metamorphose2
```

and access the man page with::
```
man metamorphose2
```

If you are using a freedesktop.org compatible window manager (like Gnome or KDE), there should be an entry in `Applications` -> `Accessories`.


### Removing

Remove the user-specific files here:

- Windows: `C:\Documents and Settings\USERNAME\Application Data\.metamorphose2`
- Linux/BSD: `~/.metamorphose2`
- Mac: `/Library/Application Support/.metamorphose2`

In Linux & BSD, if you have the sources::
```
make remove
```
To remove all user files as well::
```
make remove remusr=1
```

## Known Issues

Program locks up when 'walking' a large number of files/folders

> Not really locked up, but the time it takes to process entries can be long if you are loading many items. During this process the application doesn't refresh, giving the appearance of being locked up but is actually working on stuff.
> 
> The time in this state is dependent on your computer, whether the directory is on a local drive or a network share, and of course the number of items.
>
> This will be addressed in a future release.


Unreadable picker items under Linux (possibly other GTK)

> There seems to be a bug in wxGTK, the list can become slow and unreadable when dealing with large number of items (over 10,000).
>
> A work around may be possible.


Thumbnails fail

> There seems to be some problems with python-imaging under windows. Sometimes the image will not load.

