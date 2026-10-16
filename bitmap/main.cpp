#include <fstream>
#include <iostream>

static int read_int(const unsigned char* bytes) {
    return *reinterpret_cast<const int*>(bytes);
}

static short read_short(const unsigned char* bytes) {
    return *reinterpret_cast<const short*>(bytes);
}

static void print_pixel(std::ifstream& file, const int offset, const char* name) {
    unsigned char pixel[3] = {0, 0, 0};
    file.seekg(offset, std::ios::beg);
    file.read(reinterpret_cast<char*>(pixel), 3);

    std::cout << name << " R: " << (int)pixel[2]
              << " G: " << (int)pixel[1]
              << " B: " << (int)pixel[0] << std::endl;
}

int main(const int argc, char** argv) {
    const char* path = argc > 1 ? argv[1] : "image.bmp";

    std::ifstream file(path, std::ios::binary);
    if (!file) {
        std::cerr << "CANT LOAD FILE: " << path << std::endl;
        return 1;
    }

    unsigned char header[54];
    file.read(reinterpret_cast<char*>(header), 54);

    if (header[0] != 'B' || header[1] != 'M') {
        std::cerr << "INVALID BMP FILE SIGNATURE!" << std::endl;
        return 1;
    }

    const int data_offset = read_int(&header[10]);
    const int width = read_int(&header[18]);
    const int height = read_int(&header[22]);
    const short bits_per_pixel = read_short(&header[28]);

    std::cout << "2b signature: BM" << std::endl;
    std::cout << "4b file_size: " << read_int(&header[2]) << std::endl;
    std::cout << "4b reserved: " << read_int(&header[6]) << std::endl;
    std::cout << "4b data_offset: " << data_offset << std::endl;
    std::cout << "4b info_header_size: " << read_int(&header[14]) << std::endl;
    std::cout << "4b width: " << width << std::endl;
    std::cout << "4b height: " << height << std::endl;
    std::cout << "2b planes: " << read_short(&header[26]) << std::endl;
    std::cout << "2b bits_per_pixel: " << bits_per_pixel << std::endl;
    std::cout << "4b compression: " << read_int(&header[30]) << std::endl;
    std::cout << "4b image_size: " << read_int(&header[34]) << std::endl;
    std::cout << "4b x_pixels_per_m: " << read_int(&header[38]) << std::endl;
    std::cout << "4b y_pixels_per_m: " << read_int(&header[42]) << std::endl;
    std::cout << "4b colors_used: " << read_int(&header[46]) << std::endl;
    std::cout << "4b colors_important: " << read_int(&header[50]) << std::endl;

    const int bytes_per_pixel = bits_per_pixel / 8;
    const int row_size = ((bits_per_pixel * width + 31) / 32) * 4;

    const int first_row = data_offset;
    const int last_row = data_offset + (height - 1) * row_size;
    const int last_column = (width - 1) * bytes_per_pixel;

    std::cout << std::endl;
    print_pixel(file, last_row, "Top left:");
    print_pixel(file, last_row + last_column, "Top right:");
    print_pixel(file, first_row, "Bottom left:");
    print_pixel(file, first_row + last_column, "Bottom right:");

    return 0;
}
