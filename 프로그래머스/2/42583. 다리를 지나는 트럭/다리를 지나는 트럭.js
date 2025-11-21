function sum(array) {
    return array.reduce((acc, cur) => acc + cur, 0);
}

function solution(bridge_length, weight, truck_weights) {
    let 경과시간 = 0;
    let 다리_지나간_트럭 = [];
    let 다리_건너는_트럭 = [];
    let 대기_트럭 = truck_weights;
    
    let 트럭_건너기_완료시각 = []; // 현재 배열에 든 트럭이 언제 다 건너는지
    
    while (대기_트럭.length > 0 || 다리_건너는_트럭.length > 0) {
        경과시간 += 1;
        // console.log(경과시간);
        
        if (트럭_건너기_완료시각[0] === 경과시간) {
            트럭_건너기_완료시각.shift();
            다리_지나간_트럭.push(다리_건너는_트럭.shift());
        }
        
        if (sum(다리_건너는_트럭) + 대기_트럭[0] > weight) continue;
        else if (대기_트럭.length > 0) {
            다리_건너는_트럭.push(대기_트럭.shift());
            트럭_건너기_완료시각.push(경과시간 + bridge_length);
        }
    }
    
    
    return 경과시간;
}