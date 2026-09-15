#include <string>
#include <vector>

using namespace std;

// 1. 커스텀 비교 함수: a+b 와 b+a 중 더 큰 것을 판단
bool compare(const string& a, const string& b) {
    return a + b > b + a;
}

// 2. 퀵 정렬 알고리즘 직접 구현
void quickSort(vector<string>& arr, int low, int high) {
    if (low >= high) return; // 정렬할 원소가 1개 이하면 종료

    int i = low;
    int j = high;
    
    // 배열의 가운데 원소를 기준값(피벗, Pivot)으로 설정
    string pivot = arr[(low + high) / 2];

    // i와 j가 교차할 때까지 반복하며 배열을 둘로 분할
    while (i <= j) {
        // 왼쪽(i)에서는 피벗보다 뒤에 가야 할(우선순위가 낮은) 값을 찾음
        while (compare(arr[i], pivot)) {
            i++;
        }
        // 오른쪽(j)에서는 피벗보다 앞에 와야 할(우선순위가 높은) 값을 찾음
        while (compare(pivot, arr[j])) {
            j--;
        }

        // i와 j가 엇갈리지 않았다면 두 값의 위치를 교환(Swap)
        if (i <= j) {
            string temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }

    // 분할된 왼쪽과 오른쪽 부분 배열에 대해 각각 퀵 정렬을 재귀적으로 호출
    quickSort(arr, low, j);
    quickSort(arr, i, high);
}

string solution(vector<int> numbers) {
    vector<string> str_numbers;
    
    // int형 숫자를 string으로 변환
    for (int num : numbers) {
        str_numbers.push_back(to_string(num));
    }
    
    // 3. 직접 만든 퀵 정렬 함수 호출 (처음부터 끝까지)
    quickSort(str_numbers, 0, str_numbers.size() - 1);
    
    // 예외 처리: 가장 큰 수가 "0"으로 시작하면 전체가 "0"인 경우
    if (str_numbers[0] == "0") {
        return "0";
    }
    
    // 문자열 하나로 합치기
    string answer = "";
    for (const string& str : str_numbers) {
        answer += str;
    }
    
    return answer;
}
