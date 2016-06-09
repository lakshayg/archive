#include <iostream>
#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

const int grid_size = 50; // rows and cols in grid
const int cell_size = 10; // size of each cell in pixels
static int grid[grid_size][grid_size]; // array containing cell color
char name[] = "Conway's Game of Life";
Mat img = Mat(cell_size*grid_size, cell_size*grid_size, CV_8UC3); // Actual image being displayed
const int delay = 100;

void refresh_display() {
    Rect roi;
    Mat tmp;
    Scalar cell_color;
    for (int i=0; i<grid_size; i++) {
        for (int j=0; j<grid_size; j++) {
            roi = Rect(Point(j,i)*cell_size,Size(cell_size, cell_size)); 
            cell_color = Scalar::all(255*grid[i][j]);
            tmp = Mat(cell_size, cell_size, CV_8UC3, cell_color);
            tmp.copyTo(img(roi));
        }
    }

    // draw border lines
    for (int i=0; i<grid_size; i++) {
        line(img, Point((i+1)*cell_size, 0), Point((i+1)*cell_size, cell_size*grid_size - 1), Scalar(128,128,128));
        line(img, Point(0,(i+1)*cell_size), Point(cell_size*grid_size - 1, (i+1)*cell_size), Scalar(128,128,128));
    }
    imshow(name, img);
}

int count_neighbors(int row, int col) {
    int sum = 0;
    for (int i=-1; i<=1; i++)
        for (int j=-1; j<=1; j++)
            if (0<=row+i && row+i<=grid_size && 0<=col+j && col+j<=grid_size)
                sum += grid[row+i][col+j];
    return sum - grid[row][col];
}

void update_grid() {
    int tmp[grid_size][grid_size]; // A temporary grid for calculations
    for (int i=0; i<grid_size; i++)
        for (int j=0; j<grid_size; j++)
            tmp[i][j] = grid[i][j];

    int count;
    for (int i=0; i<grid_size; i++) {
        for (int j=0; j<grid_size; j++) {
            count = count_neighbors(i,j);
        //rules of the game
            if (count < 2)
                tmp[i][j] = 0;
            else if (count == 3)
                tmp[i][j] = 1;
            else if (count > 3)
                tmp[i][j] = 0;
        }
    }

    for (int i=0; i<grid_size; i++) // Update the original grid
        for (int j=0; j<grid_size; j++)
            grid[i][j] = tmp[i][j];
}

void on_mouse(int event, int x, int y, int flags, void* userdata) {
    if (event == EVENT_LBUTTONDOWN) {
        int col = x/cell_size;
        int row = y/cell_size;
        grid[row][col] = 1-grid[row][col];
    }
}

int main() {
   namedWindow(name, WINDOW_AUTOSIZE); // create the display window

   setMouseCallback(name, on_mouse, NULL);

   while ((char)waitKey(10) != ' ') {
       refresh_display();
   }

   while (1) {
       refresh_display();
       update_grid();
       if ((char)waitKey(delay)=='x')
           exit(0);
   }
   return 0;
}
