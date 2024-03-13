use std::convert::TryFrom;
use std::io::{self};

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let numbers: Vec<i32> = input
        .trim()
        .split_whitespace()
        .take(8)
        .map(|x| x.parse().unwrap())
        .collect();

    let [n, k, l, c, d, p, nl, np] = <[i32; 8]>::try_from(numbers).ok().unwrap();

    // n - number of friends
    // k - number of bottles
    // l - milliliters of the drink in a bottle
    // c - number of limes
    // d - number of slices to cut from a lime
    // p - grams of salt
    // nl - milliliters of the drink needed for one toast
    // np - grams of salt needed for one toast

    let drinks = k * l / nl;
    let limes = c * d;
    let salt = p / np;

    let toasts = vec![drinks, limes, salt].iter().min().unwrap() / n;
    println!("{}", toasts);
}
