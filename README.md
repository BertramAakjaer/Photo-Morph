```bash
    __    __  ____   _             _                  __  __                      _          __    __
   / /   / / |  _ \ | |__    ___  | |_   ___         |  \/  |  ___   _ __  _ __  | |__      / /   / /
  / /   / /  | |_) || '_ \  / _ \ | __| / _ \  _____ | |\/| | / _ \ | '__|| '_ \ | '_ \    / /   / /
 / /   / /   |  __/ | | | || (_) || |_ | (_) ||_____|| |  | || (_) || |   | |_) || | | |  / /   / /
/_/   /_/    |_|    |_| |_| \___/  \__| \___/        |_|  |_| \___/ |_|   | .__/ |_| |_| /_/   /_/
                                                                          |_|
```

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

> A tool for taking a image and reordering the pixels to look like another provided image. This idea is inspired by the one made by [Spu7Nix on Youtube](https://youtube.com/shorts/MeFi68a2pP8?si=l-LnmvlKlK05ktSR), but is made from scratch and with a different algorithm design.

## ✨ Features

- Decompile an image directly ot the pixels and sort them so the most used (color group) is first
- Map the pixels of one picture to another by using the before named alorithm
- Make an animation that shows this change

## 🚀 Installation
> [!Warning]
>  This tool is primarly made for Windows 11 and is only tested in Windows 11. So it may not work on other OS'.

1. Clone the repository
```bash
git clone https://github.com/BertramAakjaer/steam-market-price-tool.git

cd Photo-Morph
```

2. Install requirements
```bash
pip install -r requirements.txt
```

3. Configure your settings in `config.json`
Comming soon ⏰

## 💻 Usage

Run the main script:
```bash
python main.py
```

### 🛣️ Flow
1. If u used the program before, you will be promptet about keeping the same template:
```
Keep cached template? (Y/n):
```

2. If not your file explorer opens and you will need to pick a file for use as template
```
// Pick image for template usage //
```

3. Then you will need to give the program an image to map pixels from
```
// Choose image for mapping to template //
```

4. Lastly you will be asked if the conversion should be made into an animation
```
// Choose image for mapping to template //
```


## ⚙️ Configuration

The tool uses the `config.json` to manage user settings, here is all the settings described:


## 🔧 Technical Details


## 📚 Dependencies

- [Pillow](https://pypi.org/project/Pillow/) - Image processing library
- [art](https://pypi.org/project/art/) - Library for generating ASCII art
- [OpenCV (cv2)](https://opencv.org/) - Used for making the animation
- [tkinter](https://docs.python.org/3/library/tkinter.html) - Used for file-explorer to choose images

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

##  **Socials** 🐦

>  [aakjaer.site](https://www.aakjaer.site) &nbsp;&middot;&nbsp;
>  GitHub [@BertramAakjær](https://github.com/BertramAakjaer) &nbsp;&middot;&nbsp;
>  Twitter [@BertramAakjær](https://twitter.com/BertramAakjaer)
