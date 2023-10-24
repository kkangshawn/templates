#!/usr/bin/python3
import argparse

CMAKELIST = '''cmake_minimum_required(VERSION 3.14)
project({PROJECTNAME})

set(CMAKE_CXX_STANDARD 17)

include(FetchContent)
FetchContent_Declare(
    googletest
    GIT_REPOSITORY             https://github.com/google/googletest.git
    GIT_TAG                    f8d7d77c06936315286eb55f8de22cd23c188571 # v1.14.0
    DOWNLOAD_EXTRACT_TIMESTAMP true
)

set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

enable_testing()

add_executable(
    {PROJECTNAME}
    test_main.cc
    )
target_link_libraries(
    {PROJECTNAME}
    gtest_main
    )

include(GoogleTest)
gtest_discover_tests({PROJECTNAME})
'''

TESTMAIN = '''#include <gtest/gtest.h>

'''

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('ProjectName', help="Project Name")
    args = parser.parse_args()

    with open('CMakeLists.txt', 'w') as f:
        f.write(CMAKELIST.format(PROJECTNAME=args.ProjectName))
    with open('test_main.cc', 'w') as f:
        f.write(TESTMAIN)

    print("Successfully created a googletest project template - " + args.ProjectName)
