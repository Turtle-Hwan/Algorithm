

const clothesHash = {};

function solution(clothes) {
    clothes.forEach((clothing) => {
        if (clothing[1] in clothesHash)
        clothesHash[clothing[1]] = [...clothesHash[clothing[1]], clothing[0]];
        else clothesHash[clothing[1]] = [clothing[0]];
    });
   
    console.log(Object.keys(clothesHash).length);
    
    //n 종류 옷 입는 경우.
    let answer = 1;
    const keys = Object.keys(clothesHash);
    keys.forEach((key) => {
        answer *= clothesHash[key].length + 1
    })
    answer -= 1;
    
    /* 조합 구현? or 집합론
    조합은 nCr 이면 n! / n-r! r!
    팩토리얼 구해서 하면 된다?
    */
    
    /* 집합론이면 1, 2, ...n 일때, 
    1번 옷 입는 경우 2번옷 입는 경우 n번 옷 입는 경우 안입는 경우. 
    (n + 1) * ... - 1 (모두 안 입으만 안되니깐)
    */
    
    return answer;
}