cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

find_package(nvcloth REQUIRED)

add_executable(nvcloth_example main.cpp)
target_link_libraries(nvcloth_example nvcloth)