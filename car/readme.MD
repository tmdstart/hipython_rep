Sure, here's a more visually appealing and detailed version of your analysis, suitable for a `README.md` file:

-----

# 🚗 중고차 가격 예측 프로젝트 분석 보고서 📈

## ✨ 모델 성능 요약

저희 중고차 가격 예측 모델들의 성능은 다음과 같습니다:

| 모델               | R² 점수 |
| :----------------- | :------ |
| **XGBoost** | **0.639** |
| 랜덤 포레스트      | 0.617   |
| 다항 연산          | 0.532   |
| 릿지               | 0.53    |
| 선형 회귀          | 0.51    |
| 엘라스틱넷         | 0.41    |

\<br\>

-----

## 🔍 데이터 전처리 및 피처 엔지니어링 심층 분석

### 📊 초기 데이터셋

프로젝트에 사용된 초기 중고차 데이터는 아래와 같은 지표들을 포함하고 있었습니다:

`title`, `price_in_aed`, `kilometers`, `body_condition`, `mechanical_condition`, `seller_type`, `body_type`, `no_of_cylinders`, `transmission_type`, `regional_specs`, `horsepower`, `fuel_type`, `steering_side`, `year`, `color`, `emirate`, `motors_trim`, `company`, `model`, `date_posted`

### 🧹 피처 선택 및 제외

저희는 `title`, `price_in_aed`, `motors_trim`, `model`과 같은 특정 컬럼들을 \*\*X 데이터(예측에 사용될 피처)\*\*에서 **제외**했습니다.

`steering_side` 피처는 분석 결과 모델의 정확도에 **유의미한 영향을 주지 않아** 최종적으로 제외되었습니다.

### 🔄 범주형 데이터 인코딩

`body_condition`, `mechanical_condition`, `seller_type`, `body_type`, `no_of_cylinders`, `transmission_type`, `regional_specs`, `color`, `fuel_type`, `emirate`와 같은 범주형 데이터는 \*\*원-핫 인코딩(One-Hot Encoding)\*\*을 통해 수치형으로 변환되었습니다. 하지만 개별 피처를 제외하며 테스트했을 때, 정확도가 유의미하게 상승하기보다는 **오히려 감소하는 경향**을 보였습니다.

### 🛠️ 결측치 및 범위 데이터 처리

  * **`horsepower`**: 이 컬럼에는 `Unknown`, 결측치, `None`과 같은 다양한 결측값이 존재했습니다. 이를 처리하기 위해 \*\*중앙값(median)\*\*으로 대체하여 데이터의 손실을 최소화했습니다.
  * **`kilometers`, `year`**: 이 피처들은 종종 텍스트 형태로 범위가 입력되어 있었습니다. 저희는 이러한 텍스트에 해당하는 **중간값**을 부여하여 수치형 데이터로 변환했습니다.

### 🚀 핵심 피처 발굴: `company` & `date_posted`

가장 주목할 만한 결과는 다음과 같습니다:

  * **`company`**: 컬럼 내 데이터 종류가 매우 다양하여 원-핫 인코딩 적용 여부에 대한 고민이 많았습니다. 그러나 **원-핫 인코딩을 적용한 결과, 모델의 정확도가 무려 ✨0.1 이상 상승✨**하는 놀라운 효과를 보였습니다.
  * **`date_posted`**: 이 피처를 년, 월, 일로 분리하여 각각 원-핫 인코딩을 진행했습니다. 그 결과, 역시 **0.1 이상의 정확도 상승률**을 기록했습니다.

\<br\>

-----

## 💡 결론 및 주요 인사이트

이번 분석을 통해 다음의 핵심적인 인사이트를 얻을 수 있었습니다:

1.  **`horsepower` 피처 적용**은 모델의 정확도를 **0.2 이상 크게 향상**시켰습니다. 이는 차량의 마력이 중고차 가격을 예측하는 데 매우 중요한 요소임을 시사합니다.
2.  \*\*`company` (제조사)\*\*와 **`date_posted` (게시일)** 피처는 중고차 가격 예측 모델의 성능에 **매우 깊은 연관성**이 있음을 강력하게 보여주었습니다. 이 두 피처는 모델의 정확도 향상에 결정적인 기여를 했습니다.

이러한 결과는 중고차 가격 예측 모델 개발 시 `horsepower`, `company`, `date_posted`와 같은 피처들을 **핵심적으로 고려해야 함**을 명확히 보여주었습니다.
