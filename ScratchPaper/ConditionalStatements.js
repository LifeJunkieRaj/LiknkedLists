
let newHouse = (flowerType, flowerNum, budget) => {
    if (flowerType === "Rose" && flowerNum > 80) {
        let flowerType = 5.0;
        let total = flowerNum * flowerType;
        let finalPrice = total - (total * 0.10);
        let moneyLeft = budget - finalPrice;

        if (moneyLeft < 0) {
            console.log(`Not enough money, you need ${(moneyLeft * -1).toFixed(2)} leva more`)
        } else if (moneyLeft >= 0) {
            console.log(`Hey, you have great garden with ${flowerNum} and ${moneyLeft.toFixed(2)} leva left`)
        }
    }
    if (flowerType === "Rose" && flowerNum <= 80) {
        let flowerType = 5.0;
        let total = flowerNum * flowerType;
        //let finalPrice = total - (total * 0.10);
        let moneyLeft = budget - total;

        if (moneyLeft < 0) {
            console.log(`Not enough money, you need ${(moneyLeft * -1).toFixed(2)} leva more`)
        } else if (moneyLeft >= 0) {
            console.log(`Hey, you have great garden with ${flowerNum} and ${moneyLeft.toFixed(2)} leva left`)
        }
    }
    if (flowerType === "Dahlias" && flowerNum > 90) {
        let flowerType = 3.80;
        let total = flowerNum * flowerType;
        let finalPrice = total - (total * 0.15);
        let moneyLeft = budget - finalPrice;

        if (moneyLeft < 0) {
            console.log(`Not enough money, you need ${(moneyLeft * -1).toFixed(2)} leva more`)
        } else if (moneyLeft >= 0) {
            console.log(`Hey, you have great garden with ${flowerNum} $ and ${moneyLeft.toFixed(2)} leva left`)
        }
    }
    if (flowerType === "Dahlias" && flowerNum <= 90) {
        let flowerType = 3.80;
        let total = flowerNum * flowerType;
        //let finalPrice = total - (total * 0.15);
        let moneyLeft = budget - total;

        if (moneyLeft < 0) {
            console.log(`Not enough money, you need ${(moneyLeft * -1).toFixed(2)} leva more`)
        } else if (moneyLeft >= 0) {
            console.log(`Hey, you have great garden with ${flowerNum} ${flowerType} and ${moneyLeft.toFixed(2)} leva left`)
        }
    }
    if (flowerType === "Tulips" && flowerNum > 80) {
        let flowerType = 2.80;
        let total = flowerNum * flowerType;
        let finalPrice = total - (total * 0.15);
        let moneyLeft = budget - finalPrice;

        if (moneyLeft < 0) {
            console.log(`Not enough money, you need ${(moneyLeft * -1).toFixed(2)} leva more`)
        } else if (moneyLeft >= 0) {
            console.log(`Hey, you have great garden with ${flowerNum} ${flowerType} and ${moneyLeft.toFixed(2)} leva left`)
        }
    }
    if (flowerType === "Tulips" && flowerNum <= 80) {
        let flowerType = 2.80;
        let total = flowerNum * flowerType;
        //let finalPrice = total - (total * 0.15);
        let moneyLeft = budget - total;

        if (moneyLeft < 0) {
            console.log(`Not enough money, you need ${(moneyLeft * -1).toFixed(2)} leva more`)
        } else if (moneyLeft >= 0) {
            console.log(`Hey, you have great garden with ${flowerNum} ${flowerType} and ${moneyLeft.toFixed(2)} leva left`)
        }
    }
    if (flowerType === "Narcissus" && flowerNum <= 120) {
        let flowerType = 3;
        let total = flowerNum * flowerType;
        let finalPrice = total + (total * 0.15);
        let moneyLeft = budget - finalPrice;

        if (moneyLeft < 0) {
            console.log(`Not enough money, you need ${(moneyLeft * -1).toFixed(2)} leva more`)
        } else if (moneyLeft >= 0) {
            console.log(`Hey, you have great garden with ${flowerNum} ${flowerType} and ${moneyLeft.toFixed(2)} leva left`)
        }
    }
    if (flowerType === "Narcissus" && flowerNum > 120) {
        let flowerType = 3;
        let total = flowerNum * flowerType;
        //let finalPrice = total - (total * 0.15);
        let moneyLeft = budget - total;

        if (moneyLeft < 0) {
            console.log(`Not enough money, you need ${(moneyLeft * -1).toFixed(2)} leva more`)
        } else if (moneyLeft >= 0) {
            console.log(`Hey, you have great garden with ${flowerNum} ${flowerType} and ${moneyLeft.toFixed(2)} leva left`)
        }
    }
    if (flowerType === "Gladiolus" && flowerNum <= 80) {
        let flowerType = 2.50;
        let total = flowerNum * flowerType;
        let finalPrice = total + (total * 0.20);
        let moneyLeft = budget - finalPrice;

        if (moneyLeft < 0) {
            console.log(`Not enough money, you need ${(moneyLeft * -1).toFixed(2)} leva more`)
        } else if (moneyLeft >= 0) {
            console.log(`Hey, you have great garden with ${flowerNum} ${flowerType} and ${moneyLeft.toFixed(2)} leva left`)
        }
    }
    if (flowerType === "Gladiolus" && flowerNum > 80) {
        let flowerType = 2.50;
        let total = flowerNum * flowerType;
        //let finalPrice = total - (total * 0.15);
        let moneyLeft = budget - total;

        if (moneyLeft < 0) {
            console.log(`Not enough money, you need ${(moneyLeft * -1).toFixed(2)} leva more`)
        } else if (moneyLeft >= 0) {
            console.log(`Hey, you have great garden with ${flowerNum} ${flowerType} and ${moneyLeft.toFixed(2)} leva left`)
        }
    }
}

newHouse("Tulips", 88, 260)