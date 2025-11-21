const fs = require("fs");
// 백준 제출 시에는 '/dev/stdin', 로컬 테스트 시에는 'input.txt'
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");
let n = parseInt(input[0].split(" ")[0]); //문제 개수
let m = parseInt(input[0].split(" ")[1]); //학생 수
let students = input.slice(1);

function solution(n, m, students) {
  /* 
  각 번호 사람들이 풀 수 있는 문제들을 Set에 저장
  모든 사람들 조합해서 합집합 한 것의 길이가 문제 개수와 똑같아지는 경우 찾기
  해당 경우의 최소 사람 조합

  10명 다 넣었을 때, 9명씩 넣었을 때, ... 1명씩 넣었을 때

  10 + 10C9 + 10C8 + ... + 10C1

  1. 시간 복잡도 계산
  조합에 대한 경우의 수 : 대략 1만
  Set에 넣는 작업 10명일 때 대략 O(100)
  O(100만)
   */
  // console.log(n, m, students);

  let student_sets = students.map((student, idx) => {
    let studentNum = idx + 1;
    let problems = new Set(student.split(" ").slice(1).map(Number));
    // console.log(studentNum, problems);

    return problems;
  });

  // console.log(student_sets);

  // student_sets : 선택가능 원소 집합
  let student_select = new Set(); // 선택한 원소
  let answer = Infinity;

  function combi(start, depth, targetDepth) {
    if (depth === targetDepth) {
      // 다 선택했으면 선택 원소 출력
      if (student_select.size === n) {
        // console.log(student_select, targetDepth);
        answer = targetDepth;
      }
      return;
    }

    for (let i = start; i < student_sets.length; i++) {
      // depth 번째 수 선택
      let student_select_save = student_select;
      student_select = new Set([...student_select, ...student_sets[i]]);
      // depth + 1 번째 수 선택하기 (student_sets[i+1] 부터)
      combi(i + 1, depth + 1, targetDepth);
      // depth 번째 수 선택 취소
      student_select = student_select_save;
    }
  }

  for (let t = m; t >= 1; t--) {
    // console.log(`\n# of students: ${t}`);
    combi(0, 0, t);
  }

  return answer === Infinity ? -1 : answer;
}

console.log(solution(n, m, students));
