#!/bin/bash
dl_url=$(curl -s 'https://api.github.com/repos/WFCD/warframe-items/releases/latest' | jq -r '.tarball_url')
filename="${dl_url##*/}.tar.gz"
wget "${dl_url}" -O ${filename}
tar -xzvf ${filename} --strip-components=3 -C warframe_site/static '*/data/img'
rm -f ${filename}
