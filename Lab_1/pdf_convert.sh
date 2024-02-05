#!/bin/bash

export PATH=/Library/TeX/texbin:$PATH

echo "Enter file to be converted to PDF"
read file

jupyter nbconvert $file --to pdf

echo "${file} successfully converted!"
