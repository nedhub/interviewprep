


const breathFirstPrint = (graph, source) => {

    const queue = [ source ];

    while(queue.length > 0) {
        const current = queue.shift();
        console.log(current);
        for (let neighbor of graph[current]) {

            queue.push(neighbor);
        }
    }
}


const graph = { 

    a: ['c', 'd'],
    b: ['d'],
    c: ['e'],
    d: ['f'],
    e: [],
    f: []
}