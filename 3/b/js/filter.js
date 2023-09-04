const professores = [
    [
        "Bart",
        "Camoleze",
        "Eduardo",
        "Newton",
        [
            "Bart",
            "Newton"
        ]
    ],
    "Bart",
    "Camoleze",
    "Diego",
    "Eduardo",
    "Gabriela",
    "Maire",
    "Moises",
    "Newton",
    "Rene",
    "Sandra"
];

function findName(nome, arr) {
    let finds = [nome, 0];
    arr.filter(n => {
        if (Array.isArray(n))
            finds[1] += findName(nome, n)[1];
        else
            if (n == nome) finds[1] += 1;
    });
    return finds;
}

console.log(findName(["Bart"], professores));