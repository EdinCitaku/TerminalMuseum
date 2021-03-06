![screenshot](screenshot.png)

# TerminalMuseum

Add a unique museum-like experience to your terminal!

TerminalMuseum is a CLI tool that displays a new piece of classical art on your terminal every time you run it.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install TerminalMuseum.

```bash
pip install terminalmuseum
```

## Usage
The command to display images varies between terminal emulators, and many can not display images at all. I personally recommend using [kitty](https://sw.kovidgoyal.net/kitty/) with TerminalMuseum, as images are displayed in native resolution and loaded very quickly.

#### kitty 

If you use kitty, you don't need to install any additional tools. Just add these lines to your `.bashrc`:

```bash
terminalmuseum --command "kitty +kitten icat" --print_title
```

#### imgcat
Many terminal emulators don't natively support displaying images. In these cases you can use tools like [imgcat](https://github.com/eddieantonio/imgcat). After installation add these lines to your `.bashrc`:

```bash
terminalmuseum --command "imgcat" --print_title
```

## Art
The Art used in this project is in the public domain and was filtered and downloaded via the [openaccess](https://github.com/metmuseum/openaccess) project of the Metropolitan Museum of Art.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests or add them as appropriate.


## License
[Apache 2.0](http://www.apache.org/licenses/LICENSE-2.0)
