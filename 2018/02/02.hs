import Data.List
import Control.Arrow

occu x input = do
    length $ filter (not . null) $ map (filter (\(_,y) -> y == x)) input

solveA :: [String] -> Int
solveA input = do
    let tmp = map (map (head &&& length) . group . sort) input
    let twos = occu 2 $ tmp
    let threes = occu 3 $ tmp
    twos * threes

{-
helper :: [[(Char, Int)]] -> [(Char, Int)] -> [(Char, Int)]
helper [] o = []
helper (x:xs) o
    | (length $ x \\ o) == 1 = filter (`elem` x) o
    | otherwise = helper xs o
-}

helper2 [] o = []
helper2 (x:xs) o
    | (length $ filter (\(x,y) -> x /= y) (zip x o)) == 1 = map fst $ filter (\(x,y) -> x == y) (zip x o)
    | otherwise = helper2 xs o

solveB input =
    filter (not . null) $ map (helper2 input) input

main = do
    input <- readFile "input.txt"
    let l = lines input

    print $ solveA l
    print $ head $ solveB l
