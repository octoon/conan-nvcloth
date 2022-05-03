from numpy import source
from conans import ConanFile, CMake, tools
import os
import shutil

class NvclothConan(ConanFile):
    name = "nvcloth"
    version = "1.1.6"

    # Optional metadata
    license = "Nvidia Source Code License (1-Way Commercial)"
    author = "NVIDIA Corporation"
    url = "https://github.com/NVIDIAGameWorks/NvCloth"
    description = "NvCloth is a library that provides low level access to a cloth solver designed for realtime interactive applications."
    topics = ("cloth solver")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "use_cuda": [True, False], "use_dx11": [True, False]}
    default_options = {"shared": False, "use_cuda": False, "use_dx11": True}

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    @property
    def _build_subfolder(self):
        return "build_subfolder"

    def source(self):
        git = tools.Git(folder=self._source_subfolder)
        git.clone("https://github.com/NVIDIAGameWorks/NvCloth.git", "1.1.6")

    def _configure_cmake(self):
        osname = str(self.settings.os).lower()
        cmake = CMake(self)
        cmake.definitions["CMAKE_BUILD_TYPE"]=self.settings.build_type
        if self.settings.compiler == "Visual Studio":
            cmake.definitions["WITH_LIBCXX"]="OFF"
        else:
            if "libstdc++" in self.settings.compiler.libcxx:
                cmake.definitions["WITH_LIBCXX"]="ON"
            else:
                cmake.definitions["WITH_LIBCXX"]="OFF"
        if self.settings.compiler.runtime in ["MT", "MTd"]:
            cmake.definitions["STATIC_WINCRT"]="ON"
        else:
            cmake.definitions["STATIC_WINCRT"]="OFF"

        if self.options.use_cuda:
            cmake.definitions["NV_CLOTH_ENABLE_CUDA"]="ON"
        else:
            cmake.definitions["NV_CLOTH_ENABLE_CUDA"]="OFF"
        
        if self.options.use_dx11:
            cmake.definitions["NV_CLOTH_ENABLE_DX11"]="ON"
        else:
            cmake.definitions["NV_CLOTH_ENABLE_DX11"]="OFF"

        cmake.definitions["TARGET_BUILD_PLATFORM"] = osname

        source_folder = os.path.join(self._source_subfolder, "NvCloth")
        cmakefile = os.path.join(source_folder, "compiler", "cmake", osname)

        cmake.configure(source_folder=cmakefile)
        return cmake
    
    def _fix_source(self):
        if self.settings.os != "Windows":
            return
        filepath = os.path.join(self._source_subfolder, "NvCloth/include/NvCloth/ps/PsAllocator.h")
        # #include <typeinfo.h> to #include <typeinfo>
        with open(filepath, "r") as f:
            new_text = f.read().replace('#include <typeinfo.h>', '#include <typeinfo>')

        with open(filepath, "w") as f:
            f.write(new_text)

    def build(self):
        os.environ['GW_DEPS_ROOT'] = os.path.abspath(self._source_subfolder)
        self._fix_source()
        cmake = self._configure_cmake()
        cmake.build(target='NvCloth')

    def package(self):
        self.copy("*.h", dst="include", src=os.path.join(self._source_subfolder, "runtime", "src"))
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.jar", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        '''
        # debug_postfix = "d" if self.settings.build_type == "Debug" else ""
        shared_postfix = "shared" if self.options.shared else "static"
        self.cpp_info.libs = ["antlr4-runtime-" + shared_postfix]
        if not self.options.shared:
            self.cpp_info.defines.append("ANTLR4CPP_STATIC")
        '''