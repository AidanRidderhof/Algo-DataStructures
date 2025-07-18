class Stack {
    constructor() {
        this.array = [];
    }

    peek() {
        return this.array[this.array.length-1];
    }

    push(value) {
        this.array.push(value);
        return this;
    }

    pop() {
        this.array.pop()
        return this
    }
}

const myStack = new Stack();
myStack.push(2);
myStack.push(10);
console.log(myStack.peek());
myStack.pop();
console.log(myStack.peek());

