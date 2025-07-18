function reverse(str) {
    if(!str || typeof str != 'string' || str.length < 2) return 'invalid input';

    const newstr = [];
    const strlen = str.length-1

    for(let i = strlen; i >= 0; i--) {
        newstr.push(str[i]);

    }

    return newstr.join('');
}

function reverse2(str) {
    if(!str || typeof str != 'string' || str.length < 2) return 'invalid input';
    
    return str.split('').reverse().join('');
}

const reverse3 = str => [...str].reverse().join('');

console.log(reverse2('hello there'));