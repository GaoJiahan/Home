const fs = require("fs").promises;


async function main() {
    console.log(await fs.readdir("node_modules"));
}

console.log(__dirname);