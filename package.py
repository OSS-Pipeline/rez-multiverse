name = "multiverse"

version = "5.8.0"

authors = [
    "J-Cube"
]

description = \
    """
    Stream complex 3D data in the Autodesk Maya Viewport using powerful lookdev, layout, composition and overriding
    workflows. Render procedurally with the 3Delight NSI and Arnold off-line production renderers.
    Inter-op with SideFX Houdini. Generate 3D data for AR. Multiverse is ultra fast, memory efficient, easy to use.
    """

requires = [
    "cmake-3"
]

variants = [
    ["platform-linux"]
]

tools = [
    "i-display",
    "licserver",
    "licutils",
    "nsidepends",
    "oslc",
    "renderdl",
    "tdlmake"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

#TODO: Use the SHA1 of the archive instead.
uuid = "multiverse-5.8.0"

def commands():
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/lib/python")
    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.MV_ROOT.append("{root}")
    env.MAYA_MODULE_PATH.prepend("{root}/Maya")
    env.ARNOLD_PLUGIN_PATH.append("{root}/lib/procedurals/arnold")
    env.USD_PLUG_IN_PATH.append("{root}/lib/plugin/usd")
