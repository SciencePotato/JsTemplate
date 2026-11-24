# JsTemplate
A python file to initialize JS website structure

## Usage

Run `python3 Js_Template.py` (Windows: `py Js_Template.py`) and enter a target
directory path at the prompt, without surrounding quotes. Relative paths are
resolved from your current working directory, not the script's location.
Missing parent directories are created.

The script creates these **empty placeholders**:

```text
index.html
assets/
lib/script.js
src/scss/main.scss
src/css/main.css
```

Rerunning preserves existing files. A file occupying a required directory path
is an error, not a completed scaffold. Add your HTML, script and stylesheet
links yourself; this script does not compile SCSS, install packages, or start
a web server.

Tests: `python3 -m unittest -v test_scaffold` (standard library only).
