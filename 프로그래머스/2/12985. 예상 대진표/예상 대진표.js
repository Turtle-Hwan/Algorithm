function solution(n,a,b)
{

    // 반으로 쪼개서, 왼쪽 반에 1명, 오른쪽 반에 1명이 있으면 이 둘은 항상 마지막에 만남.
    /* 
    a < b 상태로 정렬
    
    const log2n
    mid = n / 2
    if a <= mid && mid < b : 
        answer = log2n
    
    else mid = mid / 2
    if mid < a, b 라면 a = a - mid , b = b - mid
    log2n = log2(mid)
    
    if a <= mid.... 반복
    */
    console.log(n, a, b);
    
    if (a > b) {
        const temp = a;
        a = b;
        b = temp;
    }
    
    const log2n = Math.log2(n);
    let answer = log2n;
    let mid = n;
    
    while (true) {
        mid /= 2;
        
        if (a <= mid && mid < b) {
            break;
        }
        else if (mid < a) {
            a -= mid;
            b -= mid;
        }
        answer -= 1;
        
        //console.log(mid, answer, a, b)
    }

    return answer;
}
