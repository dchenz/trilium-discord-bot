#!/bin/bash

packageName=trilium_client

pipreqs . --force --ignore $packageName,.venv
sed -i '/trilium_client/d' requirements.txt
echo "-e $packageName" >> requirements.txt
