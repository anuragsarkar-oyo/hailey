cmake_minimum_required(VERSION 3.13)


message("target and directory loading ...........")
set(CMAKE_TOOLCHAIN_FILE "Users/oyo/Desktop/vcpkg/scripts/buildsystems/vcpkg.cmake"
        CACHE STRING "")

message(${CMAKE_TOOLCHAIN_FILE})
message("laod successful")


project(Hailey)

set(CMAKE_CXX_STANDARD 14)

add_executable(Hailey src/main.cpp)