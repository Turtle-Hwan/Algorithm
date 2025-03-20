function solution(numbers) {
    const numberList = [...numbers];
    // console.log(numeberList)
    
    let numberSet = new Set();
    
    for (let i = 1; i <= numbers.length; i++) {
        permu(numberList, i).forEach((e) => numberSet.add(Number(e)))
    }
    
    console.log(numberSet)   
    
    let answer = 0;
    numberSet.forEach((e) => isPrime(e) ? answer += 1 : null)
    
    return answer;
}

/*
만들 수 있는 모든 숫자
해당 숫자가 소수인지
*/

function isPrime(n) {
    if (n === 1 || n === 0) return false;
    let a = 2;
    while (Math.sqrt(n) >= a) {
        if (n % a === 0)
            return false;
        a += 1;
    }
    return true;
}

//주어진 nums [1, 7] , n 횟수 nums.length, arr 반환 배열 [17, 71]
function permu(nums, n) {
    const result = [];
    if (n === 1) return nums.map((e) => e);
    
    nums.forEach((fixed, i, arr) => {
        const rest = [...arr.slice(0, i), ...arr.slice(i+1)];
        const permutations = permu(rest, n-1);
        const attached = permutations.map((el) => [fixed, ...el]);
        result.push(...attached);
        // console.log(result);
    });
    return result.map((arr) => arr.join(''));
}