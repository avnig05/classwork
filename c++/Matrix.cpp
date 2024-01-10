#include <iostream>
#include <vector>

using namespace std;

template<class T> 
class Matrix
    {
    public:
        vector<vector<T>> data;
        size_t rows;
        size_t cols;

        // Constructor to create an empty matrix with given dimensions
        Matrix<T>(size_t rows, size_t cols) : rows(rows), cols(cols) 
        {
            data.resize(rows, vector<T>(cols, 0.0));
        }

        // Constructor to create a matrix from a 2D vector
        Matrix<T>(const vector<vector<T>>& input) 
        {
            if (input.empty() || input[0].empty()) 
            {
                cerr << "Error: Cannot create a matrix from an empty input." << endl;
                exit(1);
            }
            rows = input.size();
            cols = input[0].size();
            data = input;
        }

        // Insert an element
        void insert(T value, size_t row, size_t col)
        {
            data[row][col] = value;
        }

        // Get the number of rows in the matrix
        size_t getRows() 
        {
            return rows;
        }

        // Get the number of columns in the matrix
        size_t getCols() 
        {
            return cols;
        }

        // Access an element in the matrix
        double& operator()(size_t row, size_t col) 
        {
            return data[row][col];
        }

        // rotate a matrix 
        void rotate() 
        {
            Matrix<T> temp(getCols(), getRows());
            for (int r = 0; r < getRows(); r++) 
            {
                for (int c = 0; c < getCols(); c++) 
                {
                    temp.insert(data[r][c], c, r);
                }
            }
            *this = temp;
        }

        // Addition of two matrices
        Matrix<T> operator+(Matrix<T>& other)
        {
            if (rows != other.rows || cols != other.cols) 
            {
                cerr << "Error: Matrix dimensions do not match for addition." << endl;
                exit(1);
            }

            Matrix<T> result(rows, cols);

            for (size_t i = 0; i < rows; ++i) 
            {
                for (size_t j = 0; j < cols; ++j) 
                {
                    result(i, j) = data[i][j] + other(i, j);
                }
            }

            return result;
        }

        Matrix<T> operator*(Matrix<T>& other) 
        {
            if (cols != other.rows) 
            {
                cerr << "Error: Matrix dimensions are incompatible for multiplication." << endl;
                exit(1);
            }

            Matrix<T> result(rows, other.cols);

            for (size_t i = 0; i < rows; ++i) 
            {
                for (size_t j = 0; j < other.cols; ++j) 
                {
                    for (size_t k = 0; k < cols; ++k) 
                    {
                        result(i, j) += data[i][k] * other(k, j);
                    }
                }
            }

            return result;
        }

        // Print the matrix
        void print()  
        {
            for (size_t i = 0; i < rows; ++i) 
            {
                for (size_t j = 0; j < cols; ++j) 
                {
                    cout << data[i][j] << ' ';
                }
                cout << endl;
            }
        }
    };

    int main()
    {
        Matrix<double>data1(3, 5); 
        for (int r = 0; r < data1.getRows(); r++)
        {
            for (int c = 0; c < data1.getCols(); c++)
            {
                data1.insert(rand() % 100, r, c);
            }
        }
        data1.print();
        data1.rotate();
        data1.print();
    }