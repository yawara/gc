#include <iostream>
#include <fstream>
#include <string>
#include <opencv2/opencv.hpp>


int main(int argc, char const *argv[]) {
  std::string pipefile = argv[1];
  std::string target = argv[2];

  cv::VideoCapture cap(0);

  while(true)
  {
    std::ifstream ifs(pipefile);
    std::string message;
    while(getline(ifs, message))
    {
      if(message == "request")
      {
        ifs.close();
        cv::Mat frame;
        cap >> frame;
        cv::imwrite(target, frame);
        std::ofstream ofs(pipefile);
        ofs << "success" << std::endl;
        break;
      } else if (message == "stop")
      {
        return 0;
      }
    }
  }
  return 0;
}
