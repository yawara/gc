all: video_opencv video_basler

### video_opencv
OPENCV_FLAGS := $(shell pkg-config --libs --cflags opencv)

video_opencv: video_opencv.cpp
	$(CXX) video_opencv.cpp $(OPENCV_FLAGS) -o video_opencv

### video_basler

# Installation directories for pylon
PYLON_ROOT ?= /opt/pylon5

# Build tools and flags
NAME			 := video_basler
LD         := $(CXX)
CPPFLAGS   := $(shell $(PYLON_ROOT)/bin/pylon-config --cflags)
CXXFLAGS   := #e.g., CXXFLAGS=-g -O0 for debugging
LDFLAGS    := $(shell $(PYLON_ROOT)/bin/pylon-config --libs-rpath)
LDLIBS     := $(shell $(PYLON_ROOT)/bin/pylon-config --libs)

$(NAME): $(NAME).o
	$(LD) $(LDFLAGS) -o $@ $^ $(LDLIBS)

$(NAME).o: $(NAME).cpp
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -c -o $@ $<

clean:
	$(RM) video_opencv video_basler
