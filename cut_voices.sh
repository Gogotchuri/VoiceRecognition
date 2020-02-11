#!/usr/bin/env bash

currDir=$(cd `dirname $0` && pwd)
voiceDir=${1}
execFile=${currDir}/vendor/extract_loudest_part
tmpDir=${currDir}/tmp_voices/
saveDir=${currDir}/test_cut/

echo "Removing old test files..."
rm -rf ${saveDir}
echo "Converting all audio to mono channel, 16Khz..."
mkdir -p ${tmpDir}
mkdir -p ${saveDir}
for filename in ${voiceDir}/*.wav; do
    baseFilename=$(basename ${filename})
    ffmpeg -loglevel panic -i "${filename}" -acodec pcm_s16le -ac 1 -ar 16000 "${tmpDir}${baseFilename}"
done
echo "Starting to seach for loudest sections in each file...."
for filename in ${tmpDir}*.wav; do
    echo "Cutting file: ${filename}"
    ${execFile} ${filename} ${saveDir}
done
echo "Cleaning up intermediates..."
rm -rf ${tmpDir}
echo "Files are written to ${saveDir}"
echo "All done!"
