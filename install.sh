#!/usr/bin/bash

# Will exit the Bash script the moment any command will itself exit with a non-zero status, thus an error.
set -e

EXTRACT_PATH=$1
INSTALL_PATH=${REZ_BUILD_INSTALL_PATH}
MULTIVERSE_VERSION=${REZ_BUILD_PROJECT_VERSION}

# We print the arguments passed to the Bash script.
echo -e "\n"
echo -e "==============="
echo -e "=== INSTALL ==="
echo -e "==============="
echo -e "\n"

echo -e "[INSTALL][ARGS] EXTRACT PATH: ${EXTRACT_PATH}"
echo -e "[INSTALL][ARGS] INSTALL PATH: ${INSTALL_PATH}"
echo -e "[INSTALL][ARGS] MULTIVERSE VERSION: ${MULTIVERSE_VERSION}"

# We install Multiverse.
echo -e "\n"
echo -e "[INSTALL] Installing Multiverse-${MULTIVERSE_VERSION}..."

# # We copy the necessary files to the install directory.
cp -R ${EXTRACT_PATH}/* ${INSTALL_PATH}

echo -e "[INSTALL] Finished installing Multiverse-${MULTIVERSE_VERSION}!"
echo -e "\n"
