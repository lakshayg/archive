#include <stdlib.h>
#include <opencv2/opencv.hpp>
#include <libfreenect_sync.h>
#include <iostream>

using namespace cv;

int main() {   
  while (waitKey(10) < 0) {
    void *data = NULL;
    unsigned int timestamp;
    freenect_sync_get_depth(&data, &timestamp, 0, FREENECT_DEPTH_REGISTERED);	        
    Mat image(480, 640, CV_16UC1, data, 0);
    std::cout << image << std::endl;
  }

  freenect_sync_stop();       
  return 0;
}
