#include <iostream>
#include <fstream>
#include <string>
#include <opencv2/opencv.hpp>
#include <pylon/PylonIncludes.h>

using namespace Pylon;
using namespace GenApi;

// Settings for using  Basler USB cameras.
#include <pylon/usb/BaslerUsbInstantCamera.h>
using namespace Basler_UsbCameraParams;
typedef CBaslerUsbInstantCamera Camera_t;

// The camera specific grab result smart pointer.
typedef Camera_t::GrabResultPtr_t GrabResultPtr_t;

int main(int argc, char const *argv[]) {
  PylonAutoInitTerm autoInitTerm;

  const char* pipefile = argv[1];
  const char* target = argv[2];
  const int exposure_time = std::stoi(argv[3]);
  std::string message;

  GrabResultPtr_t ptrGrabResult;

  Camera_t camera( CTlFactory::GetInstance().CreateFirstDevice());
  std::cout << "Using device " << camera.GetDeviceInfo().GetModelName() << std::endl;
  camera.Open();

  camera.ExposureTime.SetValue(exposure_time);
  //camera.RegisterConfiguration( new CAcquireContinuousConfiguration, RegistrationMode_ReplaceAll, Cleanup_Delete);
  //camera.Width.SetValue(2000);
  //camera.Height.SetValue(1000);
  //camera.CenterX.SetValue(true);
  //camera.CenterY.SetValue(true);

  //camera.OffsetX.SetValue(0);
  //camera.OffsetY.SetValue(0);
  camera.MaxNumBuffer = 5;

  camera.StartGrabbing();

  while(true)
  {
    std::ifstream ifs(pipefile);
    getline(ifs, message);
    ifs.close();
    if(message == "request")
    {
      try
      {
        camera.RetrieveResult( 1000, ptrGrabResult, TimeoutHandling_ThrowException);
        //camera.GrabOne( 1000, ptrGrabResult);
        if (ptrGrabResult->GrabSucceeded())
        {
          // The pylon grab result smart pointer classes provide a cast operator to the IImage
          // interface. This makes it possible to pass a grab result directly to the
          // function that saves an image to disk.
          CImagePersistence::Save( ImageFileFormat_Tiff, target, ptrGrabResult);
          std::ofstream ofs(pipefile);
          ofs << "success" << std::endl;
        }
      }
      catch (const GenericException &e)
      {
          // Error handling.
          std::cerr << "An exception occurred: " << e.GetDescription() << std::endl;
          std::ofstream ofs(pipefile);
          ofs << "failed" << std::endl;
      }
    } else if (message == "stop")
    {
      return 0;
    }
  }
  return 0;
}
