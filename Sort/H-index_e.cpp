#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> citations) {
    int h_index = 0;
    
    // 1. 논문의 인용 횟수를 '내림차순(큰 수부터)'으로 정렬합니다.
    // greater<int>()를 추가하면 내림차순 정렬이 됩니다.
    sort(citations.begin(), citations.end(), greater<int>());
    
    // 2. 정렬된 배열을 순회하며 H-Index의 최댓값을 찾습니다.
    for (int i = 0; i < citations.size(); ++i) {
        // 인용 횟수가 현재까지 살펴본 논문의 수(i + 1)보다 크거나 같으면 H-Index 조건을 만족합니다.
        // i는 0부터 시작하므로 인용 횟수(citations[i])와 논문 개수(i + 1)를 비교하는 원리입니다.
        // 여기서는 citations[i] > i 로 간단히 표현할 수 있습니다.
        if (citations[i] > i) {
            h_index++;
        } else {
            // 인용 횟수가 논문 개수보다 작아지는 순간, 더 이상 H-Index는 커질 수 없으므로 멈춥니다.
            break;
        }
    }
    
    return h_index;
}
