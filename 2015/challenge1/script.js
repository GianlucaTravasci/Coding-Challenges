const fs = require('fs');

// 1- Last floor for santa
function santaLastFloor() {
    fs.readFile('./input.txt', (err, data) => {
        const direction = data.toString();
        const directionArray = direction.split('');
        const answare = directionArray.reduce((acc, item) =>{
            if(item === '(') {
                return acc += 1;
            } else {
                return acc -= 1;
            }
        }, 0)
        console.log(answare);
    });
}
santaLastFloor();

// 2- when Santa first enter the basement
function santaBasementFloor() {
    fs.readFile('./input.txt', (err, data) => {
        const direction = data.toString();
        const directionArray = direction.split('');
        let accumulator = 0;
        let counter = 0;
        const answare = directionArray.some((item) =>{
            if(item === '(') {
                accumulator += 1;
            } else {
                accumulator -= 1;
            }
            counter++;
            return accumulator <0;
        })
        console.log(counter)
    });
}
santaBasementFloor();