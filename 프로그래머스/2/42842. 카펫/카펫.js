function solution(brown, yellow) {
    const 변의_수 = (brown - 4) / 2
    
    let answer;
    
    for (let i = 1; i <= 변의_수 / 2; i++) {
        if (i * (변의_수 - i) === yellow) {
            answer = i > (변의_수 - i) ? [i, 변의_수-i] : [변의_수-i, i];
            break;
        }
    }
    
    return answer.map((e) => e+2);
}