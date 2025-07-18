class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class Stack {
    constructor() {
        this.top = null;
        this.bottom = null;
        this.length = 0;
    }

    peek() {
        return this.top;
    }

    push(value) {
        const newNode = new Node(value);
        if (this.length===0) {
            this.bottom = newNode;
            this.top = newNode;
        }
        else {
            let holdingPointer = this.top;
            this.top = newNode;
            this.top.next = holdingPointer
        }
        this.length += 1;
        return this;
    }

    pop() {
        if (!this.top) {
            return None
        }
        if (this.top == this.bottom) {
            return None
        }
        // let holdingPointer = this.top;
        this.top = this.top.next;
        this.length--;
        return this
    }
}

const myStack = new Stack();
myStack.push(2);
myStack.push(10);
console.log(myStack.peek());
myStack.pop();
console.log(myStack.peek());

