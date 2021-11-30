import Data.Char

splitHalf l = splitAt ((length l + 1) `div` 2) l

solveA :: [Int] -> Int
solveA input = do
    sum $ map(\(x,y) -> x) $ filter (\(x,y) -> x == y) $ zip (last input : input) input

solveB :: [Int] -> Int
solveB input = do
    let t = splitHalf input
    let l = fst t
    let r = snd t
    let half = sum $ map(\(x,y) -> x) $ filter (\(x,y) -> x == y) $ zip l r
    2 * half

main = do
    input <- map digitToInt <$> readFile "input.txt"
    print $ solveA input
    print $ solveB input
