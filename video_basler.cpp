#include <iostream>
#include <fstream>
#include <string>
#include <opencv2/opencv.hpp>
#include <pylon/PylonIncludes.h>

using namespace Pylon;

// Settings for using  Basler USB cameras.
#include <pylon/usb/BaslerUsbInstantCamera.h>
typedef CBaslerUsbInstantCamera Camera_t;
// The camera specific grab result smart pointer.
typedef Camera_t::GrabResultPtr_t GrabResultPtr_t;

int main(int argc, char const *argv[]) {
  PylonAutoInitTerm autoInitTerm;

  std::string pipefile = argv[1];
  std::string target = argv[2];
  std::string message;

  GrabResultPtr_t ptrGrabResult;
  Camera_t camera( CTlFactory::GetInstance().CreateFirstDevice());
  camera.Open();

  camera.ExposureTime.SetValue(atoi(argv[1]));
  //camera.RegisterConfiguration( new CAcquireContinuousConfiguration, RegistrationMode_ReplaceAll, Cleanup_Delete);

  //camera.Width.SetValue(2000);
  //camera.Height.SetValue(1000);
  //camera.CenterX.SetValue(true);
  //camera.CenterY.SetValue(true);

  //camera.OffsetX.SetValue(0);
  //camera.OffsetY.SetValue(0);

  camera.StartGrabbing();

  while(true)
  {
    std::ifstream ifs(pipefile);
    while(getline(ifs, message))
    {
      if(message == "request")
      {
        ifs.close();
        camera.RetrieveResult( 5000, ptrGrabResult, TimeoutHandling_ThrowException);
        //camera.GrabOne( 1000, ptrGrabResult);
        if (ptrGrabResult->GrabSucceeded())
        {
          // The pylon grab result smart pointer classes provide a cast operator to the IImage
          // interface. This makes it possible to pass a grab result directly to the
          // function that saves an image to disk.
          CImagePersistence::Save( ImageFileFormat_Tiff, target, ptrGrabResult);
          std::ofstream ofs(pipefile);
          ofs << "success" << std::endl;
          break;
        }
      } else if (message == "stop")
      {
        return 0;
      }
    }
  }
  return 0;
}
