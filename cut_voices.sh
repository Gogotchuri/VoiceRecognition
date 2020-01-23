#!/usr/bin/env bash

currDir=$(cd `dirname $0` && pwd)
execFile=${currDir}/vendor/extract_loudest_section/bin/extract_loudest_section
saveDir=${currDir}/data_cut

echo "Cleaning old cuts..."
rm -rf ${saveDir}
for filename in ${currDir}/data_raw/*.wav; do
    echo "Cutting file: ${filename}"
    ${execFile} ${filename} ${saveDir}
done
echo "All done!"
