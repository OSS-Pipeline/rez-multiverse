CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# Multiverse
rez_set_archive(
    # This is a relative path from the ${REZ_REPO_PAYLOAD_DIR} environment variable,
    # that is pointing to the root directory where we can find all the archives of the package
    # we can build, using the following hierarchy:
    # "${REZ_REPO_PAYLOAD_DIR}/project_name/archive.what.ever"
    MULTIVERSE_URL multiverse/Multiverse-${REZ_BUILD_PROJECT_VERSION}-Public-Linux-EL7.tar.gz
    https://url.to/multiverse/package.tar.gz
)

# The environment variable REZ_TMP_PATH is meant to point to a location such as "/tmp/rez".
set(EXTRACT_DIR $ENV{REZ_TMP_PATH}/multiverse/${REZ_BUILD_PROJECT_VERSION})

# We configure/build/install Multiverse through the ExternalProject_Add macro,
# using three different shell scripts for each of these steps.
# If necessary, it is possible to skip one of these steps by replacing the command
# by "", an empty string.
ExternalProject_Add(
    REZ_MULTIVERSE
    URL ${MULTIVERSE_URL}
    PREFIX multiverse
    SOURCE_DIR ${EXTRACT_DIR}
    PATCH_COMMAND ""
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND bash ${CMAKE_SOURCE_DIR}/install.sh ${EXTRACT_DIR}
)

# We use a bogus CMake "install" step in order to be able to properly finish
# and get out of the CMake script.
install(
    CODE
    "execute_process(
        COMMAND echo \"\n[CMAKE] Multiverse-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
