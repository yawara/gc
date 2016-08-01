#include <iostream>
#include <fstream>
#include <string>
//#include <csignal>

#include <pylon/PylonIncludes.h>

using namespace Pylon;
using namespace GenApi;

// Settings for using  Basler USB cameras.
#include <pylon/usb/BaslerUsbInstantCamera.h>
using namespace Basler_UsbCameraParams;
typedef CBaslerUsbInstantCamera Camera_t;

// The camera specific grab result smart pointer.
typedef Camera_t::GrabResultPtr_t GrabResultPtr_t;

//void signalHandler( int signum ){}

bool fexists(const char *filename) {
  std::ifstream ifile(filename);
  return (bool)ifile;
}

int main(int argc, char const *argv[]) {
  //signal(SIGINT, signalHandler);

  PylonAutoInitTerm autoInitTerm;

  const char* pipefile = argv[1];
  const char* target = argv[2];
  //const int exposure_time = 300000;
  const char* camera_features = argv[3];
  std::string message;

  GrabResultPtr_t ptrGrabResult;

  try
  {
    Camera_t camera( CTlFactory::GetInstance().CreateFirstDevice());
    std::cout << "Using device " << camera.GetDeviceInfo().GetModelName() << std::endl;
    camera.Open();

    if(fexists(camera_features))
    {
      std::cout << "Loading camera features from " << camera_features << std::endl;
      CFeaturePersistence::Load( camera_features, &camera.GetNodeMap(), true );
    }

    //camera.ExposureTime.SetValue(exposure_time);
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
          std::cout << "try to grab" << std::endl;
          camera.RetrieveResult( 1000, ptrGrabResult, TimeoutHandling_ThrowException);
          //camera.GrabOne( 1000, ptrGrabResult);
          if (ptrGrabResult->GrabSucceeded())
          {
            // The pylon grab result smart pointer classes provide a cast operator to the IImage
            // interface. This makes it possible to pass a grab result directly to the
            // function that saves an image to disk.
            std::cout << "grabbing successfully" << std::endl;
            std::cout << "try to save image" << std::endl;
            CImagePersistence::Save( ImageFileFormat_Tiff, target, ptrGrabResult);
            std::cout << "saving image successfully" << std::endl;
            std::ofstream ofs(pipefile);
            ofs << "success" << std::endl;
          }
        }
        catch (const GenericException &e)
        {
            // Error handling.
            std::cerr << "An exception occurred: " << e.GetDescription() << std::endl;
            std::ofstream ofs(pipefile);
            ofs << "grab failed" << std::endl;
        }
      } else if (message == "stop")
      {
        return 0;
      }
    }
  }
  catch (const GenericException &e)
  {
      // Error handling.
      std::cerr << "An exception occurred: " << e.GetDescription() << std::endl;
      std::ofstream ofs(pipefile);
      ofs << "camera failed" << std::endl;
  }
  return 0;
}
