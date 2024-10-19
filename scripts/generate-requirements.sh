#!/bin/bash

packageName=trilium_client

pipreqs . --force --ignore $packageName,.venv
echo "-e $packageName" >> requirements.txt
