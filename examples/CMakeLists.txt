cmake_minimum_required(VERSION 2.8.12)
project(examples)

option(CPU_ONLY "If use cpu only" OFF)

SET(CMAKE_C_COMPILER g++)
add_compile_options(-std=c++11)

# set caffe root dir
#set(Caffe_DIR /workspace/dl/ssd/caffe/.build_release)
set(Caffe_DIR /workspace/dl/ssd/caffe/build)
find_package(Caffe)
include_directories(${Caffe_DIR}/../include)
include_directories(${Caffe_DIR}/include)
include_directories(/usr/local/cuda-9.0/targets/x86_64-linux/include)

find_package(OpenCV REQUIRED)
add_definitions(-DUSE_OPENCV)

include_directories(include
        ${OpenCV_INCLUDE_DIRS}
        )

    #add_library(classify SHARED ${SRC_FILES})
    #target_link_libraries(classify
    #    ${OpenCV_LIBS}
    #    ${Caffe_LIBRARIES}
    #    )

set(TEST_FILES src/ssd_detect.cpp)
add_executable(ssd_detect ${TEST_FILES})
target_link_libraries(ssd_detect
        ${OpenCV_LIBS}
        ${Caffe_LIBRARIES}
        )
