class Node {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
  }

  class Queue {
    constructor() {
      this.first = null;
      this.last = null;
      this.length = 0;
    }
    peek() {
        return this.first.value
    }
    enqueue(value) {
        const newNode = new Node(value);
        if (this.length == 0) {
            this.first = newNode;
            this.last = newNode;
        }
        else {
            this.last.next = newNode
            this.last = newNode
        }
        this.length++
        return this
    }
    dequeue() {
        if (!this.first) {
            return None
        }
        if (this.first == this.last) {
            this.last = null
        }
        let removed = this.first
        this.first = this.first.next
        this.length--;
        return removed
    }
    //isEmpty;
  }

  const myQueue = new Queue();
myQueue.enqueue("Joey")
myQueue.enqueue("Marsha")
myQueue.enqueue("Lily")

console.log(myQueue.peek())

myQueue.dequeue();
console.log(myQueue.peek())

  //Joy
  //Matt
  //Pavel
  //Samir