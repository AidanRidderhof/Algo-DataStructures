class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

class linkedList {
    constructor(value) {
        const newNode = new Node(value);
        this.head = newNode;
        this.tail = newNode;
        this.length = 1;
    }

    append(value) {
        const newNode = new Node(value);
        newNode.prev = this.tail;
        this.tail.next = newNode;
        this.tail = newNode;
        this.length++;
        return this;
    }

    prepend(value) {
        const newNode = new Node(value);
        newNode.next = this.head;
        this.head.prev = newNode
        this.head = newNode;
        this.length++;
        return this;
    }

    printList() {
        const array = [];
        let currentNode = this.head;
        while(currentNode != null) {
            array.push(currentNode.value);
            currentNode = currentNode.next;
        }
        return array;
    }

    traverse(index) {
        let counter = 0;
        let currentNode = this.head;
        while (counter !== index) {
            currentNode = currentNode.next;
            counter++
        }
        return currentNode;
    }

    insert(index, value) {
        if (index>=this.length) {
            return this.append(value);
        }
        else if (index <= 0) {
            return this.prepend(value);
        }
        let newNode = new Node(value);
        let leader = this.traverse(index-1);
        let follower = leader.next;
        leader.next = newNode;
        newNode.prev = leader;
        newNode.next = follower;
        this.length++;
        return this;
    }

    remove(index) {
        if (index <= 0) {
            // Remove head
            this.head = this.head.next;
            if (this.head) this.head.prev = null;
            this.length--;
            return this;
        }
        if (index >= this.length - 1) {
            // Remove tail
            this.tail = this.tail.prev;
            if (this.tail) this.tail.next = null;
            this.length--;
            return this;
        }
        const leader = this.traverse(index - 1);
        const unwantedNode = leader.next;
        const follower = unwantedNode.next;
        leader.next = follower;
        follower.prev = leader;
        this.length--;
        return this;
    }
}

LL = new linkedList(10)
LL.append(5)
LL.append(16)
LL.prepend(1)
LL.insert(2,70)
LL.insert(99, 4)
 LL.remove(2)
console.log(LL.printList())
// LL.remove(3)
// print(LL.printList())