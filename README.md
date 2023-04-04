# TreeMenuDjangoApp

TreeMenuDjangoApp is a Django app to draw a tree menu. This app could be used in more complex projects.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install necessary packages (Django packages and package to read .env local file).

```bash
pip install -r requtements.txt
```
Run the app as a standard Django project.


## Features
* Use Django template tag.
* Use Django admin panel to add a new tree menu and set up dependencies.
* Each item in the tree menu has the link (as url or named_url).
* Each item in the tree menu opens a page link.
* Active item determined through the active link.
* There could be any number of tree menus on one page.
* Only one request to the data base.

Under development: 
* Expanding menu items based on the selected item with Java Script. Now only the upper level is drawn by default.

## Notes

Check "screenshots" folder.

## License

[MIT](https://choosealicense.com/licenses/mit/)