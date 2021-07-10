
#include <iostream>
// #include <fstream>
#include <complex>
#include <vector>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include<pybind11/complex.h>
using namespace std;
namespace py = pybind11;


///////////////////DFT function
vector<complex<double>> DFT(vector<complex<double>> data)
{
    int NumberOfSamples = data.size();
    int K = NumberOfSamples;
    complex<double> Frequency;
    vector<complex<double>> Frequencies;
    Frequencies.reserve(K);

    for (int k = 0; k < K; k++)
    {
       Frequency=(0);

        for (int n = 0; n < NumberOfSamples; n++)
        {
        double real = cos(((2 * M_PI) / NumberOfSamples) * k * n);
            double img = sin(((2 * M_PI) / NumberOfSamples) * k * n);
            complex<double> cotec(real, -img);
            Frequency += data[n] * cotec;
        }
        Frequencies.push_back(Frequency);
    }

    return Frequencies;
}

/////////////////////////FFT////////////////

vector<complex<double>> FFT(vector<complex<double>> &sampels)
{
    int NumberOfSampels = sampels.size();
    if (NumberOfSampels == 1)
    {
        return sampels;
    }

    int M = NumberOfSampels / 2;

    vector<complex<double>> SampelsEven(M, 0);
    vector<complex<double>> SampelsOdd(M, 0);

    for (int i = 0; i != M; i++)
    {
        SampelsEven[i] = sampels[2 * i];
        SampelsOdd[i] = sampels[2 * i + 1];
    }
    vector<complex<double>> FrequenciesEven(M, 0);
    FrequenciesEven = FFT(SampelsEven);
    vector<complex<double>> FrequenciesOdd(M, 0);
    FrequenciesOdd = FFT(SampelsOdd);
    vector<complex<double>> Frequencies(NumberOfSampels, 0);
    for (int k = 0; k != NumberOfSampels / 2; k++)
    {
        complex<double> ComplexExponential = polar(1.0, -2 * M_PI * k / NumberOfSampels) * FrequenciesOdd[k];
        Frequencies[k] = FrequenciesEven[k] + ComplexExponential;
        Frequencies[k + NumberOfSampels / 2] = FrequenciesEven[k] - ComplexExponential;
    }
    return Frequencies;
}

PYBIND11_MODULE(Fourier, pass) {
  
    pass.def("FFT", &FFT, "A function which adds two numbers");
    pass.def("DFT", &DFT, "A function which adds two numbers");
}




























// int main()
// {
//     inFile.open("test");

//     vector<complex<double>> Data; // Create vector of complex numbers
//                                   // Place 1 + j2 in vector

//     vector<complex<double>> TransformedData;

//     vector<complex<double>> dft;

//     while (inFile >> x)
//     {
//         Data.push_back(complex<double>(x));
//     }

//     dft = DFT(Data);
//     TransformedData = FFT(Data);

//     //for (int z =0 ;z<TransformedData.size();z++)
//     for (int z = 0; z < TransformedData.size(); z++)
//     {
//         cout << "DFT: " << dft[z] << '\n';
//         cout << "FFT: " << TransformedData[z] << '\n';
//         cout << '\n';
//         // cout<<TransformedData[i].real()+TransformedData[i].imag()*1i;
//     }

//     inFile.clear();
//     inFile.seekg(0, std::ios::beg);

//     while (inFile >> x)
//     {
//         sum++;
//     }

//     cout << sum << '\n';
// }