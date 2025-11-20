# StudyAlgorithm

알고리즘 학습을 위한 예제 모음입니다.

## 개요

다양한 알고리즘과 수학적 모델을 구현한 예제 코드입니다.

## 주요 기능

### 1. Dijkstra.py
- 다익스트라 알고리즘 구현
- 최단 경로 찾기
- 그래프 기반 경로 탐색

### 2. MontyHall.py
- 몬티 홀 문제 시뮬레이션
- 전략별 승률 계산
- 통계적 검증

### 3. S_I_R.py
- 전염병 확산 모델 (SI, SIS, SIR)
- 시각화
- 수학적 모델링

## 사용 방법

### 다익스트라 알고리즘

```bash
python Dijkstra.py
```

### 몬티 홀 문제

```bash
python MontyHall.py
```

실행 횟수를 입력하세요.

### 전염병 모델

```bash
python S_I_R.py
```

SI, SIS, SIR 모델이 순차적으로 실행됩니다.

## 요구사항

- Python 3.12
- matplotlib (S_I_R.py)

## 설치

### uv 설치

#### Windows
```powershell
# PowerShell에서 실행
irm https://astral.sh/uv/install.ps1 | iex
```

#### macOS / Linux
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

설치 후 터미널을 재시작하거나 다음 명령어로 PATH에 추가:
```bash
export PATH="$HOME/.cargo/bin:$PATH"
```

### 가상환경 설정

```bash
# Python 3.12 가상환경 생성
uv venv --python 3.12

# 가상환경 활성화
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

### 패키지 설치

```bash
# uv를 사용한 패키지 설치
uv pip install -r requirements.txt
```

## 파일 구조

- `Dijkstra.py`: 다익스트라 최단 경로 알고리즘
- `MontyHall.py`: 몬티 홀 문제 시뮬레이션
- `S_I_R.py`: 전염병 확산 모델

## 알고리즘 설명

### 다익스트라 알고리즘
그래프에서 한 정점에서 다른 모든 정점까지의 최단 경로를 찾는 알고리즘입니다.

### 몬티 홀 문제
확률론의 유명한 문제로, 문을 바꾸는 전략이 더 높은 승률을 제공함을 시뮬레이션으로 검증합니다.

### SIR 모델
- **S (Susceptible)**: 감염 가능한 개체
- **I (Infected)**: 감염된 개체
- **R (Recovered)**: 회복된 개체

병원체의 확산을 수학적으로 모델링합니다.

---

해당 프로젝트는 Examples-Python의 Private Repository에서 공개 가능한 수준의 소스를 Public Repository로 변환한 것입니다.

