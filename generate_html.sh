#!/bin/bash

sudo rm */*.html
sudo jupyter nbconvert */*.ipynb --to html

sudo rm *.html
sudo jupyter nbconvert *.ipynb --to html
