#include <string>
#include <vector>
#include <algorithm> // sort 함수를 사용하기 위한 헤더

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    // commands 배열의 모든 원소(command)에 대해 반복
    for (const auto& command : commands) {
        int i = command[0];
        int j = command[1];
        int k = command[2];
        
        // 1. 배열 자르기 (인덱스는 0부터 시작하므로 i-1부터 j까지)
        // array.begin()을 기준으로 원하는 인덱스만큼 더해서 범위를 지정합니다.
        vector<int> temp(array.begin() + i - 1, array.begin() + j);
        
        // 2. 배열 정렬하기 (오름차순)
        sort(temp.begin(), temp.end());
        
        // 3. k번째 수 구해서 정답 배열에 넣기 (인덱스는 k-1)
        answer.push_back(temp[k - 1]);
    }
    
    return answer;
}
