class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
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
        this.tail.next = newNode;
        this.tail = newNode;
        this.length++;
        return this;
    }

    prepend(value) {
        const newNode = new Node(value);
        newNode.next = this.head;
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
        newNode.next = leader.next;
        leader.next = newNode;
        this.length++;
        return this;
    }

    remove(index) {
        const leader = this.traverse(index-1);
        const unwantedNode = leader.next;
        leader.next = unwantedNode.next;
        this.length--;
        return this
    }

    reverse() {
        if (!this.head || !this.head.next) {
            return this;
        }
        let prev = null;
        let current = this.head;
        this.tail = this.head;
        while (current) {
            let next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        this.head = prev;
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
console.log(LL.reverse().printList())
// print(LL.printList())