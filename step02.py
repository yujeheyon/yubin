user = "admin"

if user == "admin":
    print("관리자님 안녕하세요.")
else:
    print("일반 사용자 입니다.")

tasks = ["대시보드 UI 기획", "데이터베이스 연동", "사용자 테스트 진행"]

print("=== 오늘의 할 일 목록 ===")
for task in tasks:
    print(task)

print("===================")
students = [{"name": "철수", "score": 85}, {"name": "영희", "score": 55}]

for s in students:
    if s["score"] >= 60:
        result = "합격"
    else:
        result = "재시험"
    print(f"{s['name']}: {s['score']}점 -> {result}")

print("===================")
def calculate_stats(score_list):
    total = sum(score_list)
    avg   = total / len(score_list)
    return total, avg

score = [90, 80, 100, 70, 65, 85, 40]

total, avg = calculate_stats(score)
print(f"총점: {total}, 평균: {avg:.2f}")