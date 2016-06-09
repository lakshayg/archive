#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

Mat bgr, hsv;

void callback(int event, int x, int y, int flags, void *userdata);

int main(int argc, char **argv) {
  if (argc != 2) {
    cout << "USAGE: colortool <filename>" << endl;
    return -1;
  }

  bgr = imread(argv[1], CV_LOAD_IMAGE_COLOR);
  cvtColor(bgr, hsv, COLOR_BGR2HSV);

  namedWindow("Image", CV_WINDOW_NORMAL);
  setMouseCallback("Image", callback, NULL);
  imshow("Image", bgr);

  waitKey();
  return 0;
}

void callback(int event, int x, int y, int flags, void *userdata) {
  cout << "BGR: " << bgr.at<Vec3b>(y, x)
        <<"\t HSV: " << hsv.at<Vec3b>(y,x) << endl;
  return;
}
