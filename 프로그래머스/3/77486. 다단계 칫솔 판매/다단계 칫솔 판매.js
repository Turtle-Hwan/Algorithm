/* 
단순히 seller들의 referral을 타고타고 올라가면 될 거 같은데?

enroll -> referral -> enroll .... "-" 등장 시 까지.
"-" 인 사람은 10%를 center에 지급
*/
function solution(enroll, referral, seller, amount) {
    let answer = Array.from({length: enroll.length}, () => 0);
    
    seller.length !== 0 && seller.forEach((seller, i) => {
        const nameIndex = enroll.findIndex((name) => name === seller);
        // 자신은 90% 수익 가져감
        answer[nameIndex] += amount[i] * 90;
        
        // referralName이 "-"를 만나거나 1원 미만일 때까지 나오는 사람들한테 10%의 10%의 10%... 나눠주기
        let moneyToGiveRef = amount[i] * 10;
        let referralName = referral[nameIndex];
        while (true) {
            //console.log(referralName)
            const refNameIndex = enroll.findIndex((name) => name === referralName);
            if (referralName === "-") {
                answer[refNameIndex] += Math.ceil(moneyToGiveRef * 9 / 10);
                break;
            }
            if (Math.floor(moneyToGiveRef / 10) === 0) {
                answer[refNameIndex] += moneyToGiveRef;
                break;
            }

            //console.log(moneyToGiveRef, moneyToGiveRef * 9 / 10)
            answer[refNameIndex] += Math.ceil(moneyToGiveRef * 9 / 10);
            
            moneyToGiveRef = Math.floor(moneyToGiveRef / 10);
            
            referralName = referral[refNameIndex];
        }
    });
    
    //console.log(answer);
    
    return answer;
}