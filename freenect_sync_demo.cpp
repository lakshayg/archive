#include <stdlib.h>
#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <libfreenect_sync.h>

using namespace cv;

int main() {   
  while (waitKey(10) < 0) {
    void *data = NULL;
    unsigned int timestamp;
    freenect_sync_get_video(&data, &timestamp, 0, FREENECT_VIDEO_RGB);	        
    Mat image(480, 640, CV_8UC3, data, 0);

    cvtColor(image, image, CV_RGB2BGR);
    imshow("RGB", image);
  }

  freenect_sync_stop();       
  return 0;
}
