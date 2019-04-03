// // Dynamic Programming is useful WHEN
// // we have a large problem that can be decomposed into smaller
// // subproblems of the same structure
// //
// // SOLVE THE BRUTE FORCE FIRST

// // Write a function, lucasNumber(n), that takes in a number.
// // The function should return the n-th number of the Lucas Sequence.
// // The 0-th number of the Lucas Sequence is 2.
// // The 1-st number of the Lucas Sequence is 1
// // To generate the next number of the sequence, we add up the previous two numbers.
// //
// // For example, the sequence begins: 2, 1, 3, 4, 7, 11, ...
// //
// // Examples:
// //
// // lucasNumber(0)   // => 2
// // lucasNumber(1)   // => 1
// // lucasNumber(40)  // => 228826127
// // lucasNumber(41)  // => 370248451
// // lucasNumber(42)  // => 599074578
// //

// // lucasNumber(5)    => 11

// // Memoization - RECURSIVE DYNAMIC PROGRAMMING
// //   1. add an obj as arg into your func
// //      the obj should have the orig func arg as keys and values should be returns
// //   2. add a base case that checks if orig arg is in the memo
// //   3. wherever we return in the recursive case, store that in the memo first

// // function lucasNumber(n, memo={0: 2, 1 : 1}) {
// //     if (n in memo) return memo[n];

// //     memo[n] = lucasNumber(n - 1, memo) + lucasNumber(n - 2, memo);

// //     return memo[n];
// // }

// // Tabulation - ITERATIVE DP

// function lucasNumber(n) {
//     let table = new Array(n + 1);

//     table[0] = 2;
//     table[1] = 1;

//     for (var i = 2; i < table.length; i++) {
//         table[i] = table[i - 1] + table[i - 2];
//     }

//     return table[n];
// }

// // function lucasNumber(n, memo = {}) {
// //     if (n === 0) return 2;
// //     if (n === 1) return 1;

// //     if ((n - 1) in memo) {
// //         let lastLucas = memo[(n - 1)];
// //     } else {
// //         // recurse
// //     }

// //     if ((n - 2) in memo) {

// //     }
// //     memo[n] = lucasNumber(n - 1, memo) + lucasNumber(n - 2, memo);

// //     return memo[n];
// // }

// console.log(lucasNumber(5));
// console.log(lucasNumber(0));   // => 2
// console.log(lucasNumber(1));   // => 1
// console.log(lucasNumber(40));  // => 228826127
// console.log(lucasNumber(41));  // => 370248451
// console.log(lucasNumber(42));  // => 599074578
// console.log(lucasNumber(100));  // => 599074578

// In ruby, arrays and hashes are pass by ref
// In JS, arrays and objs are pass by ref

// Write a function, minChange(coins, amount), that accepts an array of coin values
// and a target amount as arguments. The method should the minimum number of coins needed
// to make the target amount. A coin value can be used multiple times.
//
// After you pass the first 3 examples, you'll likely need to memoize your code
// in order to pass the 4th example in a decent runtime.
//
// Examples:
//
// minChange([1, 2, 5], 11)         // => 3, because 5 + 5 + 1 = 11
// minChange([1, 4, 5], 8)         // => 2, because 4 + 4 = 8
// minChange([1, 5, 10, 25], 15)    // => 2, because 10 + 5 = 15
// minChange([1, 5, 10, 25], 100)   // => 4, because 25 + 25 + 25 + 25 = 100

// function minChange(coins, amount, memo={}) {
//     if (amount in memo) return memo[amount];
//     if (amount === 0) return 0;

//     let possibilities = [];
//     coins.forEach(coinVal => {
//         let remainder = amount - coinVal;
//         if (remainder >= 0) {
//             possibilities.push(minChange(coins, remainder, memo) + 1);
//         }
//     });

//     memo[amount] = Math.min(...possibilities);
//     return memo[amount];
// }

// console.log(minChange([1, 2, 5], 11))         // => 3, because 5 + 5 + 1 = 11
// console.log(minChange([1, 4, 5], 8))         // =>  2, because 4 + 4 = 8
// console.log(minChange([1, 5, 10, 25], 15))    // => 2, because 10 + 5 = 15
// console.log(minChange([1, 5, 10, 25], 100))   // => 4, because 25 + 25 + 25 + 25 = 100

// let arr = [
//     [1,2],
//     [3,4,5]
// ];

// let cp = arr.map((row) =>row.slice());
// console.log(cp)
