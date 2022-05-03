cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

FIND_PACKAGE(nvcloth REQUIRED)

add_executable(nvcloth_example main.cpp)
target_include_directories(nvcloth_example PRIVATE ${CONAN_INCLUDE_DIRS})
target_link_libraries(nvcloth_example ${fcdk_LIBRARIES})