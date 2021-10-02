#include <iostream>
#include <time.h>
#include <stdlib.h>
//////your code here/////

////// end your code /////

//// [MSSV]

void swap(int* xp, int* yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

template<typename T> 
void printArray(T arr[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        std::cout << arr[i] << " ";
    std::cout << std::endl;
}
void insertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++)
    {
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}
void bubbleSort(int arr[], int n)
{
    int i, j;
    for (i = 0; i < n - 1; i++)
        for (j = 0; j < n - i - 1; j++)
            if (arr[j] > arr[j + 1])
                swap(&arr[j], &arr[j + 1]);
}
void merge(int array[], int const left, int const mid, int const right)
{
    auto const subArrayOne = mid - left + 1;
    auto const subArrayTwo = right - mid;
    auto* leftArray = new int[subArrayOne],
        * rightArray = new int[subArrayTwo];
    for (auto i = 0; i < subArrayOne; i++)
        leftArray[i] = array[left + i];
    for (auto j = 0; j < subArrayTwo; j++)
        rightArray[j] = array[mid + 1 + j];

    auto indexOfSubArrayOne = 0,
        indexOfSubArrayTwo = 0;
    int indexOfMergedArray = left;
    while (indexOfSubArrayOne < subArrayOne && indexOfSubArrayTwo < subArrayTwo) {
        if (leftArray[indexOfSubArrayOne] <= rightArray[indexOfSubArrayTwo]) {
            array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
            indexOfSubArrayOne++;
        }
        else {
            array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
            indexOfSubArrayTwo++;
        }
        indexOfMergedArray++;
    }
    while (indexOfSubArrayOne < subArrayOne) {
        array[indexOfMergedArray] = leftArray[indexOfSubArrayOne];
        indexOfSubArrayOne++;
        indexOfMergedArray++;
    }
    while (indexOfSubArrayTwo < subArrayTwo) {
        array[indexOfMergedArray] = rightArray[indexOfSubArrayTwo];
        indexOfSubArrayTwo++;
        indexOfMergedArray++;
    }
}
void mergeSort(int array[], int const begin, int const end)
{
    if (begin >= end)
        return;

    auto mid = begin + (end - begin) / 2;
    mergeSort(array, begin, mid);
    mergeSort(array, mid + 1, end);
    merge(array, begin, mid, end);
}

int partition(int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = (low - 1);
    for (int j = low; j <= high - 1; j++)
    {
        if (arr[j] < pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}
void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

//////your code here/////

////// end your code /////


void printStatic(unsigned int arr[], int N)
{
    unsigned int min, max;
    unsigned int sum = 0;
    float mean;
    //////your code here/////

    ////// end your code /////
    std::cout << "min:" << min << "\nmax:" << max << "\nmean:" << mean << std::endl;
}

void insertionSortComplexity(int num_simulation)
{
    unsigned int* STEP;
    STEP = new unsigned int[num_simulation];
    int N;
    int* arr;
    srand(time(NULL));
    for (int i = 0; i < num_simulation; i++) {
        N = rand() % 1000 + 50;
        arr = new int[N];
        for (int j = 0; j < N; j++) {
            arr[j] = rand();
        }
        unsigned int step = 0;
        //////your code here/////

        ////// end your code /////
        
        STEP[i] = step;
        delete[] arr;
    }
    printStatic(STEP, num_simulation);
}

void bubbleSortComplexity(int num_simulation)
{
    unsigned int* STEP;
    STEP = new unsigned int[num_simulation];
    int N;
    int* arr;
    srand(time(NULL));
    for (int i = 0; i < num_simulation; i++) {
        N = rand() % 1000 + 50;
        arr = new int[N];
        for (int j = 0; j < N; j++) {
            arr[j] = rand();
        }
        unsigned int step = 0;
        //////your code here/////

        ////// end your code /////
        
        STEP[i] = step;
        delete[] arr;
    }
    printStatic(STEP, num_simulation);
}

void mergeSortComplexity(int num_simulation)
{
    unsigned int* STEP;
    STEP = new unsigned int[num_simulation];
    int N;
    int* arr;
    srand(time(NULL));
    for (int i = 0; i < num_simulation; i++) {
        N = rand() % 1000 + 50;
        arr = new int[N];
        for (int j = 0; j < N; j++) {
            arr[j] = rand();
        }
        unsigned int step = 0;
        //////your code here/////

        ////// end your code /////
        
        STEP[i] = step;
        delete[] arr;
    }
    printStatic(STEP, num_simulation);
}

void quickSortComplexity(int num_simulation)
{
    unsigned int* STEP;
    STEP = new unsigned int[num_simulation];
    int N;
    int* arr;
    srand(time(NULL));
    for (int i = 0; i < num_simulation; i++) {
        N = rand() % 1000 + 50;
        arr = new int[N];
        for (int j = 0; j < N; j++) {
            arr[j] = rand();
        }
        unsigned int step = 0;
        //////your code here/////

        ////// end your code /////
        
        STEP[i] = step;
        delete[] arr;
    }
    printStatic(STEP, num_simulation);
}

int main()
{
    insertionSortComplexity(10);
    bubbleSortComplexity(10);
    mergeSortComplexity(10);
    quickSortComplexity(10);
    
    float Farr[] = { 1.0,10,2 };
    int Iarr[] = { 1,10,2 };
    bool descending = true;
    
    insertionSortGeneral(Farr, 3, descending);
    insertionSortGeneral(Iarr, 3, false);
    bubbleSortGeneral(Farr, 3, descending);
    bubbleSortGeneral(Iarr, 3, false);
    mergeSortGeneral(Farr,0, 2, descending);
    mergeSortGeneral(Iarr, 0, 2, false);
    quickSortGeneral(Farr,0, 2, descending);
    quickSortGeneral(Iarr, 0, 2, false);
    
    //external sort
    sortingFile("./data.txt","./dictionary.txt");
    
}

