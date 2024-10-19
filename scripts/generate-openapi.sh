#!/bin/bash

if [ ! -d scripts ]; then
    echo "Please run this script from the project root."
    exit 1
fi

targetTriliumVersion=0.90.4
packageName=trilium_client

# Obtain the openapi.yaml from TriliumNext on Github.

sourceTarFile=v$targetTriliumVersion.tar.gz
wget https://github.com/TriliumNext/Notes/archive/refs/tags/$sourceTarFile
tar -xf $sourceTarFile --strip-components=3 Notes-$targetTriliumVersion/src/etapi/etapi.openapi.yaml
rm -f $sourceTarFile

# Generate using the extracted openapi specification.

rm -rf $packageName

docker run --rm \
    --user $(id -u):$(id -g) \
    -v ${PWD}:/local \
    openapitools/openapi-generator-cli generate \
    -i /local/etapi.openapi.yaml \
    -g python \
    -o /local/$packageName \
     --additional-properties=packageName=$packageName,projectName=$packageName,removeUnusedModels=true

rm -f etapi.openapi.yaml

# Format the generated code so it's nicer to read.

ruff format $packageName

# Move the generated Github action workflow.

mv $packageName/.github/workflows/python.yml .github/workflows/openapi-test.yaml
rm -rf $packageName/.github
sed -i '/.github\/workflows\/python.yml/d' $packageName/.openapi-generator/FILES
echo "    defaults:"                               >> .github/workflows/openapi-test.yaml
echo "      run:"                                  >> .github/workflows/openapi-test.yaml
echo "        working-directory: ./trilium_client" >> .github/workflows/openapi-test.yaml
