use std::collections::VecDeque;
use std::collections::HashSet;
use std::collections::hash_map::DefaultHasher;
use std::hash::Hash;
use std::hash::Hasher;

#[aoc_generator(day22)]
pub fn input_generator(input: &str) -> (VecDeque<u32>, VecDeque<u32>) {
    let mut player_cards: VecDeque<u32> = VecDeque::new();
    let mut crab_cards: VecDeque<u32> = VecDeque::new();
    let inp = input.split("\n\n").collect::<Vec<&str>>();
    for (p, c) in inp[0].split("\n").skip(1).zip(inp[1].split("\n").skip(1)){
        player_cards.push_back(p.parse::<u32>().unwrap());
        crab_cards.push_back(c.parse::<u32>().unwrap());
    }
    (player_cards, crab_cards)
}

#[aoc(day22, part1)]
pub fn solve_part1(input: &(VecDeque<u32>, VecDeque<u32>)) -> u32 {
    let (mut player_cards, mut crab_cards) = input.clone();
    while true{
        let played = (player_cards.pop_front(), crab_cards.pop_front());
        match played{
            (x,None) => {player_cards.push_front(x.unwrap());println!("The player won!"); break},
            (None,y) => {crab_cards.push_front(y.unwrap());println!("The fucking crab won!"); break},
            (Some(x),Some(y)) if x > y => {player_cards.push_back(x); player_cards.push_back(y)},
            (Some(x),Some(y)) if x < y => {crab_cards.push_back(y); crab_cards.push_back(x)},
            (_,_) => println!("This should not happen"),
        }
    }
    let mut winner_cards = if player_cards.len() == 0 {crab_cards} else {player_cards};
    let mut count = 0;
    for i in 1..winner_cards.len()+1{
        count += i as u32 * winner_cards.pop_back().unwrap();
    }
    count
}

fn hash(player_cards: &VecDeque<u32>, crab_cards: &VecDeque<u32>) -> u64 {
    let mut hasher = DefaultHasher::new();
    (player_cards, crab_cards).hash(&mut hasher);
    hasher.finish()
}

fn recursive_combat(player_cards: &mut VecDeque<u32>, crab_cards: &mut VecDeque<u32>) -> u32{
    let mut seen_decks = HashSet::new();
    while true{
        if !seen_decks.insert(hash(&player_cards, &crab_cards)) {
            return 1
        }
        let played = (player_cards.pop_front(), crab_cards.pop_front());
        match played{
            (Some(x),None) => {player_cards.push_front(x); return 1},
            (None,Some(y)) => {crab_cards.push_front(y); return 2},
            (Some(x),Some(y)) if x <= player_cards.len() as u32 && y <= crab_cards.len() as u32 =>
            {let w = recursive_combat(&mut player_cards.iter().take(x as usize).cloned().collect(),
                &mut crab_cards.iter().take(y as usize).cloned().collect());
                if w == 1 {player_cards.push_back(x); player_cards.push_back(y);} else{
                    crab_cards.push_back(y); crab_cards.push_back(x);}}
            (Some(x),Some(y)) if x > y => {player_cards.push_back(x); player_cards.push_back(y)},
            (Some(x),Some(y)) if x < y => {crab_cards.push_back(y); crab_cards.push_back(x)},
            (_,_) => println!("This should not happen"),
        }
    }
    1
}
#[aoc(day22, part2)]
pub fn solve_part2(input: &(VecDeque<u32>, VecDeque<u32>)) -> u32 {
    let (mut player_cards, mut crab_cards) = input.clone();
    recursive_combat(&mut player_cards, &mut crab_cards);
    let mut winner_cards = if player_cards.len() == 0 {crab_cards} else {player_cards};
    let mut count = 0;
    for i in 1..winner_cards.len()+1{
        count += i as u32 * winner_cards.pop_back().unwrap();
    }
    count
}
