function go(gobackNum, coord, direction) {
    switch (direction) {
        case 0:
            coord[1] += gobackNum;
            return coord;
        case 1:
            coord[0] += gobackNum;
            return coord;
        case 2:
            coord[1] -= gobackNum;
            return coord;
        case 3:
            coord[0] -= gobackNum;
            return coord;
    }
};

function solution(command) {
    let answer = [0, 0];
    let direction = 0;
    /* *
    0 : +y
    1 : +x
    2 : -y
    3 : -x
    4로 나눈 나머지
    */
    
    for (let i = 0; i < command.length; i++) {
        switch (command[i]) {
            case "R":
                direction = (direction + 1) % 4;
                break;
            case "L":
                direction = direction - 1;
                if (direction < 0) {
                    direction = direction + 4;
                }
                break;
            case "G":
                go(1, answer, direction);
                break;
            case "B":
                go(-1, answer, direction);
                break;                
            default:
                break;
        }
    }
    
    return answer;
}
