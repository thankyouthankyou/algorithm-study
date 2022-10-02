# algorithm-study
* 스터디 일시 : 매주 화요일 19시, 일요일 14시


## Study Rule
* Github를 통한 코드 공유 및 피드백
    * [Feature Branch Workflow](https://gmlwjd9405.github.io/2017/10/27/how-to-collaborate-on-GitHub-1.html) 방식을 이용한다


* 이론 정리
    * 매 주차 별 공부 할 주제를 지정한다 (자료구조, 알고리즘) ex) LinkedList, Stack, Heap, Tree, Sort, Two Pointer, Greedy 등등)
    * 해당 주제를 Issues에 등록한다
    * Issues에 Comment로 이론 정리 / 공부하고 싶은 개념, 어려웠던 부분, 오류가 난 부분 등 추가로 작성해도 무방하다


* 숙제
    * 자신의 개인 브랜치를 만들어 회차 별 단위로 숙제를 HomeWork 폴더에 본인 브랜치명으로 폴더를 생성하여 MarkDown 파일로 작성
    * 스터디 모임 전 Master Branch로 PR
    * PR을 같이 보며 피드백


---
### 수학1-1(나머지, 최대공약수, 최소공배수, GCD의 합, 진법)
*  최대공약수(GCD)를 구하는 방법 '유클리드 호제법'의 개념
*  최대공약수를 이용하여 최소공배수(LCM)를 구하는 방법
*  기본적인 아스키코드
*  10진수 <-> 2진수, 8진수, 16진수 변환 시 Integer API 사용

### 수학1-2(소수, 소인수분해, 팩토리얼)
*  1~N 까지의 수에서 모든 소수를 구하는 방법 '에라토스테네스의 체'의 개념
*  소인수분해의 개념과 간단한 풀이법

### 수학2-1(제곱, 행렬, 피보나치의 수, 이항계수, 파스칼의 삼각형)
*  분할정복을 이용하여 제곱을 구하는 방법
*  이진수의 원리를 이용하여 제곱을 구하는 방법
*  행렬의 곱 구하기
*  피사노 주기의 개념과 구하는 방법
*  음수 번째의 피보나치의 수에 대한 규칙성
*  이항계수 구하는 방법

### 수학2-2(카탈란 수, 오일러 피 함수, 유클리드 알고리즘, 나머지 연산, 순열)
*  카탈란 수의 개념과 적용 사례
*  카탈란 수 구하는 방법
*  오일러 피 함수의 개념과 활용
*  오일러 피 함수 구하는 방법
*  사전순으로 다음에 오는 순열

### 자료구조1
*  배열(Array)
*  연결리스트(Linked List)
*  스택(Stack)
*  큐(Queue)
*  해시테이블(Hash Table)

### 자료구조2
*  [[issues#1]](https://github.com/Green-Record/algorithm-study/issues/1)트리(Tree)
*  이진 탐색 트리(Binary Search Tree)
*  그래프(Graph)
*  힙(Heap)
*  우선순위 큐 (Priority Queue)
*  트라이(Trie)

### 알고리즘
*  정렬(Sort)
*  이진 탐색(Binary Search)
*  투 포인터(Two Point)
*  그리디(Greedy)
*  분할 정복(Divide and Conquer)
*  동적 프로그래밍(Dynamic Programming)
*  백트래킹(Back Tracking)
*  최단 경로(Shortest Path)
*  최소 신장 트리(Minimum Spanning Tree)

### 트리와 이진 탐색
*  트리와 그래프의 차이점
*  이진 트리의 순회(전위, 중위, 후위 순회)
*  이진 탐색의 개념

### 그래프1(DFS, BFS, 이분그래프, 사이클, 플러드 필)
*  트리나 그래프를 방문 또는 탐색하는 방법 1: BFS(너비 우선 탐색)
*  트리나 그래프를 방문 또는 탐색하는 방법 2: DFS(깊이 우선 탐색)
*  이분 그래프의 개념
*  이분 그래프인지 확인하는 방법
*  사이클의 개념
*  플러드 필(Flood Fill) 알고리즘의 개념

### 그래프2(DAG(Directed Acyclic Graph), 위상 정렬, 최소 비용 신장 트리(Minimum Spanning Tree), Prim, Kruskal, 최단 경로(Shortest Path), Bellman-Ford)
*  DAG(Directed Acyclic Graph)의 개념
*  위상 정렬(Topological Sort)
*  최소 비용 신장 트리(MST, Minimum Spanning Tree)
*  Prim MST 알고리즘
*  Kruskal MST 알고리즘
*  최단 경로(Shortest Path)
*  Bellman-Ford 알고리즘
