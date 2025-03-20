/* js에서 큐 구현법
1. 투포인터로 왔다갔다 하거나
2. 배열(스택) 두 개로 큐 만들거나
3. 그냥 shift 쓰고 시간복잡도 희생하거나
*/
class Queue {
    constructor(array) {
        this.queue = array;
        this.start = 0; // 첫 index
        this.end = array.length; // 마지막 + 1 index
    }
    
    size() {
        return this.end - this.start;
    }
    
    push(n) {
        this.queue[this.end] ? this.queue[this.end] = n : this.queue.push(n);
        this.end += 1;
    }
    
    empty() {
        return this.start - this.end === 0 ? true : false;
    }
    
    pop() {        
        let val;
        if (this.size() === 0) {
            this.start = 0;
            this.end = 0;
            return null;
        }
        else {
            val = this.queue[this.start];
            this.start += 1
            
            if (this.start === this.end) {
                this.start = 0;
                this.end = 0;
            }
        }
        return val;
    }
    
    print() {
        console.log(this.queue, this.start, this.end);
    }
    
    max() {
        return Math.max(...this.queue.slice(this.start, this.end));
    }
}

function solution(priorities, location) {
    const queue = new Queue(priorities);
    const queue_index = new Queue(Array.from(priorities, (x, i) => i));
    // queue.print();
    // queue_index.print();
    
    let answer = 0;
    
    
    while (!queue.empty()) {
        queue.print();
        const pop = queue.pop();
        const pop_index = queue_index.pop();
        
        if (pop >= queue.max()) {
            answer += 1;
            if (location === pop_index) break;
        }
        else {
            queue.push(pop);
            queue_index.push(pop_index);
        }
    }
    
    
    return answer;
}